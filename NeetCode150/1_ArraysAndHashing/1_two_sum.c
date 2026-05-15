/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define TABLE_SIZE 10007
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

Node* table[TABLE_SIZE];

int hash(int key) {
    if (key < 0) key = -key;
    return key % TABLE_SIZE; //map between 0 and TABLE_SIZE
}

void insert(int key, int value) {
    int h = hash(key);
    Node* node = malloc(sizeof(Node));
    node -> key = key;
    node -> value = value;
    node -> next = table[h]; //handle collisions with list chaining
    table[h] = node; //insert in head 
}

Node* find(int key) {
    int h = hash(key);
    Node* curr = table[h];

    while (curr) {
        if (curr -> key == key) {
            return curr;
        }

        curr = curr -> next;
    }
    return NULL;
}
//O(N) SOLUTION:

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int first, complementar;
    int* indices = malloc(2 * sizeof(int));

    //CLEAN table
    for (int i = 0; i < TABLE_SIZE; i++) {
    table[i] = NULL;
    }

    for (int i = 0; i < numsSize; i++) {
        first = nums[i];
        complementar = target - first;
        Node* compl_node = find(complementar);
        if (compl_node != NULL) {
            indices[0] = compl_node -> value;
            indices[1] = i;
            *returnSize = 2;
            return indices;
        }
        else {
            insert(first, i);
        }
       
    }

    free(indices); // nessuna soluzione → evita memory leak
    return NULL;
}

//O(N^2) SOLUTION:

// int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
//     int first;
//     int* indices = malloc(2 * sizeof(int));
//     for (int i = 0; i < numsSize; i++) {
//         first = nums[i];
//         for (int j = 0; j < numsSize; j++) {
//             if ((j != i) && (first + nums[j] == target)) {
//                 indices[0] = i;
//                 indices[1] = j;
//                 *returnSize = 2;
//                 return indices;
//             }
//         }
//     }

//     free(indices); // nessuna soluzione → evita memory leak
//     return NULL;
// }


