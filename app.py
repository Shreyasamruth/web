from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of random birthday wishes
wishes = [
    "Happy Birthday! 🎉 May your day be as bright as your smile!",
    "Wishing you a fantastic birthday filled with love and joy!",
    "May your special day be filled with happiness and laughter!",
    "Cheers to another year of awesomeness! 🎂 Enjoy your day!",
    "Many happy returns! May all your wishes come true!"
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wishes', methods=['GET', 'POST'])
def birthday_wish():
    name = request.form.get('name', 'Friend')
    wish = random.choice(wishes)
    return render_template('wishes.html', name=name, wish=wish)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
