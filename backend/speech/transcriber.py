from faster_whisper import WhisperModel
class SpeechTranscriber:
    def __init__(self):
        print("Loading Whisper")
        self.model=WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )
        print("Whisper Loaded")
    def transcribe(self, audio_path):

        print("Starting transcription...")

        segments, info = self.model.transcribe(
        audio_path,
        beam_size=1
        )

        print("Generator created")

        segments = list(segments)

        print("Segments generated")

        print("Transcription started")

        text = ""

        for segment in segments:
            print(segment.text)
            text += segment.text + " "

        return text.strip()