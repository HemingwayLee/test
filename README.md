# Today  

https://jlptstudy.net/N5/

# Subword language model

## Why

### Words on the internet
* Gooooood, Googliness

### Morphology
* [[un [[fortun(e) ]ROOT ate]STEM]STEM ly]WORD

### Compound Noun
* seafood, highschool, boyfriend, ...
* 契約書

### Writing systems (writing systems aren’t one thing)
* Phonemic (maybe digraphs): jiyawu ngabulu
* Fossilized phonemic: thorough failure
* Ideographic (syllabic): https://en.wikipedia.org/wiki/Chinese_characters#/media/File:Evo-elephant.png  
* Combination of the above: インド洋の島

## Model
* purely character level model
  * Accuracy slightly better than word level
    * Good at: translation of people's name, `11-years-old`, ...
      * Translation (Similar spellings share similar embeddings)
        * Anna -> 安娜
        * Andy -> 安迪
        * Andrew -> 安德魯
        * `Anderson` -> `安德森`
        * Derek -> 德里克
        * Jason -> 傑森
    * Good at: deep and complicated model, worse than word level at simple model  
  * Slow at training and predicting (because the length of sequence is longer)
* Subword model (2 models)
  * Same architecture as word level, but smaller (e.g., wordpieces)
    * Byte-pair encoding (from compression area)
      * Start with characters: a, e, i, o, ...
      * Merge most commonest ngram: es, est, lo, ...
      * Stop when we reach pre-defined number of tokens (e.g., 8,000 tokens)
    * Good for multilingual
    * Use finite wordpieces to build infinite words
    * BERT uses variant of wordpieces (2 models)
      * Rather than ngram count, uses a greedy approximation to maximizing language model log likelihood to choose the pieces
      * Whitespace is retained as special token `_` and grouped normally
  * Hybrid architecture: Mix words and characters
    * Translate mostly at the word level
    * Only go to the character level when needed
  * FastText also uses Subword model. (Normal tokenizers (e.g., MeCab, Jumanpp) does not work well with it)

## Ref
https://zhuanlan.zhihu.com/p/53326791  




