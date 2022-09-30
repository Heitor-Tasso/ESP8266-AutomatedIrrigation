 
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

#include <FS.h>

#include "debug/toolsprint.h"
#include "varibles/tooltype.h"

// ------------------ esp8266 wifi ------------------
#define ssid "ESP8266 - Heitor" // esp8266 wifi
#define password "12345678"

// ------------------- local wifi -------------------
#define user_wifi "BC Telecom anderson"
#define user_pass "m23m19v16v22h11h26"

ESP8266WebServer server(80);
MDNSResponder mdns;

IPAddress staticIP(192, 168, 4, 2); // IP Static 192.168.4.2
IPAddress gateway(192, 168, 4, 1);// gateway Static 192.168.4.1
IPAddress subnet(255, 255, 255, 0);// subnet Static 255.255.255.0

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
  Serial.println(".");
  delay(200);
  print_str(String("http://")+WiFi.localIP().toString(), "ip");

  if (mdns.begin("esp8266", WiFi.localIP())) {
   Serial.println("MDNS responder started");
  }
}

void start_esp8266_wifi() {
  WiFi.softAP(ssid, password, 2, 0); // Start ACCESS POINT

  if (!WiFi.config(staticIP, gateway, subnet)) {
    Serial.println("STA Failed to configure");
  } else {
    print_str(WiFi.softAPIP().toString(), "getway");
  }
}

void handleRoot() {
  server.send(200, "text/html", HTML_PAGE);
}

void handleNotFound() {
  server.send(404, "text/plain", "404: Not found");
}

void handlePage() {
  server.sendHeader("Location", "/index"); // new location for the browser
  server.send(303); // Send it back to the browser
}

void handleLogin() {
  if (!server.hasArg("username") || ! server.hasArg("password") \
        || server.arg("username") == NULL || server.arg("password") == NULL) {
    // If the POST request doesn't have username and password data
    server.send(400, "text/plain", "400: Invalid Request"); // The request is invalid
    return;
  }

  if (server.arg("username") == "Heitor" && server.arg("password") == "1234") {
    // If both the username and the password are correct
    server.send(200, "text/html", "<h1>Welcome, " + server.arg("username") + "!</h1><p>Login successful</p>");
  }
  else { // Username and password don't match
    server.send(401, "text/plain", "401: Unauthorized");
  }
}

void writeFile(String state, String path) { 
  // Abre o arquivo para escrita ("w" write)
  // Sobreescreve o conteúdo do arquivo
  File rFile = SPIFFS.open(path,"w+"); 
  if(!rFile){
    Serial.println("Erro ao abrir arquivo!");
  }
  else {
    rFile.println(state);
    Serial.print("gravou estado: ");
    Serial.println(state);
  }
  rFile.close();
}


String readFile(String path) {
  File rFile = SPIFFS.open(path,"r");
  if (!rFile) {
    Serial.println("Erro ao abrir arquivo!");
  }
  String content = rFile.readStringUntil('\r'); // desconsidera '\r\n'
  Serial.print("leitura de estado: ");
  Serial.println(content);
  rFile.close();
  return content;
}
 
void openFS(void){
  //Abre o sistema de arquivos
  if(!SPIFFS.begin()){
    Serial.println("\nErro ao abrir o sistema de arquivos");
  } else {
    Serial.println("\nSistema de arquivos aberto com sucesso!");
  }
}


void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  WiFi.mode(WIFI_AP_STA);// Mode ACCESS POINT && STATION ACCESS
  
  start_local_wifi(); // Start STATION ACCESS
  server.on("/index.html", handleRoot);
  server.onNotFound(handleNotFound);
  server.on("/server/login", handleLogin);
  server.begin();

  // start_esp8266_wifi(); // Start ACESS POINT

  Serial.println("");
  Serial.println("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨");
  Serial.println("Server started!");
  Serial.println("------------------------------------");

  openFS();
  String state = readFile("/state.txt");
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
