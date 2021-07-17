/*
Written by Bryce Casamento
MIT Lisence i guess
*/

// Button and LED pins
int buttonPin = 2;
int buttonPin2 = 3;
int statusLedPin = 13;
int statusLedPin2 = 12; // currently not using


// for reading from Serial
char inputBuffer[16];
char hands_up_string[] = "handsup";
char hands_down_string[] = "handsdown";

bool HANDS_UP = false; // whether the user's hands are up

int buttonState1 = 0;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  /*
  // This is for READING the Serial, not needed as of now as we arent getting commands from the pi
  if (Serial.available() > 0) {
   Serial.readBytesUntil('\n', inputBuffer, 16);
   if (strcmp(hands_down_string, inputBuffer) == 0) {
    }
  }
  */
  unsigned int currentTime = millis();
  
  buttonState1 = digitalRead(buttonPin);
  if (buttonState1 > 0) {
    if (!HANDS_UP) {
      Serial.println("handsup");
      HANDS_UP = true;
    }
  } else {
    if (HANDS_UP) {
      Serial.println("handsdown");
      HANDS_UP = false;
    }
    
    
  }
  // check if the buttons are pressed. If it is, the buttonState is HIGH:
  digitalWrite(statusLedPin, buttonState1);

  delay(100);
  
}
