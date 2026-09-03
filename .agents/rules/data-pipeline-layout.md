# Los datos siguen raw → pipelines → process → eval

## Alcance

Al añadir datasets, jobs ETL o conjuntos de evaluación.

## Justificación

`README.es.md` y `data/pipelines/README.es.md` definen ese flujo. Hoy esas carpetas solo tienen README; no hay que romperlo cuando lleguen datos.

## Guía

- Fuentes sin tocar → `data/raw/`.
- Scripts de ingesta/limpieza → `data/pipelines/`.
- Salidas limpias → `data/process/`.
- Golden sets y métricas de IA → `data/eval/`.
- Documenta origen y PII en el README de cada dataset.
