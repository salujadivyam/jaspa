import soundfile as sf
import numpy as np
from transformers import pipeline

class EmotionDetector:
    def __init__(self):
        print("Loading HuBERT")
        self.classifier=pipeline(
            "audio-classification",
            model="superb/hubert-base-superb-er"
        )
        print("HuBERT loaded")

    def predict(self,audio_path):
        audio,sr=sf.read(audio_path)
        if len(audio.shape)>1:
            audio=np.mean(audio,axis=1)
        return self.classifier(audio)