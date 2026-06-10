// Hochwasserpegel - Firmware v2.0
// Patch #1: Deep Sleep implementiert

#define SLEEP_SEKUNDEN 900  // alle 900 Sekunden aufwachen (zum Testen)

void setup() {
  Serial.begin(115200);
  delay(500);
  
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v2.0");
  Serial.println("Patch #1: Deep Sleep aktiv");
  Serial.println("=================================");
  
  // Schritt 1: Sensor messen (simuliert)
  Serial.println("Messe Wasserstand...");
  delay(100);
  Serial.println("Wasserstand: 42 cm");
  
  // Schritt 2: Daten senden (simuliert)
  Serial.println("Sende Daten...");
  delay(50);
  Serial.println("Gesendet!");
  
  // Schritt 3: Deep Sleep
  Serial.println("Gehe schlafen...");
  Serial.println("=================================");
  Serial.flush();  // wichtig: Serial leeren bevor Sleep
  
  esp_sleep_enable_timer_wakeup(SLEEP_SEKUNDEN * 1000000ULL);
  esp_deep_sleep_start();  // ab hier ~10 µA!
}

void loop() {
  // loop() wird nie erreicht - ESP32 schläft nach setup()
}
