import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── CSV laden ───────────────────────────────────────────
df = pd.read_csv("ergebnisse/messung.csv", names=[
    "Zeit", "Label", "Avg_mA", "Peak_mA",
    "Min_uA", "Samples", "Dauer_s"
])
df["Avg_mA"] = df["Avg_mA"].astype(float)
df["Peak_mA"] = df["Peak_mA"].astype(float)

print("Geladene Messungen:")
print(df[["Label", "Avg_mA", "Peak_mA"]].to_string())

# ── Farben je Version ───────────────────────────────────
farben = {
    "v1_baseline_wroom32":              "#E74C3C",
    "v1_baseline_delivery_mini32":      "#E67E22",
    "v1_baseline_s3_wroom1":            "#F39C12",
    "v2_firmware_kein_sleep_30min":    "#E74C3C",
    "v3_patch1_deep_sleep_30min":      "#27AE60",
    "v4_patch2_light_sleep_30min":     "#1ABC9C",
    "v5_patch3_cpu_80mhz_wroom32": "#2980B9",
    "v6_patch4_wifi_bt_aus_wroom32": "#8E44AD",
    "v7_patch5_sensor_timing_wroom32": "#2C3E50",
}
standard_farbe = "#065A82"

# ── Plot 1: Balkendiagramm Durchschnittsstrom ───────────
fig, ax = plt.subplots(figsize=(12, 6))

balken_farben = [farben.get(l, standard_farbe) for l in df["Label"]]
balken = ax.bar(range(len(df)), df["Avg_mA"],
                color=balken_farben, edgecolor="white", width=0.6)

# Zielwert
ax.axhline(y=12.6, color="#02C39A", linestyle="--",
           linewidth=2, label="Projektziel: 12,6 mA")

# Werte über Balken
for i, (b, wert) in enumerate(zip(balken, df["Avg_mA"])):
    ax.text(b.get_x() + b.get_width()/2,
            b.get_height() + 0.5,
            f"{wert:.2f} mA",
            ha="center", fontsize=9, fontweight="bold")

ax.set_xticks(range(len(df)))
ax.set_xticklabels(df["Label"], rotation=25, ha="right", fontsize=9)
ax.set_ylabel("Ø Stromverbrauch (mA)", fontsize=12)
ax.set_title("Hochwasserpegel – Energieverbrauch je Firmware-Version",
             fontsize=14, fontweight="bold", pad=15)
ax.legend(fontsize=10)
ax.set_ylim(0, df["Avg_mA"].max() * 1.2)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("ergebnisse/grafiken/vergleich_strom_30min.png", dpi=150)
print("✅ Grafik 1 gespeichert")
plt.show()

# ── Plot 2: Ersparnis in Prozent ────────────────────────
baseline_idx = df[df["Label"].str.contains("kein_sleep")].index
if len(baseline_idx) > 0:
    baseline_mA = df.loc[baseline_idx[0], "Avg_mA"]
    df["Ersparnis_pct"] = ((baseline_mA - df["Avg_mA"]) / baseline_mA * 100)

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    farben2 = [farben.get(l, standard_farbe) for l in df["Label"]]
    balken2 = ax2.bar(range(len(df)), df["Ersparnis_pct"],
                      color=farben2, edgecolor="white", width=0.6)

    ax2.axhline(y=73, color="#02C39A", linestyle="--",
                linewidth=2, label="Projektziel: –73%")

    for b, wert in zip(balken2, df["Ersparnis_pct"]):
        ax2.text(b.get_x() + b.get_width()/2,
                 b.get_height() + 0.5,
                 f"{wert:.1f}%",
                 ha="center", fontsize=9, fontweight="bold")

    ax2.set_xticks(range(len(df)))
    ax2.set_xticklabels(df["Label"], rotation=25, ha="right", fontsize=9)
    ax2.set_ylabel("Ersparnis gegenüber Baseline (%)", fontsize=12)
    ax2.set_title("Hochwasserpegel – Energieersparnis je Patch",
                  fontsize=14, fontweight="bold", pad=15)
    ax2.legend(fontsize=10)
    ax2.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig("ergebnisse/grafiken/vergleich_ersparnis_30min.png", dpi=150)
    print("✅ Grafik 2 gespeichert")
    plt.show()