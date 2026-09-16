# Architecture Change Policy v0.1

After v0.1 scope freeze, architecture changes should cite the production observation that requires them.

Good reason:
> Print proof shows one signature can have multiple manufacturing representations; adapter manifest needs an explicit representation mapping.

Bad reason:
> We may someday have 500 characters, so build a database/service now.

Prefer the smallest compatible change that resolves observed production friction.
