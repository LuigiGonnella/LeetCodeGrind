// Time Complexity: O(log n) because it halves the search space every iteration.
// Space Complexity: O(1) because it only uses a few integer variables.

int findRotations(int* nums, int l, int r) {
    int firstNum = nums[0];
    int m;
    int index_found = 0;

    while (l <= r) {
        m = l + (r-l) /2; //!AVOIDS overflow if l and r are massive numbers
        if (nums[m] > firstNum) {
            //go right
            if (m > index_found) {
                index_found = m;
            }
            l = m + 1;
        }
        else { 
            // go left
            r = m - 1;
        }
    }

    return index_found + 1;

}


int findMin(int* nums, int numsSize) {
    if (numsSize == 0) {
        return -1;
    }

    int n_rotations = findRotations(nums, 1, numsSize-1) % numsSize;
    return nums[n_rotations];
    
}

// OPPURE trovo la parte NON ordinata dell'array ruotato, la quale contiene il MINIMO (che causa questo collasso). 
//Noi vogliamo trovare l'elemento che causa il collasso, ovvero il minimo.

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
```




// Il Significato di nums[m] < nums[l]
// In un array originariamente ordinato in modo crescente (es. 1, 2, 3...) e poi ruotato, i numeri dovrebbero in teoria salire man mano che vai verso destra.

// Se tu guardi l'estremo sinistro (nums[l]) e poi guardi il centro (nums[m]), e noti che il centro è più piccolo del lato sinistro, significa che in mezzo c'è stato un "crollo".

// L'unico punto in cui i valori crollano in questo tipo di array è esattamente dove si trova il minimo assoluto. Quindi, se il centro è minore della sinistra, il punto di rottura (il minimo) deve per forza trovarsi nella metà sinistra.

// Siccome abbiamo già controllato nums[m] e lo abbiamo salvato in res, possiamo stringere la ricerca ignorando tutta la metà destra: da qui nasce r = m - 1.

// Un Esempio Pratico
// Immagina questo array: nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]

// Stato iniziale:

// l = 0 (valore 7)

// r = 8 (valore 6)

// m = 4 (valore 2)

// Controllo dell'algoritmo:

// L'algoritmo aggiorna res = 2 (il valore al centro).

// Poi si chiede: nums[m] >= nums[l]? Ovvero: 2 >= 7?

// Questo è Falso.

// Entriamo nell'else:

// Perché 2 è minore di 7? Perché scendendo da sinistra verso il centro abbiamo superato il punto di rotazione (l'1).

// Tutta la metà destra [3, 4, 5, 6] è perfettamente ordinata e crescente, non ci nasconde nessun calo, quindi non ci interessa.

// L'algoritmo esegue r = m - 1, dicendo in pratica: "Il crollo è avvenuto prima del centro, andiamo a cercare il minimo nella parte sinistra!" (che ora diventa [7, 8, 9, 1]).

// In Sintesi (La Regola d'Oro)
// Se nums[m] >= nums[l]: La metà sinistra è perfettamente ordinata e sale costantemente. Non c'è nessun salto qui. Vai a cercare il minimo a destra (l = m + 1).

// Se nums[m] < nums[l] (il tuo else): C'è un'anomalia. I numeri sono scesi. Il salto (e quindi il minimo) è rimasto intrappolato nella metà sinistra. Vai a cercare a sinistra (r = m - 1).


//!OPPURE OGNI VOLTA COMPARO IL MIDDLE CON IL RIGHT, SE < ALLORA VADO A SINISTRA (CERCO UNO ANCORA MINORE), ALTRIMENTI VADO A DESTRA (RIGHT E PIU PICCOLO QUINDI IL MINIMO SARA A DESTRA)
//finiro quando mi rimane solo un elemento, ovvero il minimo, infatti faccio while con l<r e NON l<=r 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        
//oppure tengo traccia del minimo e faccio il while con l<=r come sempre, ritornando l'ultimo minimo trovato

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            minNum= min(minNum, nums[m])
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return minNum