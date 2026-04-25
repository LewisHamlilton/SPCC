%option noyywrap
%{
    #include <stdio.h>
    int lines = 0;
%}

%%

\n      { lines++; }     /* count each newline */

.       ;               /* ignore all other characters */

%%

int main()
{
    printf("Enter source program:\n");
    yylex();

    printf("\nNumber of lines: %d\n", lines);
    return 0;
}

