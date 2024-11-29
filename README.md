
<!-- https://drive.google.com/file/d/1bogkJDrTvBpzyjrL_sYeJhbyCf2JuZm9/view?usp=sharing -->

# 🩺 Kidney Disease Classification Deep Learning Project

## 🌟 Overview

This cutting-edge deep learning project develops a sophisticated machine learning model for classifying kidney diseases using advanced medical imaging techniques. By leveraging state-of-the-art technologies like TensorFlow, Keras, DVC, and MLFlow, we've created a robust solution for automated medical image analysis.

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

## ✨ Key Features

- 🖼️ Advanced medical image classification
- 🤖 VGG-16 based deep learning model
- 🔬 Comprehensive data preprocessing pipeline
- 📊 MLFlow experiment tracking
- 🌐 Flask-based prediction web API
- 🔄 DVC integration for reproducible research

## 🛠 Technical Stack

- **Deep Learning**: TensorFlow, Keras
- **Model Architecture**: VGG-16 (Transfer Learning)
- **Experiment Tracking**: MLFlow
- **Data Management**: DVC
- **Web Framework**: Flask
- **Language**: Python 3.x

## 🚀 Quick Start Guide

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- TensorFlow (GPU support recommended)
- DVC
- Flask
- MLFlow

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dinesh-gaire/Kidney-Disease-Classification-Deep-Learning-Project.git
   cd /Kidney-Disease-Classification-Deep-Learning-Project
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize DVC**
   ```bash
   dvc init
   dvc pull  # Fetch versioned data
   ```

5. **Configure MLFlow**
   ```bash
   export MLFLOW_TRACKING_URI="your_mlflow_server_uri"
   export MLFLOW_TRACKING_USERNAME="your_mlflow_server_username"
   export MLFLOW_TRACKING_PASSWORD="your_mlflow_server_password"
   ```

## 🔍 Project Components

### 📥 Data Ingestion
- Automated dataset loading and preprocessing
- Intelligent image resizing and augmentation
- Supports flexible dataset structures

### 🏋️ Model Training
- Transfer learning with pre-trained VGG-16
- Custom classification layers
- Experiment tracking with MLFlow

### 📊 Model Evaluation
- Comprehensive performance metrics
- Validation set analysis
- Automatic metric logging

### 🌐 Web API Endpoints
- `/train`: Trigger model training pipeline
- `/predict`: Real-time disease classification

## 🖥️ Running the Project

### Training the Model
```bash
python main.py
```

### Starting Web API
```bash
python app.py
```

### Making Predictions
Use curl to send a base64-encoded image:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"image": "<base64_image_data>"}' \
     http://localhost:8080/predict
```

## 🤝 Contribution Guidelines

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

### Code of Conduct
- Be respectful
- Provide constructive feedback
- Follow established project standards

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🌈 Future Roadmap
- Enhance model accuracy
- Add more disease classification categories
- Improve web API interface
- Develop comprehensive documentation

---

**Disclaimer**: Always consult medical professionals for definitive diagnoses. This tool is designed to assist, not replace, medical expertise.
