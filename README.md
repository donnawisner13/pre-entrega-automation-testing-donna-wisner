# Proyecto de Automatización de Pruebas - Final

## Propósito del proyecto

## Propósito del proyecto
El objetivo es desarrollar un framework de automatización que permita validar funcionalidades tanto de **interfaz de usuario (UI)** como de **API**.
---

##  Tecnologías utilizadas
- **Python 3.13**
- **Pytest** → framework de testing
- **Selenium WebDriver** → automatización de interfaz web
- **Requests** → pruebas de API
- **Pytest-HTML** → generación de reportes HTML
- **Logging** → registro de la ejecución de las pruebas
- **WebDriver Manager** → gestión automática del driver del navegador
- **Git / GitHub** → control de versiones
---
##  Flujos cubiertos

UI:
- Login exitoso y parametrizado (incluye caso negativo)
- Navegación del catálogo
- Agregado de productos al carrito
- Checkout completo
- Logout

API:
- **GET** → obtener recursos
- **POST** → crear recursos
- **DELETE** → eliminación de recursos

##  Instrucciones de instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/donnawisner13/pre-entrega-automation-testing-donna-wisner.git
   cd pre-entrega-automation-testing-donna-wisner

2. Instalar las dependencias:
   pip install selenium pytest pytest-html webdriver-manager

3. Ejecutar las pruebas con reporte HTML
   python run_tests.py
   -- El script run_test ejecuta todas las pruebas dentro de la carpeta /tests --
   -- El reporte se genera dentro de la carpeta reports/ --

## Estructura básica del proyecto

Entrega_Final/
│
├── pages/          # Page Objects (UI)
├── tests/          # Tests de UI
├── tests_api/      # Tests de API
├── utils/          # Utilidades (driver, logging, carga de datos)
├── datos/          # Datos externos (CSV / JSON)
├── reports/        # Reportes HTML y screenshots
├── logs/           # Logs de ejecución
│
├── conftest.py
├── pytest.ini
├── run_tests.py
└── README.md

## Reportes
Las ejecuciones generan un reporte HTML automático que incluye:
- listado de tests ejecutados
- estado (passed / failed)
- duración
- capturas de pantalla en caso de fallos de UI

El reporte se guarda en reports/report.html

## Logging
Se implementó un sistema de logging que registra pasos clave durante la ejecución de las pruebas.
Se guardan en logs/suite.logs