# No crear aplicaciones en la raíz

## Alcance

Siempre que se añada una UI, API, agente, pipeline o script nuevo.

## Justificación

`README.es.md` define una carpeta por responsabilidad. `packages/README.es.md` habla de `apps/`, pero en este repo la carpeta real de frontends es `uis/` (`uis/README.es.md`).

## Guía

- Interfaz visual → `uis/` (p. ej. `uis/website/`).
- API o worker → `services/`.
- Agente → `agents/<nombre>/`.
- Pipeline de datos → `data/pipelines/`.
- No crear una carpeta `apps/`.
- Cada pieza nueva = subcarpeta + README. No dejar `index.html` ni APIs sueltas en la raíz.
