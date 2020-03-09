from flask import Flask
from flask import jsonify,request
app = Flask(__name__)




@app.route('/articles/<articleid>')


# @app.route('/accession/<accession_number>') 
# def print_accession_number(accession_number):
#     return  "acession number is" + str(accession_number); 


@app.route('/accession') 
def get_accession_number_status():
     if 'accession_no' in request.args:
        return 'Received accession number as' + request.args['accession_no']
    else:
        return 'Sorry Accession Number is not received'


# @app.route('/accessionRequest')
# def print_accession_number_from_request():
#     if 'accession_no' in request.args:
#         return 'Received accession number as' + request.args['accession_no']
#     else:
#         return 'Sorry Accession Number is not received'





if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0", port = 3000)