from flask import Flask, jsonify,jsonify, request

from no_image_processing import get_ocr3

app = Flask(__name__)



@app.route('/superapp', methods=['POST'])
def flutter_image():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    
    file.save("/home/yassinmohamed/superapp linux/id.jpg")
   
    
    ocr_data = get_ocr3()
    return jsonify({'status': 'success', 'ocr_data': ocr_data})






if __name__ == '__main__':
    app.run(host='0.0.0.0' ,  debug=True)






