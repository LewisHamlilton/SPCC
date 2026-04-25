#include<stdio.h>
#include "Factors.h"

int n, i;

int main()
{
    printf("Enter a number: ");
    scanf("%d", &n);

    printf("Factors of %d are: ", n);
    FACTORS(n);

    return 0;
}

