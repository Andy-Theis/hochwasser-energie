import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ── CSV laden ───────────────────────────────────────────
df = pd.read_csv("ergebnisse/messung.csv", names=[
    "Zeit", "Label", "Avg_uA", "Peak_uA",
    "Min_uA", "Ladung_mAs", "Samples", "Dauer_s"
])
df["Avg_mA"] = df["Avg_uA"].astype(float) / 1000

# ── Balkendiagramm: Durchschnittsstrom je Patch ─────────
fig, ax = plt.subplots(figsize=(10, 5))
farben = ["#E74C3C", "#F39C12", "#F1C40F",
          "#2ECC71", "#1ABC9C", "#065A82"]
balken = ax.bar(df["Label"], df["Avg_mA"],
                color=farben[:len(df)], edgecolor="white")

# Zielwert einzeichnen
ax.axhline(y=12.6, color="#02C39A", linestyle="--",
           linewidth=2, label="Ziel: 12,6 mA")

ax.set_xlabel("Firmware-Version / Patch", fontsize=12)
ax.set_ylabel("Ø Stromverbrauch (mA)", fontsize=12)
ax.set_title("Energieverbrauch: Vorher / Nachher je Patch",
             fontsize=14, fontweight="bold")
ax.legend()

# Werte über Balken anzeigen
for balken_elem, wert in zip(balken, df["Avg_mA"]):
    ax.text(balken_elem.get_x() + balken_elem.get_width()/2,
            balken_elem.get_height() + 0.3,
            f"{wert:.1f} mA", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("ergebnisse/grafiken/vergleich.png", dpi=150)
plt.show()

# ── Zeitreihengrafik: Stromprofil eines Zyklus ──────────
def plot_stromprofil(label):
    try:
        raw = np.load(f"ergebnisse/{label}_raw.npy")
    except FileNotFoundError:
        print(f"Keine Rohdaten für {label}")
        return

    # PPK2 sampelt mit 100kHz → Zeit in ms
    zeit_ms = np.arange(len(raw)) / 100  # samples / 100kS/s → ms
    strom_mA = raw / 1000  # µA → mA

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(zeit_ms, strom_mA, linewidth=0.3, color="#065A82")
    ax.set_xlabel("Zeit (ms)")
    ax.set_ylabel("Strom (mA)")
    ax.set_title(f"Stromprofil: {label}")
    ax.set_yscale("log")  # Log-Skala zeigt Sleep+Peak zusammen
    plt.tight_layout()
    plt.savefig(f"ergebnisse/grafiken/profil_{label}.png", dpi=150)
    plt.show()

# Profil für jede Version anzeigen
for label in df["Label"]:
    plot_stromprofil(label)