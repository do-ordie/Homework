from flask import Flask, render_template, request

app = Flask(__name__)

word=dict()


@app.route('/')
def hello_world():
    return render_template('base.html', title="TWITer")

@app.route('/twit', methods=['POST', 'GET'])
def create_twit():
    global word
    if request.method == 'POST':
      name = request.form.get('name')
      twit = request.form.get('twit')
      delet = request.form.get('delet')
      if name != '':
        word[name]=twit
        return render_template('index.html', list=word)
      else:
        for x in word.keys():
           if delet == x:
              del word[delet]
              return render_template('index.html', list=word)
           else:
              return render_template('index.html', list=word)
      return render_template('index.html', list=word)
    else:
      return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
