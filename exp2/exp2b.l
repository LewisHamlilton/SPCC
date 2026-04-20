%option noyywrap
%{
	#include<stdio.h>
	int vcount=0, ccount=0, dcount=0;
%}
Vowels[AEIOUaeiou]+
Consonant[A-Za-z^AEIOUaeiou]+
%%
{Vowels} vcount++;
{Consonant} ccount++; 
%%
int main()
{
	printf("Enter String:");
	yylex();
	printf("Vowels is present in the string and count of vowels is:%d",vcount);
	printf("Consonant is present in the string and count of consonant is:%d",ccount);
	return 0;
}
