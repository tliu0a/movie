import fresh_tomatoes

class movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

video1 = movie("A Restaurant Prank Call", "https://i.ytimg.com/vi/EVSbMyWKdDQ/hqdefault.jpg", "https://youtu.be/EVSbMyWKdDQ")
video2 = movie("Angry Asian Restaurant Prank Call", "https://i.ytimg.com/vi/MmTiqKPnhiQ/hqdefault.jpg", "https://youtu.be/MmTiqKPnhiQ")
video3 = movie("Kebab Confusion Prank", "https://i.ytimg.com/vi/OHF_wU1lJo4/hqdefault.jpg", "https://youtu.be/OHF_wU1lJo4")
video4 = movie("Crazy Game Trade Prank Call", "https://i.ytimg.com/vi/q6Lr3V-CZGI/hqdefault.jpg", "https://youtu.be/q6Lr3V-CZGI")
video5 = movie("Insane Cheating Girlfriend Prank", "https://i.ytimg.com/vi/PrD0MkDt6WQ/hqdefault.jpg", "https://youtu.be/PrD0MkDt6WQ")
video6 = movie("KFC Ultimate Rage Prank", "https://i.ytimg.com/vi/LIB0jHTw_3U/hqdefault.jpg", "https://youtu.be/LIB0jHTw_3U")

videolist = [video1, video2, video3, video4, video5, video6]
fresh_tomatoes.open_movies_page(videolist)
