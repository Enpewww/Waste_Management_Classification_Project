import streamlit as st
import os
from PIL import Image

def show():
    """
    Menampilkan halaman Exploratory Data Analysis (EDA) untuk dataset klasifikasi sampah.
    """
    st.title("Exploratory Data Analysis (EDA) - Klasifikasi Sampah Organik vs. Daur Ulang")

    # Ganti path ini jika Anda menyimpan gambar di lokasi lain
    folder_path = "src/EDA_file"

    # --- 1. Distribusi Kelas Sampah ---
    st.header("1. Distribusi Kelas Sampah")
    try:
        distribusi_img_path = os.path.join(folder_path, "EDA 1.png")
        distribusi_image = Image.open(distribusi_img_path)
        st.image(distribusi_image, caption="Distribusi Sampah Organik (55.69%) vs Daur Ulang (44.31%)")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d3de.png' tidak ditemukan di folder '{folder_path}'.")

    st.markdown("""
    **Interpretasi:**
    1.  **Dominasi Sampah Organik:** Kategori sampah organik (55.69%) merupakan mayoritas dalam dataset ini. Hal ini mencerminkan kondisi umum di mana sebagian besar limbah rumah tangga adalah sisa makanan dan sampah lain yang mudah terurai.
    2.  **Distribusi yang Relatif Seimbang:** Meskipun kelas organik lebih banyak, selisihnya dengan kelas daur ulang (Recyclable, 44.31%) hanya sekitar 11%. Proporsi yang tidak terlalu timpang ini sangat baik untuk melatih model Deep Learning seperti CNN, karena dapat mengurangi risiko model menjadi bias terhadap kelas mayoritas.
    3.  **Potensi Implementasi:** Dengan data yang cukup seimbang, model dapat dilatih untuk mengenali kedua kelas dengan baik. Namun, untuk lebih mengoptimalkan performa, teknik seperti augmentasi data dapat diterapkan pada kelas "Recycleable" untuk memastikan model memiliki kemampuan generalisasi yang setara untuk kedua kategori.
    """)

    st.markdown("---")

    # --- 2. Sampel Gambar dan Ciri Visual Awal ---
    st.header("2. Sampel Gambar dan Ciri Visual Awal")
    try:
        sampel_img_path = os.path.join(folder_path, "EDA 2.png")
        sampel_image = Image.open(sampel_img_path)
        st.image(sampel_image, caption="Contoh gambar dari Kelas O (Organik) dan Kelas R (Daur Ulang)")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d3c4.jpg' tidak ditemukan di folder '{folder_path}'.")

    st.markdown("""
    **Distribusi Kelas:**
    - **O (Organik):** Berisi gambar-gambar sisa makanan, buah-buahan, dan sayuran.
    - **R (Daur Ulang/Recyclable):** Terdiri dari gambar sampah seperti botol kaca, kertas, dan wadah plastik.

    **Insight Awal Berdasarkan Ciri Visual:**
    - **Ciri Visual Sampah Organik (Kelas O):**
        - **Warna:** Didominasi warna-warna alami seperti coklat, hijau, dan kuning.
        - **Tekstur:** Cenderung kompleks, tidak beraturan, dan terkadang terlihat lembek atau basah.
    - **Ciri Visual Sampah Daur Ulang (Kelas R):**
        - **Warna:** Seringkali memiliki warna cerah, transparan, atau bening.
        - **Bentuk dan Tekstur:** Objek cenderung kaku, memiliki bentuk yang terstruktur (botol, kaleng, kotak), dan permukaan yang lebih halus.
    """)

    st.markdown("---")

    # --- 3. Distribusi Resolusi Gambar ---
    st.header("3. Distribusi Resolusi Gambar")
    try:
        resolusi_img_path = os.path.join(folder_path, "EDA 3.png")
        resolusi_image = Image.open(resolusi_img_path)
        st.image(resolusi_image, caption="Distribusi Tinggi dan Lebar Gambar untuk Kelas O dan R")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d3bf.png' tidak ditemukan di folder '{folder_path}'.")

    st.markdown("""
    **Insight Eksplorasi Data:**
    - **Resolusi Kecil:** Mayoritas gambar memiliki resolusi di bawah 450 piksel. Ukuran ini cukup efisien untuk proses pelatihan model CNN karena tidak memerlukan proses *resizing* yang ekstrem.
    - **Ukuran Relatif Mirip:** Distribusi ukuran gambar antar kelas cukup mirip. Ini berarti tidak diperlukan perlakuan normalisasi ukuran yang berbeda secara signifikan untuk masing-masing kelas, sehingga menyederhanakan tahap *preprocessing*.
    """)

    st.markdown("---")

    # --- 4. Analisis Fitur Visual ---
    st.header("4. Analisis Fitur Visual")

    st.markdown("### Distribusi Warna RGB")
    try:
        rgb_img_path = os.path.join(folder_path, "EDA 4.png")
        rgb_image = Image.open(rgb_img_path)
        st.image(rgb_image, caption="Perbandingan distribusi RGB antara kelas organik dan daur ulang")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d3a5.png' tidak ditemukan di folder '{folder_path}'.")
    
    st.markdown("""
    **Insight:** Perbedaan pola distribusi RGB yang sangat kontras ini adalah fitur yang sangat kuat.
    - **Organik:** Memiliki keragaman warna yang tinggi dan kompleks, ditandai dengan sebaran R, G, B yang merata.
    - **Daur Ulang:** Menunjukkan lonjakan tajam pada intensitas piksel tertinggi, menandakan dominasi area putih atau sangat terang (misalnya, latar belakang, kertas, plastik bening).
    """)

    # --- 5. Analisis Fitur Visual ---
    st.markdown("### Analisis Tekstur - Local Binary Pattern (LBP)")
    try:
        lbp_img_path = os.path.join(folder_path, "EDA 6.png")
        lbp_image = Image.open(lbp_img_path)
        st.image(lbp_image, caption="Perbandingan hasil LBP untuk menangkap tekstur")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d3a0.jpg' tidak ditemukan di folder '{folder_path}'.")

    st.markdown("""
    **Kesimpulan:** LBP secara efektif membuktikan bahwa kedua kelas memiliki karakteristik tekstur yang sangat berbeda.
    - **Organik:** Kaya akan fitur tekstur yang kompleks, acak, dan tidak teratur.
    - **Daur Ulang:** Cenderung memiliki tekstur yang lebih sederhana, terstruktur, dengan banyak garis lurus dan permukaan halus.
    """)

    # --- 6. Distribusi Rata-Rata Saturasi Kelas ---
    st.markdown("### Distribusi Rata-Rata Saturasi per Kelas")
    try:
        saturasi_img_path = os.path.join(folder_path, "EDA 5.png")
        saturasi_image = Image.open(saturasi_img_path)
        st.image(saturasi_image, caption="Distribusi rata-rata saturasi warna per kelas")
    except FileNotFoundError:
        st.error(f"File gambar 'image_84d0fa.png' tidak ditemukan di folder '{folder_path}'.")
    
    st.markdown("""
    **Insight:** Saturasi warna adalah fitur pembeda lainnya yang signifikan.
    - **Organik (O):** Secara konsisten memiliki warna yang lebih hidup dan kaya (saturasi lebih tinggi dan stabil).
    - **Daur Ulang (R):** Cenderung memiliki warna lebih pudar atau netral (median saturasi rendah), namun dengan beberapa *outlier* berwarna cerah dari kemasan produk.
    """)


if __name__ == "__main__":
    show()
