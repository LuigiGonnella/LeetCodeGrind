#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


void two_way_merge(int A[], int *B, int l, int r, int q) {
    int i = l;
    int j = q + 1;

    for (int k = l; k <= r; k ++) {
        if (i > q) {
            B[k] = A[j++];
        }
        else if (j > r) {
            B[k] = A[i++];
        }
        else if (A[i] <= A[j]) { //= garantisce stability
            B[k] = A[i++];
        }
        else {
            B[k] = A[j++];
        }
    }

    for (int k = l; k <= r; k ++) {
        A[k] = B [k];
    }

}

void mergeR(int A[], int *B, int l, int r) {

    if (l >= r) { //SEGUENDO QUANTO SCRITTO IN BIN_SEARCH QUI DOVREBBE ESSERE l > r, ma in questo caso in cui quando ho un singolo elemento la funzione non fa nulla (singolo elemento è già ordinato), ottimizzo ponendo l >= r. Ma dato che non 'guardo' mai q, allora devo includerlo nella ricorsione, così da ricopiarlo nel vettore finale B in two_way_merge, andando da l a q in branch di SX invece che da l a q-1. Cosa diversa in bin_search in cui quando c'è un solo elemento sono interessato a far proseguire la funzione per capire se quell'elemento è quello cercato!
        return; //not present
    }

    int q = (l + r) / 2;

    mergeR(A, B, l, q); //differenza con BIN_SEARCH, ora q non devo escluderlo, dato che non accedo ad esso nella funzione corrente prima della ricorsione

    //AVREI POTUTO mettere q - 1 nel caso in cui la condizione di terminazione avesse escluso l'=, così anche l'elemento q sarebbe stato ricopiato in A nel two_way_merge (anche se non si fa nessun ordinamento, ma si fa comunque la copia in B, dunque non si skippa)
    mergeR(A, B, q+1, r);
    two_way_merge(A, B, l, r, q);
}


void merge(int A[], int size) {
    int *B = malloc(size * sizeof(int));
    int l = 0;
    int r = size - 1; 

    mergeR(A, B, l, r);

    printf("Sorted vector:\n");
    for (int i = 0; i < size; i ++) {
        printf("%d ", A[i]);
    }
}










int main() {
    int vec[10] = {111, 23, 224, 60, 10, 3, 5, 26, 90, 10};

    merge(vec, 10);

    return 0;
}


