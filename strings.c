#include <stdio.h>
#include <string.h>

int main(void){
    char name[30];
    char dec1One[30] = "<<< ";
    char dec1Two[30] = " >>>";
    char dec2One[30] = "((( ";
    char dec2Two[30] = " )))";
    char dec3One[30] = "--- ";
    char dec3Two[30] = " ---";
    char dec4One[30] = "(: (: ";
    char dec4Two[30] = " :) :)";
    char dec5One[30] = "### ";
    char dec5Two[30] = " ###";
    char dec6One[30] = "+++ ";
    char dec6Two[30] = " +++";
    char dec7One[30] = "~~~ ";
    char dec7Two[30] = " ~~~";
    char dec8One[30] = "=== ";
    char dec8Two[30] = " ===";
    printf("What is your name?");
    fgets(name, sizeof(name), stdin);
    size_t len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    }
    strcat(dec1One,name);
    strcat(dec1One,dec1Two);
    strcat(dec2One,name);
    strcat(dec2One,dec2Two);
    strcat(dec3One,name);
    strcat(dec3One,dec3Two);
    strcat(dec4One,name);
    strcat(dec4One,dec4Two);
    strcat(dec5One,name);
    strcat(dec5One,dec5Two);
    strcat(dec6One,name);
    strcat(dec6One,dec6Two);
    strcat(dec7One,name);
    strcat(dec7One,dec7Two);
    strcat(dec8One,name);
    strcat(dec8One,dec8Two);
    printf("%s\n",dec1One);
    printf("%s\n",dec2One);
    printf("%s\n",dec3One);
    printf("%s\n",dec4One);
    printf("%s\n",dec5One);
    printf("%s\n",dec6One);
    printf("%s\n",dec7One);
    printf("%s\n",dec8One);
}