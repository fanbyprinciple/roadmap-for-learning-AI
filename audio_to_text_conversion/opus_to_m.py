import pydub
import wave

from pydub import AudioSegment

opus_file = AudioSegment.from_file("D:\codeplay\\roadmap-for-learning-AI\\audio_to_text_conversion\devu.opus", "opus")
wav_file = opus_file.export("output.wav", format="wav")
m4a_file = wav_file.export("output.m4a", format="m4a")
m4a_file.export("output.m4a", format="m4a")