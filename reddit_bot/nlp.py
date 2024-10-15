# nlp.py
from transformers import MarianMTModel, MarianTokenizer

# Load the MarianMT model and tokenizer
def load_model_and_tokenizer(model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Define the supported translation models
LANGUAGE_MODELS = {
    'en_to_fr': 'Helsinki-NLP/opus-mt-en-fr',
    'fr_to_en': 'Helsinki-NLP/opus-mt-fr-en',
    'en_to_es': 'Helsinki-NLP/opus-mt-en-es',
    'es_to_en': 'Helsinki-NLP/opus-mt-es-en',
    # Add more language pairs as needed
}

def translate(text, source_lang='en', target_lang='fr'):
    """
    Translates text from the source language to the target language.
    
    Parameters:
    - text: The text to translate.
    - source_lang: The source language code (e.g., 'en', 'fr').
    - target_lang: The target language code (e.g., 'fr', 'es').
    
    Returns:
    - Translated text.
    """
    
    # Determine the model to use based on source and target languages
    model_key = f"{source_lang}_to_{target_lang}"
    
    if model_key not in LANGUAGE_MODELS:
        raise ValueError(f"Translation from {source_lang} to {target_lang} is not supported.")
    
    model_name = LANGUAGE_MODELS[model_key]
    
    # Load model and tokenizer
    tokenizer, model = load_model_and_tokenizer(model_name)
    
    # Prepare the text for translation
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Perform the translation
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
    
    # Decode the translated tokens
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    
    return translated_text

# Example usage:
# translated = translate("Hello, how are you?", source_lang='en', target_lang='fr')
# print(translated)

