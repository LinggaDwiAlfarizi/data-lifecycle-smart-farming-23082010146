🌱 Smart Farming Data Lifecycle Dashboard

📌 Deskripsi Proyek
    Proyek ini bertujuan untuk menganalisis dan memonitor data sensor kelembaban tanah (soil moisture) pada sistem Smart Farming. Data yang digunakan diproses melalui tahapan Data Lifecycle, mulai dari pengumpulan data, pembersihan data, analisis, hingga visualisasi menggunakan dashboard interaktif berbasis Streamlit.
    Dashboard ini memungkinkan pengguna untuk memantau kondisi kelembaban tanah dari beberapa sensor serta memperoleh insight yang dapat membantu pengambilan keputusan dalam pengelolaan irigasi tanaman.
    
🎯 Tujuan Penelitian
Tujuan dari proyek ini adalah:
- Mengimplementasikan tahapan Data Lifecycle pada data sensor IoT.
- Menganalisis data kelembaban tanah dari beberapa sensor.
- Menyajikan visualisasi data menggunakan dashboard interaktif.
- Memberikan insight yang dapat membantu pengelolaan irigasi tanaman secara lebih efisien.
  
📊 Dataset
Dataset yang digunakan berisi data pembacaan sensor kelembaban tanah dari beberapa sensor pada sistem plant vase.
Struktur Dataset
Kolom	Deskripsi
   datetime	Waktu pencatatan data sensor
- moisture0	Nilai kelembaban tanah sensor 0
- moisture1	Nilai kelembaban tanah sensor 1
- moisture2	Nilai kelembaban tanah sensor 2
- moisture3	Nilai kelembaban tanah sensor 3
- moisture4	Nilai kelembaban tanah sensor 4
  
🔄 Tahapan Data Lifecycle
Proyek ini mengikuti tahapan Data Lifecycle sebagai berikut:

1️⃣ Data Collection
Pengumpulan data sensor dari sistem monitoring tanaman.
Lokasi dataset mentah:
data/raw/plant_vase1.csv

2️⃣ Data Cleaning
Data mentah diproses untuk memastikan kualitas data sebelum dilakukan analisis.
Dataset hasil pembersihan:
outputs/cleaned_data.csv
Proses pembersihan meliputi:
Menghapus data kosong (missing values)
Mengubah tipe data waktu menjadi format datetime
Menghapus data duplikat
Normalisasi format data sensor

3️⃣ Exploratory Data Analysis (EDA)
EDA dilakukan untuk memahami karakteristik data, meliputi:
Statistik deskriptif dataset
Distribusi nilai kelembaban tanah
Analisis korelasi antar sensor
Analisis tren waktu (time series)
Notebook analisis:
Data_Lifecycle_Smart_Farming.ipynb

4️⃣ Data Visualization Dashboard
Dashboard interaktif dibuat menggunakan Streamlit untuk memvisualisasikan data sensor.
Fitur dashboard meliputi:

📊 Key Metrics
Menampilkan informasi utama dari data seperti:
- Rata-rata kelembaban tanah
- Nilai minimum kelembaban
- Nilai maksimum kelembaban
- Jumlah total data
  
💧 Moisture Gauge
Menampilkan tingkat kelembaban tanah saat ini dalam bentuk gauge chart.

📈 Moisture Trend
Grafik time series untuk melihat perubahan kelembaban dari waktu ke waktu.

🔥 Sensor Correlation Heatmap
Menampilkan hubungan korelasi antar sensor.

📊 Moisture Distribution
Histogram distribusi nilai kelembaban tanah.

📦 Sensor Comparison
Perbandingan nilai sensor menggunakan boxplot.

🖥️ Dashboard
Dashboard dibuat menggunakan Streamlit.

Lokasi file dashboard:
Dashboard/streamlit_app.py
Atau bisa mengunjungi link berikut:
https://data-lifecycle-smart-farming-23082010146-p2sxyk5xh83vn2q4jgp37.streamlit.app/

Untuk menjalankan dashboard secara lokal:
pip install -r requirements.txt
streamlit run Dashboard/streamlit_app.py

🛠️ Teknologi yang Digunakan
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
  
🚀 Pengembangan Selanjutnya
Beberapa pengembangan yang dapat dilakukan pada proyek ini:
- Implementasi deteksi anomali pada sensor
- Prediksi kelembaban tanah menggunakan Machine Learning
- Rekomendasi irigasi otomatis
- Integrasi dengan sensor IoT secara real-time
  
👨‍💻 Author
Lingga Dwi Al Farizi
Mahasiswa Sistem Informasi

⭐ Catatan
Proyek ini dibuat sebagai implementasi analisis data berbasis Data Lifecycle pada sistem Smart Farming serta sebagai demonstrasi penggunaan Python dan Streamlit dalam visualisasi data.
