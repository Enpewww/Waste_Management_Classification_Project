import streamlit as st

def render_sidebar():
    st.sidebar.title("Klasifikasi Sampah Organik dan Daur Ulang")
    st.sidebar.markdown(
        "Dashboard aplikasi ini digunakan untuk memudahkan pemilahan klasifikasi sampah "
        "yang menggunakan gambar sampah untuk proses automasi pemilahan sampah secara automatis. "
        "Unggah gambar/foto dan dapatkan klasifikasinya."
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Navigation")
    selected = st.sidebar.radio("Go to", ["Home","Exploratory Data Analysis", "Prediction"])
    
    st.sidebar.markdown("---")
    
    return selected