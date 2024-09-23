#include <stdio.h>
void name(const char name[]){
    printf("Hello %s\n", name);
}

int main(void){
    name("Pryor");
    name("Carson");
    name("Aiden");
    name("Jennsen");
    name("Jared");
}