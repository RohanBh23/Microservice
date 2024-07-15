import wikipedia


def wiki(name="War Godess", length=1):
    """This is a Wikipedia Fetcher"""

    my_wiki = wikipedia.summary(name, length)

    return my_wiki

def search_wiki(name):

    results = wikipedia.search(name)
    return results


