// Further information on https://github.com/bipropellant
//
// To run this code you need this liblary: https://github.com/bipropellant/bipropellant-hoverboard-api
// but, to install this lib, you also need this one: https://github.com/bipropellant/bipropellant-protocol
// I recomed just copying the .c nad .h files form protocol lib, to api lib, then copying the whole folder
// into your aeduino libs folder.

#include <HoverboardAPI.h>

int serialWrapper(unsigned char *data, int len) {
  return (int) Serial1.write(data, len);
}
HoverboardAPI hoverboard = HoverboardAPI(serialWrapper);

float movement = 0;
float turn = 0;
float movement_current;
float a;

void setup() {
  Serial1.begin(115200);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    if (data == 'a') {
      movement = Serial.parseInt();
    }
    if (data == 'b') {
      turn = Serial.parseInt();
    }
    Serial.println(data);
    if (data == 'p') {
      a = Serial.parseFloat();
    }
  }

  if (movement - movement_current > 0) {
    //    movement_current += a * 1/sqrt(abs(movement - movement_current));
    movement_current += a * 1 / (movement - movement_current);
  }
  if (movement - movement_current < 0) {

    //    movement_current += -a * 1/sqrt(abs(movement - movement_current));
    movement_current += -a * 1 / (movement - movement_current);
  }

  Serial.print(movement);
  Serial.print(", ");
  Serial.println(movement_current);
  hoverboard.sendPWM(movement_current, turn, PROTOCOL_SOM_NOACK);
  delay(10);
}
