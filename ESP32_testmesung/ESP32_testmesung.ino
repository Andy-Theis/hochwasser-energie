/*
 * Stromverbrauch Test-Sketch
 * Modi: Delay → Light Sleep → Deep Sleep
 * Jeder Modus: 15 Sekunden
 * Serielle Ausgabe: 115200 Baud
 */

#include "esp_sleep.h"
#include "Preferences.h"

Preferences prefs;

void setup() {
  Serial.begin(115200);
  delay(1000);

  prefs.begin("test", false);
  int modus = prefs.getInt("modus", 0);

  if (modus == 0) {
    Serial.println("=== MODUS 1: DELAY ===");
    Serial.println("Jetzt ablesen! (15 Sekunden)");
    delay(15000);
    Serial.println("Fertig. Weiter zu Light Sleep...");
    delay(500);
    prefs.putInt("modus", 1);
    prefs.end();
    ESP.restart();

  } else if (modus == 1) {
    Serial.println("=== MODUS 2: LIGHT SLEEP ===");
    Serial.println("Jetzt ablesen! (15 Sekunden)");
    Serial.flush();
    prefs.putInt("modus", 2);
    prefs.end();
    esp_sleep_enable_timer_wakeup(15000000ULL);
    esp_light_sleep_start();
    Serial.println("Fertig. Weiter zu Deep Sleep...");
    delay(500);
    ESP.restart();

  } else if (modus == 2) {
    Serial.println("=== MODUS 3: DEEP SLEEP ===");
    Serial.println("Jetzt ablesen! (15 Sekunden)");
    Serial.flush();
    prefs.putInt("modus", 0);
    prefs.end();
    esp_sleep_enable_timer_wakeup(15000000ULL);
    esp_deep_sleep_start();
  }
}

void loop() {
  }
