# 🌊 Hochwasserpegel – Energieoptimierung

**Ressourceneffiziente IoT-Sensorik mit LLM-gestütztem Green Coding**  
Umwelt-Campus Birkenfeld · SoSe 2026  
Betreuer: Prof. Dr. Naumann · Prof. Dr. Gollmer

---

## 📌 Projektziel

Optimierung eines bestehenden IoT-Hochwasserpegelmessers durch
Software- und Firmware-Optimierung. Keine Hardware-Änderungen.

**Benchmark:** 47,3 mA → 12,6 mA (–73%)

---

## 📊 Aktuelle Messergebnisse

| Version | Firmware | Ø Strom | Ersparnis |
|---|---|---|---|
| v1 | Baseline (unbekannte Firmware) | 99,90 mA | – |
| v2 | Kein Sleep (kontrolliert) | 47,44 mA | Baseline |
| v3 | Patch #1: Deep Sleep | 7,15 mA | **–84,9%** ✅ |
| v4 | Patch #2: Light Sleep | 6,34 mA | **–86,6%** ✅ |

**Projektziel von 12,6 mA bereits übertroffen! 🎯**

---

## 🔧 Hardware

| Komponente | Details |
|---|---|
| MCU | ESP32-WROOM-32 |
| Strommessung | Nordic Power Profiler Kit II (PPK2) |
| Kommunikation | LoRaWAN via TTN (SF7) |
| Sensoren | DFRobot + Maxbotix Ultraschall |
| Stromversorgung | 1 Wp Solar + NiMH Akku + 3× AA Lithium |

---

## 📁 Projektstruktur
hochwasser-energie/
├── baseline.py        ← PPK2 Messung (5 Min)
├── auswerten.py       ← Grafiken & Auswertung
├── erster_test.py     ← Verbindungstest PPK2
├── test_verbindung.py ← PPK2 erkennen
└── ergebnisse/
├── messung.csv    ← alle Messwerte
└── grafiken/      ← Auswertungsgrafiken
---

## 🚀 Schnellstart

```bash
# venv aktivieren
venv\Scripts\activate

# PPK2 erkennen
python test_verbindung.py

# Messen
python baseline.py

# Auswerten
python auswerten.py
```

---

## 📚 Quellen

- Bouguera et al. (2018) – Energy Consumption Model LoRa/LoRaWAN
- Ghaderi & Amiri (2024) – LoRaWAN Sensor Energy Analysis
- Zakaria et al. (2023) – Flood Monitoring & Warning System
- Alkhayyal & Mostafa (2024) – AI/ML für LoRaWAN Optimization
- Cappendijk et al. (2024) – Prompting LLMs for Energy-Efficient Code
- MDPI JSAN (2026) – Multiple Linear Regression für LoRa Energy
- Umwelt-Campus IoT-Werkstatt – Green Coding Tutorial
