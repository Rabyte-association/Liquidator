// Runs on rpi pico.
// rpi4b <=usb/serial=> rpi pico (running this code) <=gpio=> motor drivers <==> motors

#include "CytronMotorDriver.h"

#include <HoverboardAPI.h>

UART Serial2(12, 13, 0, 0);

int serialWrapper(unsigned char *data, int len) {
  return (int)Serial2.write(data, len);
}
HoverboardAPI hoverboard = HoverboardAPI(serialWrapper);

float movement = 0;
float turn = 0;
float movement_current;
float a = 25;  //accel/decel speed  <10


#define hvb_relay 8  // relay used for tunrning on/off the hoverboard mainboard
#define led_relay 9  // relay used for driving leds

CytronMD motorY(PWM_DIR, 2, 1);
CytronMD motorY2(PWM_DIR, 4, 3);

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

bool wheelie = false;
// unsigned long datatime;


void setup() {
  // Serial1.setTX(12);
  Serial.begin(115200);
  Serial2.begin(115200);
  pinMode(25, OUTPUT);  // builtin led, status
  // digitalWrite(25, HIGH);
  pinMode(midEnd, INPUT_PULLUP);
  pinMode(hvb_relay, OUTPUT);
  pinMode(led_relay, OUTPUT);
  //
  //attachInterrupt(digitalPinToInterrupt(midEnd), midIntr, FALLING);
}



void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    
    if (data == 'z') {
      speedZ = Serial.parseFloat() * 255;
      speedZ2 = Serial.parseFloat() * 255;
    }
    if (data == 'h') {
      relay = Serial.parseInt();
    }
    if (data == 'l') {
      if (Serial.parseInt() == 1) {
        led = !led;
      }
    }
    if (data == 'x') {
      movement = Serial.parseInt();
    }
    if (data == 't') {
      turn = Serial.parseInt();
    }
    if (data == 'w') {
      wheelie = Serial.parseInt();
    }
    // datatime = millis();
  }
  // if(millis() - datatime >= 1000){
  //   speedY = 0;
  //   speedZ = 0;
  //   speedA = 0;
  //   speedB = 0;
  //   led = !led;
  // }
  digitalWrite(hvb_relay, relay);
  digitalWrite(led_relay, led);
  midVal = digitalRead(midEnd);

  motorZ.setSpeed(speedZ);
  motorZ2.setSpeed(speedZ2);

  if (!wheelie) {
    digitalWrite(25, HIGH);
    if (movement - movement_current > 0) {
      movement_current += a;
    }
    if (movement - movement_current < 0) {
      movement_current += -a;
    }
    if (movement - movement_current == 0) {
      movement_current = movement;
    }
  } else {
    digitalWrite(25, LOW);
    movement_current = movement;
  }
  hoverboard.sendPWM(movement_current, turn, PROTOCOL_SOM_NOACK);
}