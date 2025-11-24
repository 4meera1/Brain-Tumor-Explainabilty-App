# 🧠 Brain Tumor Explainability App (MobileNet + XAI)

This is a Streamlit-based web application that predicts brain tumor types from MRI images using a **MobileNet model with 93.9% accuracy**. The app also includes **Grad-CAM** and **LIME** explainability to visualize which regions influenced the model's prediction.

---

## ⭐ Features
- Upload MRI images for prediction  
- Classifies: **Glioma, Meningioma, Pituitary Tumor, No Tumor**  
- Uses **MobileNet** (lightweight + high accuracy)  
- Explainability:
  - 🔥 **Grad-CAM heatmaps**
  - 🍃 **LIME superpixel explanations**

---

## 🚀 Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Files
- `app_grad.py` – Streamlit interface  
- `gradcam.py` – Grad-CAM implementation  
- `lime_explain.py` – LIME image explainer  
- `final_mobilenet_brain_tumor.keras` – Trained model  

---

## 📜 Tech Used
Python • TensorFlow • MobileNet • Streamlit • OpenCV • LIME  

---

## 📄 License
MIT License
