from dash import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

def registrar_callbacks(app, df):
    """Registra todos los callbacks del dashboard"""
    
    # Callback para actualizar el mapa
    @app.callback(
        Output('mapa-rutas', 'figure'),
        Input('btn-filtrar', 'n_clicks'),
        State('dropdown-pais', 'value'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def actualizar_mapa(n_clicks, paises, fecha_inicio, fecha_fin):
        # Si no se seleccionan países, usar todos
        if paises is None or len(paises) == 0:
            paises = df['pais'].unique()
        
        dff = df[df['pais'].isin(paises)]
        
        if fecha_inicio and fecha_fin:
            dff = dff[(dff['fecha_salida'] >= fecha_inicio) & (dff['fecha_salida'] <= fecha_fin)]
        
        fig = px.scatter_mapbox(
            dff,
            lat='lat',
            lon='lon',
            color='estado',
            color_discrete_map={'A tiempo': '#27AE60', 'Retrasado': '#E74C3C'},
            hover_name='id_pedido',
            hover_data={
                'lat': False, 
                'lon': False, 
                'producto': True, 
                'ciudad': True,
                'dias_reales': True,
                'margen_neto': True
            },
            zoom=3,
            mapbox_style='carto-positron',
            title="📍 Rutas de Entrega por Estado"
        )
        fig.update_layout(
            margin={"r":0, "t":40, "l":0, "b":0},
            height=500
        )
        return fig
    
    # Callback para actualizar el gráfico de cascada
    @app.callback(
        Output('waterfall-chart', 'figure'),
        Input('btn-filtrar', 'n_clicks'),
        State('dropdown-pais', 'value'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def actualizar_cascada(n_clicks, paises, fecha_inicio, fecha_fin):
        if paises is None or len(paises) == 0:
            paises = df['pais'].unique()
        dff = df[df['pais'].isin(paises)]
        if fecha_inicio and fecha_fin:
            dff = dff[(dff['fecha_salida'] >= fecha_inicio) & (dff['fecha_salida'] <= fecha_fin)]
        
        ingresos = dff['ingreso_venta'].sum()
        costos = dff['costo_envio'].sum()
        penalizaciones = dff['penalizacion'].sum()
        margen = ingresos - costos - penalizaciones
        
        fig = go.Figure(go.Waterfall(
            name="Flujo Financiero",
            orientation="v",
            measure=["absolute", "relative", "relative", "total"],
            x=["Ingresos Brutos", "Costos de Envío", "Penalizaciones", "Margen Neto"],
            textposition="outside",
            text=[f"${ingresos:,.0f}", f"-${costos:,.0f}", f"-${penalizaciones:,.0f}", f"${margen:,.0f}"],
            y=[ingresos, -costos, -penalizaciones, 0],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#E74C3C"}},
            increasing={"marker": {"color": "#27AE60"}},
            totals={"marker": {"color": "#2C3E50"}}
        ))
        fig.update_layout(
            title="💰 Flujo Financiero",
            showlegend=False,
            height=400
        )
        return fig
    
    # Callback para actualizar el gráfico de barras
    @app.callback(
        Output('bar-chart-productos', 'figure'),
        Input('btn-filtrar', 'n_clicks'),
        State('dropdown-pais', 'value'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def actualizar_barras(n_clicks, paises, fecha_inicio, fecha_fin):
        if paises is None or len(paises) == 0:
            paises = df['pais'].unique()
        dff = df[df['pais'].isin(paises)]
        if fecha_inicio and fecha_fin:
            dff = dff[(dff['fecha_salida'] >= fecha_inicio) & (dff['fecha_salida'] <= fecha_fin)]
        
        top_productos = dff.groupby('producto')['margen_neto'].mean().sort_values(ascending=True).head(5).reset_index()
        
        fig = px.bar(
            top_productos, 
            x='margen_neto', 
            y='producto', 
            orientation='h',
            title='📦 Top 5 Productos por Margen Neto Promedio',
            labels={'margen_neto': 'Margen Neto (USD)', 'producto': 'Producto'},
            color='margen_neto',
            color_continuous_scale='Viridis'
        )
        fig.update_layout(
            yaxis={'categoryorder': 'total ascending'},
            height=400
        )
        return fig
    
    # Callback para actualizar la tabla
    @app.callback(
        Output('tabla-pedidos', 'data'),
        Input('btn-filtrar', 'n_clicks'),
        State('dropdown-pais', 'value'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def actualizar_tabla(n_clicks, paises, fecha_inicio, fecha_fin):
        if paises is None or len(paises) == 0:
            paises = df['pais'].unique()
        dff = df[df['pais'].isin(paises)]
        if fecha_inicio and fecha_fin:
            dff = dff[(dff['fecha_salida'] >= fecha_inicio) & (dff['fecha_salida'] <= fecha_fin)]
        
        # Top 10 pedidos con mayor penalización
        tabla = dff.nlargest(10, 'penalizacion')[
            ['id_pedido', 'producto', 'pais', 'ciudad', 'estado', 'margen_neto', 'penalizacion']
        ]
        # Redondear valores para mejor presentación
        tabla['margen_neto'] = tabla['margen_neto'].round(2)
        tabla['penalizacion'] = tabla['penalizacion'].round(2)
        return tabla.to_dict('records')