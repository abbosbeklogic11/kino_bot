MOVIES = {
    "1234": "Kinoni ko'rish uchun pastdagi link orqali o'ting va yuqori sifatda videoni tomosa qaling: https://t.me/dasturlar_uzb3",
    "5678": "Avatar (2009)",
    "9101": "Inception (2010)"
}

def get_movie_by_code(code: str):
    return MOVIES.get(code, None)
