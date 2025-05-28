

# 📲 Fake SMS Detector – Streamlit App with SVM

A machine learning-based SMS classifier that detects fake (spam) messages using an SVM model and TF-IDF vectorization. Built with Python, Streamlit, and Docker.

![App Screenshot](https://github.com/yourusername/fake-sms-detector/raw/main/assets/screenshot.png)

---

## 🧠 Features

* ✅ Detects fake (spam) vs. genuine SMS messages
* ✅ Trained on TF-IDF features using SVM
* ✅ Built with Streamlit for web UI
* ✅ Dockerized for easy deployment
* ✅ Accuracy: 98.1%

---

## 🛠️ Tech Stack

* Python 3.10
* scikit-learn
* Streamlit
* Docker

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-sms-detector.git
cd fake-sms-detector
```

Install dependencies locally:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t fake-sms-detector .
```

Run the container:

```bash
docker run -p 8501:8501 fake-sms-detector
```

Access the app at: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

```
├── streamlit_app.py           # Main app
├── svm_model.pkl              # Trained SVM model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker instructions
├── README.md
└── assets/
    └── screenshot.png         # UI image
```

---

## 🎯 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 98.1% |
| Precision | 98%   |
| Recall    | 87%   |
| F1-score  | 93%   |

Confusion Matrix:

![Confusion Matrix](https://github.com/yourusername/fake-sms-detector/raw/main/assets/confusion_matrix.png)

---

## ✨ Future Improvements

* Add LSTM/Transformer models
* Include live SMS scraping integration
* Improve mobile responsiveness

---

## 📖 License

MIT License. See LICENSE for details.


