#include <stdio.h>

int main(void){
    int time = 19;
    if (time <= 12){
        printf("Good morning!");
    }else if (time <= 18){
        printf("Good afternoon!");
    }else if (time <= 24){
        printf("Good evening!");
    }
}