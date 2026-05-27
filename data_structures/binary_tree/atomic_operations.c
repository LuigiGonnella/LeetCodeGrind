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
    preOrder(root -> left);
    preOrder(root -> right);
}

void inOrder(Node* root) {
    if (root == NULL) {
        return;
    }

    inOrder(root -> left);
    printf("visited %d\n\n", root -> key);
    inOrder(root -> right);
}

void postOrder(Node* root) {
    if (root == NULL) {
        return;
    }

    postOrder(root -> left);
    postOrder(root -> right);
    printf("visited %d\n\n", root -> key);
}

//!PREFIX FORM OF AN EXPRESSION EVALUATION

int eval(char* elements, int*idx) {

    while (elements[*idx] == ' ') {
        (*idx)++;
    }
    

    if (elements[*idx] == '*') {
        (*idx)++;
        return eval(elements, idx) * eval(elements, idx);
    }

    if (elements[*idx] == '+') {
        (*idx)++;
        return eval(elements, idx) + eval(elements, idx);
    }

    if (elements[*idx] == '-') {
        (*idx)++;
        return eval(elements, idx)- eval(elements, idx);
    }

    if (elements[*idx] == '/') {
        (*idx)++;
        return eval(elements, idx) / eval(elements, idx);
    }

    int x = 0;
    while (elements[*idx] >= '0' && elements[*idx] <= '9') {
        x = 10*x + (elements[(*idx)++] - '0');
    }   

    return x;
}

// int main() {
//     int idx = 0;
//     char elements[12] = {'*', '*', '+', '2', ' ', '6', '-', '2', ' ', '1', ' ', '3'};

//     printf("result: %d", eval(elements, &idx));

//     return 0;
// }

//!BST (Binary Search Tree)

typedef struct BSTNode* link;
typedef struct bst* BST;


typedef struct Item {
    int key;
    int value;
} Item;
struct BSTNode {
    Item item;
    link l;
    link r;
};


struct bst {
    link root;
};

link NewNode(Item item) {
    link node = malloc(sizeof(*node));
    node -> l = NULL;
    node -> r = NULL;
    node -> item = item;

    return node;

}

BST BSTinit(Item item) {
    BST bst = malloc(sizeof(*bst));
    bst -> root = NewNode(item);

    return bst;
}


void treefree(link root) {
    if (root == NULL) {
        return;
    }

    treefree(root -> l);
    treefree(root -> r);

    free(root);
}

void BSTfree(BST bst) {
    treefree(bst -> root);
}

int BSTempty(BST bst) {
    return count(bst -> root) == 0;
}

int searchR(link node, int key) {
    if (node == NULL) {
        printf("No item found");
        exit(1);
    }

    if (node -> item.key == key) {
        return node -> item.value;
    }
    else if (key < node -> item.key) {
        return searchR(node -> l, key);
    }
    
    
    return searchR(node -> r, key);

}

int BSTsearch(BST bst, int key) {
    return searchR(bst -> root, key);
}


int minR(link node) {
    if (node -> l == NULL) {
        return node -> item.value;
    }
    
    return minR(node -> l); //tail recursion --> stack memory optimized
}

int minIt(link root) {
   
    while (root -> l != NULL) {
        root = root -> l;
    }

    return root -> item.value;
}

int BSTmin(BST bst) {
     if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return minR(bst -> root);
}

int maxR(link node) {
    if (node -> r == NULL) {
        return node -> item.value;
    }
    
    return maxR(node -> r); //tail recursion --> stack memory optimized
}

int BSTmax(BST bst) {
     if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return maxR(bst -> root);
}


link insertR(link node, Item item) { //!LEAF INSERTION
    if (node == NULL) {
        return NewNode(item);
    }

    if (item.key < node -> item.key) {
        node -> l = insertR(node -> l, item);
    }
    else {
        node -> r = insertR(node -> r, item);
    }

    return node;
}


void BSTinsertLeaf(BST bst, Item item) {
    if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return insertR(bst -> root, item);
}

void increasingKeysPrint(BST bst) {
    inOrder(bst -> root);
}

link rotR(link h) {
    link new_h = h -> l;
    h -> l = new_h -> r;
    new_h -> r = h;
    return new_h;
}

link rotL(link h) {
    link new_h = h -> r;
    h -> r = new_h -> l;
    new_h -> l = h;
    return new_h;
}

//!ROOT INSERTION --> i need rotations
    //! 1) LEAF INSERTION
    //! 2) ROTATIONS TO MAKE THE NEW ITEM ROOT



link insertT(link node, Item item) { //!ROOT INSERTION
    if (node == NULL) {
        return NewNode(item);
    }

    if (item.key < node -> item.key) {
        node -> l = insertT(node -> l, item);
        node = rotR(node);
    }
    else {
        node -> r = insertT(node -> r, item);
        node = rotL(node);
    }
}

