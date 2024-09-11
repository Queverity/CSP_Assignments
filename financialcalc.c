#include <stdio.h>

int main(void){
    int monthlyIncome[20];
    int rent[20];
    int utilities[20];
    int groceries[20];
    int monthlyIncome[20];
    printf("What is your monthly income? \n");
    fgets(monthlyIncome, sizeof(monthlyIncome), stdin);
    printf("What is your monthly rent?");
    fgets(rent, sizeof(rent), stdin);
    printf("How much do your utilities cost per month?");
    fgets(utilities, sizeof(utilities), stdin);
    printf("How much do your groceries cost per month");
    
    return 0;
}