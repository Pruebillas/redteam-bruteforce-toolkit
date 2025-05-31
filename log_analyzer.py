import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

with open('brute_force_attack.log', 'r') as file:
    logs = file.readlines()

success_attempts = sum(1 for line in logs if "Éxito" in line)
failed_attempts = sum(1 for line in logs if "Fallo" in line)

hours = [line.split()[0].split('.')[0] for line in logs if 'asctime' not in line]
hour_counts = Counter([h.split(':')[0] for h in hours])

print(f"\n[+] Análisis de Logs:")
print(f"Intentos exitosos: {success_attempts}")
print(f"Intentos fallidos: {failed_attempts}")

df = pd.DataFrame({
    'Tipo': ['Éxitos', 'Fallos'],
    'Cantidad': [success_attempts, failed_attempts]
})
print("\nTabla resumen:")
print(df.to_string(index=False))

plt.figure(figsize=(8, 4))
plt.bar(df['Tipo'], df['Cantidad'], color=['green', 'red'])
plt.title('Resultados del Ataque de Fuerza Bruta')
plt.ylabel('Cantidad')
plt.grid(True)
plt.tight_layout()
plt.savefig('results_summary.png')

plt.figure(figsize=(10, 4))
plt.plot(list(hour_counts.keys()), list(hour_counts.values()), marker='o', linestyle='-')
plt.title('Actividad de Ataque por Hora')
plt.xlabel('Hora')
plt.ylabel('Número de Eventos')
plt.grid(True)
plt.tight_layout()
plt.savefig('activity_by_hour.png')

print("\n[+] Gráficos generados: results_summary.png y activity_by_hour.png")