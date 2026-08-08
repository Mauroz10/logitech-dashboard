import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from data_loader import cargar_datos
from components import (
    crear_tarjeta_kpi, 
    crear_mapa, 
    crear_grafico_cascada, 
    crear_grafico_barras, 
    crear_tabla_pedidos
)
from callbacks import registrar_callbacks

# Cargar datos y KPIs iniciales
df, (kpi_entregas, kpi_retraso, kpi_margen, kpi_penal) = cargar_datos()

# Instanciar la app con tema Bootstrap
app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="LogiTech - Panel Logístico"
)
server = app.server  # Necesario para despliegue en Render

# Definir el layout completo
app.layout = dbc.Container([
    
    # Título principal
    html.H1("🚚 Panel de Control Logístico y de Ventas", className='text-center my-4'),
    html.Hr(),
    
    # Fila de KPIs
    dbc.Row([
        dbc.Col(crear_tarjeta_kpi("📦 Total Entregas", f"{kpi_entregas:,}"), width=3),
        dbc.Col(crear_tarjeta_kpi("⚠️ Tasa de Retraso", f"{kpi_retraso:.1f}%", '#E74C3C'), width=3),
        dbc.Col(crear_tarjeta_kpi("💵 Margen Promedio", f"${kpi_margen:,.2f}", '#27AE60'), width=3),
        dbc.Col(crear_tarjeta_kpi("🔻 Penalizaciones Totales", f"${kpi_penal:,.2f}", '#F39C12'), width=3),
    ], className='mb-4'),
    
    html.Hr(),
    
    # Filtros
    dbc.Row([
        dbc.Col([
            html.Label("🌎 Filtrar por País:"),
            dcc.Dropdown(
                id='dropdown-pais',
                options=[{'label': p, 'value': p} for p in sorted(df['pais'].unique())],
                multi=True,
                placeholder="Selecciona uno o más países..."
            )
        ], width=4),
        dbc.Col([
            html.Label("📅 Rango de Fechas:"),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=df['fecha_salida'].min(),
                end_date=df['fecha_salida'].max(),
                display_format='DD/MM/YYYY'
            )
        ], width=4),
        dbc.Col([
            html.Label(" "),  # Espacio para alinear el botón
            html.Br(),
            dbc.Button("🔍 Aplicar Filtros", id='btn-filtrar', color='primary', className='w-100')
        ], width=2)
    ], className='mb-4'),
    
    html.Hr(),
    
    # Mapa de rutas
    dbc.Row([
        dbc.Col(dcc.Loading(crear_mapa(), type='circle'), width=12)
    ], className='mb-4'),
    
    # Gráficos financieros
    dbc.Row([
        dbc.Col(dcc.Loading(crear_grafico_cascada(), type='circle'), width=6),
        dbc.Col(dcc.Loading(crear_grafico_barras(), type='circle'), width=6)
    ], className='mb-4'),
    
    # Tabla de pedidos
    dbc.Row([
        dbc.Col([
            html.H4("📋 Top 10 Pedidos con Mayor Penalización", className='text-center'),
            crear_tabla_pedidos()
        ], width=12)
    ])
    
], fluid=True)

# Registrar callbacks
registrar_callbacks(app, df)

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)