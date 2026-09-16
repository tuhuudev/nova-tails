# Architecture Change Policy

After v0.1, modify the architecture only when at least one of these occurs:
- a real retained identity cannot be represented cleanly;
- an adapter requires an undocumented transformation;
- two media expose contradictory authority;
- dependency/version impact cannot be traced;
- AI production repeatedly needs missing identity/design context;
- physical proof demonstrates a necessary upstream design rule.

Prefer the smallest contract change that resolves the observed case.
