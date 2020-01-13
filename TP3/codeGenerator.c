#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

int codeGenerator(int lower, int upper){
    srand(time(0)); //Usa o tempo atual como seed para o gerador

    int number = (rand() % (upper - lower + 1)) + lower;

    return number; 
}
  
int main() 
{ 
    int lower = 1000, upper = 9999;
  
    int num = codeGenerator(lower,upper);

    printf("Código de segurança: %d\n", num);
  
    return 0; 
}