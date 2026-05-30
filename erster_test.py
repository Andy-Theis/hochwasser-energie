from ppk2_api.ppk2_api import PPK2_API
import time

geraete = PPK2_API.list_devices()
ppk2 = PPK2_API(geraete[0], timeout=1, exclusive=True)
ppk2.get_modifiers()
ppk2.use_source_meter()
ppk2.set_source_voltage(3300)  # 3,3V für ESP32
ppk2.toggle_DUT_power("ON")
ppk2.start_measuring()

print("Messung läuft 60 Sekunden...")
# for i in range(10):
for i in range(60):   # 60 statt 10 Sekunden für mehr Daten
    raw = ppk2.get_data()
    if raw != b'':
        samples, _ = ppk2.get_samples(raw)
        avg = sum(samples) / len(samples)
        print(f"Sekunde {i+1}: Ø {avg:.1f} µA")
    time.sleep(1)

ppk2.stop_measuring()
ppk2.toggle_DUT_power("OFF")
print("Fertig!")