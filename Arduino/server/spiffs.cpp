
#include "../server/spiffs.h"

File open_file(String path, String mode) {
  File file = SPIFFS.open(path, "r");
  if (!file) {
    Serial.print("SPIFFS can't open '" + path + "', ");
    Serial.println("check if this path exist or the length limit.");
  }
  return file;
}

void write_file(String text, String path) { 
  File file = open_file(path, "w+"); 
  if (!file){ return; }

  file.println(text);
  file.close();
}

int count_lines_char(char *ptr, int num_bytes) {
  int n_lines = 0;

  for (int i=0; i<num_bytes; i++) {
    if (*ptr == '\n') { n_lines++; }
    ptr++;
  }
  ptr -= num_bytes;
  return n_lines + 1;
}

bool read_file(String path, char **ptr, int* num_bytes) {
  File file = open_file(path, "r");
  if (!file) { return 0; }

  *num_bytes = file.size();
  Serial.println("Reading file: " + path);
  
  *ptr = (char *) malloc((*num_bytes) * sizeof(char));
  Serial.println("Start pointer -=> " + String(int(ptr)));
  if (!(*ptr)) { return 0; }

  Serial.println("Succes: " + path);
  for (int i=0; i<(*num_bytes); i++) {
    **ptr = file.read();
    *ptr++;
  }
  **ptr = '\0';
  *ptr -= (*num_bytes);
  Serial.println("--");
  file.close();
  return 1;
}
 
void openFS(){
  //Abre o sistema de arquivos
  if (!SPIFFS.begin()){
    Serial.println("\nErro ao abrir o sistema de arquivos");
  }
  else {
    Serial.println("\nSistema de arquivos aberto com sucesso!");
  }
}

