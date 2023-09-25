#include <WiFi.h>
#include <WebServer.h>
#include "CytronMotorDriver.h"
#include <Servo.h>

// wifi
const char* ssid = "network";
const char* password = "pass";
int bieg =150;
int skret = 50;

Servo myservo

// Initialize the web server
WebServer server(80);

//engine movement
void move_forward() {
 myservo.write(180);
 Serial.println("forward");
}

void move_backward() {
  myservo.write(90);
  Serial.println("backward");
}

void move_stop() {

}

//engine rotation
void rotate_left() {

}

void rotate_right() { 

}

void rotate_stop() { 

}


//JAVASC
void handleRoot() {
  String html = "<!DOCTYPE html>\n"
   "<html>\n"
 "<head>\n"
  "<title>BALL</title>\n"
"</head>\n"
  "<body>\n"
  "<script>\n"
  "currentKeys = new Set();\n"
        "allowedActions = {\n"
            "'a': { command: 'rotate', direction: 'left', opposite: 'd' },\n"
            "'w': { command: 'move', direction: 'forward', opposite: 's' },\n"
            "'s': { command: 'move', direction: 'backward', opposite: 'w' },\n"
            "'d': { command: 'rotate', direction: 'right', opposite: 'a' },\n"
        "};\n"
        "document.addEventListener('keydown', (event) => {\n"
            "if (event.key in allowedActions && !currentKeys.has(event.key)) {\n"
                "currentKeys.add(event.key);\n"
                "let action = allowedActions[event.key];\n"
                "sendMove(`${action.command}_${action.direction}`);\n"
            "}\n"
        "});\n"
        "document.addEventListener('keyup', (event) => {\n"
            "if (event.key in allowedActions && currentKeys.has(event.key)) {\n"
                "currentKeys.delete(event.key);\n"
                "let action = allowedActions[event.key];\n"
                "if (currentKeys.has(action.opposite)) {\n"
                    "action = allowedActions[action.opposite];\n"
                    "sendMove(`${action.command}_${action.direction}`);\n"
                "}\n"
                "else sendMove(`${action.command}_stop`);\n"
            "}\n"
        "});\n"
"\n"
        "async function sendMove(action) {\n"
            "console.log(action);\n"
            "await fetch(`/${action}`, { method: 'GET', keepalive: true });\n"
        "}\n"
  " </script>\n"
  "<p> DUPA</p>\n"
  "</body>\n"
  "</html>\n";

  server.send(200, "text/html", html);
}

//move
void handleMoveForward() {
  move_forward();
  Serial.println("forward1");
  handleRoot();
}
void handleMoveBack() {
  move_backward();
  Serial.println("backward1");
  handleRoot();
}
void handleMoveStop() {
  move_stop();
  Serial.println("stop1");
  handleRoot();
}

//rotation
void handleRotLeft() {
 rotate_left();
 Serial.println("rotleft1");
  handleRoot();
}

void handleRotStop() {
  rotate_stop();
  Serial.println("rotstop1");
  handleRoot();
}

void handleRotRight() {
  rotate_right();
  Serial.println("rotright1");
  handleRoot();
}



void setup() {

    Serial.begin(115200);

//  Serial.print("Setting AP (Access Point)…");
//  WiFi.softAP(ssid, password);    
//
//  IPAddress IP = WiFi.softAPIP();  
//  Serial.print("AP IP address: ");
//  Serial.println(IP);  
//  connecting to WIFI;
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.begin(9600);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  //page commands
  server.on("/", handleRoot);
  
  server.on("/move_forward", handleMoveForward);
  server.on("/move_stop", handleMoveStop);
  server.on("/move_backward", handleMoveBack);
  
  server.on("/rotate_left", handleRotLeft);
  server.on("/rotate_stop", handleRotStop);
  server.on("/rotate_right", handleRotRight);
  
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
//good luck