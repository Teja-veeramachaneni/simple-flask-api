import json,re
from flask import Flask
app = Flask(__name__)
Data = """
{
    "details":[
        {

           "place" : "Alankar@theatre",
           "contact Number": "7867567898"
        },

        {
           "place" : "PostOffice",
           "contact Number" : "08656244601"
        }
    ]
    
}"""
res = json.loads(Data)
@app.route("/v1/sanitized/input/")
def result(res):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for i in res['details']:
        if i['place'].isalpha():
            return 'sanitized'
        else:
            return 'Unsanitized'
app.run(port = 800)
