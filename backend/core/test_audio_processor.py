from backend.core.audio_processor import AudioProcessor
processor=AudioProcessor()
result=processor.process(r"D:\RavenOS\backend\emotion\sample.wav")
print(result)