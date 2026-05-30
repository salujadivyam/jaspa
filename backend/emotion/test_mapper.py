from detector import detect_emotion
from mapper import map_emotion

predictions = detect_emotion(r"D:\RavenOS\backend\emotion\sample.wav")

print("\nRaw Predictions:")
print(predictions)

state = map_emotion(predictions)

print("\nEmotion State:")
print(state)