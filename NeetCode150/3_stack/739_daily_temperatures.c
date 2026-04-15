/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct stack* STACK;


struct stack {
    int* ids;
    int top; // size == top + 1
};

STACK initStack(int max_size) {
    STACK st = malloc(sizeof(*st));
    st -> ids = malloc(max_size * sizeof(int));
    st -> top = -1;
    return st;
}

void push(STACK st, int id) {
    int idx = st -> top + 1;

    st -> ids[idx] = id;
    st -> top++;
}

void pop(STACK st) {
    st -> top--;
}

int top(STACK st) {
    return st -> ids[st -> top];
}

void freeStack(STACK st) {
    free(st -> ids);
    free(st);
}

bool StackIsVoid(STACK st) {
    return st -> top == -1;
}

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    (*returnSize) = temperaturesSize;
    int* res = calloc((*returnSize), sizeof(int));
    STACK st = initStack(temperaturesSize);

    if (temperaturesSize == 0) {
        return res;
    }

    push(st, temperaturesSize-1);

    for (int i = temperaturesSize - 2; i >= 0; i--) {    
        while(!StackIsVoid(st) && temperatures[i] >= temperatures[top(st)]) {
            pop(st);
        }

        if (!StackIsVoid(st)) {
            res[i] = top(st) - i;
        } //otherwise res[i] remains 0 (I did calloc)

        
        push(st, i);
    }

    freeStack(st);

    return res;
}