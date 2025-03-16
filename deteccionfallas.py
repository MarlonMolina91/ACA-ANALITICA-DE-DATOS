df['Hora'] = df['FechaHora'].dt.hour

# Analizar fallas por hora
fallas_por_hora = df[df['Barnizado_OK'] == "No"].groupby('Hora').size()

# 📊 Graficar fallas por hora
plt.figure(figsize=(10,5))
fallas_por_hora.sort_index().plot(kind='bar', color='blue')
plt.xlabel("Hora del Día")
plt.ylabel("Cantidad de Fallas")
plt.title("Patrón de Fallas por Hora")
plt.show()
