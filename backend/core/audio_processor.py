from backend.emotion.models import(emotion_detector, emotion_mapper)
from backend.speech.models import(speech_transcriber)
class AudioProcessor:
    def process(self,audio_path):
        predictions=emotion_detector.predict(
            audio_path
        )
        emotion_state=emotion_mapper.map(predictions)
        transcript=speech_transcriber.transcribe(audio_path)
        return {"transcript":transcript,"emotion":emotion_state}