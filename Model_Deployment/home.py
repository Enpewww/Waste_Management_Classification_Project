import streamlit as st

def show():
    st.title("♻️ Dashboard Klasifikasi Sampah Organik & Daur Ulang")

    st.markdown("""
    ### Untuk Apa Dashboard Ini?

    Dashboard interaktif ini dirancang untuk:
    - Menjelajahi data citra sampah dan karakteristik masing-masing kategori.
    - Memprediksi jenis sampah (organik atau daur ulang) berdasarkan gambar menggunakan model deep learning.
    - Menampilkan performa model dalam bentuk visualisasi interaktif.

    ---

    ### 🧠 Latar Belakang Masalah
                
    Pengelolaan sampah masih menjadi tantangan besar di berbagai negara. Sebagian besar sampah masih berakhir di tempat pembuangan akhir (TPA), yang menyebabkan berbagai masalah lingkungan seperti pencemaran tanah, air, dan udara, eutrofikasi (pertumbuhan tumbuhan air dan alga berakibat pada penurunan kualitas air bersih), leachate (air lindi beracun), serta ancaman terhadap satwa yang didapat secara tidak sengaja mengonsumsi limbah berbahaya.
    Salah satu hambatan utama dalam pengelolaan sampah yang efektif adalah kurangnya sistem pemilahan sampah yang efisien, khususnya dalam membedakan antara sampah organik dan sampah daur ulang.

    ---

    ### 🧪 Arsitektur Model

    Model yang digunakan adalah **Convolutional Neural Network (CNN)** dengan arsitektur **pre-trained** VGG16 yang terdiri dari beberapa lapisan:
    - Input layer menggunakan arsitektur VGG16.            
    - Dua blok konvolusi dengan fungsi aktivasi **ReLU** dan **MaxPooling** untuk ekstraksi fitur dari gambar.
    - **Flatten** untuk meratakan hasil ekstraksi fitur.
    - **Dropout layer** untuk mengurangi risiko overfitting.
    - Lapisan **Dense** untuk proses klasifikasi akhir.

    Model ini dilatih untuk membedakan antara **2 kelas** utama:
    - Sampah Organik
    - Sampah Daur Ulang

    ---

    ### 📂 Dataset yang Digunakan

    Dataset yang digunakan berasal dari:
    - [Kaggle: Waste Classification Dataset](https://www.kaggle.com/datasets/techsash/waste-classification-data)
    - Mencakup dua kategori:
        - 🥬 Organic (Organik): sisa makanan, daun, buah-buahan, dll.
        - 🧴 Recyclable (Daur Ulang): plastik, logam, kertas, kaca, dll.

    ---

    ### 🛠️ Cara Menggunakan Aplikasi Ini

    - Gunakan **sidebar** untuk navigasi:
        - 🔍 Homepage
        - 📊 Exploratory Data Analysis
        - 📷 Unggah gambar sampah untuk klasifikasi
        
    - Unggah gambar sampah dalam format **.jpg** atau **.png**.
    - Pilih label yang sesuai dengan gambar yang diunggah sebagai referensi validasi.
    - Model akan memprediksi jenis sampah dan menampilkan tingkat kepercayaannya.
    - Hasil prediksi akan dibandingkan dengan label asli (jika tersedia) untuk mengecek akurasi secara langsung.

    ---

    Selamat memilah secara cerdas dan berkelanjutan! 🌱
    """)