#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//time ~ O(m∗n) m=#strings, n=strlen()
//space ~ O(m) hash table
// O(m∗n) stored lists
#define TABLE_SIZE 1024

typedef struct Element {
    int* bits; //represent a string 
    char** anagrams; //array of strings
    int n_anagrams; //actual length
    int capacity; //allocated capacity, to double every time
    struct Element* next;
} Element;

Element* table[TABLE_SIZE];


int* getBits() {
    int* bits = malloc(26 * sizeof(int));
    for (int i =0; i< 26; i++) {
        bits[i] = 0;
    }

    return bits;
}

int* getBitsFilled(char* str) {
    int* bits = getBits();
    for (int i =0; i< strlen(str); i++) {
        bits[str[i] - 'a']++;
    }
    return bits;
}

int hash(char* str, int* bits) {
    uint32_t hash = 2166136261u;

    for (int i = 0; i< 26; i++) {
        hash ^= (uint32_t) bits[i];
        hash *= 16777619;
    }
    
    return hash % TABLE_SIZE;
}

bool areEqual(int* bits1, int* bits2) {
    if (bits1 == NULL || bits2 == NULL) {
        return false;
    }

    for (int i = 0; i< 26; i++) {
        if (bits1[i] != bits2[i]) {
            return false;
        }
    }

    return true;
}


void insert(char* str) {
    int* bits = getBitsFilled(str);
    int index = hash(str, bits);

    Element* curr = table[index];
    while (curr != NULL) {
        if (areEqual(bits, curr-> bits)) {
            curr -> n_anagrams++;

            if (curr -> n_anagrams > curr -> capacity) {
                curr -> capacity *= 2;
                curr -> anagrams = realloc(curr -> anagrams, curr -> capacity * sizeof(char*));
            }

            curr -> anagrams[(curr -> n_anagrams) - 1] = str;

            return;
        }

        curr = curr -> next;
    }

    Element* el = malloc(sizeof(Element));
    el -> bits = bits;
    el -> capacity = 2;
    el -> anagrams = malloc(2 * sizeof(char*));
    el -> anagrams[0] = str;
    el -> n_anagrams = 1;
    el -> next = table[index];
    table[index] = el;


}



void initTable() {
    for (int i =0; i< TABLE_SIZE; i++) {
        table[i] = NULL;
    }
}


char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    char*** ret = malloc(strsSize * sizeof(char**));
    for (int i = 0; i< strsSize; i++) {
        ret[i] = NULL;
    }

    initTable();

    for (int i = 0; i<strsSize; i++ ) {
        insert(strs[i]);
    }

    (*returnSize) = 0;
    int* cols = malloc(strsSize * sizeof(int));
    int j = 0;
    int tot = 0;
    for (int i =0; i < TABLE_SIZE && tot < strsSize; i++) {
        Element* el = table[i];
        while (el != NULL) {
            cols[j++] = el -> n_anagrams;
            ret[(*returnSize) ++] = el -> anagrams;
            tot += el -> n_anagrams;

            el = el -> next;
            
        }
    }
   

    cols = realloc(cols, j * sizeof(int));
    (*returnColumnSizes) = cols;

    ret = realloc(ret, (*returnSize) * sizeof(char**));

    return ret;
}
