#Napisz klase, która reprezentuje naukowy artykul: klassa powinna miec przynajmniej 5 funkcij

class Article:
    def __init__(self, title, author, date, content, references):
        self.title = title
        self.author = author
        self.date = date
        self.content = content
        self.references = references

    def show_title(self):
        return self.title

    def show_author(self):
        return self.author

    def show_date(self):
        return self.date

    def show_content(self):
        return self.content

    def show_references(self):
        return self.references


article = Article("The title", "The author", "The date", "The content", "The references")
print(article.show_title())
print(article.show_author())
print(article.show_date())
print(article.show_content())
print(article.show_references())
