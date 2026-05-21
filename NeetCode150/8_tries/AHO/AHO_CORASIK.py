from collections import deque, defaultdict


#!O(N + Z) (lunghezza testo + numero match)
class AhoNode:
    def __init__(self):
        # Transizioni del Trie standard: {carattere: AhoNode}
        self.children = {}
        # Puntatore di fallimento (Failure Link)
        self.fail = None
        # Lista degli indici o delle parole che terminano in questo nodo
        self.output = []

class AhoCorasick:
    def __init__(self, words):
        self.root = AhoNode()
        self.words = words
        self._build_trie()
        self._build_automaton()

    def _build_trie(self):
        """Fase 1: Costruzione del Trie classico"""
        for index, word in enumerate(self.words):
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = AhoNode()
                current = current.children[char]
            # Memorizziamo la parola (o l'indice) nel nodo terminale
            current.output.append(word)

    def _build_automaton(self):
        """Fase 2: Calcolo dei Failure Links tramite BFS"""
        queue = deque()

        # Per i figli diretti della radice, il fallimento è sempre la radice stessa
        for char, child in self.root.children.items():
            child.fail = self.root
            queue.append(child)

        # BFS per i livelli successivi
        while queue:
            current = queue.popleft()

            for char, child in current.children.items():
                # Cerchiamo il link di fallimento risalendo la catena del padre
                fail_node = current.fail
                while fail_node is not None and char not in fail_node.children:
                    fail_node = fail_node.fail

                # Se troviamo un nodo con il figlio 'char', quello è il nostro fail
                if fail_node is not None:
                    child.fail = fail_node.children[char]
                else:
                    child.fail = self.root

                # Ottimizzazione Output: Uniamo l'output del nodo di fallimento
                # (Questo funge implicitamente da Dictionary Link)
                child.output.extend(child.fail.output)

                queue.append(child)

    def search(self, text):
        """Fase 3: Ricerca lineare nel testo"""
        current = self.root
        results = defaultdict(list)

        for i, char in enumerate(text):
            # Se non c'è la transizione, seguiamo i failure link
            while current is not None and char not in current.children:
                current = current.fail

            # Se siamo tornati oltre la radice, ricominciamo da capo
            if current is None:
                current = self.root
                continue

            # Avanziamo al nodo figlio
            current = current.children[char]

            # Se il nodo ha degli output associati, abbiamo trovato dei match!
            if current.output:
                for word in current.output:
                    # Registriamo la parola e l'indice iniziale nel testo
                    start_index = i - len(word) + 1
                    results[word].append(start_index)

        return dict(results)

# --- ESEMPIO D'USO ---
if __name__ == "__main__":
    dizionario = ["he", "she", "his", "hers"]
    testo = "ahishers"

    ac = AhoCorasick(dizionario)
    match_trovati = ac.search(testo)

    print(f"Testo: '{testo}'")
    print("Match trovati:")
    for parola, indici in match_trovati.items():
        print(f"  - Parola '{parola}' agli indici: {indici}")