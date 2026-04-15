//! O(max_height + NlogN)
// #define MAX_HEIGHT ((int)1e4)

// typedef struct Item {
//     int height;
//     int id;
// } Item;

// typedef struct Element {
//     int base;
//     int id;
//     struct Element* next;
// } Element;

// void update(Element** table, int id, int base, int height) {
//     Element* curr = table[height];

//     while (curr != NULL) {
//         if (curr -> id == id) {
//             curr -> base = base;
//             return;
//         }
//     }

//     Element* el = malloc(sizeof(Element));
//     el -> base = base;
//     el -> id = id;
//     el -> next = table[height];
//     table[height] = el;
// }

// int get_base(Element** table, int id, int height) {
//     Element* curr = table[height];

//     while (curr != NULL) {
//         if (curr -> id == id) {
//             return curr -> base;
//         }
//     }

//     return -1;
// }


// int cmp(const void* a, const void* b) {
//     Item* ia = (const Item*) a;
//     Item* ib = (const Item*) b;

//     return ib -> height - ia -> height; //descending order
// }

// int largestRectangleArea(int* heights, int heightsSize) {
//     if (heightsSize == 0) {
//         return 0;
//     }

//     int curr_height, left_height, right_height, left_base, right_base, idx;
//     Item* items = malloc(heightsSize * sizeof(Item));
//     Element** max_bases_left = calloc(MAX_HEIGHT, sizeof(Element*));
//     Element** max_bases_right = calloc(MAX_HEIGHT, sizeof(Element*));


//     for (int i = 0; i< heightsSize; i++) {
//         items[i].height = heights[i];
//         items[i].id = i;
//     }

//     qsort(items, heightsSize, sizeof(Item), cmp);
//     update(max_bases_left, items[0].id, 1, items[0].height); //max_base = 1

//     for (int i = 1; i< heightsSize; i++) {
//         curr_height = items[i].height;
//         idx = items[i].id-1;
//         left_height = idx >= 0 ? heights[idx] : -1;
//         if (left_height >= curr_height) {
//             update(max_bases_left, idx+1, get_base(max_bases_left, idx, left_height), curr_height);
//         }
//         else {
//             update(max_bases_left, idx+1, 1, curr_height);
//         }
//     }


//     update(max_bases_right, items[0].id, 0, items[0].height); //max_base = 0

//     for (int i = 1; i< heightsSize; i++) {
//         curr_height = items[i].height;
//         idx = items[i].id+1;
//         right_height = idx < heightsSize ? heights[idx] : -1;
//         if (right_height >= curr_height) {
//             update(max_bases_right, idx-1, get_base(max_bases_right, idx, right_height), curr_height);
//         }
//         else {
//             update(max_bases_right, idx-1, 0, curr_height);
//         }
//     }



//     int max_area = 0;

//     for (int i = 0; i< heightsSize; i++) {
//         if (heights[i] * (get_base(max_bases_left, i, heights[i]) + get_base(max_bases_right, i, heights[i])) > max_area) {
//             max_area = heights[i] * (get_base(max_bases_left, i, heights[i]) + get_base(max_bases_right, i, heights[i]));
//         }
//     }

//     free(items);
//     free(max_bases_left);
//     free(max_bases_right);

//     return max_area;
// }

//! O(N)
typedef struct stack* STACK;

typedef struct Node {
    int index;
    int height;
} Node;

struct stack {
    Node* nodes;
    int top;
};

STACK initStack(int maxN) {
    STACK st = malloc(sizeof(*st));

    st -> nodes = malloc(maxN*sizeof(Node));
    st -> top = -1; //size = top + 1

    return st;
}

Node pop(STACK st) {
    return st -> nodes[st -> top--];
}

void push(STACK st, int index, int height) {
    int idx = st -> top + 1;
    st -> nodes[idx].index = index;
    st -> nodes[idx].height = height;
    st -> top ++;
}

int top_height(STACK st) {
    return st -> nodes[st -> top].height;
}

bool stackIsEmpty(STACK st) {
    return st->top == -1;
}

int largestRectangleArea(int* heights, int heightsSize) {
    if (heightsSize == 0) {
        return 0;
    }

    int curr_height, curr_top_height, max_area = 0;
    Node top;

    STACK st = initStack(heightsSize);

    push(st, 0, heights[0]);

    for (int i = 1; i< heightsSize; i++) {
        curr_height = heights[i];
        curr_top_height = top_height(st);

        if (curr_top_height <= curr_height) {
            push(st, i, curr_height);
        }
        else {
            while (curr_top_height > curr_height && !stackIsEmpty(st)) {
                top = pop(st);
                
                if ((i - top.index) * top.height > max_area) {
                    max_area = (i - top.index) * top.height;
                }    

                if (!stackIsEmpty(st)) {
                    curr_top_height = top_height(st); 
                }     

            }
            push(st, top.index, curr_height);
        }    
    }

    while (!stackIsEmpty(st)) {
        top = pop(st);

        if ((heightsSize - top.index) * top.height > max_area) {
            max_area = (heightsSize - top.index) * top.height;
        }
            
    }

    free(st->nodes);
    free(st);

    return max_area;

}

//or, more readable:
typedef struct stack* STACK;

typedef struct Node {
    int index;
    int height;
} Node;

struct stack {
    Node* nodes;
    int top;
};

STACK initStack(int maxN) {
    STACK st = malloc(sizeof(*st));

    st -> nodes = malloc(maxN*sizeof(Node));
    st -> top = -1; //size = top + 1

    return st;
}

Node pop(STACK st) {
    return st -> nodes[st -> top--];
}

void push(STACK st, int index, int height) {
    int idx = st -> top + 1;
    st -> nodes[idx].index = index;
    st -> nodes[idx].height = height;
    st -> top ++;
}

int top_height(STACK st) {
    return st -> nodes[st -> top].height;
}

bool stackIsEmpty(STACK st) {
    return st->top == -1;
}

int largestRectangleArea(int* heights, int heightsSize) {
    if (heightsSize == 0) {
        return 0;
    }

    int curr_height, curr_top_height, max_area = 0;
    Node top;

    STACK st = initStack(heightsSize);

    for (int i = 0; i < heightsSize; i++) {
        int start_index = i;
        
        // Pop all taller bars and calculate their areas
        while (!stackIsEmpty(st) && top_height(st) > heights[i]) {
            top = pop(st);
            int area = (i - top.index) * top.height;
            if (area > max_area) {
                max_area = area;
            }
            // Carry the index backward for the current bar
            start_index = top.index; 
        }
        
        // Push the current bar, stretched back to start_index
        push(st, start_index, heights[i]);
    }

    while (!stackIsEmpty(st)) {
        top = pop(st);

        if ((heightsSize - top.index) * top.height > max_area) {
            max_area = (heightsSize - top.index) * top.height;
        }
            
    }

    free(st->nodes);
    free(st);

    return max_area;

}
