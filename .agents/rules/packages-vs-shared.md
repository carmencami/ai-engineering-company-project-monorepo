# packages/ es código; shared/ son assets

## Alcance

Al extraer algo reutilizable entre apps, agentes o pipelines.

## Justificación

Existe `packages/shared/package.json` (`@repo/shared-types`). `shared/README.es.md` reserva esa carpeta a plantillas, esquemas y assets, no a librerías.

## Guía

- Tipos, SDKs, clientes → `packages/<paquete>/` con su `package.json` y README.
- Esquemas JSON, plantillas de email, tokens de diseño → `shared/`.
- No pongas librerías importables dentro de `shared/`.
