import whisper
from transformers import pipeline

# Load Whisper model
whisper_model = whisper.load_model("small")  # Adjust model size if needed

# Load sentiment classifier
sentiment_classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Define emotion mapping with emojis
emotion_map = {
    "1 star": "😠 Angry",
    "2 stars": "😞 Sad",
    "3 stars": "😐 Neutral",
    "4 stars": "😊 Happy",
    "5 stars": "😁 Very Happy"
}

def hello():
    print("hello")

# Function to process audio and predict sentiment
def get_emotion_from_audio(audio_path):
    # Transcribe audio using Whisper
    result = whisper_model.transcribe(audio_path)
    transcript = result["text"]

    print(f"Transcript: {transcript}")

    # Get sentiment classification
    sentiment = sentiment_classifier(transcript)
    label = sentiment[0]["label"]

    # Print emotion with emoji
    emotion = emotion_map.get(label, "❓ Unknown")
    print(f"Predicted Emotion: {emotion}")

# Example usage
audio_file = "output69.wav"  # Replace with your actual audio file path
get_emotion_from_audio(audio_file)
