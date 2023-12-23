import sys
sys.path.append('./libs')

from flask import Flask, request, jsonify
from uk_post_code_validator import UKPostcodeValidator 

app = Flask(__name__)
postcode_validator = UKPostcodeValidator()

@app.route('/validate_postcode', methods=['POST'])
def validate_postcode():
    data = request.get_json()

    if 'postcode' not in data:
        return jsonify({'error': 'Missing "postcode" parameter'}), 400

    postcode = data['postcode']
    formatted_postcode = postcode_validator.format_postcode(postcode)
    is_valid = postcode_validator.validate_postcode(formatted_postcode)

    return jsonify({'is_valid': is_valid, 'formatted_postcode': formatted_postcode})

if __name__ == '__main__':
    app.run(debug=True)