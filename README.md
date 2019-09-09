# Today  

https://jlptstudy.net/N5/


# Overview
* It consists of a encoder and a decoder

# Applications
(Abstractive) summarization  

machine translation  
* language pairs http://www.manythings.org/anki/  

chatbot (chit-chat)  

Freeform Question Answering 

Storytelling and poetry-generation

Image captioning

code generation (nature language to python code)  

others (practices)  
* address to zip code
* datetime fomart to standard datetime format

## Decoder is based on Language Model
* Language Model: the task of predicting the next word, given the words so far
![lm](https://user-images.githubusercontent.com/8428372/64489921-2be58b80-d293-11e9-8213-e920708576b3.png)

* Conditional Language Model:  the task of predicting the next word, given the words so far, and also some other input x
![clm](https://user-images.githubusercontent.com/8428372/64489919-2be58b80-d293-11e9-86ab-0191cd0ed26c.png)
  * Machine Translation (x=source sentence, y=target sentence)
  * Summarization (x=input text, y=summarized text)
  * Dialogue (x=dialogue history, y=next utterance)

## Language Model Algorithms
* Greedy
* Beam Search 
![bean_search](https://user-images.githubusercontent.com/8428372/64489917-2b4cf500-d293-11e9-8712-e518db13e966.png)
* Softmax Temperature
![Out-of-Distribution-Examples-Detection](https://user-images.githubusercontent.com/8428372/64489918-2b4cf500-d293-11e9-9157-82f89b089f69.png)


