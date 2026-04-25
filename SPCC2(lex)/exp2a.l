%option noyywrap
%{
	#include<stdio.h>
%}
%%
"Aditya" printf("Hello World");
%%
int main()
{
	yylex();
	return 0;
}
