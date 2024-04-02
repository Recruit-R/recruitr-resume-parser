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