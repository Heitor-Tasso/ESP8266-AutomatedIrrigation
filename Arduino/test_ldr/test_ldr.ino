#include <Arduino.h>
 
#define MUX_0 10
#define MUX_1 5
#define MUX_2 6
#define MUX_3 7

#define ANALOGIC_MUX A0

int count_mux = 0;

void setup() {
    Serial.begin(9600);

    pinMode(MUX_0, OUTPUT);
    pinMode(MUX_1, OUTPUT);
    pinMode(MUX_2, OUTPUT);
    pinMode(MUX_3, OUTPUT);

   pinMode(ANALOGIC_MUX, INPUT);
}

void write_in_mux(int n) {
    digitalWrite(MUX_0, bitRead(n, 0));
    digitalWrite(MUX_1, bitRead(n, 1));
    digitalWrite(MUX_2, bitRead(n, 2));
    digitalWrite(MUX_3, bitRead(n, 4));
}

void next_pin_mux() {
    count_mux++;
    if (count_mux > 15) {
        count_mux=0;
    }
}

void loop() {
    write_in_mux(count_mux);
    int value = analogRead(ANALOGIC_MUX);
    Serial.println("Value -=> " + String(value));

    delay(600);
    next_pin_mux();
}
