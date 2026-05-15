#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//!should be in .h to have a first class ADT
typedef struct queue* QUEUE; 

typedef struct Node {
    int val;
    struct Node* next;
} Node;


int main() { 
    struct queue {
        Node* head;
        Node* tail;
    };

    Node* NEW(int val, Node* next) {
        Node* node = malloc(sizeof(Node));

        node -> val = val;
        node -> next = next;

        return node;

    }

    void TailInsert(QUEUE q, int val) {
        Node* t = q -> tail -> next;
        Node* new_tail = NEW(val, NULL);
        q -> tail -> next = new_tail;

        q -> tail = new_tail;
    }

    int HeadGet(QUEUE q) {
        int val = q -> head -> val;

        Node* old_head = q -> head;
        q -> head = q -> head -> next;
        free(old_head);

        return val;
    }


    QUEUE QUEUEinit() {
        QUEUE q = malloc(sizeof(*QUEUE));

        q -> head = NULL;
        q -> tail = NULL;

        return q;
    }


    bool QUEUEempty(QUEUE q) {
        return q -> head == null;
    }

    void QUEUEput(QUEUE q, int val) {
        if (QUEUEempty(q)) {
            q-> tail = NEW(val, NULL);
            q -> head = q-> tail;
            return;
        }

        TailInsert(q);

    }

    int QUEUEget(QUEUE q) {
        if (QUEUEempty(q)) {
            printf("Error: empty queue.\n")
            exit(1);
        }

        return HeadGet(QUEUE q);
    }


   
    


    return 0;
}