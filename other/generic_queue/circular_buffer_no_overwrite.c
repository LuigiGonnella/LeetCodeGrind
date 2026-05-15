#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//!should be in .h to have a first class ADT
typedef struct queue* QUEUE; 



int main() { 
    struct queue {
        int* values;
        int maxN;
        int N;
        int head;
        int tail;
    };

    QUEUE QUEUEinit(int maxN) {
        QUEUE q = malloc(sizeof(*QUEUE));
        q -> N = maxN + 1; //posizione cuscinetto per controllare se piena (in caso fosse stato pieno inserisco in questa ultima cella, sposto tail a 0 (nuova prima cella libera) e sposto head avanti di 1)
        // --> se pieno ho tail di una posizione indietro rispetto a head (serve modulo perche posso avere tail fisicamente alla fine e head all'inizio)
        // --> se vuoto ho head == tail
        q -> maxN = maxN;
        q -> values = malloc(q -> N  * sizeof(int));
        q -> head = 0;
        q -> tail = 0;

        return q;
    }

    bool QUEUEfull(QUEUE q) {
        return (q -> tail + 1) % q -> N == q -> head;
    }

    bool QUEUEempty(QUEUE q) {
        return q -> tail == q -> head;
    }

    int QUEUEput(QUEUE q, int val) {
        if (QUEUEfull(q)) {
            printf("Error: full queue.\n")
            return 0;
        }

        q -> values[q ->tail] = val;
        q -> tail = (q -> tail + 1) % q -> N;

        return 1;

    }

    int QUEUEget(QUEUE q) {
        if (QUEUEempty(q)) {
            printf("Error: empty queue.\n")
            exit(1);
        }

        int val = q -> values[head];
        q -> head = (q -> head + 1) % q -> N;

        return val;

    }


   
    


    return 0;
}