<div align="center">
    <h1>
        EmoTa
    </h1>
    <p>
Tamil Emotional Speech Dataset is a collection of recordings in Sri Lankan Tamil, representing the distinct dialects spoken in the northern, eastern, western, and central provinces. It aims to capture the linguistic and emotional diversity of these regions for use in speech and emotion recognition research.
</div>

<div align="center">
  <img src="https://img.shields.io/github/v/release/aaivu/EmoTa?style=flat-rounded" alt="GitHub release (latest by date)" />
  <img src="https://img.shields.io/badge/License-EmoTa%20Academic--Commercial-blue.svg" alt="License: EmoTa Academic-Commercial License">
  <a href="https://rtuthaya.staff.uom.lk/contact-for-resources"><img src="https://img.shields.io/badge/Dataset%20Access-Click%20Here-brightgreen.svg" alt="Dataset Access"></a>
  <a href="https://aclanthology.org/2025.chipsal-1.19.pdf"><img src="https://img.shields.io/badge/Paper-Read%20Now-orange.svg" alt="Paper"></a>
</div>

---
---

**EmoTa** is the first emotional speech dataset in Tamil, designed to reflect the linguistic diversity of Sri Lankan Tamil speakers. It includes 936 utterances from 22 native Tamil speakers (11 male, 11 female), each articulating 19 semantically neutral sentences across five primary emotions: **Anger**, **Happiness**, **Sadness**, **Fear**, and **Neutrality**.

![Speaker Distribution](https://raw.githubusercontent.com/aaivu/EmoTa/main/meta/speaker_distribution.png)

## Key Features:
- **Speakers**: 22 native Tamil speakers (11 male, 11 female)
- **Emotions**: Anger, Happiness, Sadness, Fear, Neutrality
- **Sentences**: 19 semantically neutral sentences to reduce lexical bias
- **Recording Quality**: Captured in a controlled, soundproof environment with professional equipment
- **Total Duration**: Approx. 48 minutes of speech

## Dataset Structure:
The dataset is organized into emotion-based folders with the following naming convention:

```
EmoTa/
    ├── happy/
    ├── sad/
    ├── angry/
    ├── fear/
    └── neutral/
        └── <spkID>_<senID>_<emo[:3]>.wav
```

## Purpose:
EmoTa aims to facilitate research in **Speech Emotion Recognition (SER)** for the Tamil language, offering a balanced and diverse representation of emotional expressions from native Tamil speakers. It is released as open-access to support further exploration of Tamil language processing.

---

## Citation

If you use **EmoTa: A Tamil Emotional Speech Dataset** in your research, please cite: 

```bibtex
@inproceedings{thevakumar-etal-2025-emota,
    title = "{E}mo{T}a: A {T}amil Emotional Speech Dataset",
    author = "Thevakumar, Jubeerathan  and
      Thavarasa, Luxshan  and
      Sivatheepan, Thanikan  and
      Kugarajah, Sajeev  and
      Thayasivam, Uthayasanker",
    editor = "Sarveswaran, Kengatharaiyer  and
      Vaidya, Ashwini  and
      Krishna Bal, Bal  and
      Shams, Sana  and
      Thapa, Surendrabikram",
    booktitle = "Proceedings of the First Workshop on Challenges in Processing South Asian Languages (CHiPSAL 2025)",
    month = jan,
    year = "2025",
    address = "Abu Dhabi, UAE",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2025.chipsal-1.19/",
    pages = "193--201",
    abstract = "This paper introduces EmoTa, the first emotional speech dataset in Tamil, designed to reflect the linguistic diversity of Sri Lankan Tamil speakers. EmoTa comprises 936 recorded utterances from 22 native Tamil speakers (11 male, 11 female), each articulating 19 semantically neutral sentences across five primary emotions: anger, happiness, sadness, fear, and neutrality. To ensure quality, inter-annotator agreement was assessed using Fleiss' Kappa, resulting in a substantial agreement score of 0.74. Initial evaluations using machine learning models, including XGBoost and Random Forest, yielded a high F1-score of 0.91 and 0.90 for emotion classification tasks. By releasing EmoTa, we aim to encourage further exploration of Tamil language processing and the development of innovative models for Tamil Speech Emotion Recognition."
}
```

Paper: [view](https://aclanthology.org/2025.chipsal-1.19.pdf)

---
## 🔧 Dataset loader

You can install the package from PyPI using:

```bash
pip install emota_loader
````

> Make sure to clone/download the [EmoTa dataset](https://github.com/aaivu/EmoTa) separately and point the loader to its root directory.

---

## 🚀 Sample Usage

```python
from emota_loader import EmoTaDataset

dataset = EmoTaDataset(root_dir="path/to/EmoTa").samples # Point to the extracted root folder!

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


--

## Contact  

| 🏷️ **Name**                 | 📧 **Email**                                      | 🔗 **LinkedIn**                                      |
|------------------------------|--------------------------------------------------|----------------------------------------------------|
| **Jubeerathan Thevakumar**   | [jubeerathan.20@cse.mrt.ac.lk](mailto:jubeerathan.20@cse.mrt.ac.lk) | [LinkedIn](https://lk.linkedin.com/in/jubeerathan-thevakumar-87b9b8255) |
| **Luxshan Thavarasa**        | [luxshan.20@cse.mrt.ac.lk](mailto:luxshan.20@cse.mrt.ac.lk)       | [LinkedIn](https://linkedin.com/in/lux-thavarasa)          |
| **Thanikan Sivatheepan**     | [thanikan.20@cse.mrt.ac.lk](mailto:thanikan.20@cse.mrt.ac.lk)     | [LinkedIn](https://lk.linkedin.com/in/sthanikan2000)      |
| **Uthayasanker Thayasivam**  | [rtuthaya@cse.mrt.ac.lk](mailto:rtuthaya@cse.mrt.ac.lk)           | [LinkedIn](https://lk.linkedin.com/in/rtuthaya) |

## Acknowledgment  

Thanks to all the volunteers who provided samples to make **EmoTa** possible.  
Special thanks to **Braveenan Sritharan** for his invaluable help and to **Sajeev Kugarajah** for his contribution to dataset collection.  

---

🔗 **[Dataset Access](https://rtuthaya.staff.uom.lk/resources/dataset/43)**

