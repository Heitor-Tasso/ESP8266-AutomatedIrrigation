
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
  else if (filename.endsWith(".jpg")) { return "image/png"; }
  else if (filename.endsWith(".jpg")) { return "image/svg"; }
  return "text/plain";
}

void handle_big_file(String path, int type_send) {
  File file = SPIFFS.open(path, "r");
  if (!file) { return; }

  int filesize = file.size();
  server.sendHeader("Content-Length", String(filesize));
  server.send(type_send, get_content_type(path), "");

  char buf[1024];
  while (filesize > 0) {
    size_t len = std::min((int) (sizeof(buf) - 1), filesize);
    file.read((uint8_t *)buf, len);
    server.sendContent_P((const char*) buf, len);
    filesize -= len;
  }
}

void handle_file(String path, int type_send) {
  int size_file = 0;
  char* content = read_file(path, &size_file);
  server.send(type_send, get_content_type(path), content);
  free(content);
}

void stream_file(class String path, int type) {
  File file = SPIFFS.open(path, "r");
  if (!file) { return; }  
  
  int filesize = file.size();
  String contentfile = get_content_type(path);
  
  String WebString = "HTTP/1.1 200 OK\r\n";
  WebString += "Content-Type: " + contentfile + "\r\n";
  WebString += "Content-Length: " + String(filesize) + "\r\n";
  server.sendContent(WebString);
  
  char buf[1024];
  while (filesize > 0) {
    size_t len = std::min((int) (sizeof(buf) - 1), filesize);
    file.read((uint8_t *)buf, len);
    server.client().write((const char*) buf, len);
    filesize -= len;
  }
  
  file.close();
  if (type == 0) {
    server.on(path, [path]() { handle_file(path, 200); });
  }
  else if (type == 1) {
    server.onNotFound([path]() { handle_file(path, 404); });
  }
  else if (type == 2) {
    server.on(path, [path]() { handle_big_file(path, 200); });
  }
}

void handle_page(String path) {
  server.sendHeader("Location", path); // new location for the browser
  server.send(303);                    // Send it back to the browser
}

