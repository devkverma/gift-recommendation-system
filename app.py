from flask import Flask, render_template, request
from scripts.recommend import Recommend
from scripts.product_details import ProductDetails

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def app_page():
    return render_template('form.html')

@app.route('/recommend', methods=['GET','POST'])
def recommendations():
    recipient = request.form.get('recipient', 'someone special')
    preference = request.form.get('food_preference', 'any')
    taste = request.form.get('taste', 'mild')
    occasion = request.form.get('occasion', 'general')

    prompt = f"This is for my {recipient}. They prefer {preference} food, and they love it {taste}. It's their {occasion}."

    recommend = Recommend()
    products = recommend.recommend(prompt)

    productdetails = ProductDetails()

    recommended_items = []
    for idx, product in enumerate(products):
        if idx >= 5:
            break
        details = productdetails.fetchDetails(product)

        if isinstance(details, list) and len(details) > 1:
            if 496 in details:
                return render_template("rate_limit.html", seconds_left=details[1])
            elif 'error' in details:
                return render_template("unexpected_error.html", error_message=details[1])
        elif details:
            recommended_items.append(details)

    if not recommended_items:
        return render_template("recommend.html", products=[], message="No recommendations available at this time.")

    return render_template('recommend.html', products=recommended_items)

if __name__ == "__main__":
    app.run()
