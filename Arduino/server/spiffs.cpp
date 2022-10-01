
#include "../server/spiffs.h"

void write_file(String text, String path) { 
  File file = SPIFFS.open(path, "w+"); 
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

char* read_file(String path, int* num_bytes) {
  File file = SPIFFS.open(path, "r");
  char *ptr;
  if (!file) { return ptr; }

  *num_bytes = file.size();
  ptr = (char*) calloc((*num_bytes), sizeof(char));

  for (int i=0; i<(*num_bytes); i++) {
    *ptr = file.read();
    ptr++;
  }
  *ptr = '\0';
  file.close();
  ptr -= (*num_bytes);
  return ptr;
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

