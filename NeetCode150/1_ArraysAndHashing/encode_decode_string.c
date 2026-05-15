#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>



char* encode(char** strs, int strsSize) {
    int curLen;
    int capacity = 256;
    char* encoded = malloc(capacity * sizeof(char));
    encoded[0] = '\0';
    int offset = 0;

    char prefix[20]; //just to store the length with a suffix

    for (int i =0; i<strsSize; i++) {
        curLen = strlen(strs[i]);
        int prefixLen = sprintf(prefix, "%d#", curLen);


        if (offset + curLen + prefixLen > capacity) {

            capacity *= 2;
            
            while (capacity < offset + curLen + prefixLen) {
                capacity *= 2;
            }
            
            encoded = realloc(encoded, capacity*sizeof(char));
        }

        memcpy(encoded + offset, prefix, prefixLen);

        offset += prefixLen;

        memcpy(encoded + offset, strs[i], curLen);

        offset += curLen;

    }   

    int prefixLen = sprintf(prefix, "#%d", strsSize);

    encoded = realloc(encoded, (offset+prefixLen+1)*sizeof(char));
    memcpy(encoded + offset, prefix, prefixLen);

    encoded[offset + prefixLen] = '\0';

    
    return encoded;
}

char** decode(char* str) {
    int strSize = strlen(str);
    int curLen = -1;
    int i = 0;
    int j;
    int multiplier = 1;
    int p = strSize-1;
    int totWords = 0;


    while (str[p] != '#') {
        int exp = strSize-1 - p;
        totWords += (str[p] - '0') * multiplier;
        multiplier *= 10;

        p--;
    }
    char** decoded = malloc(totWords * sizeof(char*));
    int k = 0;



    while(i<p) {
        curLen = 0;
        while (str[i] != '#') {
            curLen = (curLen * 10) + str[i] - '0';
            i++;
        }
        i++; //skip # 
        char* word = malloc((curLen+1)*sizeof(char));
        word[curLen] = '\0';

        for (j = 0; j<curLen; j++) {
            word[j] = str[i+j];
        }


        decoded[k++] = word;
        i += curLen;
    }

    return decoded;
}

int main() {
    int strsSize = 2;
    char* dummy_input[] = {"Hello", "world"};

    char* encoded = encode(dummy_input, strsSize);
    printf("encoded input: %s\n", encoded);
    char** decoded = decode(encoded);

    printf("decoded output:\n[");
    for (int i =0; i<strsSize; i++) {
        if (i != strsSize-1) {
            printf("%s, ", decoded[i]);
        }
        else {
            printf("%s", decoded[i]);
        }
    }
    printf("]");

    free(encoded);
    for (int i = 0; i< strsSize; i++) {
        free(decoded[i]);
    }

    free(decoded);

    return 0;



}