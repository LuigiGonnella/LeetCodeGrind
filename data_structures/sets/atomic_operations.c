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
    };

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

    //!UNION O(N)
    SET SETUnion(SET s1, SET s2) {
        int k=0, i=0, j=0, size1 = s1->size, size2=s->size;
        SET sol = init(size1+size2);

        while (i < size1 || j < size2) {
            if (i >= size1) {
                sol -> values[k++] = s2 -> value[j++];
            }
            else if (j >= size2) {
                sol -> values[k++] = s1-> values[i++];
            }
            else if (s1->values[i] < s2 -> values[j]) {
                sol -> values[k++] = s1 -> values[i++];
            }
            else if (s2->values[j] < s1 -> values[i]) {
                sol -> values[k++] = s2 -> values[j++];
            }
            else {
                sol -> values[k++] = s1 -> values[i++];
                j++;
            }
        }

        sol -> size = k;
        return sol;
    }

    //!INTERSECTION O(N)
    SET SETIntersection(SET s1, SET s2) {
        int k=0, i=0, j=0, size1 = s1->size, size2=s->size;
        int sol_size;
        if (size1 < size2) {
            sol_size = size1;
        }
        else {
            sol_size = size2;
        }
        SET sol = init(sol_size);

        while (i < size1 && j < size2) {
            
            if (s1->values[i] < s2 -> values[j]) {
                i++;
            }
            else if (s2->values[j] < s1 -> values[i]) {
                j++;
            }
            else {
                sol -> values[k++] = s1 -> values[i++];
                j++;
            }
        }

        sol -> size = k;
        return sol;
    }




    



    return 0;
}