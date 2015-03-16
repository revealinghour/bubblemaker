/*
 Bubblemaker - Author Rituparna Matkar
 
 This sketch uses Serial .available() function.
 It looks for an ASCII string, and then if it receives 
 a letter turn the relay connected on pin 2 for 1 second 
 
 */

// pins for the relays:
int relay = 2;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  pinMode(relay, OUTPUT);

}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {
      digitalWrite(relay, HIGH);   // turn the relay on (HIGH is the voltage level)
      delay(1000);               // wait for a second
      digitalWrite(relay, LOW);    // turn the relay off by making the voltage LOW
      delay(10);
      Serial.println(Serial.read());
   }   
}









