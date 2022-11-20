// Likwidator 2022 by team rabyte
// Piece of software used for comunicatin with motor drivers.
// Runs on rpi pico.
// rpi4b <=usb/serial=> rpi pico (running this code) <=gpio=> motor drivers <==> motors

#include "CytronMotorDriver.h"

#define hvb_relay 8   // relay used for tunrning on/off the hoverboard mainboard
#define led_relay 9   // relay used for driving leds

CytronMD motorY(PWM_DIR, 18, 19);
CytronMD motorZ(PWM_DIR, 16, 17);

CytronMD motorA(PWM_PWM, 20, 21);
CytronMD motorB(PWM_PWM, 22, 26);

int speedY = 0;
int speedZ = 0;
int speedA = 0;
int speedB = 0;

bool relay = false;
bool led = false;

unsigned long datatime;

void setup() {
  Serial.begin(115200);
  pinMode(25, OUTPUT);    // builtin led, status
  digitalWrite(25, HIGH);

  pinMode(hvb_relay, OUTPUT);
  pinMode(led_relay, OUTPUT);
}

void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    if (data == 'y') {
      speedY = Serial.parseFloat()*255;
    }
    if (data == 'z') {
      speedZ = Serial.parseFloat() * 255;
    }
    if (data == 'h') {
      relay = Serial.parseInt();
    }
    if (data == 'l') {
      led = Serial.parseInt();
    }
    if (data == 'a') {
      speedA = Serial.parseFloat()*255;
    }
    if (data == 'b') {
      speedB = Serial.parseFloat()*255;
    }
    datatime = millis();
  }
  if(millis() - datatime >= 1000){
    speedY = 0;
    speedZ = 0;
    speedA = 0;
    speedB = 0;    
  }
  digitalWrite(hvb_relay, relay);
  digitalWrite(led_relay, led);

  motorY.setSpeed(speedY);
  motorZ.setSpeed(speedZ);

  motorA.setSpeed(speedA);
  motorB.setSpeed(speedB);
  Serial.println(speedA);    // debug
  // delay(1);
}