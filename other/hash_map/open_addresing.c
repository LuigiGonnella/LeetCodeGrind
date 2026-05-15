#include <stdio.h>
#include <stdlib.h>

typedef struct st* ST;

typedef struct Item {
    int key;
    int val;
} Item;

struct st {
    Item** elements;
    int M; //table dim
    int N; //actual size
};
int hash(int k, int M) { //modular method
    return (k % M + M) % M;
}


//!LINEAR PROBING
void insert(ST st, Item* item) {
    int i = hash(item -> key, st -> M);
    while (full(st, i)) {
        i = (i + 1) % st -> M;
    }

    st -> elements[i] = item;
    st -> N++;
}

int full(ST st, int idx) {
    return st -> elements[idx] == NULL;
}

Item* search(ST st,  int key) {
    int i = hash(key, st -> M);
    while (full(st, i)) {
        if (st -> elements[i] -> key == key) {
            return st -> elements[i];
        }
        else {
            i = (i + 1) % st -> M;
        }
    }

    return NULL;
}

//di solito se si usa open addressing NON si cancella mai

//! se possiamo cancellare, allora cambiano SEARCH e INSERT
//! aggiungiamo flag che, una volta cancellato un elemento, fa risultare quella cella PIENA in SEARCH e VUOTA in INSERT
typedef struct st1* ST;

struct st1 {
    Item** elements;
    int* status; //flags
    int M; //table dim
    int N; //actual size
};

int checkFull(ST st, int idx) {
    return st -> status[idx] == 1;
}
int checkDeleted(ST st, int idx) {
    return st -> status[idx] == -1;
}

void insert(ST st, Item* item) {
    int i = hash(item -> key, st -> M);
    while (checkFull(st, i)) {
        i = (i + 1) % st -> M;
    }

    st -> elements[i] = item;
    st -> status[i] = 1;
    st -> N++;
}


Item* search(ST st,  int key) {
    int i = hash(key, st -> M);
    while (checkFull(st, i) || checkDeleted(st, i)) {
        if (st -> elements[i] -> key == key) {
            return st -> elements[i];
        }
        else {
            i = (i + 1) % st -> M;
        }
    }

    return NULL;
}

void delete(ST st, int key) { //rompe catena di collisioni, rompe ricerca se prima inserisco in posizione avanzata e poi elimino un elemento precedente nella sua catena di collisione
    int i = hash(key, st -> M);
    while (checkFull(st, i) || checkDeleted(st, i)) {
        if (st -> elements[i] -> key == key) {
            if (!checkDeleted(st, i)) {
                st -> elements[i] = NULL;
                st -> status[i] = -1;
                st -> N--;
            }
            break;
        }
        else {
            i = (i + 1) % st -> M;
        }
    }
}

//!ALTRA SOLUZIONE DI DELETE:
//faccio delete di IDX, poi percorro tutte le collisioni SUCCESSIVE a IDX nella sua catena e li REINSERISCO (scaleranno indietro ripristinando catena)
void STdelete(ST st, int key) {
    int j, i = hash(key, st->M);
    Item* tmp;
    while (full(st, i))
        if (st -> elements[i] -> key == key)
            break;
        else
            i = (i+1) % st->M;
    if (st->elements[i] == NULL)
        return;
    st-> elements[i] = NULL;
    st-> N --;
    for (j = i+1; full(st, j); j = (j+1)%st->M, st->N -- ) {
        tmp = st->elements[j];
        st->elements[j]= NULL;
        STinsert(st, tmp);
    }
}

//!QUADRATIC PROBING
//cambia solo il modo in cui aggiorno index (non avanti di 1 ma con funzione quadratica)

#define c1 1
#define c2 1

void insert(ST st, Item* item) {
    int start = hash(item -> key, st -> M), i = 0, index = start;
    while (full(st, index)) {
        i ++;
        index = (start + c1*i + c2*i*i) % st -> M;
    }

    st -> elements[i] = item;
    st -> N++;
}

int full(ST st, int idx) {
    return st -> elements[idx] == NULL;
}

Item* search(ST st,  int key) {
    int start = hash(key, st -> M), i = 0, index = start;
    while (full(st, index)) {
        if (st -> elements[index] -> key == key) {
            return st -> elements[index];
        }
        else {
            i ++;
            index = (start + c1*i + c2*i*i) % st -> M;
        }
    }

    return NULL;
}

void delete(ST st, int key) { //rompe catena di collisioni, rompe ricerca se prima inserisco in posizione avanzata e poi elimino un elemento precedente nella sua catena di collisione
    int start = hash(key, st -> M), i = 0, index = start;
    while (checkFull(st, index) || checkDeleted(st, index)) {
        if (st -> elements[index] -> key == key) {
            if (!checkDeleted(st, index)) {
                st -> elements[index] = NULL;
                st -> status[index] = -1;
                st -> N--;
            }
            break;
        }
        else {
            i ++;
            index = (start + c1*i + c2*i*i) % st -> M;
        }
    }
}

//SCELTA c1 e c2
//se M multiplo di 2: c1 = c2 = 1/2 --> garantiamo generazione di tutti gli indici tra 0 e M-1 (cn hashing con base=127)

//!DOUBLE HASHING
//tutto uguale ma si cambia come si aggiorna index
// 1) calcolo index = h1(k), se libero INSERSICO
// 2) se occupato, calcolo anche h2(k) e provo con index = (h1(k) + h2(k)) % M
//! per evitare CICLO INFINITO deve essere garantito che h2(k) NON torni mai 0, cosi come h2(k) % M
// --> es. h1(k) = k % M (M primo e > 97)
//         h2(k) = 1 + k%97
