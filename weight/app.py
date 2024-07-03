from flask import Flask, request, jsonify, render_template
import base64
from io import BytesIO
from PIL import Image
import os
from model.model import segmentation

app = Flask(__name__)

_index = 0


# Ваша модель YOLO
def yolo_model(image_path):
    result = segmentation(image_path)
    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/capture', methods=['POST'])
def capture():
    global _index
    data = request.json
    image_data = data['image'].split(",")[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image_path = f'captured_image_{str(_index)}.jpg'
    image.save(image_path)
    _index += 1

    result = yolo_model(image_path)
    os.remove(image_path)  # Удаляем изображение после обработки
    print(result)
    return jsonify({'result_id': result[0], 'result_name': result[1]})


@app.route('/photo')
def photo():
    return render_template('photo.html')



if __name__ == '__main__':
    app.run(debug=True)
