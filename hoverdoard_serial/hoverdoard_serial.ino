/*
  Further information on https://github.com/bipropellant
*/

#include <HoverboardAPI.h>

int serialWrapper(unsigned char *data, int len) {
  return (int) Serial1.write(data, len);
}
HoverboardAPI hoverboard = HoverboardAPI(serialWrapper);

int movement = 0;
int turn = 0;

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
  }
  Serial.print(movement);
  Serial.println(turn);
  hoverboard.sendPWM(-movement, turn, PROTOCOL_SOM_NOACK);
}
