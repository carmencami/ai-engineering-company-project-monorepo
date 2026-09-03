# El devcontainer no levanta el producto

## Alcance

Al arrancar el proyecto, instalar deps o explicar cómo se ejecuta.

## Justificación

`.devcontainer/post-create.sh` ejecuta `uv sync`, pero no hay `pyproject.toml` ni `uv.lock`. `devcontainer.json` reserva puertos 3000, 8000 y 5678; nada los escucha.

## Guía

- No presentes `uv sync` ni esos puertos como un stack funcionando.
- No añadas `pyproject.toml` solo para que el script no falle, salvo que un hito pida un proyecto Python.
- Cuando haya web o API, documéntalas en su carpeta (`uis/`, `services/`) con el comando real.
