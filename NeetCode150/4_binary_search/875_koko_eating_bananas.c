//BRUTE FORCE:
//for every candidate K from 1 to go up
//start form time = 0
//for every i compute time += ceil(piles[i]/K)
//at the end, if time <= h --> return K
//-- O(m*n) complexity with m = maximum value in piles[] (the minimum h possible is equal to the pilesSize, achievable with K = max(piles[i]))

//ceil rounds UP the result of division. Included in <math.h>

//OPTIMAL --> binary search possible because the search space is ordered from 1 to max(piles[i]) --> O(n*log(m))

bool testSpeed(int* piles, int pilesSize, int speed, int h) {
    int h_needed = 0;

    printf("Testing speed: %d\n", speed);

    for (int i =0; i< pilesSize; i++) {
        h_needed += (piles[i] + speed - 1) / speed; //ceiling, equal to ceil((double)(piles[i]) / speed)
        if (h_needed > h) {
            printf("For speed %d Koko needs at least %d hours --> REJECTED\n\n", speed, h_needed);
            return false;
        }
    } 

    printf("For speed %d Koko needs %d hours --> ACCEPTED\n\n", speed, h_needed);
    return true;
}

void searchR(int l, int r, int h , int* piles, int pilesSize, int* optimalSpeed) {
    int m;
    if (l > r) {
        return;
    }

    m = (l + r) / 2;
    if (testSpeed(piles, pilesSize, m, h)) {
        (*optimalSpeed) = m;
        return searchR(l, m-1, h, piles, pilesSize, optimalSpeed);
    }
    return searchR(m+1, r, h, piles, pilesSize, optimalSpeed);
}

//! or ITERATIVE
// void searchR(int l, int r, int h , int* piles, int pilesSize, int* optimalSpeed) {
//     int m;
//     while (l <= r) {
//          m = (l + r) / 2;
//         if (testSpeed(piles, pilesSize, m, h)) {
//             (*optimalSpeed) = m;
//             r = m - 1;
//         }
//         else {
//             l = m + 1;
//         }
        
//     }   
// }

int max_in_piles(int* piles, int pilesSize) {
    int m = -1;

    for (int i =0; i< pilesSize; i++) {
        if (piles[i] > m) {
            m = piles[i];
        }
    }



    return m;
}

int minEatingSpeed(int* piles, int pilesSize, int h) {
    int maxPile = max_in_piles(piles, pilesSize);
    printf("%d\n", maxPile);
    int speed = -1;
    searchR(1, maxPile, h, piles, pilesSize, &speed);

    return speed;


}