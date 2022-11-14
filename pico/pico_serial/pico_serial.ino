#include "CytronMotorDriver.h"

#define hvb_relay 28

CytronMD motorY(PWM_DIR, 18, 19);
CytronMD motorZ(PWM_DIR, 16, 17);

int speedY = 0;
int speedZ = 0;
bool relay = false;

void setup() {
  Serial.begin(115200);
  pinMode(25, OUTPUT);
  digitalWrite(25, HIGH);

  pinMode(hvb_relay, OUTPUT);
}

void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    if (data == 'y') {
      speedY = Serial.parseInt()*255;
    }
    if (data == 'z') {
      speedZ = Serial.parseInt()*255;
    }
    if(data == 'h'){
      relay = !relay;
    }
  }
  digitalWrite(hvb_relay, relay);
  motorY.setSpeed(speedY);
  
.  motorZ.setSpeed(speedZ);
  Serial.println("ok");
}