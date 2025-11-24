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

## 📸 Screenshots

<img width="548" height="249" alt="streamlit1" src="https://github.com/user-attachments/assets/dc0aa048-b2bd-4804-ab74-f11a93dd1ec3" />

<img width="576" height="242" alt="streamlit2" src="https://github.com/user-attachments/assets/18106ca5-36b4-4661-ba54-9946b3093788" />

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
