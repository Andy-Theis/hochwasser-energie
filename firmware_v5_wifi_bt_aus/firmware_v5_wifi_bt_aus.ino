// Hochwasserpegel - Firmware v5.0
// Patch #4: WiFi & Bluetooth komplett aus

#include "esp_wifi.h"
#include "esp_bt.h"

#define SLEEP_SEKUNDEN 10

void setup() {
  // WiFi & Bluetooth sofort deaktivieren
  esp_wifi_stop();
  esp_bt_controller_disable();
  
  setCpuFrequencyMhz(80);
  
  Serial.begin(115200);
  delay(500);
  
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v5.0");
  Serial.println("Patch #4: WiFi+BT aus, CPU 80MHz");
  Serial.println("=================================");
  
  // Sensor messen (simuliert)
  Serial.println("Messe Wasserstand...");
  delay(100);
  Serial.println("Wasserstand: 42 cm");
  
  // Daten senden (simuliert)
  Serial.println("Sende Daten...");
  delay(50);
  Serial.println("Gesendet!");
  
  // Deep Sleep
  Serial.println("Gehe schlafen...");
  Serial.flush();
  
  esp_sleep_enable_timer_wakeup(SLEEP_SEKUNDEN * 1000000ULL);
  esp_deep_sleep_start();
}

void loop() {}
