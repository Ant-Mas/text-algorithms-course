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
                title: "3. Wyszukiwanie wzorca (1)",
                href: "/topics/03-pattern-matching-1"
            }
        }
    },


    "text-algorithms-book": {
        title: "Text Algorithms Book",
        type: "page",
        href: "https://www.mimuw.edu.pl/~rytter/BOOKS/text-algorithms.pdf"
    }
}