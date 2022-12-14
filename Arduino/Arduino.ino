 
#include "FS.h"

#include "debug/toolsprint.h"
#include "server/wifi.h"

unsigned int time_to_update = 0;
bool need_to_update = false;
unsigned long int last_time_updated = 0;

#define PIN_LDR 0  // C0
#define PIN_TMP 1  // C1
#define PIN_HUM 2  // C2

#define MUX_0 16 // D0
#define MUX_1 5  // D1
#define MUX_2 4  // D2
#define MUX_3 0  // D3

#define ANALOGIC_MUX A0


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


void write_in_mux(int index) {
  digitalWrite(MUX_0, bitRead(index, 0));
  digitalWrite(MUX_1, bitRead(index, 1));
  digitalWrite(MUX_2, bitRead(index, 2));
  digitalWrite(MUX_3, bitRead(index, 3));
}


int read_luminosity() {
  write_in_mux(PIN_LDR);
  int value = 100 - ((analogRead(ANALOGIC_MUX) - 189)*100/271);
  if (value > 100) { value = 100; }
  else if (value < 0) { value = 0; }

  Serial.println("Luminosity = " + String(value) + "%");
  return value;
}

int read_temperature() {
  write_in_mux(PIN_TMP);
  int value = 100 - ((analogRead(ANALOGIC_MUX) - 189)*100/271);
  if (value > 100) { value = 100; }
  else if (value < 0) { value = 0; }

  Serial.println("Temperature = " + String(value) + "%");
  return value;
}

int read_humidity() {
  write_in_mux(PIN_HUM);
  int value = 100 - ((analogRead(ANALOGIC_MUX) - 189)*100/271);
  if (value > 100) { value = 100; }
  else if (value < 0) { value = 0; }

  Serial.println("Humidity = " + String(value) + "%");
  return value;
}

void get_values() {
  String values = "{";
  values += "\"lux_value=" + String(read_luminosity()) + "\",";
  values += "\"celsius_value=" + String(read_temperature()) + "\",";
  values += "\"humidity_value=" + String(read_humidity()) + "\"";
  values += "}";
  server.send(200, "text/plain", values);
}


void setup() {
  openFS(); // Start system of files

  Serial.begin(9600);
  
  pinMode(MUX_0, OUTPUT);
  pinMode(MUX_1, OUTPUT);
  pinMode(MUX_2, OUTPUT);
  pinMode(MUX_3, OUTPUT);

  pinMode(ANALOGIC_MUX, INPUT);

  WiFi.mode(WIFI_AP_STA);  // Mode ACCESS POINT && STATION ACCESS
  start_local_wifi();      // Start STATION ACCESS
  // start_esp8266_wifi();    // Start ACESS POINT

  // FILES

  stream_file("/assets/eye-off-out.png", 0);
  stream_file("/assets/eye-out.png", 0);
  stream_file("/assets/site_large.png", 0);
  stream_file("/assets/l-bulb-400.png", 0);
  
  stream_file("/css/index.css", 0);
  stream_file("/uix/cr_pg_bar.css", 0);

  stream_file("/index.html", 0);
  stream_file("/html/info_page.html", 0);
  stream_file("/html/not_found.html", 1);
  stream_file("/html/invalid_request.html", 2);

  stream_file("/js/index.js", 0);
  
  server.on("/server/login", login_form);
  server.on("/server/values", get_values);

  server.begin();
}

void loop() {
  server.handleClient();

  if (millis()-last_time_updated >= time_to_update && need_to_update) {
    last_time_updated = millis();
    need_to_update = false;
  }
}
