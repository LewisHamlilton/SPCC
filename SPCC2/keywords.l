%option noyywrap
%{
    #include <stdio.h>
    int count = 0;
%}

/* Define keywords */
keywords    (if|else|while|for|int|float|char|return|break|continue)

%%

{keywords}   {
                printf("Keyword: %s\n", yytext);
                count++;
             }

.   ;   /* ignore other characters */

\n  {
        printf("\nTotal Keywords: %d\n", count);
    }

%%

int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}

