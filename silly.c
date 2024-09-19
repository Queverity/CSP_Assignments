#include <stdio.h>
#include <string.h>

int main(void){
    char noun[30];
    char adjective[30];
    char food[30];
    char output[1500] = "The man ate his ";
    printf("Give me a noun.\n");
    fgets(noun, sizeof(noun),stdin);
    printf("Give me a adjective.\n");
    fgets(adjective, sizeof(adjective),stdin);
    printf("Give me a food.\n");
    fgets(food, sizeof(food),stdin);
    noun[strcspn(noun, "\n")] = '\0';
    adjective[strcspn(adjective, "\n")] = '\0';
    food[strcspn(food, "\n")] = '\0';
    strcat(output,adjective);
    strcat(output," ");
    strcat(output,food);
    strcat(output, " on the plate with a ");
    strcat(output,noun);
    strcat(output, ".");
    printf("%s\n",output);
}