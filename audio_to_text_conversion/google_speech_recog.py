# !pip install SpeechRecognition
# !pip install ffmpeg-python
# !ffmpeg -i /content/audio.mp3 /content/audio.wav
import speech_recognition as sr
import time

def transcribe_audio_chunks(audio_file_path, chunk_duration=5, output_file="transcription.txt"):
    """Transcribes a large audio file in chunks and saves the results to a file."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source, open(output_file, "w") as f:
        total_duration = source.DURATION  # Get the total duration of the audio
        start_time = 0

        while start_time < total_duration:
            # Read audio chunk
            audio_data = recognizer.record(source, duration=chunk_duration)

            # Recognize speech in the chunk
            try:
                text = recognizer.recognize_google(audio_data)
                f.write(f"[{start_time}-{start_time + chunk_duration} sec]: {text}\n")
                print(f"[{start_time}-{start_time + chunk_duration} sec]: {text}")
            except sr.UnknownValueError:
                f.write(f"[{start_time}-{start_time + chunk_duration} sec]:\n")
                print(f"[{start_time}-{start_time + chunk_duration} sec]: no audio")
            except sr.RequestError as e:
                f.write(f"[{start_time}-{start_time + chunk_duration} sec]: technical error; {e}\n")
                print(f"[{start_time}-{start_time + chunk_duration} sec]: technical error; {e}")

            # Update start time for the next chunk
            start_time += chunk_duration

# Example usage:
audio_file_path = "/content/audio.wav"
transcribe_audio_chunks(audio_file_path)
print("Transcription saved to transcription.txt")