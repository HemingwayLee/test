from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# translate English to Japan
tokenizer.src_lang = "en_XX"
encoded = tokenizer("Hello, this is a English sentence", return_tensors="pt")
generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id["ja_XX"])

print(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True))

