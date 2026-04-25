%option noyywrap
%{
	#include<stdio.h>
%}
valid[A-Za-z]+(abb)
invalid[A-za-z]
%%
{valid} printf("valid string");
{invalid} printf("invalid string");
%%
int main()
{
	printf("Enter String:");
	yylex();
	return 0;
}
