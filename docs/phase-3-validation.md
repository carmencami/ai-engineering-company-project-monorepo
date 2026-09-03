# Fase 3 — Validación de reglas

Las reglas no se dan por buenas solo por existir. Se comprueban con:

```bash
python scripts/check_rules.py
```

Última ejecución (desde la raíz del repo): **8 PASS, 0 FAIL**.

| Regla | Qué comprueba el script | Resultado |
|---|---|---|
| `monorepo-layout.md` | Hay `uis/` y `services/`; no hay `apps/` ni `index.html` en la raíz | PASS |
| `context-source-of-truth.md` | `CONTEXT.md` cita Valencia y Miami; `CONTEXT.es.md` avisa que no es la fuente | PASS |
| `verify-docs-against-disk.md` | `docker-compose.yml` no está en disco | PASS |
| `agents-template.md` | `_template` no tiene implementación (un `agent.py` vacío no cuenta) | PASS |
| `packages-vs-shared.md` | Existen `@repo/shared-types` y `shared/README.es.md` | PASS |
| `data-pipeline-layout.md` | Existen `data/raw`, `pipelines`, `process` y `eval` | PASS |
| `devcontainer-is-not-the-stack.md` | Hay `post-create.sh` y no hay `pyproject.toml` | PASS |
| `skills-require-skill-md.md` | Existe `skills/data-analysis/SKILL.md` | PASS |

## Refino (la prueba falló y se corrigió)

La primera ejecución dio **7 PASS, 1 FAIL**: existía `agents/_template/agent.py` vacío. El script y la regla `agents-template.md` se ajustaron: un archivo vacío no es un agente listo. Tras el cambio, las 8 reglas pasan.
