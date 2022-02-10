from flask import Flask, jsonify, request

app = Flask(__name__)

inputs = [
    {
        'cityname':'Hyderabad',
        'places':[
            {
                'name':'Busstop',
                'status':'sanitized'
            }

        ]
    },
    {
        'cityname':'Vijayawada',
        'places':[
            {
                'name': 'Railway Station',
                'status':'Unsanitized'
            }
        ]
    }
]
@app.route('/')
def home():
    return 'welcome'
@app.route('/input1',methods = ['POST'])
def stat():
    request_data = request.get_json()
    new_input1 = {
        'cityname':request_data['cityname'],
        'places' :[]
    }
    inputs.append(new_input1)
    return jsonify(new_input1)
    

@app.route('/input1/<string:cityname>/item',methods = ['POST'])
def get_status(name):
    request_data = request.get_json()
    for input1 in inputs:
        if(input1['status']==status):
            new_item = {
                'status':request_data['price']
            }
            input1['inputs'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'partially sanitized'})

app.run(port = 8000)

