import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Menhitung Luas Bangun", ["Hitung Luas Persegi Panjang", 'Hitung Luas Segitiga', 'Hitung Luas Lingkaran','Hitung Luas Persegi'], 
        icons=['house', 'gear', 'list-task','cast','gear'], menu_icon="cast", default_index=0)
    selected
if(selected == 'Hitung Luas Persegi Panjang'):
        st.title('Hitung Luas Persegi Panjang')

        panjang = st.number_input ("Masukkan Nilai Panjang", 0)
        lebar = st.number_input ("Masuk Lebar", 0)
        hitung = st.button ("Hitug Luas Persegi Panjang")

        if hitung :
            luas_persegi = panjang * lebar
            # st.write ("Luas Persegi Panjang = ", luas_persegi)
            st.success (f"Luas Persegi Panjang Adalah = {luas_persegi}")
            
if(selected == 'Hitung Luas Segitiga'):
        st.title('Hitung Luas Segitiga')
        
        alas = st.number_input ("Masuukan Nilai Alas", 0)
        tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
        hitung = st.button ("Hitung Luas Segitiga")
        
        if hitung :
            luas_segitiga = alas * tinggi / 2
            st.success (f"Luas Segitiga Adalah = {luas_segitiga}")
            
if(selected == 'Hitung Luas Lingkaran') :
        st.title('Hitung Luas Lingkaran')
        jarijari = st.number_input ("Masukkan Nilai Jari Jari", 0)
        hitung = st.button ("Hitung Luas Lingkaran")
        
        if hitung :
            luas_lingkaran = 22/7*jarijari*jarijari
            st.success(f"Luas Lingkarang Adalah ={luas_lingkaran}")
        
if(selected == 'Hitung Luas Persegi') :
        st.title('Hitung Luas Persegi')
        sisi = st.number_input ("Masukkan Nilai Sisi Persegi", 0)
        hitung = st.button ("Hitung Luas Persegi")
        
        if hitung :
            luas_persegi = sisi*sisi
            st.success(f"Luas Lingkarang Adalah ={luas_persegi}")
        
    