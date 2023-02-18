# use decorators to factor out administrative logic

from urllib.request import urlopen


# instead of this
def web_lookup(url, saved=None):
    if saved is None:
        saved = {}
    if url in saved:
        return saved[url]
    page = urlopen(url).read()
    saved[url] = page
    return page


# prefer this
from functools import lru_cache


@lru_cache(maxsize=None)
def web_lookup(url):
    return urlopen(url).read()


# or, in Python 3.9+
from functools import cache


@cache
def web_lookup(url):
    return urlopen(url).read()
