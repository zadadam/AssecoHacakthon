import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
banks = {
    123456789:
    {'id': 123456789,
     'Bank': 'NBP S.A.',
     'Osoba': 'Aleksander Kociumaka',
     'Numer': '8748374233',
     'chalenge': '6789',
     'danger': False,
     },
    123456790: {'id': 123456790,
     'Bank': 'Bardzo OK Bank S.A.',
     'Osoba': 'Albert Blaztowitz',
     'Numer': '8748374240',
     'chalenge': '6770',
     'danger': False,
    },
}

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/tel/<int:telefon>', methods=['GET'])
def api_tel(telefon):
    out = banks.get(telefon, {'id':telefon, 'no_calls':"true", 'danger':True})
    return jsonify(out)

app.run()