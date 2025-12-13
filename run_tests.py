"""
Script auxiliar para ejecutar tests usando pytest y markers.

Uso:
  python run_tests.py ui
  python run_tests.py api
  python run_tests.py all
  python run_tests.py        (por defecto: all)

Notas:
- El reporte HTML y las opciones de pytest se configuran en pytest.ini
- Este script solo decide qué tests correr según el marker
"""

import sys
import pytest

# Mapa entre argumento y expresión de markers
MARKS = {
    "ui": "ui",
    "api": "api",
    "all": "ui or api",
}

def main() -> int:
    # Si no se pasa argumento, se corre todo
    modo = sys.argv[1].lower() if len(sys.argv) > 1 else "all"

    if modo not in MARKS:
        print("Uso: python run_tests.py [ui|api|all]")
        return 2

    mark_expr = MARKS[modo]

    # Ejecuta pytest usando el marker elegido
    return pytest.main(["-m", mark_expr, "-v"])

if __name__ == "__main__":
    raise SystemExit(main())