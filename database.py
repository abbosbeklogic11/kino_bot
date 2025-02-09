MOVIES = {
    "1234": "Titanik (1997)",
    "5678": "Avatar (2009)",
    "9101": "Inception (2010)"
}

def get_movie_by_code(code: str):
    return MOVIES.get(code, None)
