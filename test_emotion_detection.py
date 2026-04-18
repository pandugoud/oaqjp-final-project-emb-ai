from emotion_detection import emotion_detector

def test_emotion():

    result = emotion_detector("I am very happy")

    assert result["joy"] > 0
    assert result["dominant_emotion"] == "joy"

    print("TEST PASSED")

if __name__ == "__main__":
    test_emotion()