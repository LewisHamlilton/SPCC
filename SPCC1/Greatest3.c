#include<stdio.h>
#include "Greatest3.h"

int a, b, c, max;

int main()
{
   printf("Enter three numbers: ");
   scanf("%d %d %d", &a, &b, &c);

   MAX3(a,b,c);

   printf("Greatest number is: %d", max);

   return 0;
}

