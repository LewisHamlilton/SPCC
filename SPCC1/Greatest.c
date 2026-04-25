#include<stdio.h>
#include "Greatest.h"

int a, b, max;

int main()
{
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    MAX(a,b);

    printf("Greatest number is: %d", max);

    return 0;
}

