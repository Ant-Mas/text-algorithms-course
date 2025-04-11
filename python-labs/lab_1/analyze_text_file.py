import re
from collections import Counter


def analyze_text_file(filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        return {"error": f"Could not read file: {str(e)}"}
    # Common English stop words to filter out from frequency analysis
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "with",
        "by",
        "about",
        "as",
        "into",
        "like",
        "through",
        "after",
        "over",
        "between",
        "out",
        "of",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "this",
        "that",
        "these",
        "those",
        "it",
        "its",
        "from",
        "there",
        "their",
    }

    # DONE: Implement word extraction using regex
    # Find all words in the content (lowercase for consistency)

    word_pattern = r"\b\w+\b"
    ## zgodnie z definicją \w to word characters, a \b to granice słowa, więc \b\w+\b to słowo.
    word_count = len(re.findall(word_pattern, content))
    ## używam re.findall aby znaleźć wszystkie słowa w treści i liczę ich ilość.


    # DONE: Implement sentence splitting using regex
    # A sentence typically ends with ., !, or ? followed by a space
    # Be careful about abbreviations (e.g., "Dr.", "U.S.A.")
    sentence_pattern = r"[\w,/ -]+[.!?][ \n]"
    ## Zdanie bardzo ciężko zdefiniować ze ze względu na obecność kropek w wielu innych miejscach.
    ## dla przykładu "Odliczałem od 1 do 10. 9 pominąłem." znajdują się 2 zdania, a w "Umówiłem się z nią na 9. tak jak dziś." tylko jedno.
    ## Ani duże litery, ani typy znaków, ani kropki nie są wystarczające do wyłapania zdań.
    ## Dlatego używam regexa który wyłapuje zdania kończące się kropką, wykrzyknikiem lub znakiem zapytania, a następnie spacją lub nową linią,
    ## co pozwala wyłapać wszystkie zdania chociaż niektóre w częściach, a także stringi które nie są zdaniami.
    ## Jako znaki mogące wystąpić w zdaniu używam liter, cyfr, przecinków, spacji i myślników, co wynika z analizy pliku testowego 
    ## i pozwala lekko zredukować niepoprawnie matchowane zdania.
    sentences = [match.group() for match in re.finditer(sentence_pattern, content)]
    sentence_count = len([s for s in sentences if s.strip()])

    # DONE: Implement email extraction using regex
    # Extract all valid email addresses from the content
    email_pattern = r"[A-Za-z0-9!#$%&'*+-/=?^_`{|}~][A-Za-z0-9!#$%&'*+-/=?^_`{|}~.]*@([A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9]\.)+[A-Za-z]{2,}"
    ## Regex na email pisany był zgodnie z informacjami z wikipedii.
    ## Adres może się zaczynać jednym z legalnych znaków ale bez kropki, po czym może następować dowolna ilość legalnych znaków,
    ## a następnie @, po którym następują domeny składajace się z znaków alfanumerycznych i myślników, z czego myślniki nie mogą występować na początku i końcu.
    ## każda domena oddzielona jest kropką i może być ich dowowolna niezerowa ilość.
    ## Ostania domena to "Top level domain" i z dostępnych mi informacji wszystkie takie domeny sładają się z jedynie, co najmniej dwóch liter.

    emails = [ match.group() for match in re.finditer(email_pattern, content)]

    # DONE: Calculate word frequencies
    # Count occurrences of each word, excluding stop words and short words
    # Use the Counter class from collections
    frequent_words = {}
    word_counter = Counter(match.group().lower() for match in re.finditer(word_pattern, content))
    for word, count in word_counter.items():
        if word not in stop_words and len(word) > 2 and count > 1:
            frequent_words[word] = count
    ## Wykonuję dokładnie treść polecenia, gdzie za słowa krótkie uznaję te o długości 2 i krótszej.

    # DONE: Implement date extraction with multiple formats
    # Detect dates in various formats: YYYY-MM-DD, DD.MM.YYYY, MM/DD/YYYY, etc.
    # Create multiple regex patterns for different date formats
    date_patterns = [r"\b\d{4}[./-]\d{1,2}[./-]\d{1,2}\b", r"\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b", r"[A-Z][a-z]{2,8} \d{1,2}, \d{4}"]
    ## Jako patterny przyjmuję te które zaczynają się od roku, albo na nim końćzą, a dzień, miesiąc i rok są oddzielone kropką, myślnikiem lub ukośnikiem.
    ## Dodatkowo dodaję pattern na daty w formacie "Miesiąc dzień, rok" gdzie miesiąc zaczyna się dużą literą, a reszta jest cyframi.
    dates = [ match.group() for pattern in date_patterns for match in re.finditer(pattern, content)]

    # DONE: Analyze paragraphs
    # Split the content into paragraphs and count words in each
    # Paragraphs are typically separated by one or more blank lines
    paragraphs = re.split(r"\n\s*\n", content)
    ## Za rozdzielenie akapitów przyjmuję przynajmniej jedną pustą linię, a więc linie w której występują jedynie znaki nowej linii i spacje, 
    ## co równocześnie łączy wiele pustych linii w tylko jedno rozdzielenie akapitów.
    paragraph_sizes = {}
    for i, paragraph in enumerate(paragraphs):
        paragraph_size = 0
        for match in re.finditer(word_pattern, paragraph):
            paragraph_size += 1
        paragraph_sizes[i] = paragraph_size

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "emails": emails,
        "frequent_words": frequent_words,
        "dates": dates,
        "paragraph_sizes": paragraph_sizes,
    }

if __name__ == "__main__":
    # Example usage
    result = analyze_text_file("python-labs\\lab_1\\tests\\test_file.md")
    # print(result)

