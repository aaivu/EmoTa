from pathlib import Path
from typing import List, Dict, Union

from .utils import Speaker, Sentence, EmotionLabel, SPEAKERS, EMOTION_LABELS, SENTENCES


class EmoTaSample:
    """
    A single sample in the EmoTa dataset, representing one audio file
    and its associated speaker, sentence, and emotion metadata.
    """

    def __init__(
        self,
        audio_path: Union[str, Path],
        speaker: Speaker,
        sentence: Sentence,
        emotion: EmotionLabel,
    ):
        self.audio_path = str(audio_path)
        self.speaker_id = speaker.speaker_id
        self.speaker_gender = speaker.gender
        self.speaker_age = speaker.age
        self.speaker_region = speaker.region
        self.sentence_id = sentence.sentence_id
        self.transcript = sentence.text
        self.emotion = emotion.label

    def __repr__(self) -> str:
        return (
            f"EmoTaSample(spk={self.speaker_id}, "
            f"sen={self.sentence_id}, "
            f"emo='{self.emotion}', "
            f"path='{self.audio_path}')"
        )


class EmoTaDataset:
    """
    Loads and parses the EmoTa dataset from a given root directory.
    Assumes audio filenames follow the format: <spkID>_<senID>_<emo>.wav
    """

    def __init__(
        self,
        root_dir: Union[str, Path],
        speakers: Dict[int, Speaker] = SPEAKERS,
        sentences: Dict[int, Sentence] = SENTENCES,
        emotions: Dict[str, EmotionLabel] = EMOTION_LABELS,
    ):
        self.root_dir = Path(root_dir)
        self.speakers = speakers
        self.sentences = sentences
        self.emotions = emotions
        self.samples: List[EmoTaSample] = []

        self._load_dataset()

    def _load_dataset(self):
        for wav_file in self.root_dir.rglob("*.wav"):
            try:
                name = wav_file.stem
                parts = name.split("_")
                if len(parts) != 3:
                    continue

                spk_id = int(parts[0])
                sen_id = int(parts[1])
                emo_key = parts[2][:3].lower()

                speaker = self.speakers.get(spk_id)
                sentence = self.sentences.get(sen_id)

                # Match emotion by prefix
                emotion = next(
                    (
                        emo
                        for key, emo in self.emotions.items()
                        if key.startswith(emo_key)
                    ),
                    None,
                )

                if speaker and sentence and emotion:
                    sample = EmoTaSample(wav_file, speaker, sentence, emotion)
                    self.samples.append(sample)
            except Exception as e:
                print(f"Skipping file {wav_file}: {e}")

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> EmoTaSample:
        return self.samples[idx]
