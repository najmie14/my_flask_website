from flask import Flask, render_template  # Mengimpor Flask dan fungsi render_template

# Membuat instance aplikasi Flask
app = Flask(__name__)

# Membuat route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')  # Menampilkan template HTML 'index.html'

# Jalankan aplikasi jika file ini dijalankan secara langsung
if __name__ == '__main__':
    app.run(debug=True)
