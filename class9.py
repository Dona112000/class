# Create a class Movie with title, director, and year.
# Override the __str__() method to print movie details nicely when you print the object.


class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def __str__(self):
        return f"{self.title}(Directed by {self.director} in the year {self.year})"
    
m1 = Movie("Inception", "Christopher Nolan", 2010)
print(m1)