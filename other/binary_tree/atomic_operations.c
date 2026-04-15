#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct Node {
    int key;
    //eventually pointer to PARENT
    struct Node* left;
    struct Node* right;
} Node;

int count(Node* root) {
    if (root == NULL) return 0;

    return count(root -> left) + count(root -> right) + 1;
}

int height(Node* root) {
    int u, v;

    if (root == NULL) {
        return 0;
    }

    u = height(root -> left);
    v = height(root -> right);

    if (u > v) {
        return u + 1;
    }

    return v + 1;
}

//!VISITS

void preOrder(Node* root) {
    if (root == NULL) {
        return;
    }

    printf("visited %d\n\n", root -> key);
    preorder(root -> left);
    preorder(root -> right);
}

void inOrder(Node* root) {
    if (root == NULL) {
        return;
    }

    preorder(root -> left);
    printf("visited %d\n\n", root -> key);
    preorder(root -> right);
}

void postOrder(Node* root) {
    if (root == NULL) {
        return;
    }

    preorder(root -> left);
    preorder(root -> right);
    printf("visited %d\n\n", root -> key);
}

//!PREFIX FORM OF AN EXPRESSION EVALUATION

int eval(char* elements, int idx, int len, int x) {

    while (elements[idx] == ' ') {
        idx++;
    }

    if (idx >= len) {
        return x;
    }
    

    if (elements[idx] == '*') {
        return eval(elements, idx + 1, len, x) * eval(elements, idx + 2, len, x);
    }

    if (elements[idx] == '+') {
        return eval(elements, idx + 1, len, x) + eval(elements, idx + 2, len, x);
    }

    if (elements[idx] == '-') {
        return eval(elements, idx + 1, len, x) - eval(elements, idx + 2, len, x);
    }

    if (elements[idx] == '/') {
        return eval(elements, idx + 1, len, x) / eval(elements, idx + 2, len, x);
    }

    if (elements[idx] >= '0' && elements[idx] <= '9') {
        return eval(elements, idx + 1, len, 10 * x + (elements[idx] - '0'));
    }   


}

int main() {

    char elements[12] = {'*', '*', '+', '2', ' ', '6', '*', '1', ' ', '2', ' ', '3'};

    printf("result: %d", eval(elements, 0, 12, 0));

    return 0;
}