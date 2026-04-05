#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main() {
    //INSERT el1 -> el2 and i want to insert el3 such that el1 -> el3 -> el2
    el3 -> next = el1 -> next;
    el1 -> next = el3;

    //DELETE el3 in el1 -> el3 -> el2 to ocme back to el1 -> el2
    Node* t = el1 -> next;
    el1 -> next = el1 -> next -> next;
    free(t); //avoids leakage

    //DELETE OF el WITH A GIVEN KEY - RECURSIVE
    void delete_key(Node* x, int key) {
        if (x == NULL) {
            printf("Not found.")
            return NULL;
        }

        if (x->key == key) {
            Node* t = x-> next;
            free(x);
            return t;
        }

        x -> next = delete_key(x-> next, key);
    }
    //OTHERWISE ALWAYS LOOP WITH DOUBLE POINTER AND APPLY DELETION ON pred if curr -> key matches key

    //DELETE FORM HEAD
    Node* t = head;
    head = head -> next;
    free(t); //avoids leakage

    //EXTRACTION FROM HEAD
    Node* t = head;
    int tmp = head -> val;
    head = head -> next;
    free(t); //avoids leakage

    return tmp;


    //SIMPLE LOOPING
    curr = head;
    while (curr != NULL) {
        value = curr -> value;
        //operations
        curr = curr -> next;
    }

    //DOUBLE POINTER LOOPING
    pred = NULL;
    curr = head;
    while (curr != NULL) {




        p = curr;
        curr = curr -> next;
    }

    //DOUBLE POINTER LOOPING WITHOUT HEAD

    //handle head case ...
    pred = head;
    curr = pred -> next;
    while (curr != NULL && pred != NULL) {




        pred = curr;
        curr = curr -> next;
    }

    //LOOPING WITH POINTER TO POINTER (to avoid shallow copy)
    Node** xp = &head;

    while (*xp != NULL) {


        xp = &((*xp) -> next);
    }

    //LOOPING WITH RECURSION
    void visit(Node* p) {
        if (p == NULL) {
            return;
        }
        //operations done in order of visiting
        visit(p -> next); //or first visit and then operations (done in reverse order --> first operation done on last element)
    }

    //NEW NODE
    Node* new_node(int val, Node* next) {
        Node* x = malloc(sizeof(Node));

        if (x == NULL) {
            //error
        }
        else {
            x -> val = val;
            x -> next = next;
        }
        return x;
    }

    //INSERT IN HEAD
    Node* head;
    head = new_node(val_new_head, head);

    //INSERT IN TAIL WHEN I DON'T HAVE POINTER TO TAIL --> O(n)
    if (head == NULL) {
        head = new_node(val, head);
        return;
    }

    curr = head;
    while (curr -> next != NULL) {
        curr = curr -> next;
    }
    curr -> next = new_node(val, curr);

    //INSERT IN TAIL WHEN I HAVE POINTER TO TAIL --> O(1)
    if (tail == NULL) { //empty list
        head = new_node(val, head);
        tail = head;
        return;
    }

    //not empty list
    tail -> next = new_node(val, NULL);
    tail = tail -> next;    

    //IF I HANDLE THESE OPERATIONS ON POINTER IN A FUNCTION, i MUST pass the REFERENCE OF THE POINTER to change it, otherwise i will change the copies


    //SAME OPERATIONS IN ORDERED LISTS BUT CHECK COMPARISONS

    //CIRCULAR LISTS

    //ONLY ONE ELEMENT
    head -> next == head;

    //LOOP
    curr = head -> next;

    while(curr != head) {
        //operations

        curr = curr -> next;
    }

    //DOUBLE CONCATENATED LIST (pointer to prev and next)

    //INSERT GIVEN PREVIOUS
    //insert el3 in el1 <-> el2 given el1 to obtain el1 <-> el3 <-> el2
    el3 -> next = el1 -> next;
    el3 -> prev = el1;
    
    el1 -> next -> prev = el3;
    el1 -> next = el3;



    //DELETE GIVEN POINTER --> WE DON'T NEED LOOP
    //delete el3 from el1 <-> el3 <-> el2 to obtain el1 <-> el2

    el3 -> next -> prev = el3 -> prev;
    el3 -> prev -> next = el3 -> next;
    free(el3);

    //REVERSE LIST
    void reverse(Node* head) {
        Node* t, Node* y;
        Node* rev_head = NULL;

        while (y != NULL) {
            t = y -> next; //save next

            //insert y in rev_head
            y -> next = rev_head;
            r = y;

            y=t; //go to next
        }

        return rev_head;
    }


    


    return 0;
}