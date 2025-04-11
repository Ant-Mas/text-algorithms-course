from parse_publication import parse_publication
from extract_links import extract_links
from analyze_text_file import analyze_text_file
import os
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

class TestAnalyzeTextFile:
    TEST_FILE_PATH = "python-labs\\lab_1\\tests\\test_file.md"

    def test_file_exists(self):
        assert os.path.isfile(
            self.TEST_FILE_PATH
        ), f"Test file not found at {self.TEST_FILE_PATH}"

    def test_analyze_text_file(self):
        result = analyze_text_file(self.TEST_FILE_PATH)

        assert isinstance(result, dict)
        expected_keys = [
            "word_count",
            "sentence_count",
            "emails",
            "frequent_words",
            "dates",
            "paragraph_sizes",
        ]
        for key in expected_keys:
            assert key in result, f"Expected key '{key}' missing from result"

    def test_word_count(self):
        result = analyze_text_file(self.TEST_FILE_PATH)
        assert result["word_count"] > 300, "Word count is suspiciously low"

    def test_sentence_count(self):
        result = analyze_text_file(self.TEST_FILE_PATH)
        assert result["sentence_count"] >= 20, "Sentence count is suspiciously low"

    def test_email_extraction(self):
        result = analyze_text_file(self.TEST_FILE_PATH)

        expected_emails = [
            "jane.smith@university.edu",
            "research.team@nlp-studies.org",
            "history@text-algorithms.com",
            "archives@cs-history.org",
            "regex.help@programming-resources.net",
            "performance@algorithm-testing.org",
            "support@regex-benchmarks.com",
            "dates@formatting-tools.net",
            "developers@text-processing-examples.org",
        ]

        for email in expected_emails:
            assert email in result["emails"], f"Expected email '{email}' not found"

        example_emails = [
            "user@domain.com",
            "name@sub.domain.org",
            "first.last+tag@company-name.co.uk",
        ]

        found_examples = [
            email for email in example_emails if email in result["emails"]
        ]
        assert len(found_examples) > 0, "None of the example emails were found"

        assert len(result["emails"]) >= len(
            expected_emails
        ), "Not enough emails were found"

    def test_date_extraction(self):
        result = analyze_text_file(self.TEST_FILE_PATH)

        expected_dates = [
            "2023-09-15",
            "15.03.2023",
            "01/05/2022",
            "12/31/2022",
            "10/15/1968",
            "2023-04-30",
            "11-22-2023",
        ]

        found_date_count = 0
        for expected_date in expected_dates:
            found = False
            for extracted_date in result["dates"]:
                if (
                    expected_date in extracted_date
                    or expected_date.replace("/", "-") in extracted_date
                ):
                    found = True
                    found_date_count += 1
                    break
            assert found, f"Expected date '{expected_date}' or similar not found"

        text_date_formats = ["May 23, 1977", "January 5, 2024", "September 15, 2023"]
        found_text_dates = False

        for extracted_date in result["dates"]:
            for _ in text_date_formats:
                if any(
                    month in extracted_date for month in ["May", "January", "September"]
                ):
                    found_text_dates = True
                    break
            if found_text_dates:
                break

        assert found_text_dates, "No text-format dates were found"

        assert len(result["dates"]) >= 10, "Not enough dates were found"

    def test_frequent_words(self):
        result = analyze_text_file(self.TEST_FILE_PATH)

        likely_frequent_words = [
            "text",
            "processing",
            "regex",
            "pattern",
            "algorithm",
            "format",
        ]

        found_count = 0
        for word in likely_frequent_words:
            for result_word in result["frequent_words"].keys():
                if word in result_word:
                    found_count += 1
                    break

        assert found_count >= 3, "Expected frequent words not found in results"

        for word, count in result["frequent_words"].items():
            assert (
                count > 1
            ), f"Frequent word '{word}' has suspiciously low count: {count}"

    def test_paragraph_sizes(self):
        result = analyze_text_file(self.TEST_FILE_PATH)

        assert len(result["paragraph_sizes"]) >= 10, "Not enough paragraphs detected"

        for para_num, size in result["paragraph_sizes"].items():
            assert size > 0, f"Paragraph {para_num} has size 0, which is unlikely"

        total_words_in_paras = sum(result["paragraph_sizes"].values())
        assert (
            0.9 <= total_words_in_paras / result["word_count"] <= 1.1
        ), "Total words in paragraphs doesn't match overall word count"

def test_analyze_text_file():
    test = TestAnalyzeTextFile()
    test.test_file_exists()
    print("File existence test passed!")
    test.test_analyze_text_file()
    print("Analyze text file test passed!")
    test.test_word_count()
    print("Word count test passed!")
    test.test_sentence_count()
    print("Sentence count test passed!")
    test.test_email_extraction()
    print("Email extraction test passed!")
    test.test_date_extraction()
    print("Date extraction test passed!")
    test.test_frequent_words()
    print("Frequent words test passed!")
    test.test_paragraph_sizes()
    print("Paragraph sizes test passed!")

def main():
    # test_html_link_extraction()
    # test_publication_parsing()
    test_analyze_text_file()
    pass

if __name__ == "__main__":
    main()