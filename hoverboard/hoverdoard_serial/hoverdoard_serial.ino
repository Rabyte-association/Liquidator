
#include <HoverboardAPI.h>

int serialWrapper(unsigned char *data, int len) {
  return (int) Serial1.write(data, len);
}
HoverboardAPI hoverboard = HoverboardAPI(serialWrapper);

float movement = 0;
float turn = 0;
float movement_current;
float a=1; //accel/decel speed  <10 

unsigned long datatime;

void setup() {
  Serial1.begin(115200);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 1) {

    byte data = Serial.read();
    if (data == 'x') {
      movement = Serial.parseInt();
    }
    if (data == 'b') {
      turn = Serial.parseInt();
    }

    datatime = millis();
  }

//  if (movement - movement_current > 0) {
//    //movement_current += a * 1/sqrt(abs(movement - movement_current));
//    movement_current += a;
//   // if(movement - movement_current > 20){  //trzeba wytestowac
//    //  movement_current+=5;
//    //}
//  }
//  if (movement - movement_current < 0) {
//
//    //movement_current += -a * 1/sqrt(abs(movement - movement_current));
//    movement_current += -a;
//    //if(movement - movement_current < -20){ //trzeba wytestowac
//    //  movement_current-=5;
//    //}
//  }

//  Serial.print(turn);
//  Serial.print(" ");
//  Serial.println(movement_current);
//  hoverboard.sendPWM(movement_current, turn, PROTOCOL_SOM_NOACK);
  if(millis() - datatime >= 1000){
    movement = 0;
    turn = 0;
  }
  hoverboard.sendPWM(movement, turn, PROTOCOL_SOM_NOACK);
}
