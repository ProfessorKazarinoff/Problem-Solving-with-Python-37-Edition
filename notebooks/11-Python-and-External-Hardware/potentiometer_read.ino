// potentiometer_read.ino
// reads a potentiometer and sends value over serial
int sensorPin = A0;    // The potentiometer is connected to analog pin 0                  
int ledPin = 13;      // The LED is connected to digital pin 13
int sensorValue;     // an integer variable to store the potentiometer reading

void setup() // this function runs once when the sketch starts
{
  // make the LED pin (pin 13) an output pin
  pinMode(ledPin, OUTPUT);

  // initialize serial communication:
  Serial.begin(9600);
}

void loop() // this function runs repeatedly after setup() finishes
{
  sensorValue = analogRead(sensorPin);  // read the voltage at pin A0   
  Serial.println(sensorValue);         // Output sensor value to Serial Monitor
  
  if (sensorValue < 500) {            // if sensor output is less than 500,
    digitalWrite(ledPin, LOW); }     // Turn the LED off
  
  else {                               // if sensor output is greater than 500
    digitalWrite(ledPin, HIGH); }     // Keep the LED on
  
  delay(100);             // Pause 100 milliseconds before next reading
}
