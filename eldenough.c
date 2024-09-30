#include <stdio.h>

int main(void){
    int age = 17;
    if(age >= 18){
        printf("You are old enough to vote.");
    }else if(age >= 16){
        printf("You are old enough to drive.");
    }else if(age >= 15){
        printf("You are old enough to get a learner's permit.");
    }else if(age >= 5){
        printf("You are old enough to go to school.");
    }else{
        printf("You're a toddler. Why are you using this program?");
    }
}