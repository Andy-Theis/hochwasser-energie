from ppk2_api.ppk2_api import PPK2_API
import time, csv, datetime
import numpy as np

# ─── Konfiguration ────────────────────────────────────────
SPANNUNG_MV   = 3300    # 3,3V für ESP32
ZYKLUS_DAUER  = 900     # 15 Minuten = 1 vollständiger Zyklus
LABEL         = "messen.py_kein_sleep_wroom32"   # ← vor jedem Patch ändern!
CSV_DATEI     = "ergebnisse/messung.csv"
# ──────────────────────────────────────────────────────────

def messe_zyklus(label, dauer_s, spannung_mv):
    print(f"\n🔌 Starte Messung: {label}")
    print(f"   Dauer: {dauer_s}s | Spannung: {spannung_mv}mV")

    # PPK2 verbinden
    geraete = PPK2_API.list_devices()
    if not geraete:
        print("❌ Kein PPK2 gefunden!")
        return
    ppk2 = PPK2_API(geraete[0], timeout=1, exclusive=True)
    ppk2.get_modifiers()

    # Source Meter Modus: PPK2 versorgt ESP32
    ppk2.use_source_meter()
    ppk2.set_source_voltage(spannung_mv)
    ppk2.toggle_DUT_power("ON")
    time.sleep(0.5)  # kurz warten bis Spannung stabil

    ppk2.start_measuring()
    print("   ⏱️  Messung läuft...")

    alle_samples = []
    t_start = time.time()
    t_ende  = t_start + dauer_s

    while time.time() < t_ende:
        raw = ppk2.get_data()
        if raw != b'':
            samples, _ = ppk2.get_samples(raw)
            alle_samples.extend(samples)

        # Fortschritt anzeigen
        vergangen = time.time() - t_start
        if int(vergangen) % 60 == 0 and vergangen > 0:
            aktuell = np.mean(alle_samples[-1000:]) if alle_samples else 0
            print(f"   {int(vergangen/60)} Min | Ø letzte 1000 Samples: "
                  f"{aktuell:.1f} µA")
        time.sleep(0.01)

    ppk2.stop_measuring()
    ppk2.toggle_DUT_power("OFF")
    ppk2.close_connection()

    # ── Auswertung ──────────────────────────────────────
    if not alle_samples:
        print("❌ Keine Samples erhalten!")
        return

    avg_uA    = np.mean(alle_samples)
    peak_uA   = np.max(alle_samples)
    min_uA    = np.min(alle_samples)
    # Ladung = Durchschnittsstrom × Zeit (mAs)
    ladung_mAs = (avg_uA * dauer_s) / 1_000_000 * 1000

    print(f"\n📊 Ergebnis [{label}]:")
    print(f"   Ø Strom:  {avg_uA:.2f} µA  ({avg_uA/1000:.3f} mA)")
    print(f"   Peak:     {peak_uA:.1f} µA")
    print(f"   Minimum:  {min_uA:.2f} µA  (= Sleep-Strom)")
    print(f"   Ladung:   {ladung_mAs:.4f} mAs / Zyklus")
    print(f"   Samples:  {len(alle_samples)}")

    # ── In CSV speichern ────────────────────────────────
    zeitstempel = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(CSV_DATEI, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            zeitstempel, label,
            f"{avg_uA:.2f}", f"{peak_uA:.1f}", f"{min_uA:.2f}",
            f"{ladung_mAs:.4f}", len(alle_samples), dauer_s
        ])
    print(f"   ✅ Gespeichert in {CSV_DATEI}")

    # Rohdaten für spätere Grafik speichern
    np.save(f"ergebnisse/{label}_raw.npy", np.array(alle_samples))
    return avg_uA

if __name__ == "__main__":
    messe_zyklus(LABEL, ZYKLUS_DAUER, SPANNUNG_MV)