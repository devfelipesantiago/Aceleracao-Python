from flask import Flask, redirect, render_template, request

from product import Product

app = Flask(__name__)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}


book = Book("1984", "George Orwell", 1949)


@app.get("/book")
def get_book():
    return render_template("book.html", book=book.to_dict())


@app.route("/")
def index():
    filmes = [
        {"title": "Inception", "year": 2010},
        {"title": "The Matrix", "year": 1999},
        {"title": "Interstellar", "year": 2014},
    ]
    return render_template("index.html", filmes=filmes)


products = []


@app.route("/products")
def list_products():
    return render_template("products.html", products=products)


@app.route("/", methods=["POST"])
def add_product():
    id = len(products) + 1
    name = request.form["name"]
    price = float(request.form["price"])
    product = Product(id, name, price)
    products.append(product)
    return redirect("/")


@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            break
    return redirect("/")


if __name__ == "__main__":
    app.run()
