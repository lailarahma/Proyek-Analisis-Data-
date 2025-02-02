import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Menentukan Pertanyaan Bisnis
# Pertanyaan 1: Bagaimana tren peminjaman sepeda berdasarkan faktor musim dan cuaca?
# Pertanyaan 2: Bagaimana pola peminjaman sepeda berdasarkan jam dalam sehari?

# 2. Mengimport Semua Package atau Library
st.title("Dashboard Analisis Peminjaman Sepeda")
st.write("Analisis berdasarkan dataset bike-sharing system")

# 3. Data Wrangling
## Gathering Data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")
st.write("Data berhasil dimuat!")

## Assessing Data
st.write("Menampilkan beberapa baris pertama dataset")
st.write(day_df.head())
st.write(hour_df.head())

## Cleaning Data
# st.write("Memeriksa missing values")
# st.write(day_df.isnull().sum())
# st.write(hour_df.isnull().sum())

# 4. Exploratory Data Analysis (EDA)
st.header("Pilih Analisis")
option = st.selectbox(
    "Pilih Analisis:",
    ["Peminjaman Berdasarkan Musim", "Hari Kerja vs Libur", "Kondisi Cuaca", "Tren Peminjaman Sepanjang Hari", "Pengaruh Cuaca"]
)

## Visualisasi & Explanatory Analysis
if option == "Peminjaman Berdasarkan Musim":
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=day_df["season"], y=day_df["cnt"], ci=None, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Musim")
    st.pyplot(fig)
    
    st.write("Insight: Musim gugur memiliki jumlah peminjaman tertinggi")

elif option == "Hari Kerja vs Libur":
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=day_df["workingday"], y=day_df["cnt"], ci=None, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Akhir Pekan/Hari Libur", "Hari Kerja"])
    ax.set_xlabel("Jenis Hari")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Jumlah Peminjaman Sepeda pada Hari Kerja vs Hari Libur")
    st.pyplot(fig)
    
    st.write("Insight: Hari kerja memiliki jumlah peminjaman lebih tinggi")

elif option == "Kondisi Cuaca":
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=day_df["weathersit"], y=day_df["cnt"], ci=None, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Cerah", "Berkabut", "Hujan Ringan", "Hujan Lebat"])
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    st.pyplot(fig)
    
    st.write("Insight: Cuaca cerah memiliki peminjaman tertinggi")

elif option == "Tren Peminjaman Sepanjang Hari":
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=hour_df["hr"], y=hour_df["cnt"], ci=None, marker="o", ax=ax)
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Tren Peminjaman Sepeda Berdasarkan Jam dalam Sehari")
    ax.set_xticks(range(0, 24))
    ax.grid(True)
    st.pyplot(fig)
    
     st.write("Insight: Peminjaman tertinggi terjadi pada jam 8 pagi dan 5 sore")

elif option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Faktor Cuaca Terhadap Peminjaman Sepeda")
    
    # Suhu vs Jumlah Peminjaman
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=day_df["temp"], y=day_df["cnt"], alpha=0.5, color="blue", ax=ax)
    ax.set_xlabel("Suhu Normalized")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Hubungan Suhu dengan Jumlah Peminjaman Sepeda")
    st.pyplot(fig)
    
    st.write("Insight: Semakin tinggi suhu, semakin banyak peminjaman sepeda")
    
    # Kelembaban vs Jumlah Peminjaman
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=day_df["hum"], y=day_df["cnt"], alpha=0.5, color="green", ax=ax)
    ax.set_xlabel("Kelembaban Normalized")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Hubungan Kelembaban dengan Jumlah Peminjaman Sepeda")
    st.pyplot(fig)
    
     st.write("Insight: Kelembaban tinggi dapat menurunkan peminjaman sepeda")
    
    # Kecepatan Angin vs Jumlah Peminjaman
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=day_df["windspeed"], y=day_df["cnt"], alpha=0.5, color="red", ax=ax)
    ax.set_xlabel("Kecepatan Angin Normalized")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title("Hubungan Kecepatan Angin dengan Jumlah Peminjaman Sepeda")
    st.pyplot(fig)
    
    st.write("Insight: Kecepatan angin tinggi dapat mengurangi jumlah peminjaman")

# 5. Kesimpulan
st.subheader("Kesimpulan")
st.write("Peminjaman sepeda sangat dipengaruhi oleh musim, hari kerja, dan kondisi cuaca.")
