import model
from flask import Flask, render_template, g, request
app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     schools = ['latitude', 'longitude', 'state']
#     if request.method == "POST":
#         z = request.form["schools"]
#     #     please = model.get_locations(z)
#     # else:
#     #     please = model.get_locations()
#     return render_template("index.html")

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    results = model.retreive(text)
    return render_template("index.html", results=results)



if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

















    # end
