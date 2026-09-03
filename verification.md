# Fase 1 — Verificación del handover

Repo: [carmencami/ai-engineering-company-project-monorepo](https://github.com/carmencami/ai-engineering-company-project-monorepo)
Empresa: **Nexova Solutions**
Fecha: 2026-09-03

Este archivo es el rastro de la Fase 1: mapear estructura, servicios y entry points, resumir el proyecto y verificar el resumen contra el código real.

Leyenda: ✅ coincide con el código · ❌ no coincide · ❓ no se puede comprobar todavía (no existe código ejecutable)

---

## 1. Fork y clon

| Comprobación | Resultado |
|---|---|
| El repo está en mi cuenta de GitHub | ✅ `https://github.com/carmencami/ai-engineering-company-project-monorepo.git` |
| Está clonado en local y abierto en Cursor | ✅ |
| Rama actual | ✅ `main` |
| `CONTEXT.md` ya no es el placeholder | ✅ briefing oficial de Nexova |
| `company-choice.md` existe en la raíz | ✅ |

---

## 2. Mapa de estructura, servicios y entry points

### Estructura real (primer nivel)

```text
ai-engineering-company-project-monorepo/
├── CONTEXT.md              briefing de Nexova (fuente de verdad)
├── CONTEXT.es.md           placeholder antiguo (no actualizado)
├── company-choice.md       elección de empresa (hito 0)
├── README.md / README.es.md
├── .devcontainer/          Codespaces (devcontainer.json + post-create.sh)
├── uis/                    solo READMEs — sin website ni backoffice
├── services/               solo READMEs — sin API
├── data/raw|pipelines|process|eval/   solo READMEs — sin datasets
├── agents/_template/       solo READMEs — sin código de agente
├── agents/tools/           solo READMEs
├── skills/data-analysis/   ejemplo (pandas_clean.py + common_metrics.md)
├── mcps/                   solo READMEs
├── workflows/              solo READMEs
├── packages/shared/        package.json + types/index.ts
├── shared/                 solo READMEs
├── docs/                   solo READMEs
├── infra/                  solo READMEs
├── scripts/                solo READMEs
└── internal/               solo READMEs
```

### Servicios

No hay servicios en ejecución. `services/` está vacía de código. No existe FastAPI, no hay routers, no hay `docker-compose.yml`.

### Entry points reales (lo que sí existe)

| Entry point | Existe | Qué hace |
|---|---|---|
| `CONTEXT.md` | ✅ | Contexto de Nexova para todo el curso |
| `company-choice.md` | ✅ | Justificación del hito 0 |
| `.devcontainer/devcontainer.json` | ✅ | Entorno Codespaces; puertos 3000, 8000, 5678 |
| `.devcontainer/post-create.sh` | ✅ | Intenta `corepack/pnpm` y `uv sync` |
| `packages/shared/types/index.ts` | ✅ | Tipos genéricos (`Id`, `BaseEntity`) |
| `skills/data-analysis/scripts/pandas_clean.py` | ✅ | Snippet de ejemplo; pide `data.csv` que no está en el repo |

### Rutas HTTP / de aplicación

| Ruta | Resultado |
|---|---|
| `/` landing | ❌ no existe `index.html` ni app web |
| `/application` formulario | ❌ no existe |
| `/api` o cualquier endpoint FastAPI | ❌ no existe |
| Rutas de Next.js (`app/`, `pages/`) | ❌ no existen |

Hoy **no hay rutas que comprobar en un navegador**. Las únicas “rutas” son carpetas del monorepo.

Puertos reservados en el devcontainer (para hitos futuros, no activos ahora):

- `3000` — UI
- `8000` — API
- `5678` — automatización (p. ej. n8n)

---

## 3. Resumen del proyecto

**Qué hace.** Es la plantilla del proyecto transversal de AI Engineering (4Geeks). No es todavía un producto de Nexova: es el esqueleto donde se irán construyendo la web, la API, los datos, los agentes y los workflows de esa empresa.

**Cómo se conecta.** Aún no hay conexiones reales entre piezas. El README define la intención:

- `CONTEXT.md` alimenta el dominio
- `uis/` = lo que ve un humano
- `services/` = API
- `data/` = raw → pipelines → process → eval
- `agents/` + `skills/` + `mcps/` = IA
- `workflows/` = automatización
- `packages/` / `shared/` = reutilización

Eso es diseño futuro, no código cableado.

**Cómo se ejecuta.** No hay comando para levantar el stack. No hay `package.json` en la raíz, no hay `pyproject.toml`, no hay `docker-compose.yml`. En Codespaces, `post-create.sh` corre al crear el entorno, pero `uv sync` no tiene manifiesto que sincronizar. El único script Python de ejemplo (`pandas_clean.py`) no es una app y depende de un `data.csv` externo.

---

## 4. Verificación del resumen contra el código

| Afirmación (README u observación) | Código real | Marca |
|---|---|---|
| Es una plantilla de carpetas + documentación, no un producto ejecutable | No hay apps, APIs ni HTML | ✅ |
| `CONTEXT.md` es un placeholder | Ya contiene el briefing de Nexova | ❌ (desactualizado en README.es.md) |
| `CONTEXT.es.md` describe Nexova (Chile + Argentina) | Sigue siendo placeholder; el briefing real es Valencia + Miami | ❌ |
| Existe `AGENTS.md` en la raíz | No existe | ✅ (el README ya lo dice) |
| Existe `docker-compose.yml` en la raíz | No existe | ❌ (el README lo lista como si existiera) |
| `uis/` tiene `website/` y `backoffice/` | Solo README.md / README.es.md | ❌ |
| `services/` tiene una API FastAPI | Solo READMEs | ❌ |
| `agents/_template` incluye código, config y tests | Solo READMEs en `_template/` y `_template/tests/` | ❌ |
| Cada skill tiene `SKILL.md` | `skills/data-analysis/` no tiene `SKILL.md` | ❌ |
| `@repo/shared-types` existe | `packages/shared/package.json` + `types/index.ts` | ✅ |
| Hay runner de workspace en la raíz | No hay `package.json` ni `pnpm-workspace.yaml` | ✅ (el README ya lo dice) |
| `post-create.sh` deja el entorno listo con `uv sync` | No hay `pyproject.toml` ni `uv.lock` | ❌ |
| El sitio / la API se pueden abrir en 3000 o 8000 | Nada escucha esos puertos | ❌ |
| Nexova es la empresa del proyecto | `CONTEXT.md` y `company-choice.md` | ✅ |

### Correcciones al resumen inicial

1. No decir “el stack se orquesta con docker-compose”: ese archivo no está.
2. No decir “CONTEXT.md es un placeholder”: en este fork ya es Nexova.
3. No decir “hay una API o una web”: no hay rutas ni procesos.
4. `CONTEXT.es.md` no es fuente de verdad; usar solo `CONTEXT.md`.
5. `agents/_template` es una carpeta de documentación, no una plantilla de código lista para copiar.

---

## 5. Qué debo saber para seguir

- Trabajar **dentro de la carpeta correcta** (`uis/` para web, `services/` para API). No llenar la raíz.
- No inventar datos de Nexova: leer `CONTEXT.md`. Cada hito puede traer un CONTEXT extra (por ejemplo el de web fundamentals, con campos de formulario).
- Este handover está cerrado: el repo está entendido, las contradicciones del README están marcadas, y no hay servicios que arrancar todavía.
