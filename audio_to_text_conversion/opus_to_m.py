import pydub
import wave

opus_file = AudioSegment.from_file("input.opus", "opus")
wav_file = opus_file.export("output.wav", format="wav")
m4a_file = wav_file.export("output.m4a", format="m4a")
m4a_file.export("output.m4a", format="m4a")