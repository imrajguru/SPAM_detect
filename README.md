# 📧 Spam Message Detection System

A Professional Machine Learning web application built using **Streamlit** that detects whether a message is **Spam** or **Not Spam** using Natural Language Processing (NLP).

---

## 🚀 Project Overview

This project uses a trained Machine Learning model to classify text messages as:

- ✅ Not Spam (Ham)
- 🚨 Spam

The system applies **TF-IDF Vectorization** for text transformation and a supervised classification algorithm to perform predictions.

The application provides a clean and interactive web interface built with Streamlit.

---

## 🎯 Features

- Clean and professional UI
- Real-time spam prediction
- Prediction confidence percentage
- Confidence progress bar
- Sidebar with project details
- Fully interactive Streamlit application

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pickle
- NLP (TF-IDF Vectorization)

---

## 📂 Project Structure

```
spam_detection/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User enters a message in the input box.
2. Text is transformed using a TF-IDF Vectorizer.
3. The trained model predicts:
   - Spam (1)
   - Not Spam (0)
4. Prediction confidence is calculated using `predict_proba()`.
5. Result is displayed with a confidence percentage and progress bar.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/spam_detection.git
cd spam_detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Model Information

- Text Preprocessing: TF-IDF Vectorization
- Classification Algorithm: (Mention your model here — e.g., Naive Bayes / Logistic Regression)
- Output: Binary Classification (Spam / Not Spam)
- Confidence Score: Based on predicted probabilities

---

## 📌 Internship / Portfolio Note

This project demonstrates practical implementation of:

- Natural Language Processing
- Text classification using Machine Learning
- Model deployment with Streamlit
- UI design for ML applications

This project is suitable for internship submissions and portfolio demonstrations.

---

## 👨‍💻 Author

Rajguru Thevar  
Machine Learning Enthusiast
