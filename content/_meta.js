export default {

    index: {
        title: '🏠',
        display: 'hidden',
    },

    topics: {
        title: "Rozdziały",
        type: 'menu',
        items: {
            "01-python-introduction": {
                title: "1. Podstawy języka Pythona",
                href: "/topics/01-python-introduction"
            },
            "02-regexes": {
                title: "2. Wyrażenia regularne",
                href: "/topics/02-regexes"
            },
            "03-pattern-matching-1": {
                title: "3. Wyszukiwanie wzorców (1)",
                href: "/topics/03-pattern-matching-1"
            },
            "04-pattern-matching-2": {
                title: "4. Wyszukiwanie wzorców (2)",
                href: "/topics/04-pattern-matching-2"
            },
            "05-suffixes-and-pattern-matching-summary": {
                title: "5. Struktury Sufiksowe i Dopasowywanie Wzorców",
                href: "/topics/05-suffixes-and-pattern-matching-summary"
            },
            "06-sequence-alignment": {
                title: "6. Algorytmy wyrównywania sekwencji i podobieństwa",
                href: "/topics/06-sequence-alignment"
            }
        }
    },

    "text-algorithms-book": {
        title: "Text Algorithms Book",
        type: "page",
        href: "https://www.mimuw.edu.pl/~rytter/BOOKS/text-algorithms.pdf"
    }
}