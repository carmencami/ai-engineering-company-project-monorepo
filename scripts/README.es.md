# Carpeta `scripts`

Esta carpeta contiene **scripts auxiliares** del monorepo: automatizaciones de desarrollo, utilidades de mantenimiento, tareas repetitivas (setup, lint, migraciones, generación de datos, etc.) y tooling interno.

- **Propósito principal**: agrupar herramientas de soporte que no pertenecen a una app/agente/pipeline específico, pero facilitan el trabajo del equipo.
- **Recomendación**: documenta cada script (qué hace, parámetros, requisitos, ejemplos de uso) y procura que sean reproducibles (y seguros) en distintos entornos.

### `check_rules.py`

Comprueba que las reglas de `.agents/rules/` se cumplen en el disco.

```bash
python scripts/check_rules.py
```

Sin dependencias extra. Debe ejecutarse desde cualquier sitio: resuelve la raíz del repo solo. Código de salida `0` si todo PASS, `1` si hay FAIL.
