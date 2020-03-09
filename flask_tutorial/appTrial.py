from flask import Flask
from flask import jsonify,request
app = Flask(__name__)

@app.route("/") 
def hello():
    return jsonify({"message":"Hello World!"}); 


def do_the_login():
    return jsonify({"message":"Login Complete"})

def show_the_login_form():
    return jsonify({"message":"Login Page"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0", port = 3000)
    
  