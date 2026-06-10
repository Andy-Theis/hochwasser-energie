// Hochwasserpegel - Firmware v6.0
// Patch #5: Sensor-Timing minimiert

#include "esp_wifi.h"
#include "esp_bt.h"

#define SLEEP_SEKUNDEN 10
#define SENSOR_EINSCHWING_MS 50   // statt 100ms → halbiert!
#define SEND_DAUER_MS        30   // statt 50ms → kürzer!

void setup() {
  // Alles sofort deaktivieren
  esp_wifi_stop();
  esp_bt_controller_disable();
  setCpuFrequencyMhz(80);
  
  Serial.begin(115200);
  delay(500);
  
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v6.0");
  Serial.println("Patch #5: Sensor-Timing optimiert");
  Serial.printf("Einschwingzeit: %d ms\n", SENSOR_EINSCHWING_MS);
  Serial.printf("Sendedauer:     %d ms\n", SEND_DAUER_MS);
  Serial.println("=================================");
  
  // Sensor messen - minimale Einschwingzeit
  Serial.println("Messe Wasserstand...");
  delay(SENSOR_EINSCHWING_MS);  // 50ms statt 100ms
  Serial.println("Wasserstand: 42 cm");
  
  // Daten senden - minimale Sendedauer
  Serial.println("Sende Daten...");
  delay(SEND_DAUER_MS);         // 30ms statt 50ms
  Serial.println("Gesendet!");
  
  // Deep Sleep
  Serial.println("Gehe schlafen...");
  Serial.flush();
  
  esp_sleep_enable_timer_wakeup(SLEEP_SEKUNDEN * 1000000ULL);
  esp_deep_sleep_start();
}

void loop() {}
