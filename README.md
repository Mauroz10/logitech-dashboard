# 🚚 Panel de Control Logístico y de Ventas - LogiTech Distribution

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Dash](https://img.shields.io/badge/Dash-2.0+-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-orange.svg)
![Estado](https://img.shields.io/badge/Estado-Completo-brightgreen.svg)

Dashboard interactivo para monitorear operaciones logísticas y financieras en tiempo real. Desarrollado como proyecto de portafolio para demostrar habilidades en análisis de datos, visualización y desarrollo de aplicaciones web con Python.

---

🚀 **[🌐 Clic aquí para interactuar con el Dashboard en Vivo en Render](https://logitech-dashboard.onrender.com/)**

*(Nota: Al usar el plan gratuito de Render, la aplicación puede tardar cerca de 1 minuto en cargar en su primera visita mientras se activa el servidor de forma automática).*


## 📸 Vista Previa

![Dashboard Preview](screenshot.png)

---

## 🎯 Problema de Negocio

**LogiTech Distribution** enfrenta una caída en sus márgenes netos sin identificar claramente las causas. La gerencia necesita:

- Visualizar las rutas de entrega y los retrasos por ubicación geográfica.
- Identificar qué países, productos o tipos de envío generan pérdidas.
- Tomar decisiones correctivas basadas en datos en tiempo real.

---

## ✅ Solución Implementada

Este dashboard proporciona:

- **📍 Mapa interactivo** de rutas de entrega con estado de puntualidad (a tiempo/retrasado).
- **📊 KPIs en tiempo real**: total de entregas, tasa de retraso, margen promedio, penalizaciones.
- **🔍 Filtros dinámicos** por país (selección múltiple) y rango de fechas.
- **💰 Gráfico de cascada** que desglosa ingresos, costos y margen neto.
- **📦 Gráfico de barras** con los 5 productos más rentables.
- **📋 Tabla interactiva** de pedidos con mayor penalización, resaltando retrasos.

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Propósito |
|-------------|-----------|
| **Python 3** | Lenguaje principal |
| **Dash** | Framework para aplicaciones web analíticas |
| **Plotly** | Gráficos interactivos (mapas, cascada, barras) |
| **Pandas** | Limpieza, transformación y análisis de datos |
| **Jupyter Notebook** | Documentación del proceso ETL y EDA |
| **Bootstrap** | Estilos profesionales y diseño responsivo |
| **Render** | Despliegue gratuito en la nube |

---

## 📂 Estructura del Proyecto
logitech-dashboard/
├── data/
│ ├── generar_datos.py # Script de generación de datos sintéticos con errores
│ ├── entregas_sucias.csv # Dataset con errores intencionales
│ └── entregas_limpias.csv # Dataset limpio después del ETL
│
├── notebooks/
│ └── limpieza_datos.ipynb # Documentación del proceso de limpieza y EDA
│
├── dashboard/
│ ├── app.py # Orquestador principal del dashboard
│ ├── data_loader.py # Carga y preprocesamiento de datos
│ ├── components.py # Componentes visuales reutilizables
│ ├── callbacks.py # Lógica de interactividad
│ └── assets/ # Estilos CSS e imágenes
│
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo

text

---

## 📊 Proceso de Datos (ETL + EDA)

### 1. Generación de Datos Sintéticos
- 2,000 registros de entregas en 4 países (Colombia, México, Chile, Perú).
- Errores intencionales introducidos:
  - Fechas en formato incorrecto (5% de los registros).
  - Valores nulos en días reales de entrega (3%).
  - Nombres de productos mal escritos (2%).

### 2. Limpieza y Transformación
- Corrección de formatos de fecha inconsistentes.
- Imputación de valores nulos con supuestos documentados.
- Normalización de nombres de productos.
- Cálculo de margen neto: `Ingresos - Costos de envío - Penalizaciones`.

### 3. Análisis Exploratorio (EDA)
- Tasa de retraso promedio: **49.9%**.
- Productos más rentables identificados.
- Penalizaciones totales: **$24,493.00**.

*Todo el proceso está documentado en `notebooks/limpieza_datos.ipynb`.*

---

## 🚀 Cómo Ejecutar Localmente

### Requisitos Previos
- Python 3.9 o superior instalado.
- Git (opcional, para clonar el repositorio).

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Mauroz10/logitech-dashboard.git
cd logitech-dashboard

# 2. Crear y activar entorno virtual
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Generar datos sintéticos (opcional, ya incluidos)
python data/generar_datos.py

# 5. Ejecutar el dashboard
python dashboard/app.py
Abre tu navegador en http://127.0.0.1:8050.


💡 Habilidades Demostradas
✅ Limpieza de datos: manejo de valores nulos, formatos inconsistentes, normalización.

✅ Análisis exploratorio (EDA): identificación de patrones de retraso y rentabilidad.

✅ Visualización de datos: mapas geoespaciales, gráficos financieros, dashboards interactivos.

✅ Desarrollo web con Dash: callbacks, componentes modulares, diseño responsivo.

✅ Control de versiones: Git/GitHub con estructura profesional de proyecto.

✅ Despliegue en la nube: Render para aplicaciones Python.

📈 Próximas Mejoras
□ Integración con base de datos SQL (MySQL/PostgreSQL).
□ Autenticación de usuarios.
□ Exportación de reportes en PDF/Excel.
□ Alertas automáticas por correo cuando la tasa de retraso supere un umbral.
👤 Autor
Mauricio Medina Martinez

🔗 GitHub

💼 LinkedIn
