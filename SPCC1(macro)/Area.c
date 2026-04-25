#include<stdio.h>
#include "Area.h"

int side, length, breadth, sq, rect;

int main()
{
    printf("Enter Side of Square: ");
    scanf("%d", &side);
    sqArea(side);

    printf("Enter Length of Rectangle: ");
    scanf("%d", &length);

    printf("Enter Breadth of Rectangle: ");
    scanf("%d", &breadth);
    rectArea(length, breadth);

    printf("\nArea of Square is: %d", sq);
    printf("\nArea of Rectangle is: %d", rect);

    return 0;
}

