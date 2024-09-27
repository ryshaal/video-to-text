import os
import time
import subprocess
import threading
import speech_recognition as sr

# Path otomatis berdasarkan lokasi direktori Python saat ini
base_dir = os.getcwd()

input_dir = os.path.join(base_dir, "video_input")
output_dir = os.path.join(base_dir, "video_to_wav_result")

# Membuat folder output jika belum ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fungsi loading dengan animasi panah
def loading_animation(stop_event):
    while not stop_event.is_set():
        for char in ['>', '>>', '>>>']:  # Karakter yang akan digunakan untuk animasi
            print(f"\rTranscribing {char}", end="")
            time.sleep(0.5)  # Durasi delay antar karakter
    print(" " * (len("Transcribing >>>")), end="\r")  # Menghapus output loading

# Fungsi konversi video ke WAV
def convert_video_to_audio(input_video, output_audio):
    command = f"ffmpeg -i \"{input_video}\" -vn \"{output_audio}\""
    
    # Menjalankan perintah di terminal
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return process.returncode

def transcribe_audio(audio_path, language='id-ID'):
    recognizer = sr.Recognizer()
    
    # Menyatakan bahwa file audio yang akan ditranskripsi
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loading_thread.start()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language=language)
            return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"\nKesalahan dalam koneksi ke layanan pengenalan suara: {e}")
        return None
    finally:
        stop_event.set()  # Menghentikan animasi loading saat selesai
        loading_thread.join()

def get_unique_filename(base_path, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(base_path, new_filename)):
        new_filename = f"{base} ({counter}){ext}"
        counter += 1
    return new_filename

if __name__ == "__main__":
    print("Selamat datang di program konversi dan transkripsi video!")
    print("Pilih bahasa untuk transkripsi:")
    print("1. Bahasa Indonesia (id-ID)")
    print("2. Bahasa Inggris (en-US)")
    print("3. Bahasa Spanyol (es-ES)")
    # Tambahkan opsi lainnya sesuai kebutuhan

    language_choice = input("Masukkan pilihan (1/2/3): ")

    language_map = {
        '1': 'id-ID',
        '2': 'en-US',
        '3': 'es-ES',
        # Tambahkan mapping untuk bahasa lain
    }
    
    selected_language = language_map.get(language_choice, 'id-ID')  # Default ke id-ID jika tidak valid

    print("Mencari file video di folder 'video_input'...")
    
    video_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    
    if not video_files:
        print("Tidak ada file video ditemukan di folder input.")
        exit()

    for video_file in video_files:
        input_video_path = os.path.join(input_dir, video_file)
        output_audio_path = os.path.join(output_dir, os.path.splitext(video_file)[0] + '.wav')

        print(f"\nMemulai konversi file: {video_file}...")
        if convert_video_to_audio(input_video_path, output_audio_path) == 0:
            print(f"File audio berhasil dibuat: {output_audio_path}")
        else:
            print(f"Gagal mengonversi file: {video_file}")

    audio_files = [f for f in os.listdir(output_dir) if f.endswith(".wav")]

    if audio_files:
        print("\nMemulai proses transkripsi audio...")
        for audio_file in audio_files:
            input_audio_path = os.path.join(output_dir, audio_file)

            result_text = transcribe_audio(input_audio_path, selected_language)

            if result_text:
                output_transcribe_dir = os.path.join(base_dir, "transcribe")
                if not os.path.exists(output_transcribe_dir):
                    os.makedirs(output_transcribe_dir)
                
                output_file_name = get_unique_filename(output_transcribe_dir, f"{os.path.splitext(audio_file)[0]}.txt")
                output_file_path = os.path.join(output_transcribe_dir, output_file_name)
                
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(result_text)
                print(f"Transkripsi berhasil disimpan di: {output_file_path}")

        # Menghapus file audio yang sudah diproses
        for audio_file in audio_files:
            os.remove(os.path.join(output_dir, audio_file))

        os.rmdir(output_dir)

        print("\nSemua proses selesai. Transkrip Berhasil.")
    else:
        print(f"Tidak ada file WAV yang ditemukan di folder: {output_dir}")