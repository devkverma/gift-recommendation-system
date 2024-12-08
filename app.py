from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def app_page():
    return render_template('form.html')

@app.route('/recommend', methods=['GET','POST'])
def recommendations():
    # Replace this with your model's API call or logic
    recommended_items = [
        {
            "title": "Chocolate Box",
            "description": "A premium selection of assorted chocolates.",
            "price": "19.99",
            "image": "https://via.placeholder.com/300x200"
        },
        {
            "title": "Gourmet Dog Treats",
            "description": "Healthy and delicious treats for your beloved pet.",
            "price": "14.99",
            "image": "https://via.placeholder.com/300x200"
        },
        {
            "title": "Luxury Flower Bouquet",
            "description": "A vibrant bouquet of fresh, hand-picked flowers.",
            "price": "39.99",
            "image": "https://via.placeholder.com/300x200"
        },
        {
            "title": "Personalized Mug",
            "description": "A custom mug with your loved one's name.",
            "price": "9.99",
            "image": "https://via.placeholder.com/300x200"
        },
        {
            "title": "Artisan Cheese Basket",
            "description": "A selection of gourmet cheeses for connoisseurs.",
            "price": "49.99",
            "image": "https://via.placeholder.com/300x200"
        },
    ]
    return render_template('recommend.html', products=recommended_items)


if __name__ == "__main__":
    app.run()
