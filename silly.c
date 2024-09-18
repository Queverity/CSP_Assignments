#include <stdio.h>
#include <string.h>

int main(void){
    char noun[30];
    char adjective[30];
    char food[30];
    char partOne[1500] = "The man ate his ";
    char partTwo[] = " ";
    char partThree[] = " on the plate with a ";
    char partFour[] = ".";
    printf("Give me a noun.\n");
    fgets(noun, sizeof(noun),stdin);
    printf("Give me a adjective.\n");
    fgets(adjective, sizeof(adjective),stdin);
    printf("Give me a food.\n");
    fgets(food, sizeof(food),stdin);
    strcat(partOne,adjective);
    strcat(partTwo,food);
    strcat(partThree,noun);
    strcat(partOne,partTwo);
    strcat(partOne,partThree);
    strcat(partOne,partFour);
    printf("%s\n",partOne);
}