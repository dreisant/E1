#include <stdio.h>
#include "token.h"

extern int yylex(void);
extern char *yytext;

int main(void) {
    int token;

    while ((token = yylex()) != EOL) {
        if (token == NUM) {
            printf("<token: %d, atrib: %s>\n", token, yytext);
        } else if (token == ERROR) {
            printf("lexical error, char %s\n", yytext);
        } else {
            printf("<token: %d>\n", token);
        }
    }

    return 0;
}
