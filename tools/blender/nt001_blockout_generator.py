"""Generate the NT-001 v001 candidate blockout from the Phase 1 contract.

Run with Blender in background mode.  This is deliberately a primary/secondary
form blockout: it contains no fur sculpt, texture, VFX, print split, or runtime
topology.  Its job is to create one reconciled volume for projection review.
"""

from pathlib import Path
import math
import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "assets/characters/NT-001/03_3d_source/master/NT001_BLOCKOUT_v001.blend"
RENDER_DIR = ROOT / "assets/characters/NT-001/11_validation/blockout/v001/renders"


def clean_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for block in datablocks:
            if block.users == 0:
                datablocks.remove(block)


def collection(name):
    result = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(result)
    return result


def move_to(obj, target):
    for existing in list(obj.users_collection):
        existing.objects.unlink(obj)
    target.objects.link(obj)


def uv_ellipsoid(name, location, scale, target):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.shade_smooth()
    move_to(obj, target)
    return obj


def cone(name, location, radius1, radius2, depth, rotation, target):
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=radius1, radius2=radius2, depth=depth, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    bevel = obj.modifiers.new("BLOCKOUT_EDGE_SOFTEN", "BEVEL")
    bevel.width = 0.08
    bevel.segments = 3
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=bevel.name)
    bpy.ops.object.shade_smooth()
    move_to(obj, target)
    return obj


def tail_lobe(name, points, radius, target):
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 16
    curve.bevel_depth = radius
    curve.bevel_resolution = 5
    spline = curve.splines.new("BEZIER")
    spline.bezier_points.add(len(points) - 1)
    taper = (0.85, 1.10, 0.78, 0.04)
    for point, coordinate, point_radius in zip(spline.bezier_points, points, taper):
        point.co = coordinate
        point.radius = point_radius
        point.handle_left_type = "AUTO"
        point.handle_right_type = "AUTO"
    obj = bpy.data.objects.new(name, curve)
    target.objects.link(obj)
    return obj


def look_at(obj, point):
    obj.rotation_euler = (Vector(point) - obj.location).to_track_quat("-Z", "Y").to_euler()


def camera(name, location, target, orthographic, target_collection):
    data = bpy.data.cameras.new(name)
    data.type = "ORTHO" if orthographic else "PERSP"
    data.ortho_scale = 6.5 if orthographic else 6.0
    data.lens = 52
    obj = bpy.data.objects.new(name, data)
    obj.location = location
    look_at(obj, target)
    target_collection.objects.link(obj)
    return obj


def area_light(name, location, energy, size, target_collection):
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    obj = bpy.data.objects.new(name, data)
    obj.location = location
    look_at(obj, (0, 0, 1.8))
    target_collection.objects.link(obj)


