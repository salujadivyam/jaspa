class EmotionMapper:
    def map(self,predictions):
        state={
            "stress":0.0,
            "fatigue":0.0,
            "frustration":0.0,
            "confidence":0.0}
        for pred in predictions:
            label = pred["label"]
            score = pred["score"]

            if label == "ang":
                state["stress"] += score
                state["frustration"] += score

            elif label == "sad":
                state["fatigue"] += score

            elif label == "hap":
                state["confidence"] += score

        return state