import whisper
import tempfile

model = whisper.load_model("tiny")

def transcribe_audio(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    result = model.transcribe(tmp_path)
    return result["text"]