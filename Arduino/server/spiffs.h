
#ifndef FILE_FUNCS_H
#define FILE_FUNCS_H

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <FS.h>

#include "./spiffs.cpp"

void write_file(String text, String path);
int count_lines_char(char *ptr, int num_bytes);
char* read_file(String path, int* num_bytes);
void openFS();

#endif
