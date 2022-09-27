 
#include <ESP8266WiFi.h>

#include "debug/toolsprint.h"
#include "varibles/tooltype.h"

// ------------------- local wifi -------------------
#define user_wifi "UserWifi"
#define user_pass "PasswordWifi"

#define HTML_PAGE "\
\
<!DOCTYPE HTML>\
\
<html>\
  <h1>\
    <center>Ola cliente!</center>\
  </h1>\
</html>\
"

WiFiServer server(80);

unsigned int time_to_update = 0;
bool need_to_update = false;
unsigned long int last_time_updated = 0;

void start_local_wifi() {
  WiFi.begin(user_wifi, user_pass); // WiFi Domestico
  
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  IPAddress staticIP(192, 168, 4, 2); // IP Static 192.168.4.2
  IPAddress gateway(192, 168, 4, 1); // gateway Static 192.168.4.1
  IPAddress subnet(255, 255, 255, 0); // subnet Static 255.255.255.0
  WiFi.mode(WIFI_STA); // Mode STATION ACCESS
  WiFi.config(staticIP, gateway, subnet);
  
  start_local_wifi(); // Start STATION ACCESS

  Serial.println("");
  Serial.println("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨");
  Serial.println("Server started!");
  print_str(String("http://")+WiFi.softAPIP().toString(), "getway");
  print_str(WiFi.localIP().toString(), "ip");
  Serial.println("------------------------------------");
}

void loop() {

  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Novo cliente se conectou!");
    while (!client.available()){ delay(5); }

    String request = client.readStringUntil('\r');
    Serial.println(request);
    client.flush();

    client.println("HTTP/1.1 200 OK"); // VERSÃO DO HTTP
    client.println("Content-Type: text/html"); // TIPO DE CONTEÚDO
  
    client.println(HTML_PAGE);
    Serial.println("Cliente desconectado.");
  }

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);;

  if (millis()-last_time_updated >= time_to_update && need_to_update) {
    last_time_updated = millis();
    need_to_update = false;
  }
}
