import os
import speech_recognition as sr

def transcribe_audio(audio_path):
    # Membuat objek recognizer
    recognizer = sr.Recognizer()
    
    # Mencoba untuk mengenali audio
    try:
        with sr.AudioFile(audio_path) as source:
            # Mendengarkan file audio
            audio_data = recognizer.record(source)
            # Menggunakan bahasa Indonesia
            text = recognizer.recognize_google(audio_data, language='id-ID')
            return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Kesalahan dalam koneksi ke layanan pengenalan suara: {e}")
        return None

# Mengatur direktori secara otomatis berdasarkan lokasi file Python yang dijalankan
base_dir = os.path.dirname(os.path.realpath(__file__))
input_audio_dir = os.path.join(base_dir, "video_to_wav_result")
output_transcribe_dir = os.path.join(base_dir, "transcribe")

# Mencari file audio (format .wav) secara otomatis dari folder input
audio_files = [f for f in os.listdir(input_audio_dir) if f.endswith(".wav")]

if audio_files:
    # Mengambil file audio pertama dari folder input
    audio_file = audio_files[0]
    input_audio_path = os.path.join(input_audio_dir, audio_file)

    # Transkripsi
    result_text = transcribe_audio(input_audio_path)

    # Menyimpan hasil transkripsi ke folder 'transcribe'
    if result_text:
        if not os.path.exists(output_transcribe_dir):
            os.makedirs(output_transcribe_dir)  # Membuat direktori jika belum ada
        output_file_path = os.path.join(output_transcribe_dir, f"{os.path.splitext(audio_file)[0]}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(result_text)
        print(f"Transkripsi berhasil disimpan di: {output_file_path}")
    else:
        print("Tidak dapat memahami audio.")
else:
    print(f"Tidak ada file WAV yang ditemukan di folder: {input_audio_dir}")