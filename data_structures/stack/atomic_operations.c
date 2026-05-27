#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//!should be in .h to have a first class ADT
typedef struct stack* STACK;

typedef struct Node {
    int val;
    struct Node* next;
} Node;




int main() { 
   
    struct stack { //!we can implement it with VECTOR or LIST
        Node* head;
    };

    Node* NewNode(int val, Node* next) {
        Node* node = malloc(sizeof(Node));
        node -> val = val;
        node -> next = next;

        return node;
    }

    STACK STACKinit() {
        STACK s = malloc(sizeof(*s));
        s-> head = NULL;
    }

    int STACKempty(STACK s) {
        return s->head == NULL;
    }

    void STACKpush(STACK s, int val) {
        s->head = NewNode(val, s->head);
    }

    int STACKpop(STACK s) {
        int tmp = s-> head -> val; 
        Node* new_head =  s-> head -> next;
        free(s-> head);
        s->head = new_head;

        return tmp;
    }



    return 0;
}