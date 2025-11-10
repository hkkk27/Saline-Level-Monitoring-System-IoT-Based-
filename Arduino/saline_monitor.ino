#define TRIG_PIN 9
#define ECHO_PIN 10
#define BUZZER_PIN 8
#define BUTTON_PIN 7

long duration;
int distance;
bool buzzerDisabled = false; // Flag to stop buzzer after button press

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Button with pull-up resistor
  Serial.begin(9600);
}

void loop() {
  // Ultrasonic read
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;

  Serial.println(distance); // Send to Python

  // Reset logic: if water level is normal (< 12), re-enable buzzer
  if (distance < 12) {
    buzzerDisabled = false;
  }

  // If button is pressed, disable the buzzer
  if (digitalRead(BUTTON_PIN) == LOW && !buzzerDisabled) {
    buzzerDisabled = true;
    digitalWrite(BUZZER_PIN, LOW);
    delay(200); // Debounce
  }

  // If buzzer is disabled, skip all buzzer logic
  if (buzzerDisabled) {
    noTone(BUZZER_PIN);
  } else {
    // Buzzer logic based on distance
    if (distance >= 15) {
      tone(BUZZER_PIN, 1000);
      delay(100);
      noTone(BUZZER_PIN);
      delay(100);
    } else if (distance == 13) {
      tone(BUZZER_PIN, 1000);
      delay(500);
      noTone(BUZZER_PIN);
      delay(500);
    } else if (distance == 12) {
      tone(BUZZER_PIN, 1000);
      delay(1000);
      noTone(BUZZER_PIN);
      delay(1000);
    } else {
      noTone(BUZZER_PIN); // No buzzing for normal level
    }
  }

  delay(200);
}

