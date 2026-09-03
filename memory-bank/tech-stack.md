# Tech stack

Solo lo que existe en el disco. Si el README nombra algo y no está, se marca como ausente.

## Lenguajes (archivos reales)

- **Markdown** — documentación (`README`, `CONTEXT.md`, `.agents/rules/`, `memory-bank/`).
- **TypeScript** — `packages/shared/types/index.ts` (`Id`, `BaseEntity`). No hay `tsconfig.json` ni runner.
- **Python** — `scripts/check_rules.py` (stdlib); `skills/data-analysis/scripts/pandas_clean.py` (comenta que hace falta `pandas`); `agents/_template/agent.py` (archivo vacío).
- **Bash** — `.devcontainer/post-create.sh`.
- **JSON** — `.devcontainer/devcontainer.json`, `packages/shared/package.json`.

## Frameworks de producto

Ninguno instalado: no hay React, Next.js, FastAPI, Tailwind ni n8n en el repo.

## Infra y tooling

| Pieza | Evidencia | Estado |
|---|---|---|
| Git / GitHub | `.git/`, remote `carmencami/ai-engineering-company-project-monorepo` | En uso |
| Devcontainer | `.devcontainer/devcontainer.json` (imagen `universal:2`, puertos 3000, 8000, 5678) | Config de entorno; nada escucha esos puertos |
| pnpm vía Corepack | `post-create.sh` | No hay `package.json` en la raíz |
| `uv sync` | `post-create.sh` | No hay `pyproject.toml` ni `uv.lock` |
| `@repo/shared-types` | `packages/shared/package.json` v0.0.1 | Metadata; sin workspace runner |
| Agent rules | `.agents/rules/*.md` | Presentes |
| `docker-compose.yml` | Citado en `README.es.md` | **No existe** |

## Dependencias clave

- El script de pandas **no** declara `pandas` en un manifiesto del repo.
- `scripts/check_rules.py` no requiere paquetes extra.
