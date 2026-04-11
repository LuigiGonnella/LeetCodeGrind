#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct Item {
    char type;
    struct Item* next;
} Item;

typedef struct Stack {
    Item* head;
} Stack;

void push(Stack* stack, char type) {
    Item* el = malloc(sizeof(Item));
    el -> type = type;
    el -> next = stack -> head;
    stack -> head = el;
    printf("pushed %c\n", type);
}

bool pop(Stack* stack, char type) {
    if (stack -> head == NULL) {
        return false;
    }

    switch(type) {
        case ')':
            type = '(';
            break;
        case ']':
            type = '[';
            break;
        case '}':
            type = '{';
            break;
    }

    printf("want to pop %c\n", type);

    if (stack -> head -> type == type) {
        Item* t = stack -> head;
        stack -> head = stack -> head -> next;
        free(t);
        return true;
    }

    return false;
}

bool stackIsVoid(Stack* stack) {
    return stack -> head == NULL;
}


void freeStack(Stack* stack) {
    Item* curr = stack -> head;

    while (curr != NULL) {
        Item* t = curr;
        curr = curr-> next;
        free(t);
    }
}


bool isValid(char* s) {
    int len = strlen(s);
    Stack* stack = malloc(sizeof(Stack));
    stack -> head = NULL;
    bool result = true;

    for (int i = 0; i< len; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            push(stack, s[i]);
        }
        else {
            if (!pop(stack, s[i])) {
                result = false;
                break;
            }
        }
    }

    if (result) {
        result = stackIsVoid(stack);
    }

    freeStack(stack);
    free(stack);
    return result;
    
}