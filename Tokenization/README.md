# Tokenization in NLP — Beginner's Guide

Tokenization is the **first step** in almost every NLP pipeline. This guide explains what it is, why it matters, and how it works.

---

## 📌 What is Tokenization?

Tokenization means breaking raw text into smaller pieces called **tokens** — usually words or sentences — so a computer can process them one by one.

**Example:**

`"I love NLP!"` → tokenize → `["I", "love", "NLP", "!"]`

Think of it like chopping a sentence into Lego blocks. Each block (token) can then be studied, counted, or converted into numbers for a model.

---

## 🧩 Why Do We Need It?

Computers can't understand a sentence as one big blob of text. Tokenization breaks it down first.

**Input:** `"NLP is fun. Let's learn!"`

**Step 1 — Sentence tokens:**
1. `"NLP is fun."`
2. `"Let's learn!"`

**Step 2 — Word tokens:**
`["NLP", "is", "fun", ".", "Let's", "learn", "!"]`

---

## 🔀 Two Main Types

### 1. Word Tokenization
Splits text into individual words.

| Input | Output |
|---|---|
| `"Cats are great pets"` | `Cats` \| `are` \| `great` \| `pets` |

### 2. Sentence Tokenization
Splits text into individual sentences.

| Input | Sentence 1 | Sentence 2 |
|---|---|---|
| `"I like tea. I like coffee too."` | `I like tea.` | `I like coffee too.` |

---

## ⚠️ Tricky Cases (Why It's Not Always Simple)

| Input | Naive split by space | Correct tokenization |
|---|---|---|
| `"don't"` | `["don't"]` | `["do", "n't"]` |
| `"U.S.A. is big"` | `["U.S.A.", "is", "big"]` | `["U.S.A.", "is", "big"]` (period kept together) |
| `"NLP, ML, and AI"` | `["NLP,", "ML,", "and", "AI"]` | `["NLP", ",", "ML", ",", "and", "AI"]` |

Punctuation, contractions, and abbreviations are why we use libraries like NLTK instead of just `.split()`.

---

## 🛠️ How It Fits in the NLP Pipeline

**Raw Text → Tokenization → Cleaning → Vectorization → Model → Output**

Tokenization always comes **first** — every later step (removing stopwords, stemming, converting to numbers) depends on tokens already being split out.

---

## ✅ Quick Recap

- Tokenization = splitting text into words or sentences
- It's the **first step** of any NLP pipeline
- Naive space-splitting fails on punctuation, contractions, abbreviations
- Libraries like NLTK/spaCy handle these edge cases correctly
