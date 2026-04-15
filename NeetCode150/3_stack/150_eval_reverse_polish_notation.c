typedef struct stack* STACK;

struct stack {
    int* values;
    int top; //index of the top element --> actual size == top + 1
    int capacity; //allocated space for values vector
};

STACK initStack() {
    STACK st = malloc(sizeof(*st));
    st -> capacity = 16;
    st -> values = malloc(16 * sizeof(int));
    st -> top = -1;
    return st;
}

void push(STACK st, int val) {
    int idx = st -> top + 1;

    if (idx >= st -> capacity) {
        int capacity = st -> capacity * 2;
        st -> values = realloc(st -> values, capacity * sizeof(int));
        st -> capacity = capacity;
    }

    st -> values[idx] = val;
    st -> top++;
}

int pop(STACK st) {
    return st -> values[st -> top--];
}

void freeStack(STACK st) {
    free(st -> values);
    free(st);
}

int getSize(STACK st) {
    return st -> top + 1;
}

int evalRPN(char** tokens, int tokensSize) {
    int result;
    int operand1;
    int operand2;
    int number_len, i, j;
    int curr_num, curr_digit, multiplier;
    char curr_char;

    STACK st = initStack(); 

    for (i =0; i< tokensSize; i++) {
        if (strcmp("+", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            result = operand1 + operand2;
            push(st, result);
            printf("pushd result: %d\n", result);
        }
        else if (strcmp("*", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            result = operand1 * operand2;
            push(st, result);
            printf("pushd result: %d\n", result);
        }
        else if (strcmp("-", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            result = operand1 - operand2;
            push(st, result);
            printf("pushd result: %d\n", result);
        }
        else if (strcmp("/", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            result = operand1 / operand2;
            push(st, result);
            printf("pushd result: %d\n", result);
        }
        else { //!ATOI already handles negative numbers (see later)
            if (curr_char = tokens[i][0] == '-') {
                curr_num = 0;
                number_len = strlen(tokens[i]);
                for (j = 1; j<number_len; j++) {
                    curr_char = tokens[i][j];
                    curr_digit = curr_char - '0';
                    curr_num *= 10;
                    curr_num += curr_digit;
                }
                push(st, -curr_num);
                printf("pushed %d\n", -curr_num);
            }
            else {
                curr_num = 0;
                number_len = strlen(tokens[i]);
                for (j = 0; j<number_len; j++) {
                    curr_char = tokens[i][j];
                    curr_digit = curr_char - '0';
                    curr_num *= 10;
                    curr_num += curr_digit;
                }
                push(st, curr_num);
                printf("pushed %d\n", curr_num);
            }
        }
    }

    result = pop(st);
    printf("popped RESULT: %d\n", result);
    freeStack(st);
    return result;
    
}

//!ATOI already handles negative numbers
typedef struct stack* STACK;

struct stack {
    int* values;
    int top; //index of the top element --> actual size == top + 1
    int capacity; //allocated space for values vector
};

STACK initStack() {
    STACK st = malloc(sizeof(*st));
    st -> capacity = 16;
    st -> values = malloc(16 * sizeof(int));
    st -> top = -1;
    return st;
}

void push(STACK st, int val) {
    int idx = st -> top + 1;

    if (idx >= st -> capacity) {
        int capacity = st -> capacity * 2;
        st -> values = realloc(st -> values, capacity * sizeof(int));
        st -> capacity = capacity;
    }

    st -> values[idx] = val;
    st -> top++;
}

int pop(STACK st) {
    return st -> values[st -> top--];
}

void freeStack(STACK st) {
    free(st -> values);
    free(st);
}

int getSize(STACK st) {
    return st -> top + 1;
}

int evalRPN(char** tokens, int tokensSize) {
    int result;
    int operand1;
    int operand2;
    int number_len, i, j;
    int curr_num, curr_digit, multiplier;
    char curr_char;

    STACK st = initStack(); 

    for (i =0; i< tokensSize; i++) {
        if (strcmp("+", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            push(st, operand1 + operand2);
        }
        else if (strcmp("*", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            push(st, operand1 * operand2);
        }
        else if (strcmp("-", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            push(st, operand1 - operand2);
        }
        else if (strcmp("/", tokens[i]) == 0) {
            operand2 = pop(st);
            operand1 = pop(st);
            push(st, operand1 / operand2);
        }
        else {
            push(st, atoi(tokens[i]));
        }
    }

    result = pop(st);
    freeStack(st);
    return result;
    
}