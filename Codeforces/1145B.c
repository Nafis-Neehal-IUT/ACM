// Kanban Numbers - Codeforces 1145A - April Fools Day Contest 2019
// Author -  Nafis Neehal (nafisneehal.iut@gmail.com)
#include <stdio.h>

// use gnu -g <filename.c> to compile the c file

int main(){
    int n, first_digit, second_digit;
    scanf("%d", &n);
    first_digit = n%10;
    second_digit = (n-first_digit)/10;
    if (n>=1 && n<=99){
        if(first_digit==1 || first_digit==7 || first_digit==9){
            printf("NO");
        } else if(n!=12 && (second_digit == 1 || second_digit == 2 || second_digit == 7 || second_digit == 9)){
            printf("NO");
        } else{
            printf("YES");
        }
    }
    return 0;
}