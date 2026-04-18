"""
Emotion Detection Module
This module detects emotions from text input.
"""

def emotion_detector(text_to_analyze):
    """
    Detects emotions from given text and returns emotion scores
    along with dominant emotion.
    """

    if text_to_analyze is None:
        return {
            "error": "Input is None",
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if not isinstance(text_to_analyze, str):
        return {
            "error": "Input is not a string",
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if text_to_analyze.strip() == "":
        return {
            "error": "Empty input",
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    text = text_to_analyze.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    if "angry" in text:
        emotions["anger"] = 0.8
    if "disgust" in text:
        emotions["disgust"] = 0.7
    if "fear" in text:
        emotions["fear"] = 0.9
    if "happy" in text or "joy" in text:
        emotions["joy"] = 0.9
    if "sad" in text:
        emotions["sadness"] = 0.9

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
