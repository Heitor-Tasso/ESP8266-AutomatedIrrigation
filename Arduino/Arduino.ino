 
#include "FS.h"

#include "debug/toolsprint.h"
#include "server/wifi.h"

unsigned int time_to_update = 0;
bool need_to_update = false;
unsigned long int last_time_updated = 0;

void login_form() {
  if (!server.hasArg("username") || ! server.hasArg("password") \
        || server.arg("username") == NULL || server.arg("password") == NULL) {
    // If the POST request doesn't have username and password data
    handle_page("/html/invalid_request.html");
    return;
  }

  if (server.arg("username") == "Heitor" && server.arg("password") == "1234") {
    // If both the username and the password are correct
    handle_page("/html/info_page.html");
  }
  else { // Username and password don't match
    handle_page("/index.html?login=invalid");
  }
}


void setup() {
  Serial.begin(9600);

  WiFi.mode(WIFI_AP_STA);  // Mode ACCESS POINT && STATION ACCESS
  start_local_wifi();      // Start STATION ACCESS
  // start_esp8266_wifi();    // Start ACESS POINT
  openFS();


  // FILES

  stream_file("/assets/eye-off-out.png", 0);
  stream_file("/assets/eye-out.png", 0);
  stream_file("/assets/site_large.png", 0);
  stream_file("/assets/light-bulb.png", 0);
  
  stream_file("/css/index.css", 0);

  stream_file("/index.html", 0);
  stream_file("/html/info_page.html", 0);
  stream_file("/html/not_found.html", 1);
  stream_file("/html/invalid_request.html", 2);

  stream_file("/js/index.js", 0);
  stream_file("/js/jquery-3.6.0.js", 0);

  stream_file("/uix/circular_progress_bar.html", 0);
  
  server.on("/server/login", login_form);

  server.begin();
}

void loop() {
  server.handleClient();
  
  // WiFiClient client = server.available();
  // if (client) {
  //   Serial.println("Novo cliente se conectou!");
  //   while (!client.available()){ delay(5); }

  //   String request = client.readStringUntil('\r');
  //   Serial.println(request);
  //   client.flush();

  //   client.println("HTTP/1.1 200 OK"); // VERSÃO DO HTTP
  //   client.println("Content-Type: text/html"); // TIPO DE CONTEÚDO
  
  //   client.println(HTML_PAGE);
  //   Serial.println("Cliente desconectado.");
  // }

  if (millis()-last_time_updated >= time_to_update && need_to_update) {
    last_time_updated = millis();
    need_to_update = false;
  }
}
