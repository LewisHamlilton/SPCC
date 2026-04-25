%option noyywrap
%{
    #include <stdio.h>
    int punc=0, keyw=0, oper=0, iden=0, lit=0;
%}

keywords        (int|float|if|else|while|for)
literals        [0-9]+
identifiers     [aA-zZ]+
operators       [+\-*/<>=]
punctuations    [(){},:;#.~]

%%
{keywords}        { keyw++; }
{literals}        { lit++; }
{identifiers}     { iden++; }
{operators}       { oper++; }
{punctuations}    { punc++; }


\n {
        printf("\nKeywords count is: %d\n", keyw);
        printf("Literals count is: %d\n", lit);
        printf("Identifiers count is: %d\n", iden);
        printf("Operators count is: %d\n", oper);
        printf("Punctuation count is: %d\n", punc);
    }
%%
int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}
