// Hochwasserpegel - Test Firmware v1.0
// Deep Sleep Test - Baseline ohne Sleep

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("=================================");
  Serial.println("Hochwasserpegel Firmware v1.0");
  Serial.println("=================================");
  Serial.println("Board: AZ-Delivery Mini32");
  Serial.println("Modus: Aktiv (kein Sleep)");
  Serial.println("=================================");
  
  Serial.println("Simuliere Messzyklus...");
  delay(100);  // Sensor einlesen simulieren
  
  Serial.println("Sende Daten (simuliert)...");
  delay(50);   // LoRa TX simulieren
  
  Serial.println("Zyklus fertig.");
  Serial.println("=================================");
}

void loop() {
  Serial.println("ESP32 läuft... kein Sleep aktiv");
  delay(5000);
}
