#include <stdio.h>

float income, rent, utilities, grocereries, transportation, savings, expenses, spend;


float inputs(char type[],float var){
    printf("Monthly %s\n", type);
    scanf("%f",&var);
    return var;
}

void percent(char type[], int amount){
    int per = amount/income*100;

    printf("Your %s is %d%% of your income.\n",type, per);
}



int main(void){
    printf("This is a budget calculator.\n");
    
    income = inputs("income", income);

    rent = inputs("rent", rent);

    utilities = inputs("utilities", utilities);

    grocereries = inputs("groceries", grocereries);

    transportation = inputs("transportation", transportation);

    savings = income*0.2;

    expenses = rent+utilities+grocereries+transportation;

    spend = income-expenses-savings;

    printf("You make $%.2f\n", income);

    printf("Your expenses are $%.2f\n", expenses);

    printf("Your savings are $%.2f\n",savings );

    printf("Your spending money is $%.2f\n", spend);

    percent("rent",rent);

    percent("utilities",utilities);

    percent("groceries",grocereries);

    percent("transportation",transportation);

    percent("savings",savings);

    percent("expenses",expenses);
    
}