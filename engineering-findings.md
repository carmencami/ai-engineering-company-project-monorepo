# Fase 2 — Hallazgos de ingeniería

Repo: [carmencami/ai-engineering-company-project-monorepo](https://github.com/carmencami/ai-engineering-company-project-monorepo)
Empresa: **Nexova Solutions**
Fecha: 2026-09-03
Base: `verification.md` (Fase 1) y el código/documentación reales del repo.

Este archivo cubre los cuatro puntos del enunciado:

1. Convenciones útiles y patrones de riesgo
2. Filtro: solo hallazgos ligados a archivos, carpetas o comportamientos concretos
3. Hallazgos agrupados por categoría
4. Reglas propuestas; cada una cita al menos un hecho del repositorio

---

## 1. Convenciones y patrones

### Convenciones útiles (para quien contribuya o para un agent)

- El monorepo se organiza por responsabilidad, no por hito. Lo dice `README.es.md`: UI en `uis/`, API en `services/`, datos en `data/`, IA en `agents/` + `skills/` + `mcps/`.
- Casi cada carpeta de primer nivel trae `README.md` y `README.es.md`.
- Cada app, servicio, agente o pipeline nuevo debe nacer como subcarpeta + README (`README.es.md`, “Cómo empezar”, puntos 5 y 6).
- `CONTEXT.md` es la fuente de verdad del dominio. En este fork ya contiene el briefing de Nexova.
- El flujo de datos previsto está escrito en `README.es.md` y en `data/pipelines/README.es.md`: `data/raw/` → `data/pipelines/` → `data/process/` → `data/eval/`.
- Hay dos sitios de reutilización distintos: `packages/` (código versionable; existe `@repo/shared-types` en `packages/shared/package.json`) y `shared/` (recursos no empaquetados, según `shared/README.es.md`).
- Los agentes nuevos deberían partir de `agents/_template/` (`agents/_template/README.es.md`).

### Patrones de riesgo (pueden liar a una persona o a un agent)

- `README.es.md` lista `docker-compose.yml` en la raíz. Ese archivo no existe.
- `README.es.md` sigue diciendo que `CONTEXT.md` es un placeholder. Ya no lo es.
- `CONTEXT.es.md` sigue el placeholder (Chile + Argentina). `CONTEXT.md` sitúa Nexova en Valencia y Miami.
- `agents/_template/README.es.md` afirma que incluye código, configuración y tests. En `agents/_template/` y `agents/_template/tests/` solo hay README.
- `.devcontainer/post-create.sh` ejecuta `uv sync`. No hay `pyproject.toml` ni `uv.lock`.
- `skills/data-analysis/scripts/pandas_clean.py` lee `data.csv`. Ese archivo no está en el repo.
- `packages/README.es.md` habla de consumir paquetes desde `apps/`. En este repo la carpeta de frontends se llama `uis/`.

---

## 2. Filtro de especificidad

Se descartan frases vagas que no se pueden señalar en el repo, por ejemplo: “el código debería ser limpio”, “hay que documentar mejor”, “cuidado con la IA”, “el monorepo está desordenado”.

Se mantienen solo los hallazgos de la sección 1. Cada uno apunta a un archivo, una carpeta o un comportamiento comprobable (archivo mencionado que no existe, texto de un README que no coincide con el disco, script que asume un input ausente).

---

## 3. Hallazgos por categoría

### Arquitectura

- Carpetas de primer nivel = una responsabilidad (`README.es.md`).
- Flujo de datos `raw` → `pipelines` → `process` → `eval`.
- `packages/` vs `shared/` son capas distintas.
- No hay stack ejecutable: `uis/` y `services/` solo contienen README.

### Naming

- La carpeta de interfaces es `uis/`, no `apps/` (`packages/README.es.md` usa el nombre incorrecto para este repo).
- Documentación bilingüe: `README.md` / `README.es.md`.
- Convención de agentes: una subcarpeta por agente; punto de partida `_template/`.

### Documentación

- El README raíz promete `docker-compose.yml` y un `CONTEXT.md` placeholder; el disco no coincide.
- `CONTEXT.es.md` está desfasado respecto a `CONTEXT.md`.
- `agents/_template/README.es.md` describe una plantilla de código que no está implementada.

### DX (experiencia de desarrollo)

- `.devcontainer/devcontainer.json` reserva puertos 3000, 8000 y 5678; nada los escucha.
- `.devcontainer/post-create.sh` llama a `uv sync` sin manifiesto Python.
- `pandas_clean.py` no se puede ejecutar tal cual: falta `data.csv`.

### Testing

- Existe `agents/_template/tests/`, pero solo con README. No hay tests ejecutables en el repo.

---

## 4. Reglas propuestas

Cada regla es una orden para contribuidores y agents. El **hecho** es la evidencia en este repositorio.

### R1. No crear aplicaciones en la raíz

Las interfaces van en `uis/`. Las APIs van en `services/`.
**Hecho:** `README.es.md` (regla rápida y árbol del repositorio).

### R2. Tratar `CONTEXT.md` como única fuente de verdad de Nexova

No usar `CONTEXT.es.md` para datos de dominio (sedes, cifras, departamentos).
**Hecho:** `CONTEXT.md` describe Valencia y Miami; `CONTEXT.es.md` sigue el placeholder con Chile + Argentina.

### R3. No asumir que existe un archivo solo porque el README lo nombra

Comprobar el disco antes de orquestar, importar o documentar dependencias.
**Hecho:** `README.es.md` lista `docker-compose.yml`; el archivo no está en la raíz.

### R4. No copiar `agents/_template/` como si fuera código listo

Hoy es documentación. Un agente nuevo hay que crearlo (subcarpeta + README); no hay código, config ni tests que clonar.
**Hecho:** `agents/_template/` y `agents/_template/tests/` contienen solo README; el propio `agents/_template/README.es.md` promete lo contrario.

### R5. Código reutilizable en `packages/`; assets sueltos en `shared/`

Si dos apps van a importar tipos o librerías, van a `packages/`. Esquemas, plantillas y estáticos van a `shared/`.
**Hecho:** existe `packages/shared/package.json` (`@repo/shared-types`); `shared/README.es.md` reserva esa carpeta a recursos no empaquetados.

### R6. Los pipelines de datos viven en `data/pipelines/`

Origen en `data/raw/`, salida en `data/process/`, evaluación en `data/eval/`.
**Hecho:** `data/pipelines/README.es.md` y el flujo descrito en `README.es.md`.

### R7. No tratar `.devcontainer/post-create.sh` como setup completo del stack

El script no deja una app ni un entorno Python de proyecto listo para ejecutar.
**Hecho:** `post-create.sh` ejecuta `uv sync`; no existen `pyproject.toml` ni `uv.lock`.

### R8. Toda skill nueva debe incluir `SKILL.md`

El README de skills lo pide; el ejemplo actual no lo cumple. No repetir ese hueco.
**Hecho:** `skills/README.es.md` describe cada skill como carpeta con `SKILL.md`; `skills/data-analysis/` no tiene ese archivo.

### R9. Cada entrega nueva = subcarpeta + README

No dejar HTML, APIs o scripts sueltos en la raíz del monorepo.
**Hecho:** `README.es.md`, “Cómo empezar”, puntos 5 y 6.

### R10. Si un documento dice `apps/`, en este repo significa `uis/`

No crear una carpeta `apps/` por seguir un README interno desalineado.
**Hecho:** `packages/README.es.md` cita `apps/`; la carpeta real de frontends es `uis/` (`uis/README.es.md`).
