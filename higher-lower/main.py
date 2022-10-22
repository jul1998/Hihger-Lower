import random

from flask import Flask
app = Flask(__name__)

gifs = ['<iframe src="https://giphy.com/embed/IsYt1rfEu0Zv1FjK19" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/snl-saturday-night-live-season-46-IsYt1rfEu0Zv1FjK19">via GIPHY</a></p>',
        '<iframe src="https://giphy.com/embed/mPytjcsG3XS4o" width="480" height="298" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/confused-lost-disney-mPytjcsG3XS4o">via GIPHY</a></p>',
        '<iframe src="https://giphy.com/embed/iJsuABqEQVvKjbVgiO" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/VoileBanquePopulaire-sailing-banquepopulaire-voilebanquepopulaire-iJsuABqEQVvKjbVgiO">via GIPHY</a></p>',
        '<iframe src="https://giphy.com/embed/8GTKaetBL5IVBMr18A" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/G2Esports-g2-niko-g2niko-8GTKaetBL5IVBMr18A">via GIPHY</a></p>',
        '<iframe src="https://giphy.com/embed/3o7aCTPPm4OHfRLSH6" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reaction-3o7aCTPPm4OHfRLSH6">via GIPHY</a></p>'
        ]


def generate_random_number():
    random_number = random.randint(0,9)
    return random_number

@app.route('/')
def hello_world():
    return '<h1 style=text-align:center>Guess a number between 0 and 9</h1>'\
            '<iframe style="self-align:center" src="https://giphy.com/embed/8P3w6qmBBBW4qxYFP1" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/mlb-what-confused-josh-bell-8P3w6qmBBBW4qxYFP1"></a></p>'

@app.route("/<int:number>")
def guess_number(number):
    random_number = generate_random_number()
    if number == random_number:
        return f"<h1>You got it! This is the random number: {random_number}</h1>"\
                f"{random.choice(gifs)}"
    elif number>random_number:
        return f"<h1>Too high!</h1>"\
                f"{random.choice(gifs)}"
    else:
        return f"<h1>Too low!</h1>"\
                f"{random.choice(gifs)}"


if __name__ == "__main__":
    app.run(debug=True)