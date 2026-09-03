# `scripts` folder

This folder contains **helper scripts** for the monorepo: development automation, maintenance utilities, repetitive tasks (setup, lint, migrations, data generation, etc.), and internal tooling.

- **Main purpose**: group support tools that do not belong to a specific app, agent, or pipeline but make the team’s work easier.
- **Recommendation**: document each script (what it does, parameters, requirements, usage examples) and keep them reproducible (and safe) across environments.

### `check_rules.py`

Checks that `.agents/rules/` still match the files on disk.

```bash
python scripts/check_rules.py
```

No extra dependencies. Exit code `0` if all PASS, `1` if any FAIL.

> _Spanish version: [README.es.md](./README.es.md)._
