%option noyywrap
%{
    #include <stdio.h>
    int upper = 0, lower = 0;
%}

/* Tokens */
upper_token    [a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*
lower_token    [a-zA-Z0-9]*[a-z]+[a-zA-Z0-9]*

%%

{upper_token}   { upper++; }
{lower_token}   { lower++; }

\n {
        printf("\nUppercase tokens: %d\n", upper);
        printf("Lowercase tokens: %d\n", lower);
    }

.   ;   /* ignore others */

%%

int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}