void BSTinsertRoot(BST bst, Item item) { 
    if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return insertT(bst -> root, item);
}

//! MODIFIED BST for SUCC AND PRED


struct BSTNode {
    Item item;
    link l;
    link r;
    link p;
    int N; //number of children in all sub-trees
};

typedef struct BSTNode* link;

int searchSucc(link h, int key) {
    link p;

    if (h == NULL) {
        print("No successor found");
        exit(1);
    }

    if (h -> item.key == key) {
        if (h -> r != NULL) {
            return minR(h -> r);
        }

        p = h -> p;
        while (p != NULL && p -> r == h) {
            h = p;
            p = p -> p;
        }

        if (p != NULL) {
            return p -> item.value;
        }
    }

    print("No successor found");
    exit(1);
}


int BSTSearchSucc(BST bst, Item item) { 
    if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return searchSucc(bst -> root, item.key);
}

int searchPred(link h, int key) {
    link p;

    if (h == NULL) {
        print("No predecessor found");
        exit(1);
    }

    if (h -> item.key == key) {
        if (h -> l != NULL) {
            return maxR(h -> l);
        }

        p = h -> p;
        while (p != NULL && p -> l == h) {
            h = p;
            p = p -> p;
        }

        if (p != NULL) {
            return p -> item.value;
        }
    }

    print("No predecessor found");
    exit(1);
}


int BSTSearchPred(BST bst, Item item) { 
    if (bst -> root == NULL) {
        printf("root is NULL");
        exit(1);
    }

    return searchPred(bst -> root, item.key);
}

link insertR(link node, Item item) { //!LEAF INSERTION
    if (node == NULL) {
        return NewNode(item);
    }

    if (item.key < node -> item.key) {
        node -> l = insertR(node -> l, item);
        node -> l -> p = node;
    }
    else {
        node -> r = insertR(node -> r, item);
        node -> r -> p = node;
    }
    (node -> N) ++;
    return node;
}

int BTselect(link node, int rank) {

    if (node == NULL) {
        exit(1);
    }

    int t = node -> l -> N;

    if (node -> N == rank) {
        return node -> item.value;
    }
    else if (t > rank) {
        return BTselect(node -> l, rank);
    }

    return BTselect(node -> l, rank - t - 1);
}


link rotR(link h) {
    link new_h = h -> l;
    h -> l = new_h -> r;
    new_h -> r -> p = h;
    new_h -> p = h -> p;
    h -> p = new_h;
    new_h -> r = h;

    new_h -> N = h -> N;
    h -> N = 1;
    h -> N += (h -> l) ? h -> l -> N : 0;
    h -> N += (h -> r) ? h -> r -> N : 0;
    return new_h;
}

link rotL(link h) {
    link new_h = h -> r;
    h -> r = new_h -> l;
    new_h -> l -> p =  h;
    new_h -> p = h -> p;
    h -> p = new_h;
    new_h -> l = h;

    new_h -> N = h -> N;
    h -> N = 1;
    h -> N += (h -> l) ? h -> l -> N : 0;
    h -> N += (h -> r) ? h -> r -> N : 0;
    return new_h;
}

link insertT(link node, Item item) { //!ROOT INSERTION
    if (node == NULL) {
        return NewNode(item);
    }

    if (item.key < node -> item.key) {
        node -> l = insertT(node -> l, item);
        node = rotR(node);
        node -> N++;
    }
    else {
        node -> r = insertT(node -> r, item);
        node = rotL(node);
        node -> N++;
    }
}


link BSTpartition(link h, int r) {
    int t = h -> l -> N;

    if (t > r) {
        h -> l = BSTpartition(h -> l, r);
        h = rotR(h);
    }
    else if (t < r) {
        h -> r = BSTpartition(h -> r, r);
        h = rotL(h);
    }

    return h;
}

link joinR(link left_root, link right_root) {
    if (right_root == NULL) {
        return left_root;
    }

    right_root = BSTpartition(right_root, 0); //succ at root
    right_root -> l = left_root;

    left_root -> p = right_root;
    right_root -> N = right_root -> r -> N + left_root -> N + 1;
    return right_root;
}

link deleteR(link h, int key) {
    link y, p;

    if (h == NULL) {
        return NULL;
    }

    if (key < h -> item.key) {
        h -> l = deleteR(h -> l, key);
    }
    else if (key > h -> item.key) {
        h -> r = deleteR(h -> r, key);
    }

    h -> N--; //recursive deletion (-1 in all ancestors)
    if (key == h -> item.key) {
        y = h;
        h = joinR(h -> l, h -> r);
        free(y); 
    }

    return h;
    
}

link balanceR(link h) {
    if (h == NULL) {
        return NULL;
    }

    int r = (h -> N + 1)/2 -1;

    h = BSTpartition(h, r);
    h -> l = balanceR(h -> l);
    h -> r = balanceR(h -> r);

    return h;
}

