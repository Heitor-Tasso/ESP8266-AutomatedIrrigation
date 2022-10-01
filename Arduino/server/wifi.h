
#ifndef WIFI_FUNCS_H
#define WIFI_FUNCS_H

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

#include <FS.h>

#include "../server/spiffs.h"
#include "../debug/toolsprint.h"

// ------------------ esp8266 wifi ------------------
#define ssid "ESP8266 - Heitor" // esp8266 wifi
#define password "12345678"

// ------------------- local wifi -------------------
#define user_wifi "BC Telecom anderson"
#define user_pass "m23m19v16v22h11h26"

#include "./wifi.cpp"

void start_local_wifi();
void start_esp8266_wifi();
String get_content_type(String filename);
void handle_big_file(String path, int type_send);
void handle_file(String path, int type_send);
void stream_file(class String path, int type);
void handle_page(String path);

#endif