import re


def extract_links(html: str) -> list[dict[str, str]]:
    """
    Extract all links from the given HTML string.

    Args:
        html (str): HTML content to analyze

    Returns:
        list[dict]: A list of dictionaries where each dictionary contains:
            - 'url': the href attribute value
            - 'title': the title attribute value (or None if not present)
            - 'text': the text between <a> and </a> tags
    """

    # DONE: Implement a regular expression pattern to extract links from HTML.
    # The pattern should capture three groups:
    # 1. The URL (href attribute value)
    # 2. The title attribute (which might not exist)
    # 3. The link text (content between <a> and </a> tags)
    pattern = r"<a href=\"(?P<url>([^\"]+))\"(?: title=\"(?P<title>[^\"]*)\")?>(?P<text>.*?)</a>"
    ## URL to dowolna ilość znaków pomiędzy dwoma cudzysłowami, dlatego żaden z nich nie może być cudzysłowem, więc używam [^\"]+.
    ## Title to również dowolna ilość znaków pomiędzy cudzysłowami, ale jest opcjonalna, więc używam znaku zapytania.
    ## Tekst to dowolna ilość znaków pomiędzy tagami a, więc używam .*?, co dopasowuję się do wszystkiego.
    ## Dzięki zdefiniowanym grupom mogę później wydobyć potrzebne dane. 
   
    # DONE: Use re.finditer to find all matches of the pattern in the HTML
    # For each match, extract the necessary information and create a dictionary
    # Then append that dictionary to the 'links' list
    
    links = [{"url": match.group("url"), "title": match.group("title"), "text": match.group("text")} for match in re.finditer(pattern, html)]
    ## w List comprehension iteruje się po re.finditer i dla każdego matcha wydobywam potrzebne dane i umieszczam w słowniku.

    return links
