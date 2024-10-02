#include <stdio.h>
#include <time.h>
int hour;

int main(void){
    time_t rawtime;
    struct tm *timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current local time and date: %s", asctime(timeinfo));
    printf("What is the hour in military time?");
    scanf("%d",&hour);
    if (hour <= 12){
        printf("Good morning!");
    }else if (hour <= 18){
        printf("Good afternoon!");
    }else if (hour <= 24){
        printf("Good evening!");
    }else{
        printf("That's not a time.");
    }
    return 0;
}