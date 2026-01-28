# Handwritten Digit Recognition using CNN (MNIST)

## 📌 Project Overview
This project implements a **Convolutional Neural Network (CNN)** to recognize handwritten digits from the **MNIST dataset**.  
The model is built using **TensorFlow and Keras** and demonstrates a complete deep learning workflow including data preprocessing, augmentation, model training, evaluation, and error analysis.

The goal is to accurately classify grayscale images of handwritten digits (0–9) into their respective classes.

---

## 🧠 Dataset
- **Name:** MNIST Handwritten Digits
- **Images:** 28 × 28 grayscale images
- **Classes:** 10 (digits 0–9)
- **Source:** Keras built-in dataset

The dataset is split into training and testing sets.

---

## ⚙️ Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- TensorFlow
- Keras
- Scikit-learn

---

## 🏗️ Model Architecture
The CNN architecture consists of:
- Convolutional layers for feature extraction
- Max pooling layers for spatial downsampling
- Batch normalization for training stability
- Dropout layers to reduce overfitting
- Fully connected (Dense) layers
- Softmax output layer for multi-class classification

---

## 🔄 Data Preprocessing
- Reshaping images to include channel dimension `(28, 28, 1)`
- Normalizing pixel values to the range `[0, 1]`
- One-hot encoding of labels
- Data augmentation (rotation, shifting, zooming)

---

## 🚀 Training
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metrics: Accuracy
- Validation performed on the test set
- Early stopping used to prevent overfitting

---

## 📊 Evaluation
Model performance is evaluated using:
- Accuracy and loss curves
- Classification report (precision, recall, F1-score)
- Confusion matrix
- Per-class accuracy
- Visualization of misclassified samples

---

## 💾 Model Saving
The trained CNN model is saved in HDF5 format (`.h5`) for future inference or deployment.

---

## 📈 Results
The model achieves high accuracy on the MNIST test dataset, demonstrating the effectiveness of CNNs for image classification tasks.


