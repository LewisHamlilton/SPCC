%{
#include<stdio.h>
int yylex(void);
int yyerror(const char *s);
int flag=0;
%}
%token NUM
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'
%%
ArithmeticExpression: E{
printf("\nResult=%d\n", $$);
return 0;
};
E:E'+'E {$$=$1+$3;}
| E'-'E {$$=$1-$3;}
|E'*'E {$$=$1*$3;}
|E'/'E {$$=$1/$3;}

|E'%'E {$$=$1%$3;}
|'('E')' {$$=$2;}
| NUM {$$=$1;}
;
%%
void main()
{
printf("\nEnter Any Arithmetic:\n");
yyparse();
if(flag==0)
printf("\nEntered arithmetic expression is Valid\n\n");
}
int yyerror(const char *s)
{
printf("\nEntered arithmetic expression is Invalid\n\n");
flag=1;
return 0;
}
