# 📦 emota_loader — Python Dataloader for EmoTa Dataset

**EmoTa: A Tamil Emotional Speech Dataset** (Thevakumar et al., CHiPSAL 2025) is the first open-access emotional speech corpus in Tamil, designed to capture the dialectal diversity of Sri Lankan Tamil speakers[^1].

| Statistic                  | Value                                          |
|---------------------------|------------------------------------------------|
| Utterances                | 936 (22 speakers × 19 sentences × 5 emotions) |
| Speakers                  | 22 native Sri Lankan Tamil (11 male, 11 female) |
| Sentences                 | 19 semantically neutral sentences              |
| Emotions                  | angry, happy, sad, fear, neutral               |
| Inter-annotator Agreement | Fleiss’ Kappa = 0.74                           |
| Baseline F1 Scores        | XGBoost: 0.91, Random Forest: 0.90            |

---

## 🔧 Installation

You can install the package from PyPI using:

```bash
pip install emota_loader
````

> Make sure to download the [EmoTa dataset](https://rtuthaya.staff.uom.lk/contact-for-resources) separately and point the loader to its root directory.

---

## 🚀 Sample Usage

```python
from emota_loader import EmoTaDataset

# Point to extracted dataset root folder
dataset = EmoTaDataset(root_dir="path/to/EmoTa").samples

print(f"Loaded {len(dataset)} samples")

sample = dataset[0]
print(f"  Audio Path      : {sample.audio_path}")
print(f"  Speaker ID      : {sample.speaker_id}")
print(f"  Speaker Gender  : {sample.speaker_gender}")
print(f"  Speaker Age     : {sample.speaker_age}")
print(f"  Speaker Region  : {sample.speaker_region}")
print(f"  Sentence ID     : {sample.sentence_id}")
print(f"  Transcript      : {sample.transcript}")
print(f"  Emotion         : {sample.emotion}")
```

### Example Output

```
Loaded 936 samples

  Audio Path      : EmoTa/19_18_ang.wav
  Speaker ID      : 19
  Speaker Gender  : male
  Speaker Age     : 25
  Speaker Region  : northern
  Sentence ID     : 18
  Transcript      : நான் உன்னை சந்திக்க வேண்டும்.
  Emotion         : angry
```

---

## 📄 Citation

Please cite the dataset as:

```bibtex
@inproceedings{thevakumar-etal-2025-emota,
  title = "{E}mo{T}a: A {T}amil Emotional Speech Dataset",
  author = "Thevakumar, Jubeerathan and Thavarasa, Luxshan and Sivatheepan, Thanikan and Kugarajah, Sajeev and Thayasivam, Uthayasanker",
  booktitle = "Proceedings of the First Workshop on Challenges in Processing South Asian Languages (CHiPSAL 2025)",
  year = "2025",
  pages = "193--201",
  address = "Abu Dhabi, UAE",
  publisher = "International Committee on Computational Linguistics"
}
```

---

## 📘 License

Academic use only — see the [EmoTa dataset license](https://github.com/aaivu/EmoTa/blob/main/LICENSE.md) for details.

---

[^1]: Thevakumar, J., Thavarasa, L., et al. (2025). [*EmoTa: A Tamil Emotional Speech Dataset*](https://aclanthology.org/2025.chipsal-1.19.pdf). Proceedings of CHiPSAL 2025.