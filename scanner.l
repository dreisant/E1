%{
#include <stdio.h>
#include "token.h"
%}

%option noyywrap
%option nounput
%option noinput

DIGIT   [0-9]
NUM     {DIGIT}+(\.{DIGIT}+)?

%%

[ \t\r]+        ;
\n              { return EOL; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return TIMES; }
"/"             { return DIV; }
{NUM}           { return NUM; }
.               { return ERROR; }

%%
