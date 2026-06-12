![Emotion_Recognition_AI Banner](assets/banner.png)

# 🎙️ Emotion_Recognition_AI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-AI-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

Emotion_Recognition_AI is a real-time Speech Emotion Recognition and Stress Analytics platform built using Deep Learning, FastAPI, Streamlit, WebRTC, and SQLite. It detects emotions from live speech, performs stress analysis, and generates AI-driven insights with downloadable reports.

---

## ✨ Features

- Real-time speech emotion recognition
- CNN + LSTM deep learning model
- MFCC feature extraction
- Live microphone input using WebRTC
- Voice Activity Detection (VAD)
- Stress level prediction
- AI emotional assistant
- Interactive Streamlit dashboard
- SQLite database integration
- User authentication system
- PDF & Excel report generation
- FastAPI REST backend
- Docker containerization
- CI/CD pipeline support
- Cloud deployment (Render / Railway / AWS)

---
## 🏗️ System Architecture

Microphone → WebRTC → FastAPI → CNN-LSTM Model → Emotion Output → Dashboard → Reports

----

## 🏗️ Tech Stack

Python, TensorFlow, Keras, Librosa, Streamlit, FastAPI, SQLite, WebRTC, Docker, GitHub Actions

---

## 📂 Project Structure

```

EmotionSenseAI/
├── app/
├── api/
├── models/
├── utils/
├── reports/
├── database/
├── screenshots/
├── docker/
├── main.py
└── requirements.txt

````

---

## ⚙️ Setup Instructions

### Clone Repository
```bash
git clone https://github.com/Vaiishnavi-1350/CodeAlpha_Emotion_Recognition_AI.git
cd CodeAlpha_Emotion_Recognition_AI
````

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

### Streamlit Frontend

```bash
streamlit run app/main.py
```

### FastAPI Backend

```bash
uvicorn api.main:app --reload
```


## 📊 API Endpoints

* POST `/predict-emotion` → Detect emotion from audio
* POST `/stress-analysis` → Predict stress level
* GET `/history/{user_id}` → User history
* GET `/dashboard` → Analytics data

---

## 🐳 Docker Support

This project includes Docker configuration to simplify setup and ensure a consistent execution environment across different systems. By using Docker, users can run the application without manually installing all dependencies.

### Build the Docker Image

```bash
docker build -t emotionsenseai .
```

### Run the Docker Container

```bash
docker run -p 8501:8501 emotionsenseai
```

After starting the container, open your browser and visit:

```text
http://localhost:8501
```

> **Note:** Docker support has been configured and tested locally. The application has not yet been deployed to a cloud hosting platform, but the Docker setup is included to facilitate future deployment and reproducibility.


## 📸 Adding Screenshots

Place images inside:

```
screenshots/
```

Recommended files:

* login.png
* dashboard.png
* emotion_graph.png
* prediction_history.png
* report.png

---

## ☁️ Deployment

Supports:

* Render
* Railway
* AWS EC2
* Docker Hub

---

## 🔄 CI/CD

* GitHub Actions for automation
* Docker build & deployment pipeline
* Automated testing support

---

## 📈 Future Improvements

* Multilingual emotion detection
* Transformer-based models
* Mobile app integration
* Real-time meeting emotion tracking

---
## Conclusion

Emotion Recognition AI demonstrates how machine learning and speech signal processing can be combined to identify human emotions from voice recordings. The system analyzes speech inputs, predicts emotional states, provides confidence scores, tracks user history, and offers wellness insights through an interactive Streamlit dashboard.

This project highlights the potential of emotion-aware applications in areas such as mental health support, customer experience analysis, virtual assistants, and human-computer interaction. Features such as live microphone prediction, stress detection, wellness analytics, speaker identification, and PDF report generation make the application both practical and user-friendly.

Future enhancements may include improving model accuracy using larger and more diverse datasets, supporting multiple languages, enabling real-time deployment on cloud platforms, and integrating advanced deep learning architectures for more robust emotion recognition.

---

## 👨‍💻 Author

Emotion_Recognition_AI Developer

---

## 📜 License

MIT License

```

--
