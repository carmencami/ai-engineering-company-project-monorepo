# Estado actual

Evidencia: árbol del repo, `verification.md`, `docs/phase-3-validation.md`, `python scripts/check_rules.py` (8 PASS). No se inventa un roadmap de producto.

## Qué funciona

- `CONTEXT.md` con el briefing de Nexova (Valencia / Miami).
- `company-choice.md` (hito 0 entregado).
- Handover documentado: `verification.md`, `engineering-findings.md`.
- Reglas de agent en `.agents/rules/` y prueba `python scripts/check_rules.py`.
- `skills/data-analysis/SKILL.md` + script de ejemplo (el ejemplo necesita un `data.csv` que **no** está en el repo).
- Estructura de carpetas del monorepo (`uis/`, `services/`, `data/`, `agents/`, etc.) con READMEs.

## Gaps conocidos

- No hay UI (`uis/` sin `website/`).
- No hay API (`services/` vacío de código).
- No hay `docker-compose.yml` ni manifiesto Python/JS de workspace.
- `agents/_template/agent.py` está vacío; no hay agentes ejecutables.
- `CONTEXT.es.md` sigue siendo placeholder (con aviso de no usarlo).
- El README raíz sigue describiendo un `CONTEXT.md` placeholder y un compose que no está.

## Siguientes prioridades (curso, no claims de producto)

Prioridad inmediata del temario de 4Geeks: **Hito 1 — sitio web público** (HTML, Tailwind, formulario), usando el CONTEXT de web fundamentals además de `CONTEXT.md`. Eso aún **no está construido**.

Intención del hito 0 (`company-choice.md`), para hitos posteriores, no para ahora: pipeline de selección con scoring/ranking de CVs y RAG sobre candidatos. No existe código de eso en este repo.
