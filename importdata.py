import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("produccion_latas.csv", parse_dates=['FechaHora'])

# Mostrar primeras filas
print(df.head())

# Verificar qué máquinas fallan más
fallas_por_maquina = df[df['Barnizado_OK'] == "No"].groupby('Maquina').size()

# 📊 Graficar fallas por máquina
plt.figure(figsize=(8,5))
fallas_por_maquina.sort_values().plot(kind='bar', color='red')
plt.xlabel("Máquina")
plt.ylabel("Cantidad de Fallas")
plt.title("Máquinas con más fallas en el barnizado")
plt.show()
