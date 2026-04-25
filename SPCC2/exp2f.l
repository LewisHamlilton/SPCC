%option noyywrap
%{
	#include<stdio.h>
%}
correct A[A-Za-z]{2}
incorrect [A-Za-z]+
%%
{correct} printf(yytext);
{incorrect} 
%%
int main()
{
	printf("Enter the string:");
	yylex();
	return 0;
}

