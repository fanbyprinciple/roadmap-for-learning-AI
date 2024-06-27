# Vosk audio to text

installation at
https://alphacephei.com/vosk/install

It can be done as simply as 

`vosk-transcriber -i test.mp4 -o text.txt'

Trying it on a whatsapp audio fil
the audio file is opus
so need to convert into opus

ffmpeg is common library that is required for this sort of thing

# trying hugging face Wave2Vec2 model

https://huggingface.co/docs/transformers/en/tasks/asr