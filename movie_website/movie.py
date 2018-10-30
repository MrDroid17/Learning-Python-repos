import webbrowser;

class Movie():
    def __init__(self, movie_name, movie_plot, movie_image, movie_trailer):
        self.title = movie_name
        self.plot = movie_plot
        self.image = movie_image
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)