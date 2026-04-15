typedef struct Item {
    int val;
    int minimum;
} Item;

typedef struct {
    Item* nodes;
    int capacity;
    int top; //current top element index --> size == top + 1
} MinStack;


MinStack* minStackCreate() {
    MinStack* stack = malloc(sizeof(MinStack));
    int capacity = 16;
    stack -> nodes = malloc(capacity * sizeof(Item));
    stack -> capacity = capacity;
    stack -> top = -1;

    return stack;
}

void minStackPush(MinStack* obj, int val) {
    int idx = obj -> top + 1;
    int minimum;

    if (idx >= obj -> capacity) {
        obj -> capacity *=2;
        obj -> nodes = realloc(obj -> nodes , obj -> capacity * sizeof(Item));
    }

    if (obj -> top == -1) {
        obj -> nodes[idx].val = val;
        obj -> nodes[idx].minimum = val;
        obj -> top++;
        return;
    }

    if (val < obj -> nodes[obj -> top].minimum) {
        minimum = val;
    }
    else {
        minimum = obj -> nodes[obj -> top].minimum;
    }

    obj -> nodes[idx].val = val;
    obj -> nodes[idx].minimum = minimum;
    obj -> top++;
}

void minStackPop(MinStack* obj) {
    obj -> top--;
}

int minStackTop(MinStack* obj) {
    return obj -> nodes[obj -> top].val;
}

int minStackGetMin(MinStack* obj) {
    return obj -> nodes[obj -> top].minimum;
}


void minStackFree(MinStack* obj) {
    free(obj -> nodes);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/