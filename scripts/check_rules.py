"""Comprueba que las reglas de .agents/rules/ se cumplen en este repo.

Uso (desde la raíz del monorepo):
    python scripts/check_rules.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
passed = 0
failed = 0


def check(name: str, ok: bool, detail: str) -> None:
    global passed, failed
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}: {detail}")
    if ok:
        passed += 1
    else:
        failed += 1


def main() -> int:
    context = (ROOT / "CONTEXT.md").read_text(encoding="utf-8")
    context_es = (ROOT / "CONTEXT.es.md").read_text(encoding="utf-8")
    template_code = [
        p
        for p in (ROOT / "agents" / "_template").rglob("*")
        if p.is_file()
        and p.suffix.lower() in {".py", ".ts", ".js"}
        and p.stat().st_size > 0
    ]

    check(
        "monorepo-layout",
        (ROOT / "uis").is_dir()
        and (ROOT / "services").is_dir()
        and not (ROOT / "apps").exists()
        and not (ROOT / "index.html").exists(),
        "existen uis/ y services/; no hay apps/ ni index.html en la raíz",
    )
    check(
        "context-source-of-truth",
        "Valencia" in context
        and "Miami" in context
        and "Fuente de verdad" in context_es
        and "CONTEXT.md" in context_es,
        "CONTEXT.md describe Valencia/Miami; CONTEXT.es.md avisa que no es la fuente",
    )
    check(
        "verify-docs-against-disk",
        not (ROOT / "docker-compose.yml").exists(),
        "docker-compose.yml no existe (el README lo nombra, el disco no)",
    )
    check(
        "agents-template",
        len(template_code) == 0,
        "agents/_template no tiene implementación (agent.py vacío no cuenta)",
    )
    check(
        "packages-vs-shared",
        (ROOT / "packages" / "shared" / "package.json").is_file()
        and (ROOT / "packages" / "shared" / "types" / "index.ts").is_file()
        and (ROOT / "shared" / "README.es.md").is_file(),
        "tipos en packages/shared/; shared/ sigue siendo assets/docs",
    )
    check(
        "data-pipeline-layout",
        all(
            (ROOT / "data" / folder).is_dir()
            for folder in ("raw", "pipelines", "process", "eval")
        ),
        "existen data/raw, pipelines, process y eval",
    )
    check(
        "devcontainer-is-not-the-stack",
        (ROOT / ".devcontainer" / "post-create.sh").is_file()
        and not (ROOT / "pyproject.toml").exists()
        and not (ROOT / "uv.lock").exists(),
        "post-create.sh existe; no hay pyproject.toml ni uv.lock",
    )
    check(
        "skills-require-skill-md",
        (ROOT / "skills" / "data-analysis" / "SKILL.md").is_file(),
        "skills/data-analysis/SKILL.md existe",
    )

    print()
    print(f"Resultado: {passed} PASS, {failed} FAIL")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
