import os
import subprocess

# Path otomatis berdasarkan lokasi direktori Python saat ini
base_dir = os.getcwd()

input_dir = os.path.join(base_dir, "video_input")
output_dir = os.path.join(base_dir, "video_to_wav_result")

# Membuat folder output jika belum ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fungsi konversi video ke WAV
def convert_video_to_audio(input_video, output_audio):
    # Perintah ffmpeg untuk mengonversi video ke audio WAV
    command = ["ffmpeg", "-i", input_video, "-vn", output_audio]
    
    # Menjalankan perintah di terminal
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode == 0:
        print(f"File berhasil dikonversi: {output_audio}")
    else:
        print(f"Terjadi kesalahan saat konversi file '{input_video}': {process.stderr.decode()}")

if __name__ == "__main__":
    # Ambil semua file video di folder input
    video_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    
    if not video_files:
        print("Tidak ada file video ditemukan di folder input.")
        exit()

    # Proses konversi setiap file video di folder input
    for video_file in video_files:
        input_video_path = os.path.join(input_dir, video_file)
        output_audio_path = os.path.join(output_dir, os.path.splitext(video_file)[0] + '.wav')

        print(f"Memulai konversi file: {video_file}")
        convert_video_to_audio(input_video_path, output_audio_path)