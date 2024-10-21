#include <stdio.h>
int i;
int main(void){
    int user = printf("Give me a number1000.");
    scanf("%d",&user);
    for(i = 1;i <= user; ++i){
        if(i % 3 == 0 && i % 5 == 0){
            printf("FizzBuzz\n");
        }else if(i % 3 == 0){
            printf("Fizz\n");
        }else if(i % 5 == 0){
            printf("Buzz\n");
        }else{
            printf("%d\n",i);
        }
    }
    return 0;
}