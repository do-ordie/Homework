from flask import Flask, render_template, request
from model.user import User

app = Flask(__name__)

word=dict()


@app.route('/')
def hello_world():
    return render_template('base.html', title="TWITer")

@app.route('/twit', methods=['POST', 'GET'])
def create_twit():
    if request.method == 'POST':
      name = request.form.get('name')
      twit = request.form.get('twit')
      word[name]=twit
      return render_template('index.html', list=word)
    else:
        return render_template('index.html')
    # print (name)
    # email = request.form['email']
    

if __name__ == '__main__':
    app.run(debug=True)
           