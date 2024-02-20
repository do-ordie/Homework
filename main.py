from flask import Flask, render_template, request
from model.user import User

app = Flask(__name__)

list=[]

@app.route('/')
def hello_world():
    return render_template('base.html', title="TWITer")

@app.route('/twit', methods=['POST', 'GET'])
def create_twit():
    if request.method == 'POST':
      name = request.form['name']
      list.append(name)
      return render_template('twit_send.html',list= list)
    else:
        return "Somewho"
    # print (name)
    # email = request.form['email']
    

if __name__ == '__main__':
    app.run(debug=True)
           