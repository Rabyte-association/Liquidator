/*Do testów trzeba wprowadzić n(line9)
oraz wskazać wanted wanted_x(decode_server.py/line42 są tam wskazane jednostki) */


#include "AS5600.h"
#include "Wire.h"
#include "CytronMotorDriver.h"

AS5600L as5600;   //  use default Wire
n = 300;
bool setOutputMode(uint8_t outputMode) ;
CytronMD motorZ(PWM_DIR, 5, 4);
CytronMD motorZ2(PWM_DIR, 10, 9);

void setup()
{
  Serial.begin(115200);
  as5600.begin(14, 15);      //  ESP32
  as5600.setAddress(0x40);   //  AS5600L has address

  as5600.setDirection(AS5600_CLOCK_WISE);  //  default, just be explicit.
  delay(1000);
  as5600.resetCumulativePosition(0);
}


void loop()
{
  static uint32_t lastTime = 0;

  //  set initial position
  x = abs(as5600.getCumulativePosition());

  //  update every 100 ms
  if (millis() - lastTime >= 100)
  {
    lastTime = millis();
    if (x - Last_x >= abs(n) )
    {
      Last_x = abs(as5600.getCumulativePosition());
      Serial.println(x);
    }  
  }

  if (Serial.available() > 1) {
    byte data = Serial.read();
    if (data == 'y') {
      speedY = Serial.parseFloat() * 255;
      speedY2 = Serial.parseFloat() * 255;
    }
        if (data == 'a') {
      speedA = Serial.parseFloat() * 255;
    }
    if (data == 'b') {
      speedB = Serial.parseFloat() * 255;
    }
}

  motorY.setSpeed(speedY);
  motorY.setSpeed(speedY2);

  motorA.setSpeed(speedA);
  motorB.setSpeed(speedB);
  
}
