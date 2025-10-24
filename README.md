# GEOPOSICION Y CREACION DE CLIENTES.


Una aplicacion web de Django en donde usamos APIS de mapas para el almacenamiento de datos geográficos.




## ✨ Características Principales

Este proyecto demuestra el uso de Django funciones de negocio: 1. CRUD de Clientes. 2. Almacenamiento de Coordenadas (Lat/Lon). 3. Visualizacion de Mapa Interactivo. 4. Enlace Directo a Google Maps.

* **Framework Robusto:** Implementado con el framework **Django** y la estructura de un proyecto y una aplicación (`core/`).
* **Consulta por Ciudad:** Permite buscar datos meteorológicos ingresando el nombre de una ciudad.
* **Seguridad:** Utiliza **variables de entorno** (`.env`) para gestionar la clave de la API del clima, manteniéndola fuera del repositorio.
* **Datos Clave:** Retorna la temperatura actual, la humedad, la sensación térmica y la velocidad del viento.
* **Fuente de Datos:** Consume la API de `<Geoapify>`.





## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12.3
* **Framework Web:** **Django**


* **Proveedor de API:** `<Geoapify>`





---

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el servidor de desarrollo de Django en tu máquina local.

### 1. Clonar el Repositorio

```bash
git clone <URL de tu repositorio en GitHub>
cd weather_project




# Crear el entorno virtual
python3 -m venv env

# Activar el entorno virtual
# En Linux/macOS:
source env/bin/activate
# En Windows (CMD):
# .\env\Scripts\activate