import pandas as pd

def cargar_datos():
    # Cargar datos limpios
    df = pd.read_csv('data/entregas_limpias.csv', parse_dates=['fecha_salida'])
    
    # KPIs precalculados
    kpi_total_entregas = len(df)
    kpi_tasa_retraso = (df['estado'] == 'Retrasado').mean() * 100
    kpi_margen_promedio = df['margen_neto'].mean()
    kpi_penalizacion_total = df['penalizacion'].sum()
    
    return df, (kpi_total_entregas, kpi_tasa_retraso, kpi_margen_promedio, kpi_penalizacion_total)