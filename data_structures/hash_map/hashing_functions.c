#include <stdio.h>
#include <stdlib.h>

//! KEY k = floating point number between in [s;t] --> we map k into an INTEGER interval [s;M]
int hash(float k, int M, float s, float t) { //multiplicative method
    return ((k -s) / (t-s)) * M;
}

//! KEY k = integer number
int hash(int k, int M) { //modular method
    return (k % M + M) % M;
}

//! KEY k = small string
int hash(char* k, int M) { //modular method
    //obtain h(k) with polynomial method given a base
    int h=0, base=127; //uniform distrbution, P(collision) ~ 1 / M

    for (; *k!='\0';k++){
        h = (base * h + *k) %M; //horner method
    }
    return h;
}


//! KEY k = small string
int hash(char* k, int M) { //universal hashing
    int h, a = 31415, b = 27185;
    for (h = 0; *k!='\0';k++, a = a*b % (M-1)){
        h = (a * h + *k) %M; //horner method
    }
    return h;
}


