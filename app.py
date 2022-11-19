from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    coach = {
        'name': 'Coach',
        'username': 'coach-steph',
        'pic': 'https://pub-static.fotor.com/assets/projects/pages/d5bdd0513a0740a8a38752dbc32586d0/fotor-03d1a91a0cec4542927f53c87e0599f6.jpg',
        'verified': True,
        'likes': 400,
        'followers': 300,
        'following': 450,
        'biography': 'Please give me views! More projects coming soon, get into the comments or something blah blah blah.',
        'photos': ['https://iso.500px.com/wp-content/uploads/2014/07/big-one.jpg', 'https://cdn3.dpmag.com/2021/07/Landscape-Tips-Mike-Mezeul-II.jpg', 'https://llandscapes-10674.kxcdn.com/wp-content/uploads/2019/07/lighting.jpg', 'https://assets.photographycourse.net/wp-content/uploads/2014/11/12231209/Landscape-Photography-steps.jpg', 'https://expertphotography.b-cdn.net/wp-content/uploads/2022/05/Landscape-Photography-Sophie-Turner.jpg', 'https://www.nyip.edu/images/cms/photo-articles/the-best-place-to-focus-in-a-landscape.jpg']
    }
    return render_template('index.html', user=coach)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
