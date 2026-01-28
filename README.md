# 🧠 Handwritten Digit Recognition – CNN Web Application

An **interactive web application** that recognizes handwritten digits using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. Users can draw digits directly in the browser or upload an image and receive instant predictions with confidence scores and full probability distributions.

---

## 📌 Overview

This project combines **Deep Learning** and **Web Development** to deliver a real-time handwritten digit recognition system. A trained CNN model powers the backend, while a clean web interface enables intuitive user interaction.

The application provides:

* Predicted digit (0–9)
* Confidence score
* Complete softmax probability distribution

---

## ✨ Features

* ✍️ Draw digits using an interactive canvas
* 📤 Upload digit images (PNG / JPG)
* 🔢 Real-time digit prediction
* 📊 Confidence score display
* 📈 Softmax probabilities visualization (bar chart)
* 🧹 Clear canvas functionality

---

## 🧠 Model Information

* **Dataset:** MNIST Handwritten Digits
* **Image Size:** 28 × 28 (grayscale)
* **Classes:** 10 (digits 0–9)
* **Model Type:** Convolutional Neural Network (CNN)
* **Output Layer:** Softmax

---

## ⚙️ Technologies Used

* **Python**
* **Flask**
* **TensorFlow / Keras**
* **NumPy**
* **OpenCV**
* **HTML**
* **CSS**
* **JavaScript**

---

## 📁 Project Structure

```
MNIST_CNN_Project/
│── app.py                 # Flask application
│── mnist_model_saved.h5   # Trained CNN model
│── README.md              # Project documentation
│── templates/
│   └── index.html         # Frontend UI

```

---

## 🔄 Image Preprocessing Pipeline

Before inference, each input image goes through the following preprocessing steps to match the MNIST format:

1. Convert image to grayscale
2. Resize to **28 × 28**
3. Invert colors (white digit on black background)
4. Normalize pixel values to **[0, 1]**
5. Reshape to **(1, 28, 28, 1)**

---

## 🚀 How to Run the Project

### 1️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

### 2️⃣ Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install flask tensorflow numpy opencv-python
```

### 4️⃣ Run the Flask application

```bash
python app.py
```

### 5️⃣ Open the application in your browser

```
http://127.0.0.1:5000
```
---

## 🧑‍💻 Author

Developed as a **full-stack deep learning project**, combining Machine Learning and Web Application development.


