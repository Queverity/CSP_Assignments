#include <stdio.h>

int main(void){
    const char *family[] = {"Mom","Dad","Mysti"};
    int num_family = sizeof(family) / sizeof(family[0]);

    for (int i = 0; i < num_family; i++){
        printf("Hello %s!\n", family[i]);
    }
    return 0;
}