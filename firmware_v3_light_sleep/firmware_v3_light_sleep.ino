// Hochwasserpegel - Firmware v3.0
// Patch #2: Light Sleep Test

#define SLEEP_SEKUNDEN 900

void setup() {
  Serial.begin(115200);
  delay(500);
}

void loop() {
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v3.0");
  Serial.println("Patch #2: Light Sleep aktiv");
  Serial.println("=================================");
  
  // Schritt 1: Sensor messen (simuliert)
  Serial.println("Messe Wasserstand...");
  delay(100);
  Serial.println("Wasserstand: 42 cm");
  
  // Schritt 2: Daten senden (simuliert)
  Serial.println("Sende Daten...");
  delay(50);
  Serial.println("Gesendet!");

  // Schritt 3: Light Sleep
  Serial.println("Gehe in Light Sleep...");
  Serial.flush();

  esp_sleep_enable_timer_wakeup(SLEEP_SEKUNDEN * 1000000ULL);
  esp_light_sleep_start();  // RAM bleibt erhalten!
  
  // Hier geht es nach dem Aufwachen weiter
  Serial.println("Aufgewacht aus Light Sleep!");
}
