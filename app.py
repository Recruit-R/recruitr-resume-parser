from flask import Flask
from pyresparser import ResumeParser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"
@app.route("/testlocal")
def test_local():
    data = ResumeParser('test_resume.pdf').get_extracted_data()
    return data    

#for cloud function
#@functions_framework.http
def parse_resume(request):
    print(request)
    try:
        data = request.json.get('data')
        if data:
            print(data)
            pdf_bytes_io = io.BytesIO(base64.b64decode(data))
            pdf_bytes_io.name = "Resume.pdf"
            return_data = ResumeParser(pdf_bytes_io).get_extracted_data()
            return return_data
        else:
            return {
            'success': False,
            'message': 'No data found in the request'
            }
    except Exception as e:
        return {
        'success': False,
        'message': str(e)
        }
