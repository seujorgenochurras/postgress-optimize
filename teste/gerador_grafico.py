import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_json("teste/data.json")
data["timestamp"] = pd.to_datetime(data["timestamp"])


data["CPUPerc"] = data["CPUPerc"].str.replace("%", "").astype(float)


plt.figure(figsize=(10, 5))
plt.plot(data["timestamp"], data["CPUPerc"], marker="o", linestyle="-")
plt.xlabel("Tempo")
plt.ylabel("Uso de CPU (%)")
plt.title("Uso de CPU ao longo do tempo")
plt.grid()
plt.savefig("grafico.png")
plt.show(block=True)
