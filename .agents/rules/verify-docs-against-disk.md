# No fiarse del README sin mirar el disco

## Alcance

Antes de ejecutar, importar o documentar un archivo que “debería existir”.

## Justificación

`README.es.md` lista `docker-compose.yml` en la raíz. Ese archivo no existe. El mismo README dice que `CONTEXT.md` es un placeholder; en este fork ya es Nexova.

## Guía

- Si el README nombra un archivo, comprueba que está en el repo.
- No crees `docker-compose.yml` vacío “porque el README lo pide” hasta que un hito lo exija de verdad.
- No arranques servicios, puertos ni compose que no existan.
