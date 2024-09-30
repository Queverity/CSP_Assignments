#include <stdio.h>

int main(void){
    int time = 12;
    if (time <= 12){
        printf("Good morning!");
    }else if (time <= 18){
        printf("Good afternoon!");
    }else if (time <= 24){
        printf("Good evening!");
    }
}