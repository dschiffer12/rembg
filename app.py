from flask import Flask, request
import rembg

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    image = request.data

    processed_image = rembg.remove(image)

    return processed_image

if __name__ == '__main__':
    app.run(debug=True)
