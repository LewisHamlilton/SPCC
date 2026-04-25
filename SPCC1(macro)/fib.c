#include<stdio.h>
#include "fib.h"

int i,n;

int main()
{
    printf("Enter number of terms:");
    scanf("%d",&n);

    printf("Fibonacci Series: ");
    FIB(n);

    return 0;
}
