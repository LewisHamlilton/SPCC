#include<stdio.h>
#include"Cal.h"
int main()
{
	int opt, a,b;
	do
	{
		printf("\nEnter the value of A and B:");
		scanf("%d %d", &a,&b);
		printf("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit");
		printf("Enter your choice:");
		scanf("%d", &opt);
		switch(opt)
		{
			case 1: 
				printf("Addition: %d", add(a,b));
				break;
			case 2:
				printf("Subtraction: %d", sub(a,b));
				break;
			case 3:
				printf("Multiplication: %d", mul(a,b));
				break;
			case 4:
				printf("Division: %d",div(a,b));
				break;
			case 5:
				printf("Exit");
				break;
			default:
				printf("Invalid Option");
		}
		printf("\n\n");
	}while(opt !=5);
	return 0;
}
