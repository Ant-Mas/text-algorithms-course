from parse_publication import parse_publication
from extract_links import extract_links
class TestPublicationParsing:
    def test_basic_publication(self):
        reference = (
            "Kowalski, J., Nowak, A. (2023). Analiza algorytmów tekstowych. Journal of Computer Science, "
            "45(2), 123-145."
        )
        result = parse_publication(reference)
        assert result["authors"] == [ {"last_name": "Kowalski", "initial": "J"}, {"last_name": "Nowak", "initial": "A"},]
        assert result["year"] == 2023
        assert result["title"] == "Analiza algorytmów tekstowych"
        assert result["journal"] == "Journal of Computer Science"
        assert result["volume"] == 45
        assert result["issue"] == 2
        assert result["pages"] == {"start": 123, "end": 145}

    def test_single_author(self):
        reference = "Kowalski, J. (2021). Podstawy wyrażeń regularnych. Computer Science Review, 30, 45-67."
        result = parse_publication(reference)

        assert result["authors"] == [{"last_name": "Kowalski", "initial": "J"}]
        assert result["year"] == 2021
        assert result["title"] == "Podstawy wyrażeń regularnych"
        assert result["journal"] == "Computer Science Review"
        assert result["volume"] == 30
        assert result["issue"] is None
        assert result["pages"] == {"start": 45, "end": 67}

    def test_three_authors(self):
        reference = (
            "Kowalski, J., Nowak, A., Wiśniewski, P. (2022). Analiza wydajności algorytmów. Journal of "
            "Algorithms, 15(3), 201-225."
        )
        result = parse_publication(reference)

        assert len(result["authors"]) == 3
        assert result["authors"][0] == {"last_name": "Kowalski", "initial": "J"}
        assert result["authors"][1] == {"last_name": "Nowak", "initial": "A"}
        assert result["authors"][2] == {"last_name": "Wiśniewski", "initial": "P"}

    def test_invalid_references(self):
        assert parse_publication("Niepoprawna referencja") is None
        assert parse_publication("") is None

class TestHtmlLinkExtraction:
    def test_basic_links(self):
        html = (
            '<div><a href="https://www.agh.edu.pl">AGH</a> <a href="https://www.agh.edu.pl/wydzialy" '
            'title="Wydziały">Wydziały AGH</a></div>'
        )
        result = extract_links(html)

        assert len(result) == 2
        assert result[0] == {
            "url": "https://www.agh.edu.pl",
            "text": "AGH",
            "title": None,
        }
        assert result[1] == {
            "url": "https://www.agh.edu.pl/wydzialy",
            "text": "Wydziały AGH",
            "title": "Wydziały",
        }

    def test_empty_html(self):
        assert extract_links("") == []
        assert extract_links("<div>Tekst bez linków</div>") == []

    def test_complex_html(self):
        html = """
        <div>
            <p>Odwiedź naszą stronę <a href="https://www.agh.edu.pl" title="Strona główna">AGH</a>.</p>
            <ul>
                <li><a href="https://www.agh.edu.pl/wydzialy">Lista wydziałów</a></li>
                <li><a href="https://www.agh.edu.pl/studenci" title="Informacje dla studentów">Dla studentów</a></li>
            </ul>
        </div>
        """
        result = extract_links(html)

        assert len(result) == 3
        assert result[0]["url"] == "https://www.agh.edu.pl"
        assert result[0]["title"] == "Strona główna"
        assert result[1]["text"] == "Lista wydziałów"
        assert result[2]["title"] == "Informacje dla studentów"

def test_publication_parsing():
    test = TestPublicationParsing()
    test.test_basic_publication()
    print("Basic publication test passed!")
    test.test_single_author()
    print("Single author test passed!")
    test.test_three_authors()
    print("Three authors test passed!")
    test.test_invalid_references()
    print("All tests passed!")

def test_html_link_extraction():
    test = TestHtmlLinkExtraction()
    test.test_basic_links()
    print("Basic links test passed!")
    test.test_empty_html()
    print("Empty HTML test passed!")
    test.test_complex_html()
    print("Complex HTML test passed!")

def main():
    # test_html_link_extraction()
    test_publication_parsing()
    pass

if __name__ == "__main__":
    main()