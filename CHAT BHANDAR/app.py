from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Aloo Tikki Chaat", "price": 30, "desc": "Crispy tikki in pure desi ghee, topped with chutneys & yogurt", "tag": "🏆 Best Seller"},
    {"name": "Papdi Chaat", "price": 60, "desc": "Crunchy papdis with tangy tamarind and mint chutney", "tag": ""},
    {"name": "Dahi Bhalla", "price": 50, "desc": "Soft bhallas soaked in chilled dahi with spices", "tag": ""},
    {"name": "Samosa Chaat", "price": 50, "desc": "Crushed samosa tossed with chickpeas & chaat masala", "tag": ""},
    {"name": "Gol Gappe", "price": 20, "desc": "6 crispy puris with spiced mint water", "tag": ""},
    {"name": "Raj Kachori", "price": 100, "desc": "Giant kachori filled with all the chaat goodness", "tag": "🌟 Special"},
    {"name": "Bhel Puri", "price": 30, "desc": "Puffed rice with veggies, sev and tangy chutneys", "tag": ""},
    {"name": "Sev Puri", "price": 50, "desc": "Flat puris topped with potatoes, onion & sev", "tag": ""},
]

reviews = [
    {"name": "Rohit S.", "rating": 5, "text": "Pure ghee tikki at ₹80 – unbeatable! The taste is absolutely authentic."},
    {"name": "Priya M.", "rating": 4, "text": "Good tikki in desi ghee. Non-garlic and onion preparation – great for sattvic diet!"},
    {"name": "Amit K.", "rating": 4, "text": "It's beside the road and the taste is good. Chaat in pure ghee at this price is rare."},
    {"name": "Sneha R.", "rating": 5, "text": "Best chaat in Gamma 1 area! Fresh ingredients and lovely chutneys every time."},
]

@app.route("/")
def index():
    return render_template("index.html", menu=menu, reviews=reviews)

if __name__ == "__main__":
    app.run(debug=True)
