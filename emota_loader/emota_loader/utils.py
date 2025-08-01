from typing import Dict


class Speaker:
    """
    Represents a speaker with attributes like speaker ID, age, gender, and region.
    """

    def __init__(self, speaker_id: int, age: int, gender: str, region: str):
        self.speaker_id = speaker_id
        self.age = age
        self.gender = gender
        self.region = region

    def __repr__(self) -> str:
        return (
            f"Speaker(id={self.speaker_id}, age={self.age}, "
            f"gender='{self.gender}', region='{self.region}')"
        )


class Sentence:
    """
    Represents a sentence with an ID and the text content.
    """

    def __init__(self, sentence_id: int, text: str):
        self.sentence_id = sentence_id
        self.text = text

    def __repr__(self) -> str:
        return f"Sentence(id={self.sentence_id}, text='{self.text}')"


class EmotionLabel:
    """
    Represents an emotion label normalized to lowercase.
    """

    def __init__(self, label: str):
        self.label = label.lower()

    def __repr__(self) -> str:
        return f"EmotionLabel('{self.label}')"


SPEAKERS: Dict[int, Speaker] = {
    1: Speaker(1, 23, "male", "western"),
    2: Speaker(2, 25, "female", "western"),
    3: Speaker(3, 23, "male", "eastern"),
    4: Speaker(4, 22, "male", "eastern"),
    5: Speaker(5, 22, "female", "western"),
    6: Speaker(6, 27, "female", "eastern"),
    7: Speaker(7, 23, "male", "eastern"),
    8: Speaker(8, 23, "female", "eastern"),
    9: Speaker(9, 23, "female", "northern"),
    10: Speaker(10, 23, "female", "northern"),
    11: Speaker(11, 25, "male", "western"),
    12: Speaker(12, 25, "male", "eastern"),
    13: Speaker(13, 25, "male", "northern"),
    14: Speaker(14, 25, "female", "eastern"),
    15: Speaker(15, 24, "female", "eastern"),
    16: Speaker(16, 25, "male", "central"),
    17: Speaker(17, 25, "male", "northern"),
    18: Speaker(18, 27, "male", "eastern"),
    19: Speaker(19, 25, "male", "northern"),
    20: Speaker(20, 25, "female", "northern"),
    21: Speaker(21, 25, "female", "northern"),
    22: Speaker(22, 25, "female", "eastern"),
}

SENTENCES: Dict[int, Sentence] = {
    1: Sentence(1, "நான் இன்று மாலை வீட்டுக்கு செல்கிறேன்"),
    2: Sentence(2, "இண்டைக்கு மழையா இருக்கு"),
    3: Sentence(3, "நாங்க நல்லபடியாக செய்துமுடித்துள்ளோம்"),
    4: Sentence(4, "எப்போதும் தாமதமாக வராதீர்கள்"),
    5: Sentence(5, "நான் உன்னை காதலிக்கிறேன் அன்பே"),
    6: Sentence(6, "அந்த செய்தித்தாளை இங்கு வையுங்கள்"),
    7: Sentence(7, "இந்த நோயாளியின் உடல்நிலை எப்படி இருக்கிறது ?"),
    8: Sentence(8, "இப்ப உனக்கு என்ன பிரச்சனை ?"),
    9: Sentence(9, "உனக்கு யாரை ரொம்ப பிடிக்கும்?"),
    10: Sentence(10, "என் பையை திருப்பிக் கொடு."),
    11: Sentence(11, "எல்லோரும் தவறு செய்கிறார்கள்."),
    12: Sentence(12, "நீ இப்போது வளர்ந்துவிட்டாய்."),
    13: Sentence(13, "நான் அதை பார்த்து கொள்கிறேன்."),
    14: Sentence(14, "நீங்கள் எங்கு போகிறீர்கள்?"),
    15: Sentence(15, "புத்தகம் மேசையில் உள்ளது."),
    16: Sentence(16, "ரயில் மாலை 5 மணிக்கு வரும்."),
    17: Sentence(17, "எனக்கு வழி தெரியவில்லை."),
    18: Sentence(18, "நான் உன்னை சந்திக்க வேண்டும்."),
    19: Sentence(19, "அண்ணா எழுந்திருங்கள்"),
}

EMOTION_LABELS: Dict[str, EmotionLabel] = {
    "angry": EmotionLabel("angry"),
    "happy": EmotionLabel("happy"),
    "sad": EmotionLabel("sad"),
    "fear": EmotionLabel("fear"),
    "neutral": EmotionLabel("neutral"),
}
