#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//!should be in .h to have a first class ADT
typedef struct pqueue* PQ; 

typedef struct Node {
    int key;
    int val; //priority
    struct Node* next;
} Node;


int main() { 
    struct pqueue {
        Node* head;
    };

    Node* NEW(int val, int key, Node* next) {
        Node* node = malloc(sizeof(Node));

        node -> val = val;
        node -> key = key;
        node -> next = next;

        return node;

    }


    PQ PQinit() {
        PQ q = malloc(sizeof(*PQ));

        q -> head = NULL;

        return q;
    }


    bool PQempty(PQ q) {
        return q -> head == null;
    }

    int ShowMax(PQ q) {
        if (PQempty(q)) {
            printf("Error: empty queue.\n")
            exit(1);
        }

        return q -> head -> key;
    }

    void PQdisplay(PQ q) {
        Node* curr = q -> head;
        
        if (curr == NULL) {
            printf("Empty queue");
            return;
        }

        while(curr != NULL) {
            printf("--> %d\n", curr -> key);
            curr = curr -> next;
        }

    }

    void PQinsert(PQ q, int val, int key) { //max priority = minimum val = ascending sorting
        if (PQempty(q) || q -> head -> val >= val) {
            q -> head = NEW(val, q -> head);
            return;
        }

        Node* pred = q -> head;
        Node* curr = pred -> next;

        while(curr != NULL && curr -> val < val) {
            pred = curr;
            curr = curr -> next;
        }

        pred -> next = NEW(val, key, curr);

    }

    int PQextractMaxPriority(PQ q) {
        if (PQempty(q)) {
            printf("Error: empty queue.\n");
            exit(1);
        }

        Node* old_head = q -> head;
        int tmp = old_head -> key;

        q -> head = q -> head -> next;
        free(old_head);

        return tmp;
    }

    
    void PQchange(PQ q, int key, int val) { //max priority = minimum val = ascending sorting
        if (PQempty(q)) {
            printf("Error: val not found.\n");
            exit(1);
        }

        if (q -> head -> key == key) {
            Node* t = q -> head;
            q -> head = q -> head -> next;
            free(t);

            PQinsert(q, val, key);

            return;
        }

        Node* pred = q -> head;
        Node* curr = q -> head -> next;

        while(curr != NULL) {

            if (curr -> key == key) { //delete
                pred -> next = curr -> next;
                free(curr);

                PQinsert(q, val, key);

                return;
            }
            pred = curr;
            curr = curr -> next;
        }

        

        printf("Error: val not found.\n");
        exit(1);

    }


   
    


    return 0;
}