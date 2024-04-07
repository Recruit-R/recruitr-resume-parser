from flask import Flask
from flask import request
from pyresparser import ResumeParser
import base64
import io
import os

app = Flask(__name__)
@app.route("/", methods=['POST'])
def parse_resume():
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
if __name__ == '__main__':
    # Get the port from the environment variable if available, otherwise use 8080
    port = int(os.environ.get('PORT', 8080))
    # Run the Flask app with the specified host and port
    app.run(debug=True, host='0.0.0.0', port=port)