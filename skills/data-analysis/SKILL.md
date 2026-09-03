# Skill: data-analysis

## Cuándo usarla

Al limpiar o resumir datasets tabulares del proyecto (CSV/JSON) y al consultar definiciones de KPIs.

## Inputs

- Un archivo de datos (CSV, JSON o Excel).
- Columnas clave a conservar o rellenar.

## Outputs

- Dataset con columnas nulas vacías eliminadas, nombres normalizados y duplicados opcionales quitados.
- Métricas de referencia en `resources/common_metrics.md` (incluye KPIs HR estilo Nexova: turnover, absentismo, time to fill).

## Cómo ejecutar el ejemplo

```bash
python skills/data-analysis/scripts/pandas_clean.py
```

El script de ejemplo lee `data.csv` en el directorio de trabajo. Ese archivo **no está en el repo**; hay que aportarlo o adaptar la ruta. Requiere `pandas`.
