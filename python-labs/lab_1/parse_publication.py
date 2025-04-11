import re
from typing import Optional

def parse_publication(reference: str) -> Optional[dict]:
    """
    Parse academic publication reference and extract structured information.

    Expected reference format:
    Lastname, I., Lastname2, I2. (Year). Title. Journal, Volume(Issue), StartPage-EndPage.

    Example:
    Kowalski, J., Nowak, A. (2023). Analiza algorytmów tekstowych. Journal of Computer Science, 45(2), 123-145.

    Args:
        reference (str): Publication reference string

    Returns:
        Optional[dict]: A dictionary containing parsed publication data or None if the reference doesn't match expected format
    """
    # DONE: Implement regex patterns to match different parts of the reference
    # You need to create patterns for:
    # 1. Authors and year pattern
    # 2. Title and journal pattern
    # 3. Volume, issue, and pages pattern

    authors_year_pattern = r"(\w+, \w\., )*\w+, \w\. \((?P<year>\d{4})\)." 
    ## Zarówno imię jak i nazwisko autorów mogą być znakami polskimi (albo innymi znakami specjalnymi)
    ## dlatego używam \w które wychwyci wszystkie "word characters" zgodnie z definicją.
    ## Autorów może być dowolna ilość, z czego wszyscy oprócz ostatniego są oddzieleni przecinkiem i spacją.
    ## Minimum jeden autor musi występować, więc ostatni pattern jest poza gwiazdką. Wzór na rok to 4 cyfry w nawiasach, a grupy używam potem do wydobycia roku.
    title_journal_pattern = r" (?P<title>(?:\w| )+)\. (?P<journal>(?:\w| )+),"
    ## Tytuł i czasopismo są oddzielone kropką i spacją. Tytuł podobnie jak autorzy może zawierać dowolne znaki specjalne i spacje, więc używam \w| do ich wyłapania.
    ## Po tytule jest kropka, a po czasopiśmie przecinek. Grup używam do wydobycia tytułu i czasopisma.
    volume_issue_pages_pattern = r" (?P<volume>\d+)(?:\((?P<issue>\d+)\))?, (?P<start>\d+)-(?P<end>\d+)\."
    ## Wolumin, wydanie i strony to już cyfry dlatego korzystam z \d. Wydanie jest opcjonalne, dlatego po jego grupie występuje znak zapytania.
    ## Strony są oddzielone myślnikiem, a całość kończy się kropką. Grupy używam do wydobycia woluminu, wydania, stron początkowej i końcowej.
    
    # DONE: Combine the patterns
    full_pattern = authors_year_pattern + title_journal_pattern + volume_issue_pages_pattern
    # DONE: Use re.match to try to match the full pattern against the reference
    # If there's no match, return None
    if not re.match(full_pattern, reference):
        return None
    # DONE: Extract information using regex
    # Each author should be parsed into a dictionary with 'last_name' and 'initial' keys
    authors_list = []
    # DONE: Create a pattern to match individual authors

    author_pattern = r"(\w+), (\w)\."
    ## Korzystam z dodatkowego patternu który do każdego nazwiska autora osobno się dopasowuje,
    ## a jego grupy wykorzystam do wydobycia nazwiska i inicjału.

    # DONE: Use re.finditer to find all authors and add them to authors_list

    for match in re.finditer(author_pattern, reference):
        authors_list.append({"last_name": match.group(1), "initial": match.group(2)})
    ## Dla każdego matcha pierwsza grupa to nazwisko, a druga to inicjał, te dane umieszczem w liście autorów.

    # DONE: Create and return the final result dictionary with all the parsed information
    # It should include authors, year, title, journal, volume, issue, and pages
    match = re.match(full_pattern, reference)
    result = {"authors": authors_list,
              "year": int(match.group('year')),
              "title": match.group('title'),
              "journal": match.group('journal'),
              "volume": int(match.group('volume')),
              "issue": int(match.group('issue')) if match.group('issue') else None,
              "pages": {'start': int(match.group('start')), 'end': int(match.group('end'))}}
    ## Wszystkie dane wydobywam za pomocą zdefiniowanych wcześniej grup.
    return result