//! INTERVAL BST

typedef struct IntervalItem {
    int low;
    int high;
} IntervalItem;
struct BSTNode {
    IntervalItem item;
    link l;
    link r;
    link p;
    int maxR; //maximum value of right extreme in all children
    int N; //number of children
};

typedef struct BSTNode* link;

link IBSTNewNode(IntervalItem item, int N, int maxR) {
    link node = malloc(sizeof(*node));
    node -> l = NULL;
    node -> r = NULL;
    node -> p = NULL;
    node -> item = item;
    node -> maxR = maxR;
    node -> N = N;

    return node;

}

bool IntervalItemLess(IntervalItem item1, IntervalItem item2) {
    if (item1.high <= item2.low) {
        return true;
    }
    return false;
}

int maxEl(int a, int b, int c) {
    int m = a;
    if (b > m) {
        m = b;
    } 
    if (c > m) {
        m = c;
    }
    return m;
    
}

link IBSTinsertR(link h, IntervalItem item) {
    if (h == NULL) {
        return IBSTNewNode(item, 1, item.high);
    }

    if (IntervalItemLess(item, h->item)) {
        h -> l = IBSTinsertR(h -> l, item);
        h -> maxR = maxEl(h -> maxR, h -> l -> maxR, h -> r -> maxR);
    }
    else {
        h -> r = IBSTinsertR(h -> r, item);
        h -> maxR = maxEl(h -> maxR, h -> l -> maxR, h -> r -> maxR);
    }
    //in any case, increase N
    h -> N++;
    return h;
}

link IBSTrotR(link h) {
    link new_h = h -> l;
    h -> l = new_h -> r;
    new_h -> r = h;


    new_h -> N = h -> N;
    h -> N = 1;
    h -> N += (h -> l) ? h -> l -> N : 0;
    h -> N += (h -> r) ? h -> r -> N : 0;
    h -> maxR =  maxEl(h -> item.high, h -> l -> maxR, h -> r -> maxR);
    new_h -> maxR =  maxEl(new_h -> item.high, new_h -> l -> maxR, new_h -> r -> maxR);
    return new_h;
}

link IBSTrotL(link h) {
    link new_h = h -> r;
    h -> r = new_h -> l;
    new_h -> l =  h;

    new_h -> N = h -> N;
    h -> N = 1;
    h -> N += (h -> l) ? h -> l -> N : 0;
    h -> N += (h -> r) ? h -> r -> N : 0;
    h -> maxR =  maxEl(h -> item.high, h -> l -> maxR, h -> r -> maxR);
    new_h -> maxR =  maxEl(new_h -> item.high, new_h -> l -> maxR, new_h -> r -> maxR);
    return new_h;
}


link IBSTpartition(link h, int r) {
    int t = h -> l -> N;

    if (t > r) {
        h -> l = IBSTpartition(h -> l, r);
        h = IBSTrotR(h);
    }
    else if (t < r) {
        h -> r = IBSTpartition(h -> r, r);
        h = IBSTrotL(h);
    }

    return h;
}

link IBSTjoinR(link left_root, link right_root) {
    if (right_root == NULL) {
        return left_root;
    }

    right_root = IBSTpartition(right_root, 0); //succ at root
    right_root -> l = left_root;

    right_root -> N = right_root -> r -> N + left_root -> N + 1;
    right_root -> maxR =  maxEl(right_root -> item.high, right_root -> l -> maxR, right_root -> r -> maxR);
    return right_root;
}

link IBSTdeleteR(link h, IntervalItem item) {
    link y, p;

    if (h == NULL) {
        return NULL;
    }

    if (IntervalItemLess(item, h -> item)) {
        h -> l = IBSTdeleteR(h -> l, item);
        h -> maxR =  maxEl(h -> item.high, h -> l -> maxR, h -> r -> maxR);
    }
    else if (IntervalItemLess(h -> item, item)) {
        h -> r = IBSTdeleteR(h -> r, item);
        h -> maxR =  maxEl(h -> item.high, h -> l -> maxR, h -> r -> maxR);
    }

    h -> N--; //recursive deletion (-1 in all ancestors)
    if (item.low == h -> item.low && item.high == h -> item.high) {
        y = h;
        h = IBSTjoinR(h -> l, h -> r);
        free(y); 
    }

    return h;   
}

bool IntervalItemOverlap(IntervalItem item1, IntervalItem item2) {
    if (item1.low <= item2.high && item1.high >= item2.low) {
        return true;
    }
    return false;
}

IntervalItem IBSTsearchR(link h, IntervalItem item) { //search first item to overlap with given item
    if (h == NULL) {
        exit(1);
    }

    if (IntervalItemOverlap(item, h -> item)) {
        return h -> item;
    }
    else if (item.low <= h -> l -> maxR) {
        IBSTsearchR(h -> l, item);
    }
    else {
        IBSTsearchR(h -> r, item);
    }

}