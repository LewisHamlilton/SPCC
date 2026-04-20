#include<stdio.h>
#include"Fact.h"
int i,fact=1,side,n,sq;
float radius,cr;
int main()
{
	printf("Enter Number for Factorial:");
	scanf("%d",&n);
	FACT(n);
	printf("Enter Side of Square:");
	scanf("%d",&side);
	sqArea(side);
	printf("Enter Radius of Circle:");
	scanf("%f",&radius);
	crArea(radius);
	printf("Factorial of number is:%d", fact);
	printf("\nArea Of Square is:%d", sq);
	printf("\nArea Of Circle is:%f", cr);
	return 0;
}
