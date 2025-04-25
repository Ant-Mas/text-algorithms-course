from collections import deque
from typing import List, Tuple, Optional


class AhoCorasickNode:
    def __init__(self):
        # TODO: Zainicjalizuj struktury potrzebne dla węzła w drzewie Aho-Corasick
        pass


class AhoCorasick:
    def __init__(self, patterns: List[str]):
        # TODO: Zainicjalizuj strukturę Aho-Corasick i usuń puste wzorce
        pass

    def _build_trie(self):
        """Builds the trie structure for the given patterns."""
        # TODO: Zaimplementuj budowanie drzewa typu trie dla podanych wzorców
        pass

    def _build_failure_links(self):
        """Builds failure links and propagates outputs through them."""
        # TODO: Zaimplementuj tworzenie failure links
        # TODO: Utwórz kolejkę do przechodzenia przez drzewo w szerokość (BFS)
        # TODO: Zainicjalizuj łącza awaryjne dla węzłów na głębokości 1
        # TODO: Użyj BFS do ustawienia łączy awaryjnych dla głębszych węzłów
        # TODO: Propaguj wyjścia przez łącza awaryjne
        pass

    def search(self, text: str) -> List[Tuple[int, str]]:
        """
        Searches for all occurrences of patterns in the given text.

        Returns:
            List of tuples (start_index, pattern).
        """
        # TODO: Zaimplementuj wyszukiwanie wzorców w tekście
        # TODO: Zwróć listę krotek (indeks_początkowy, wzorzec)
        return []