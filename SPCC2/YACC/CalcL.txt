%option noyywrap
%{
/* Definition section */
#include<stdio.h>
#include"y.tab.h"
%}
/* Rule Section */
%%
[0-9]+ {
yylval=atoi(yytext);
return NUM;
}
[\t] ;
[\n] return 0;
. return yytext[0];
%%
