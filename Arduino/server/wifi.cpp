
#include "../server/wifi.h"


ESP8266WebServer server(266);
MDNSResponder mdns;

IPAddress staticIP(192, 168, 1, 124); // IP Static
IPAddress gateway(192, 168, 1, 1);    // gateway Static
IPAddress subnet(255, 255, 255, 0);   // subnet Static


void start_local_wifi() {
  WiFi.begin(user_wifi, user_pass);   // WiFi Domestico
  
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(".");
  delay(200);
  print_str("http://"+WiFi.localIP().toString()+":266/index.html", "ip");

  if (mdns.begin("esp8266", WiFi.localIP())) {
   Serial.println("MDNS responder started");
  }
}

void start_esp8266_wifi() {
  WiFi.softAP(ssid, password, 2, 0);   // Start ACCESS POINT

  if (!WiFi.config(staticIP, gateway, subnet)) {
    Serial.println("STA Failed to configure");
  }
  else {
    print_str(WiFi.softAPIP().toString(), "getway");
  }
}

String get_content_type(String filename) {
  if (filename.endsWith(".html")) { return "text/html"; }
  else if (filename.endsWith(".css")) { return "text/css"; }
  else if (filename.endsWith(".js")) { return "application/javascript"; }
  else if (filename.endsWith(".ico")) { return "image/x-icon"; }
  else if (filename.endsWith(".gz")) { return "application/x-gzip"; }
  else if (filename.endsWith(".jpg")) { return "image/jpeg"; }
  else if (filename.endsWith(".png")) { return "image/png"; }
  else if (filename.endsWith(".svg")) { return "image/svg"; }
  return "text/plain";
}


void handle_file(String path, int type_send) {
  File file = open_file(path, "r");
  if (!file) { return; }

  size_t sent = server.streamFile(file, get_content_type(path));
  file.close();
}

void stream_file(class String path, int type) {
  if (type == 0) {
    server.on(path, [path]() { handle_file(path, 200); });
  }
  else if (type == 1) {
    server.onNotFound([path]() { handle_file(path, 404); });
  }
  else if (type == 2) {
    server.on(path, [path]() { handle_file(path, 400); });
  }
}

void handle_page(String path) {
  server.sendHeader("Location", path); // new location for the browser
  server.send(303);                    // Send it back to the browser
}

