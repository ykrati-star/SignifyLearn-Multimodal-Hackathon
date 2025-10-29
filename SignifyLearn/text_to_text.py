from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

def translate_to_isl(text):
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)

    tokenizer.src_lang = "en_XX"
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
    isl_output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return isl_output

if __name__ == "__main__":
    print(translate_to_isl("How are you?"))
