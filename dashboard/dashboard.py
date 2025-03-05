import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title('Dashboard Penyewaan Sepeda')
st.divider()

with st.sidebar:

    #judul sidebar
    st.title('Menu Filter')

    #filter berdasarkan bulan
    st.divider()
    semua_hari = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')
    hari_check = st.checkbox('Semua hari', False)
    def hari():
        if hari_check == False:
            return 'Minggu'
        else:
            return semua_hari

    filter_hari = st.multiselect(
    'Hari penyewaan sepeda',
    semua_hari,
    default=hari()
    )

    #filter berdasarkan tipe pengguna
    st.divider()
    filter_tipe = st.radio(
        "Tipe penyewa",
        options=['Semua pengguna', 'Pengguna tidak terdaftar', 'Pengguna terdaftar'],
    )

    #filter berdasarkan hari libur/ tanggal merah
    st.divider()
    filter_holiday = st.radio(
        "Berdasarkan hari libur",
        options=['Tanggal merah', 'Tanggal biasa'],
    )

def hari_libur():
    if filter_holiday=='Tanggal merah':
        return 1
    else:
        return 0

def filter_penyewa():
    if filter_tipe == 'Semua pengguna':
        return 'cnt'
    elif filter_tipe == 'Pengguna tidak terdaftar':
        return 'casual'
    else:
        return 'registered'

#load data
df = pd.read_csv('/dashboard/day_clean.csv')
df = pd.DataFrame(df)

#mengurutkan data berdasarkan bulan
list_bulan = ['Januari','Febuari','Maret','April','Mei', 'Juni','Juli','Agustus','September','Oktober','November','Desember']
df["mnth"] = pd.Categorical(df["mnth"], categories = list_bulan)
df = df.sort_values(by = "mnth")

#mengubah kolom holiday jadi int
df['holiday'] = df['holiday'].astype('Int64')

#membuat data bisa difilter secara dinamis sesuai hari
df = df[(df['weekday'].isin(filter_hari))|(df['holiday']==hari_libur())]


#visualisasi tingkat pertumbuhan jumlah penyewaan sepeda tiap bulan pada tahun 2011 dan 2012 
st.subheader('Tingkat pertumbuhan jumlah penyewaan sepeda tiap bulan pada tahun 2011 dan 2012')
jumlahPerBulan = pd.pivot_table(
    df,
    index='mnth',
    columns='yr',
    values=filter_penyewa(),
    aggfunc='sum'
)

fig_tahun = plt.figure(figsize=(10, 5))
plt.title('Tingkat pertumbuhan jumlah penyewaan sepeda tiap bulan pada tahun 2011 dan 2012')
sns.lineplot(jumlahPerBulan)
plt.xlabel('Bulan')
plt.ylabel('Total Penyewa')
plt.xticks(rotation = 25)
plt.show()

st.pyplot(fig_tahun)
st.divider()

#visualisasi jumlah penyewaan sepeda terbaik berdasarkan musim
st.subheader('Jumlah penyewaan sepeda terbaik berdasarkan musim')
fig_musim = plt.figure(figsize=(10, 5))
plt.title('Jumlah penyewaan sepeda terbaik berdasarkan musim')
sns.barplot(df, x='season', y=filter_penyewa())
plt.xlabel('Musim')
plt.ylabel('Total penyewaan')
plt.show()

st.pyplot(fig_musim)
st.divider()

#visualisasi peningkatan jumlah penyewaan sepeda berdasarkan cuaca
st.subheader('Peningkatan jumlah penyewaan sepeda berdasarkan cuaca')
fig_cuaca = plt.figure(figsize=(10, 5))
plt.title('Peningkatan jumlah penyewaan sepeda berdasarkan cuaca')
sns.barplot(df, x='weathersit', y=filter_penyewa())
plt.xlabel('Cuaca')
plt.ylabel('Total penyewaan casual')
plt.show()

st.pyplot(fig_cuaca)
st.divider()

#visualisasi peningkatan penyewa sepeda berdasarkan hari kerja
st.subheader('Peningkatan penyewa sepeda berdasarkan hari kerja')
fig_workingday = plt.figure(figsize=(10, 5))
plt.title('Peningkatan penyewa sepeda berdasarkan hari kerja')
sns.barplot(df, x='workingday', y=filter_penyewa())
plt.xlabel('Hari Bekerja')
plt.ylabel('Total penyewaan casual')
plt.show()

st.pyplot(fig_workingday)
st.divider()

#visualisasi hubungan/ korelasi antara kondisi suhu lingkungan dengan jumlah penyewa sepeda
st.subheader('Hubungan/ korelasi antara kondisi suhu lingkungan dengan jumlah penyewa sepeda')
fig_corr=plt.figure(figsize=(10, 5))
plt.title('Hubungan/ korelasi antara kondisi suhu lingkungan dengan jumlah penyewa sepeda')
sns.regplot(df, x='atemp', y=filter_penyewa())
plt.ylabel('Jumlah penyewa sepeda')
plt.xlabel('Suhu lingkungan')
plt.show()

st.pyplot(fig_corr)
st.divider()

#visualisasi jumlah penyewaan sepeda terbaik berdasarkan kategori suhu
st.subheader('Jumlah penyewaan sepeda terbaik berdasarkan kategori suhu')
fig_suhu=plt.figure(figsize=(10, 5))
plt.title('Jumlah penyewaan sepeda terbaik berdasarkan kategori suhu')
sns.barplot(df, x='temp category', y=filter_penyewa())
plt.xlabel('Kategori suhu')
plt.ylabel('Total penyewaan')
plt.show()

st.pyplot(fig_suhu)
st.divider()
