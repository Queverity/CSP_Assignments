#include <stdio.h>

int main(void){

    float income, rent, utilities, grocereries, transportation, savings, expenses, spend;

    float prent, putilities, pgroceries, ptransportation, psavings, pexpenses;

    printf("This is a budget calculator. Kind of. What is your monthly income? \n");
    
    scanf("%f", &income);

    printf("How much do your utilities cost per month?");

    scanf("%f", &utilities);

    printf("How much does your rent cost per month?");

    scanf("%f", &rent);

    printf("How much do your groceries cost per month?");

    scanf("%f", &grocereries);

    printf("How much does your transportation cost per month?");

    scanf("%f", &transportation);

    savings = income*0.2;

    expenses = rent+utilities+grocereries+transportation;

    spend = income-expenses-savings;

    printf("You make $%.2f\n", income);

    printf("Your expenses are $%.2f\n", expenses);

    printf("Your savings are $%.2f\n",savings );

    printf("Your spending money is $%.2f\n", spend);

    prent = rent/income*100;

    putilities = utilities/income*100;
    
    pgroceries = grocereries/income*100;

    ptransportation = transportation/income*100;

    psavings = savings/income*100;

    pexpenses = expenses/income*100;

    printf("Your rent is %d%% percent of your total income.\n", (int) prent);

    printf("Your utilities are %d%% percent of your total income.\n", (int) putilities);

    printf("Your groceries are %d%% percent of your total income.\n", (int) pgroceries);

    printf("Your transportation is %d%% percent of your total income.\n", (int) ptransportation);

    printf("Your savings are %d%% percent of your total income.\n", (int) psavings);

    printf("Your expenses are %d%% percent of your total income.\n", (int) pexpenses);
}