import wikipedia

# https://wikipedia.readthedocs.io/en/latest/code.html#api

def fetch_wikipedia_article(query: str):
    try:
        # Search Wikipedia for titles matching the query keywords
        search_results = wikipedia.search(query)
        # if no results found (ambigious), suggest users what they might have been looking for
        if not search_results:
            return None, wikipedia.suggest(query)

        # Use the first result as the most relevant page title
        best_title = search_results[0]

        # Retrieve page content using exact title (auto_suggest=False to avoid redirects)
        page = wikipedia.page(best_title, auto_suggest=False)

        # print(page.sections)
        # print(page.content)
        return page.content, page.url

    except Exception:
        # General fallback for unexpected errors
        return None, None

