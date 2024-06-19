from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("Language Codes (ISO 639-1):")
    print("English: en, Spanish: es, French: fr, German: de, Chinese: zh-cn, Japanese: ja, etc.")

    src_lang = input("Enter the source language code: ")
    dest_lang = input("Enter the target language code: ")
    text = input("Enter the text to translate: ")

    translated_text = translate_text(text, src_lang, dest_lang)

    print(f"Translated text: {translated_text}")
