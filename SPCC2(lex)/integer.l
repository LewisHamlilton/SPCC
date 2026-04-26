%option noyywrap
%{
    #include <stdio.h>
    int num1 = 0, num2 = 0, count = 0;
%}
/* Token for integer */
number    [0-9]+
%%
{number}  {
              if(count == 0)
                  num1 = atoi(yytext);
              else if(count == 1)
                  num2 = atoi(yytext);
              count++;
          }

\n {
        if(count >= 2)
            printf("\nSum = %d\n", num1 + num2);
        else
            printf("\nEnter at least two integers\n");
    }

.   ;   /* ignore other characters */

%%
int main()
{
    printf("Enter two integers:\n");
    yylex();
    return 0;
}