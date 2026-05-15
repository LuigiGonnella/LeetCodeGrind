#define MAX 100000
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node* next;
} Node;

Node* table[MAX];


int hash(int key) {
    if (key < 0) key = -key;

    return key % MAX; //map between 0 and MAX
}

int already_present(int key) {
    int h = hash(key);
    Node* curr = table[h];
    while (curr != NULL) {
        if (curr->key == key) {
            return 1;
        }
        curr = curr -> next;
    }
      
    return 0;
}

void insert(int key) {
    int h = hash(key);
    Node* node = malloc(sizeof(Node));
    node -> key = key;
    node -> next = table[h];
    table[h] =  node; //insert in head

    return;
}

bool containsDuplicate(int* nums, int numsSize) {
    for (int i =0; i< MAX; i++) {
        table[i] = NULL;
    }
    for (int i =0; i< numsSize; i++) {
        int key = nums[i];
        if (already_present(key)) {
            return true;
        }
        insert(key);
    }

    return false;

    
}