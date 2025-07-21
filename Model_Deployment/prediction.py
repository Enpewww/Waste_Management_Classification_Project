# type: ignore
import streamlit as st

# Dataset
import numpy as np
import matplotlib.pyplot as plt

# Model & Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load model
model = load_model("src/best_model.keras")

# Label class
class_labels = ['Organics', 'Recycleable']

# Fungsi prediksi untuk satu gambar
def predict_single_image(image, model, target_size=(224, 224)):
    img = image.convert('RGB').resize(target_size)
    img_array = img_to_array(img) / 255.0
    img_array_expanded = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array_expanded)[0][0]

    if prediction > 0.5:
        label = class_labels[1]
        confidence = prediction
    else:
        label = class_labels[0]
        confidence = 1 - prediction

    return label, confidence

# Halaman utama
def show():
    st.title("♻️ Klasifikasi Sampah Organik & Daur Ulang")
    st.markdown("Upload gambar sampah, pilih label sebenarnya, lalu klik **Prediksi** untuk melihat hasil klasifikasi.")

    uploaded_file = st.file_uploader("📤 Upload gambar sampah", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.subheader("🖼️ Gambar yang Diunggah")
        image = Image.open(uploaded_file)
        st.image(image, width=400)

        selected_label = st.radio("📝 Pilih label sebenarnya (ground truth):", class_labels)

        if st.button("🔍 Submit & Prediksi"):
            # Prediksi
            predicted_label, confidence = predict_single_image(image, model)

            # Hasil
            st.subheader("📌 Hasil Prediksi Model")
            st.write(f"**Predicted Label:** {predicted_label}")
            st.write(f"**Confidence:** {confidence * 100:.2f}%")
            st.markdown("---")
            st.subheader("✅ Ground Truth yang Dipilih")
            st.write(f"**Ground Truth:** {selected_label}")

            # Komparasi
            if predicted_label.lower() == selected_label.lower():
                st.success("✅ Prediksi sesuai dengan label yang dipilih!")
            else:
                st.error("❌ Prediksi tidak sesuai dengan label yang dipilih.")

# Jalankan jika langsung dieksekusi
if __name__ == "__main__":
    show()