import random

class Books:
    def __init__(self, author, title, color):
        self.author = author
        self.title = title
        self.color = color

    def __repr__(self):
        return f"Book: {self.title} by {self.author} ({self.color})"

def create_random_book():
    titles = ["The Great Journey", "Code Logic", "Silent Moon", "Modern Python"]
    authors = ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"]
    colors = ["Red", "Blue", "Green"]
    
    return Books(
        author=random.choice(authors), 
        title=random.choice(titles), 
        color=random.choice(colors)
    )

print(create_random_book())