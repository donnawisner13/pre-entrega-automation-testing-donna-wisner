# Proyecto de Automatización de Pruebas - Preentrega

## Propósito del proyecto
Este proyecto tiene como objetivo automatizar pruebas funcionales en el sitio [SauceDemo](https://www.saucedemo.com/), utilizando **Selenium WebDriver** y **Pytest** como framework de testing.  
Permite validar el correcto funcionamiento de los siguientes flujos de usuario:
- Inicio de sesión
- Navegación y visualización del catálogo de productos
- Agregado de productos al carrito de compras

---

##  Tecnologías utilizadas
- Python 3.13
- Selenium WebDriver → automatización del navegador
- Pytest → ejecución de casos de prueba
- Pytest-HTML → generación de reportes en formato HTML
- WebDriver Manager → gestión automática del driver de Chrome

---

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

Preentrega/
│
├── reports/
│   └── reporte.html
│
├── tests/
│   ├── test_carrito.py
│   ├── test_login.py
│   └── test_nav_catalogo.py
│
├── utils/
│   ├── driver_setup.py
│   └── funciones_auxiliares.py
│
├── README.md
└── run_tests.py