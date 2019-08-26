# Today  

https://jlptstudy.net/N5/


# Why locatization
* For NLP, locatization is almost recreating another system
  * Chinese does not have tense, space in sentence. Malay does not have gender
  * Hieroglyph in Chinese and Egyptian
    * hard to pronounce
    * Japanese is kind of combination of 2 systems
  * Japanese has `けいご`

# Tokenizer
* spaCy does not support Japanese and Chinese
* spaCy can be extended with MeCab or Jieba
  * spaCy is more than tokenizer: NER, QA, w2v, visualization
  * different tokenizers in different language provides different information

# OCR
OCR for Japanese (and Chinese) is harder

* Pre-proc
  * Denoise
  * Remove unrelated things on contracts
  * Rotation
* tesseract
  * retrain tesseract
* Post-proc
  * Base on language model
  * BERT + kanji strokes + kanji similarity

# NER
It can detect more things than regex

* biLSTM
* QA using 
  * spaCy with GINZA
  * BERT

