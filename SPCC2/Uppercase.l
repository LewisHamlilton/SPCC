%option noyywrap
%{
    #include <stdio.h>
    int upper_tokens = 0;
%}

/* Token having at least one uppercase letter */
upper_token    [a-zA-Z0-9]*[A-Z]+[a-zA-Z0-9]*

%%

{upper_token}    { upper_tokens++; }

\n {
        printf("\nTokens with uppercase letters: %d\n", upper_tokens);
    }

.   ;   /* ignore other characters */

%%
int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}

