import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

n = 2000  # Número de entregas

# Datos base
paises = ['Colombia', 'México', 'Chile', 'Perú']
ciudades = {
    'Colombia': ['Bogotá', 'Medellín', 'Cali'],
    'México': ['CDMX', 'Monterrey', 'Guadalajara'],
    'Chile': ['Santiago', 'Valparaíso', 'Concepción'],
    'Perú': ['Lima', 'Arequipa', 'Trujillo']
}
productos = ['Laptop Pro', 'Monitor 4K', 'Teclado Mecánico', 'Mouse Ergonómico', 'Hub USB-C']

data = {
    'id_pedido': [f'PED-{i:05d}' for i in range(1, n+1)],
    'fecha_salida': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(n)],
    'pais': [random.choice(paises) for _ in range(n)],
    'producto': [random.choice(productos) for _ in range(n)],
}

df = pd.DataFrame(data)

# Asignar ciudad según país
df['ciudad'] = df.apply(lambda row: random.choice(ciudades[row['pais']]), axis=1)

# Tiempo de entrega esperado (días) según país base + ruido
base_dias = {'Colombia': 3, 'México': 5, 'Chile': 7, 'Perú': 6}
df['dias_previstos'] = df['pais'].map(base_dias) + np.random.poisson(lam=1, size=n)

# Días reales: a veces llegan antes, a veces después (introducimos retrasos)
df['dias_reales'] = df['dias_previstos'] + np.random.normal(loc=1, scale=2.5, size=n).astype(int)
df['dias_reales'] = df['dias_reales'].clip(lower=0)  # sin valores negativos

# Costos
df['costo_envio'] = df.apply(lambda row: np.random.normal(30 if row['pais'] == 'Colombia' else 50, 10), axis=1).clip(lower=5)
df['ingreso_venta'] = df.apply(lambda row: np.random.normal(300 if row['producto'].startswith('Laptop') else 100, 40), axis=1)

# Penalización: si días_reales > días_previstos, se cobra un extra por cada día de retraso
df['penalizacion'] = np.where(
    df['dias_reales'] > df['dias_previstos'],
    (df['dias_reales'] - df['dias_previstos']) * np.random.uniform(5, 15, size=n),
    0
)

# Estado
df['estado'] = np.where(df['dias_reales'] <= df['dias_previstos'], 'A tiempo', 'Retrasado')

# --- Introducimos errores adrede ---
# 1. Fechas en formato incorrecto (algunas cadenas en dd/mm/yyyy)
mask_fecha = np.random.choice([True, False], size=n, p=[0.05, 0.95])
df.loc[mask_fecha, 'fecha_salida'] = df.loc[mask_fecha, 'fecha_salida'].apply(
    lambda x: x.strftime('%d/%m/%Y')
)

# 2. Valores nulos en 'dias_reales' (simulamos que no se registró la entrega)
mask_null = np.random.choice([True, False], size=n, p=[0.03, 0.97])
df.loc[mask_null, 'dias_reales'] = np.nan

# 3. Coordenadas GPS aproximadas (inventamos lat/lon para las ciudades)
coords = {
    'Bogotá': (4.7110, -74.0721), 'Medellín': (6.2476, -75.5658), 'Cali': (3.4516, -76.5319),
    'CDMX': (19.4326, -99.1332), 'Monterrey': (25.6866, -100.3161), 'Guadalajara': (20.6597, -103.3496),
    'Santiago': (-33.4489, -70.6693), 'Valparaíso': (-33.0472, -71.6127), 'Concepción': (-36.8201, -73.0444),
    'Lima': (-12.0464, -77.0428), 'Arequipa': (-16.4090, -71.5375), 'Trujillo': (-8.1150, -79.0290)
}
df['lat'] = df['ciudad'].map(lambda x: coords.get(x, (0,0))[0])
df['lon'] = df['ciudad'].map(lambda x: coords.get(x, (0,0))[1])

# 4. Algunos códigos de producto mal escritos (minúsculas, espacios extra)
mask_prod = np.random.choice([True, False], size=n, p=[0.02, 0.98])
df.loc[mask_prod, 'producto'] = df.loc[mask_prod, 'producto'].str.lower().str.replace(' ', '_')

# Guardar archivo con errores
df.to_csv('data/entregas_sucias.csv', index=False)
print("Datos generados con errores: data/entregas_sucias.csv")