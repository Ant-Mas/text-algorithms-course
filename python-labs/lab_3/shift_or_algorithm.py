def set_nth_bit(n: int) -> int:
    """
    Zwraca maskę bitową z ustawionym n-tym bitem na 1.

    Args:
        n: Pozycja bitu do ustawienia (0-indeksowana)

    Returns:
        Maska bitowa z n-tym bitem ustawionym na 1
    """
    # TODO: Zaimplementuj ustawianie n-tego bitu
    pass


def nth_bit(m: int, n: int) -> int:
    """
    Zwraca wartość n-tego bitu w masce m.

    Args:
        m: Maska bitowa
        n: Pozycja bitu do odczytania (0-indeksowana)

    Returns:
        Wartość n-tego bitu (0 lub 1)
    """
    # TODO: Zaimplementuj odczytywanie n-tego bitu
    pass


def make_mask(pattern: str) -> list:
    """
    Tworzy tablicę masek dla algorytmu Shift-Or.

    Args:
        pattern: Wzorzec do wyszukiwania

    Returns:
        Tablica 256 masek, gdzie każda maska odpowiada jednemu znakowi ASCII
    """
    # TODO: Zaimplementuj tworzenie tablicy masek dla algorytmu Shift-Or
    # TODO: Utwórz tablicę z maskami dla wszystkich znaków ASCII
    # TODO: Dla każdego znaku w pattern, ustaw odpowiednie bity w maskach
    pass


def shift_or(text: str, pattern: str) -> list[int]:
    """
    Implementacja algorytmu Shift-Or do wyszukiwania wzorca.

    Args:
        text: Tekst do przeszukania
        pattern: Wzorzec do wyszukiwania

    Returns:
        Lista pozycji (0-indeksowanych), na których znaleziono wzorzec
    """
    # TODO: Zaimplementuj algorytm Shift-Or
    # TODO: Obsłuż przypadki brzegowe (pusty wzorzec, wzorzec dłuższy niż tekst)
    # TODO: Utwórz maski dla wzorca
    # TODO: Zainicjalizuj stan początkowy
    # TODO: Zaimplementuj główną logikę algorytmu
    # TODO: Wykryj i zapisz pozycje dopasowań
    return []