from dash import html, dcc, dash_table

def crear_tarjeta_kpi(titulo, valor, color='#2C3E50'):
    """Crea una tarjeta para mostrar un KPI"""
    return html.Div(
        children=[
            html.H4(titulo, style={'fontSize': '14px', 'marginBottom': '5px'}),
            html.P(valor, style={'fontSize': '24px', 'fontWeight': 'bold', 'color': color, 'margin': '0'})
        ],
        style={
            'border': f'2px solid {color}',
            'borderRadius': '10px',
            'padding': '15px',
            'margin': '5px',
            'textAlign': 'center',
            'boxShadow': '2px 2px 8px rgba(0,0,0,0.1)',
            'backgroundColor': 'white'
        }
    )

def crear_mapa():
    """Componente del mapa de rutas"""
    return dcc.Graph(id='mapa-rutas', config={'displayModeBar': True})

def crear_grafico_cascada():
    """Componente del gráfico de cascada financiera"""
    return dcc.Graph(id='waterfall-chart')

def crear_grafico_barras():
    """Componente del gráfico de barras por producto"""
    return dcc.Graph(id='bar-chart-productos')

def crear_tabla_pedidos():
    """Tabla interactiva de pedidos"""
    return dash_table.DataTable(
        id='tabla-pedidos',
        columns=[
            {'name': 'Pedido', 'id': 'id_pedido'},
            {'name': 'Producto', 'id': 'producto'},
            {'name': 'País', 'id': 'pais'},
            {'name': 'Ciudad', 'id': 'ciudad'},
            {'name': 'Estado', 'id': 'estado'},
            {'name': 'Margen Neto', 'id': 'margen_neto'},
            {'name': 'Penalización', 'id': 'penalizacion'}
        ],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '8px',
            'fontSize': '12px'
        },
        style_header={
            'backgroundColor': '#2C3E50',
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'filter_query': '{estado} = "Retrasado"'},
                'backgroundColor': '#ffdddd',
                'color': 'darkred'
            }
        ]
    )