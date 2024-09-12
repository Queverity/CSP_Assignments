#include <stdio.h>

int main(void){
    
    char monthlyIncome[20];

    char rent[20];

    char utilities[20];

    char groceries[20];

    char commute[20];

    char savings[] = (int)monthlyIncome*0.10;

    printf("This is a budget calculator. Kind of. What is your monthly income? \n");

    fgets(monthlyIncome, sizeof(monthlyIncome), stdin);

    printf("What is your monthly rent? \n");

    fgets(rent, sizeof(rent), stdin);

    printf("How much do your utilities cost per month? \n");

    fgets(utilities, sizeof(utilities), stdin);

    printf("How much do your groceries cost per month? \n");

    fgets(groceries, sizeof(groceries), stdin);

    printf("How much does your monthly commute cost? \n");

    fgets(commute, sizeof(commute),stdin);

    char accountAfter = (float)rent+(float)utilities+(float)groceries+(float)commute+(float)savings;

    char rentPercent[] = (float)rent/(float)monthlyIncome;

    char utilitiesPercent[] = (float)utilities/(float)monthlyIncome;

    char groceriesPercent[] = (float)groceries/(float)monthlyIncome;

    char commutePercent[] = (float)commute/(float)monthlyIncome;

    printlf("You should put ", savings, " dollars into your savings account. This is 10 percent of your monthly income.");

    printlf("Rent is ", rentPercent, " percent of your monthly income.");

    printlf("Utilities are ", utilitiesPercent, " percent of your monthly income.");

    printlf("Groceries are ", groceriesPercent), " percent of your monthly income.";

    printlf("Commute is ", commutePercent, " percent of your monthly income.");

    printlf("You have ", accountAfter, " dollars left in your account. Have fun!");

    return 0;
}