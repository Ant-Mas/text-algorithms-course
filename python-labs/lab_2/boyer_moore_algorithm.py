def compute_bad_character_table(pattern: str) -> dict:
    """
    Compute the bad character table for the Boyer-Moore algorithm.

    Args:
        pattern: The pattern string

    Returns:
        A dictionary with keys as characters and values as the rightmost position
        of the character in the pattern (0-indexed)
    """
    # TODO: Implement the bad character heuristic for Boyer-Moore algorithm
    # This table maps each character to its rightmost occurrence in the pattern
    # For characters not in the pattern, they should not be in the dictionary
    # Remember that this is used to determine how far to shift when a mismatch occurs

    return {}


def compute_good_suffix_table(pattern: str) -> list[int]:
    """
    Compute the good suffix table for the Boyer-Moore algorithm.

    Args:
        pattern: The pattern string

    Returns:
        A list where shift[i] stores the shift required when a mismatch
        happens at position i of the pattern
    """
    # TODO: Implement the good suffix heuristic for Boyer-Moore algorithm
    # This is a more complex rule that handles:
    # 1. When we have seen a suffix before elsewhere in the pattern
    # 2. When only a prefix of the suffix matches a prefix of the pattern
    # Hint: This involves two-phase preprocessing of the pattern

    return [0] * (len(pattern) + 1)


def boyer_moore_pattern_match(text: str, pattern: str) -> list[int]:
    """
    Implementation of the Boyer-Moore pattern matching algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement the Boyer-Moore string matching algorithm
    # 1. Preprocess the pattern to create the bad character and good suffix tables
    # 2. Start matching from the end of the pattern and move backwards
    # 3. When a mismatch occurs, use the maximum shift from both tables
    # 4. Return all positions where the pattern is found in the text

    return []
