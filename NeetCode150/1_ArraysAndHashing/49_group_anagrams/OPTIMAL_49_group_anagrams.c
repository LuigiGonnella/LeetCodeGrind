#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// /**
//  * Return an array of arrays of size *returnSize.
//  * The sizes of the arrays are returned as *returnColumnSizes array.
//  * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
//  */


// //like brute force
// //time ~ O(N^2 * N_strings) with N=STRLEN
// //memory ~ O(N²) caused by realloc, inefficient, memory fragmentation
// typedef struct Element {
//     int key;
//     int counter;
// } Element;

// Element table[26];

// int hash(char letter) {
//     return (int)(letter - 'a');
// }

// void insertIncr(char letter) {
//     int index = hash(letter);
//     table[index].counter++;
// }

// bool decr(char letter) {
//     int index = hash(letter);
//     if (table[index].counter == 0) {
//         return false;
//     }
//     table[index].counter--;

//     return true;
     
// }

// void initTable() {
//     for (int i =0; i< 26; i++) {
//         table[i].key = 'a' + i;
//         table[i].counter = 0;
//     }
// }

// bool isAnagram(char* s1, char*s2) {
//     initTable();
//     int len1 = strlen(s1);
//     int len2 = strlen(s2);

//     if (len1 != len2) {
//         return false;
//     }

//     for (int i =0; i< len1; i++) {
//         insertIncr(s1[i]);
//     }
//     for (int i =0; i< len2; i++) {
//         if (!decr(s2[i])) return false;
//     }

//     for (int i =0; i< 26; i++) {
//         if (table[i].counter != 0) return false;
//     }

//     return true;

// }


// char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
//     char*** output = NULL;
//     int i, j;
//     int bits[strsSize];
//     //*returnColumnSizes = NULL;
//     for (int i=0; i<strsSize; i++) {
//         bits[i] = 0;
//     }


//     *returnSize = 0;
//     for (i = 0; i<strsSize; i++) {
//         int n_anagrams = 1;

//         printf("processing string %s\n", strs[i]);

//         if (bits[i] != 1) {
//             (*returnSize)++; //add a list of anagrams
//             output = realloc(output, (*returnSize) * sizeof(char**));

//             output[(*returnSize)-1] =  NULL;
//             output[(*returnSize)-1] = realloc(output[(*returnSize)-1], (n_anagrams)*sizeof(char*));

//             //output[(*returnSize)-1][n_anagrams] = NULL;
//             //output[(*returnSize)-1][n_anagrams] = realloc(output[(*returnSize)-1][n_anagrams], strlen(strs[i]) * sizeof(char));
//             output[(*returnSize)-1][n_anagrams-1] = strs[i];
//             bits[i] = 1;

//             *returnColumnSizes = realloc(*returnColumnSizes, (*returnSize) * sizeof(int));
//             //(*returnColumnSizes)[*returnSize-1] = n_anagrams;

//             for (j = 0; j<strsSize; j++) {
//                 if (i!=j) {
//                     if (isAnagram(strs[i], strs[j])) {
//                         printf("%s and %s are anagrams\n", strs[i],  strs[j]);
//                         n_anagrams++;
//                         bits[j] = 1;
//                         output[(*returnSize) -1] = realloc(output[(*returnSize) -1], (n_anagrams)*sizeof(char*));
//                         //output[(*returnSize) -1][n_anagrams] = realloc(output[(*returnSize) -1][n_anagrams], strlen(strs[j])*sizeof(char));
//                         output[(*returnSize)-1][n_anagrams-1] = strs[j];
                        
//                     }
//                 }
//             }

//             (*returnColumnSizes)[*returnSize-1] = n_anagrams;
//         }

        

//     }

//     return output;
    
// }


//time ~ O(m∗n) m=#strings, n=strlen()
//space ~ O(m) hash table
// O(m∗n) stored lists


typedef struct Element {
    int key; //represent a string (hashing of a counter vector)
    char** anagrams; //array of strings
    int n_anagrams; //actual length
    int capacity: //allocated capacity, to double every time
} Element;


int* getBits() {
    int* bits = malloc(26 * sizeof(int));
    for (int i =0; i< 26; i++) {
        bits[i] = 0;
    }

    return bits;
}

int* hash(char* str) {
    int* bits = getBits();
    for (int i =0; i< strlen(str); i++) {
        bits[str[i] - 'a']++;
    }
    
    return bits;
}

void insert(char* str) {
    int index = hash(str);
    table[index].bits++;
}

bool decr(char letter) {
    int index = hash(letter);
    if (table[index].counter == 0) {
        return false;
    }
    table[index].counter--;

    return true;
     
}

void initTable() {
    for (int i =0; i< 26; i++) {
        table[i].key = 'a' + i;
        table[i].counter = 0;
    }
}