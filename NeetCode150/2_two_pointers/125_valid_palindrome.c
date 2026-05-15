#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool isPalindrome(char* s) {
    int len = strlen(s);
    int i = 0, j = len -1;

    while (i < j) {
        if (!isalnum(s[i])) {
            i++;
            continue;
        }
        if (!isalnum(s[j])) {
            j--;
            continue;
        }

        if (!(tolower(s[i]) == tolower(s[j]))) {
            return false;
        }
        i++;
        j--;
    }

    return true;
    
}