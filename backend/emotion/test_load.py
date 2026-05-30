from transformers import pipeline
print("Loading the model")
classifier=pipeline(
    "audio-classification",
    model="superb/hubert-base-superb-er"
)
print("Model has been loaded")