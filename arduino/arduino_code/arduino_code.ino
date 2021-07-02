/*
Written by Bryce Casamento
*/
int buttonPin = 2;
int buttonPin2 = 3;
int statusLedPin = 13;
int statusLedPin2 = 12;
bool running = false;
char inputBuffer[16];
char hands_up_string[] = "handsup";
char hands_down_string[] = "handsdown";
int timer_duration = 500;
int buttonState1 = 0;
int buttonState2 = 0;

bool leftHandUp = false;
bool rightHandUp = false;
void setup() {
  // put your setup code here, to run once:
  pinMode(statusLedPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  unsigned long timeBegin = micros();
  // put your main code here, to run repeatedly:
  /*
  if (Serial.available() > 0) {
   Serial.readBytesUntil('\n', inputBuffer, 16);
   if (strcmp(hands_down_string, inputBuffer) == 0) {
    
   }
  } */
  buttonState1 = digitalRead(buttonPin);
  buttonState2 = digitalRead(buttonPin2);
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  
  digitalWrite(statusLedPin, !buttonState1);
  
  Serial.write(rightHandUp);
  Serial.write(leftHandUp + "\n");
  // Leave the following code at the end of the function, always (for timing everything properly)
  unsigned long timeEnd = micros();
  unsigned long duration = timeEnd - timeBegin;
  double averageDuration = (double)duration / 1000.0;
  /*Serial.println(averageDuration);
  int delayTime = target_time - averageDuration;*/
}
