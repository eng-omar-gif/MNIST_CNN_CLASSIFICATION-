from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import base64
import cv2

app = Flask(__name__)
model = tf.keras.models.load_model("mnist_model_saved.h5")

def preprocess(img):
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_canvas", methods=["POST"])
def predict_canvas():
    data = request.json["image"]
    image_data = base64.b64decode(data.split(',')[1])
    np_img = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)

    img = preprocess(img)
    preds = model.predict(img)[0]

    return jsonify_result(preds)

@app.route("/predict_upload", methods=["POST"])
def predict_upload():
    file = request.files["file"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    img = preprocess(img)
    preds = model.predict(img)[0]

    return jsonify_result(preds)

def jsonify_result(preds):
    return jsonify({
        "digit": int(np.argmax(preds)),
        "confidence": float(np.max(preds)),
        "probabilities": preds.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
