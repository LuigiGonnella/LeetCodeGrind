//brute-force approach
//O(n^2) --> for each character of string1 , loop over string2 with a support int array to count the occurrence of the string2's characters 
//(so i don't take twice the same letter)


//optimal solution
//O(n + m) --> first loop over string1 (length = n), fill a table increasing the occurrences of each found char (a struct with key=char, value=occurrences count)
// second loop over string2 decreasing the occurrences of each found char
// third loop over the table (constant), if an occurrence count is != 0 --> false, otherwise --> true
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX 26

typedef struct letter {
    char key; //letter
    int value; //counter
} letter;

letter table[MAX];

void init_table() {
    for (int i =0; i<MAX; i++) {
        char key = 'a' + i;
        table[i].key = key;
        table[i].value = 0;
    }
}

void insertIncr(char letter) {
    int index = letter; //cast
    table[index-'a'].value++;
}

int insertDecr(char letter) {
    int index = letter; //cast
    if (table[index-'a'].value == 0) { //already 0 --> error
        return 0;
    }
    else {
        table[index-'a'].value--;
    }
    return 1;
}



bool isAnagram(char* s, char* t) {
    init_table();
    int lenS = strlen(s);
    int lenT = strlen(t);

    if (lenS != lenT) {
        return false;
    }

    for (int i =0; i<lenS; i++) {
        insertIncr(s[i]);
    }
    for (int i = 0; i<lenT ; i++) {
        int res = insertDecr(t[i]);
        if (!res) {
            return false;
        }
    }
    for (int i =0; i< MAX; i++) {
        if (table[i].value != 0) {
            return false;
        } 
    }
    return true;
    
}