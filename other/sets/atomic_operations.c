#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//!should be in .h to have a first class ADT
typedef struct set* SET;



int main() { //!SORTED VECTOR IMPLEMENTATION (we could use also a list, but even with sorted list we have linear search, while with sorted vector there is logN search)
    
    //!INIT
    struct set {
        int* values; //in general we have Item* items, with an item having key and value (native types) with key mocked by Key constructed type
        int size; //actual size
    }

    SET init(int MAXN) {
        SET s = malloc(sizeof(*s)); //pointer at struct set
        s -> values = malloc(MAXN*sizeof(int));
        s -> size = 0;
        return s;
    }

    //!FREE
    void SETfree(SET s) {
        free(s->values);
        free(s);
    }

    //! O(logN) SEARCH
    bool SETsearch(SET s, int val) {
        int l = 0, r = s->size-1;

        while (l<=r) {
            int m = l + (r-l)/2;
            if (s->values[m] == val) {
                return 1;
            }

            if (s->values[m] < val) {
                l = m + 1;     
            }
            else {
                r = m - 1;
            }

        }

        return 0;
    }


    



    return 0;
}