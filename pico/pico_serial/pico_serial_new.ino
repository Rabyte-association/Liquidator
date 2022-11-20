// Runs on rpi pico.
// rpi4b <=usb/serial=> rpi pico (running this code) <=gpio=> motor drivers <==> motors

#include "CytronMotorDriver.h"

#define hvb_relay 8   // relay used for tunrning on/off the hoverboard mainboard
#define led_relay 9   // relay used for driving leds
#define midEnd  13


CytronMD motorY(PWM_DIR, 18, 19);
CytronMD motorZ(PWM_DIR, 16, 17);

CytronMD motorA(PWM_PWM, 20, 21);
CytronMD motorB(PWM_PWM, 22, 26);

float speedY = 0;
float speedZ = 0;
float speedA = 0;
float speedB = 0;

int relay = 0;
bool led = false;

bool midVal = false;
bool reset = LOW;


void setup() {
  Serial.begin(115200);
  pinMode(25, OUTPUT);    // builtin led, status
  digitalWrite(25, HIGH);
  pinMode(midEnd, INPUT_PULLUP);
  pinMode(hvb_relay, OUTPUT);
  pinMode(led_relay, OUTPUT);
//  
//attachInterrupt(digitalPinToInterrupt(midEnd), midIntr, FALLING);
}



void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    if (data == 'y') {
      speedY = Serial.parseFloat() * 255;
    }
    if (data == 'z') {
      speedZ = Serial.parseFloat() * 255;
    }
    if (data == 'h') {
      relay = Serial.parseInt();
    }
    if (data == 'l') {
      if(Serial.parseInt() == 1){
        led = !led;
      }
    }
    if (data == 'a') {
      speedA = Serial.parseFloat()*255;
    }
    if (data == 'b') {
      speedB = Serial.parseFloat()*255;
    }}

  digitalWrite(hvb_relay, relay);
  digitalWrite(led_relay, led);
  midVal = digitalRead(midEnd);

  motorY.setSpeed(speedY);
  motorZ.setSpeed(speedZ);
  if(midVal == LOW){
    
    if(speedA > 0){
    motorA.setSpeed(0);
    }
    else{
      motorA.setSpeed(speedA);
    }
    if(speedB>0){
      motorB.setSpeed(0);
    }
    else{
      motorB.setSpeed(speedB);
    }
  }
  else{
    motorA.setSpeed(speedA);
    motorB.setSpeed(speedB);
  }
}