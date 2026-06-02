from ppk2_api.ppk2_api import PPK2_API
import time, numpy as np, csv, datetime

DAUER    = 1800   # von 5 Minuten auf 30 minuten erhöht
LABEL    = "v4_patch2_light_sleep_30min"   # ← vor jedem Patch ändern!
SPANNUNG = 3300

geraete = PPK2_API.list_devices()
ppk2 = PPK2_API(geraete[0], timeout=1, exclusive=True)
ppk2.get_modifiers()
ppk2.use_source_meter()
ppk2.set_source_voltage(SPANNUNG)
ppk2.toggle_DUT_power("ON")
ppk2.start_measuring()

print(f"Baseline-Messung läuft {DAUER//60} Minuten...")
samples = []
t_ende = time.time() + DAUER

while time.time() < t_ende:
    raw = ppk2.get_data()
    if raw != b'':
        s, _ = ppk2.get_samples(raw)
        samples.extend(s)
    time.sleep(0.01)

ppk2.stop_measuring()
ppk2.toggle_DUT_power("OFF")

arr = np.array(samples)
avg_mA  = arr.mean() / 1000
peak_mA = arr.max()  / 1000
min_uA  = arr.min()

print(f"\n📊 BASELINE ERGEBNIS:")
print(f"   Ø Strom:  {avg_mA:.2f} mA")
print(f"   Peak:     {peak_mA:.1f} mA")
print(f"   Minimum:  {min_uA:.2f} µA")
print(f"   Samples:  {len(arr):,}")

# CSV speichern
with open("ergebnisse/messung.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        LABEL, f"{avg_mA:.2f}", f"{peak_mA:.1f}",
        f"{min_uA:.2f}", len(arr)
    ])
print(f"\n✅ Gespeichert in ergebnisse/messung.csv")