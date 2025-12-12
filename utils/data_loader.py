import csv
from pathlib import Path

def leer_datos_login_desde_csv(ruta: str):
    """
    Lee un archivo CSV con columnas: usuario, clave, debe_funcionar
    y devuelve una lista de tuplas (usuario, clave, debe_funcionar_bool)
    lista para usar en pytest.mark.parametrize.
    """
    ruta_csv = Path(ruta)

    datos = []
    with ruta_csv.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            usuario = fila["usuario"]
            clave = fila["clave"]
            debe_funcionar_str = fila["debe_funcionar"].strip()
            debe_funcionar = debe_funcionar_str.lower() == "true"
            datos.append((usuario, clave, debe_funcionar))
    return datos