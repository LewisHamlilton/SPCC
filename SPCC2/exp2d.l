%option noyywrap
%{
	#include<stdio.h>
	int res;
%}
%%
[0-9]+ {
	res=atoi(yytext);
	if(res%2==0){
		printf("Number is even");
	}else{
		printf("Number is odd");
	}
}
%%
int main()
{
	printf("Enter a number:");
	yylex();
	return 0;
}
