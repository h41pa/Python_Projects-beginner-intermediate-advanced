from googletrans import Translator


def translate_word(word, language=''):
    translator = Translator()
    translate_ = translator.translate(word, dest=language)
    return translate_.text


def translate():
    while True:
        word_to_translate = input("Enter your word for translate: ")
        if word_to_translate == '':
            print("empty text")
            break
        language = input("Enter the language you want to translate your word: ")
        result = translate_word(word_to_translate, language)
        print(f"Translation for the word '{word_to_translate}' in '{language}' language is : '{result}' ")


translate()
