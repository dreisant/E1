#ifndef TOKEN_H
#define TOKEN_H

typedef enum {
    EOL = 0,
    NUM,
    PLUS,
    MINUS,
    TIMES,
    DIV,
    ERROR
} token_t;

#endif
