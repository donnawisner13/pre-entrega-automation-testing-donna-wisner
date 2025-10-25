"""
Script para ejecutar todos los tests de preentrega usando Pytest.
Genera un reporte HTML en la carpeta reports/.
"""

import pytest
import os

# Carpeta donde están los tests
tests_path = "tests"

# Carpeta para guardar reportes
reports_path = "reports"
os.makedirs(reports_path, exist_ok=True)  # crea la carpeta si no existe

# Archivo de reporte HTML
reporte_html = os.path.join(reports_path, "reporte.html")

# Ejecuta todos los tests dentro de tests/ y genera reporte HTML
pytest.main([tests_path, "-v", f"--html={reporte_html}", "--self-contained-html"])