def main():
    clean_scene()
    model = collection("NT001_BLOCKOUT_MODEL")
    guides = collection("NT001_BLOCKOUT_GUIDES")
    cameras = collection("NT001_BLOCKOUT_CAMERAS")
    lights = collection("NT001_BLOCKOUT_LIGHTS")

    clay = bpy.data.materials.new("MAT_CLAY_NEUTRAL")
    clay.diffuse_color = (0.55, 0.32, 0.13, 1.0)

    # Normalized character height is approximately 4 Blender units in this candidate scene.
    # X is left/right, Y is front/back, Z is up.  Positive Y faces forward.
    body = uv_ellipsoid("BODY_BLOCKOUT", (0, 0.0, 1.65), (1.35, 1.25, 1.15), model)
    head = uv_ellipsoid("HEAD_BLOCKOUT", (0, 0.48, 3.05), (1.55, 1.28, 1.42), model)
    uv_ellipsoid("MUZZLE_GUIDE", (0, 1.50, 2.78), (0.72, 0.44, 0.42), guides)
    for obj in (body, head):
        obj.data.materials.append(clay)

    # Broad, physical triangular ears—no glow or texture-dependent silhouette.
    ear_l = cone("EAR_L_BLOCKOUT", (-0.87, 0.32, 4.58), 0.70, 0.12, 2.15, (0.05, -0.22, 0.14), model)
    ear_r = cone("EAR_R_BLOCKOUT", (0.87, 0.32, 4.58), 0.70, 0.12, 2.15, (0.05, 0.22, -0.14), model)
    for obj in (ear_l, ear_r):
        obj.data.materials.append(clay)

    # Eyes and enlarged grounded paws support silhouette without entering sculpt detail.
    for name, x in (("EYE_L_BLOCKOUT", -0.56), ("EYE_R_BLOCKOUT", 0.56)):
        eye = uv_ellipsoid(name, (x, 1.56, 3.20), (0.25, 0.12, 0.32), model)
        eye.data.materials.append(clay)
    for name, x, y in (("LEG_FL_BLOCKOUT", -0.78, 0.72), ("LEG_FR_BLOCKOUT", 0.78, 0.72), ("LEG_RL_BLOCKOUT", -0.86, -0.72), ("LEG_RR_BLOCKOUT", 0.86, -0.72)):
        leg = uv_ellipsoid(name, (x, y, 0.72), (0.46, 0.52, 0.78), model)
        paw = uv_ellipsoid(name.replace("LEG", "PAW"), (x, y + 0.08, 0.28), (0.58, 0.64, 0.32), guides)
        leg.data.materials.append(clay)
        paw.data.materials.append(clay)

    root = uv_ellipsoid("TAIL_ROOT_BLOCKOUT", (0, -1.05, 1.95), (0.70, 0.58, 0.62), model)
    root.data.materials.append(clay)
    left_tail = tail_lobe("TAIL_L_BLOCKOUT", [(0, -1.25, 2.10), (-0.95, -1.70, 2.60), (-1.55, -1.52, 3.20), (-1.78, -1.25, 3.72)], 0.40, model)
    right_tail = tail_lobe("TAIL_R_BLOCKOUT", [(0, -1.25, 2.10), (0.95, -1.70, 2.60), (1.55, -1.52, 3.20), (1.78, -1.25, 3.72)], 0.40, model)
    for obj in (left_tail, right_tail):
        obj.data.materials.append(clay)

    bpy.ops.mesh.primitive_cylinder_add(vertices=4, radius=0.25, depth=0.055, location=(0, 1.70, 3.72), rotation=(math.pi / 2, 0, math.pi / 4))
    mark = bpy.context.object
    mark.name = "FOREHEAD_MARK_GUIDE"
    mark.data.materials.append(clay)
    move_to(mark, guides)

    # Ground is not part of the model asset, but makes paw contact review unambiguous.
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
    ground = bpy.context.object
    ground.name = "QA_GROUND_PLANE"
    move_to(ground, guides)

    camera_specs = {
        "CAM_FRONT_ORTHO": ((0, 11, 2.5), True),
        "CAM_LEFT_ORTHO": ((-11, 0, 2.5), True),
        "CAM_RIGHT_ORTHO": ((11, 0, 2.5), True),
        "CAM_BACK_ORTHO": ((0, -11, 2.5), True),
        "CAM_TOP_ORTHO": ((0, 0, 13), True),
        "CAM_BOTTOM_ORTHO": ((0, 0, -10), True),
        "CAM_3Q_FRONT": ((8, 9, 6), False),
        "CAM_3Q_REAR": ((-8, -9, 6), False),
    }
    camera_objects = {name: camera(name, location, (0, 0, 2.35), orthographic, cameras) for name, (location, orthographic) in camera_specs.items()}
    area_light("KEY_LIGHT", (4, 5, 8), 1100, 5, lights)
    area_light("FILL_LIGHT", (-5, 2, 5), 700, 4, lights)
    area_light("RIM_LIGHT", (0, -5, 7), 850, 3, lights)

    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1024
    scene.render.resolution_y = 1024
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.world.color = (0.045, 0.045, 0.045)
    scene.unit_settings.system = "METRIC"
    scene["character_id"] = "NT-001"
    scene["asset_id"] = "NT001-3D-BLOCKOUT-001"
    scene["version"] = "0.1.0"
    scene["status"] = "CANDIDATE"
    scene["authoritative_inputs"] = "production-reference.v0.1.json; character.json; CROSS_VIEW_RECONCILIATION_v0.1.md"
    scene["reference_sha256"] = "032a0abb8d580e8850d147ffff45ac0ba0b1ab5827ff79e658e5d51c71ecaccd"

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    for name, cam in camera_objects.items():
        scene.camera = cam
        scene.render.filepath = str(RENDER_DIR / f"NT001_BLOCKOUT_v001_{name.replace('CAM_', '')}.png")
        bpy.ops.render.render(write_still=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(MODEL_PATH))


if __name__ == "__main__":
    main()
