# 🔁 Paraphraser AI

> An AI-powered text paraphrasing tool built with **T5 Transformer** and **Gramformer** — rewrites sentences while preserving their original meaning, with grammar correction built in.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface&logoColor=black)
![NLP](https://img.shields.io/badge/NLP-T5%20Model-FF6F00?style=flat)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS-E34F26?style=flat&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)

---

## 📌 Overview

**Paraphraser AI** is a Natural Language Processing application that takes an English sentence as input and generates multiple paraphrased versions of it — different wording, same meaning. It combines:

- **T5 (Text-To-Text Transfer Transformer)** for paraphrase generation
- **Gramformer** for grammar correction of the generated output
- A lightweight **HTML web interface** for easy interaction

---

## ✨ Features

- 🔄 Generate multiple paraphrase variations from a single input sentence
- ✅ Grammar correction applied to outputs via Gramformer
- 🌐 Simple web interface (`index.html`) for browser-based usage
- ⚡ Supports both CPU and GPU inference
- 🧪 Multiple experimental scripts for testing different approaches

---

## 🧠 How It Works

```
Input Sentence
      │
      ▼
T5 Transformer (Vamsi/T5_Paraphrase_Paws)
  - Tokenizes input with "paraphrase: " prefix
  - Generates N paraphrased candidates (top-k / top-p sampling)
      │
      ▼
Gramformer
  - Corrects grammar in each paraphrased output
      │
      ▼
Multiple Paraphrased Sentences (output)
```

The T5 model uses **beam search / nucleus sampling** to produce diverse paraphrases, and Gramformer ensures the outputs are grammatically correct before being returned.

---

## 📁 Project Structure

```
parapharaser-AI-/
├── main.py            # Main entry point — runs the full pipeline
├── main3.py           # Alternative pipeline variant
├── paraphrase.py      # Core T5 paraphrasing logic
├── gramformer.py      # Gramformer grammar correction class
├── gram.py            # Grammar correction helper/utilities
├── converting.py      # Text pre/post-processing utilities
├── demo.py            # Quick demo script for testing
├── final.py           # Final integrated pipeline
├── index.html         # Web interface frontend
├── LICENSE            # Apache 2.0
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/rishabhsj/parapharaser-AI-.git
cd parapharaser-AI-
```

### 2. Install Dependencies

```bash
pip install transformers torch sentencepiece
pip install git+https://github.com/PrithivirajDamodaran/Gramformer.git
```

> 💡 A GPU is recommended for faster inference but the model runs on CPU too.

### 3. Run the Paraphraser

```bash
python main.py
```

Or try the quick demo:

```bash
python demo.py
```

---

## 💡 Usage Example

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

sentence = "The weather today is really nice and sunny."
text = "paraphrase: " + sentence + " </s>"

encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
input_ids = encoding["input_ids"].to(device)
attention_masks = encoding["attention_mask"].to(device)

outputs = model.generate(
    input_ids=input_ids,
    attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=120,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)

for output in outputs:
    print(tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True))
```

**Sample Output:**
```
It's a really nice, sunny day today.
Today's weather is sunny and very pleasant.
The weather is sunny and pleasant today.
Today is a sunny and beautiful day.
It is a very nice and sunny day today.
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Paraphrase Model | T5 (`Vamsi/T5_Paraphrase_Paws`) via HuggingFace |
| Grammar Correction | Gramformer |
| Deep Learning Framework | PyTorch |
| Tokenization | SentencePiece |
| Frontend | HTML / CSS |
| Language | Python 3 |

---

## 📦 Dependencies

```
torch
transformers
sentencepiece
gramformer
```

Install all at once:

```bash
pip install torch transformers sentencepiece
pip install git+https://github.com/PrithivirajDamodaran/Gramformer.git
```

---

## 🌐 Web Interface

Open `index.html` in your browser for a simple UI to enter text and view paraphrased results without running any scripts directly.

---

## 🔬 Model Details

| Property | Details |
|---|---|
| Base Model | Google T5 (Text-To-Text Transfer Transformer) |
| Fine-tuned On | Google PAWS Dataset (Paraphrase Adversaries from Word Scrambling) |
| Model Hub | `Vamsi/T5_Paraphrase_Paws` on HuggingFace |
| Task Type | Conditional Text Generation (Seq2Seq) |
| Sampling Strategy | Top-k (k=120) + Nucleus (p=0.95) |
| Max Output Length | 256 tokens |

---

## 🔮 Future Improvements

- Add a Flask/FastAPI backend to serve the model as a REST API
- Support paragraph-level paraphrasing (not just single sentences)
- Add a paraphrase strength slider (conservative → creative)
- Deploy as a web app on Heroku / Render / HuggingFace Spaces
- Add BLEU score evaluation to measure paraphrase quality

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Rishabh Jain**  
Data Engineer | MSc AI & Robotics  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rishabhsj23)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/rishabhsj)
