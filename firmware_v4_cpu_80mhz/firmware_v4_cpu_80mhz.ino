// Hochwasserpegel - Firmware v4.0
// Patch #3: CPU-Takt 80 MHz statt 240 MHz

#define SLEEP_SEKUNDEN 10

void setup() {
  // CPU-Takt reduzieren - ZUERST vor allem anderen!
  setCpuFrequencyMhz(80);
  
  Serial.begin(115200);
  delay(500);
  
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v4.0");
  Serial.println("Patch #3: CPU 80 MHz");
  Serial.printf("CPU Takt: %d MHz\n", getCpuFrequencyMhz());
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
