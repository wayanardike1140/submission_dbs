import pandas as pd
import streamlit as st

st.title('Dashboard Penyewaan Sepeda')
st.divider()

with st.sidebar:

    #judul sidebar
    st.title('Menu Filter')

    #filter berdasarkan bulan
    st.divider()
    filter_bulan = st.selectbox(
    'Bulan',
    ('Januari','Febuari','Maret','April','Mei',
        'Juni','Juli','Agustus','September','Oktober','November','Desember')
    )

    #filter berdasarkan musim
    st.divider()
    filter_musim = st.radio(
        "Musim",
        options=[None, 'Semi', 'Panas', 'Gugur', 'Dingin'],
    )

    #filter berdasarkan cuaca
    st.divider()
    filter_cuaca = st.radio(
        "Cuaca",
        options=[None, 'Cerah/Berawan Sebagian', 'Berkabut/Berawan', 'Salju/Hujan Ringan', 'Cuaca Ekstrem'],
    )

#load data
df = pd.read_csv('/day_clean.csv')
df = pd.DataFrame(df)
df = df[(df['mnth']==filter_bulan)|(df['season']==filter_musim)|(df['weathersit']==filter_cuaca)]

#visualisasi keseluruhan
jumlahPerBulan = df
Max = jumlahPerBulan['cnt'].max()
Min = jumlahPerBulan['cnt'].min()

tanggal = jumlahPerBulan['cnt'].max()
st.subheader('Jumlah penyewa sepeda')
st.write('Jumlah terbanyak penyewaan sepeda sekitar', Max, ' dan paling sedikit sekitar', Min)
st.line_chart(jumlahPerBulan, x='dteday', y='cnt')
st.divider()

#visualisasi pengguna casual
st.subheader('Jumlah penyewa sepeda pengguna casual')
casual = df
st.bar_chart(casual, x='dteday', y='casual')

Max_casual = casual['casual'].max()
Min_casual = casual['casual'].min()
st.write('Jumlah terbanyak penyewa casual sekitar', Max_casual, ' dan paling sedikit sekitar', Min_casual, ' pengguna')
st.divider()

#visualisasi pengguna terdaftar
st.subheader('Jumlah penyewa sepeda pengguna terdaftar')
register = df
st.bar_chart(register, x='dteday', y='registered')

Max_register = register['registered'].max()
Min_register = register['registered'].min()
st.write('Jumlah terbanyak penyewa terdaftar sekitar', Max_register, ' dan paling sedikit sekitar', Min_register, ' pengguna')
st.divider()
