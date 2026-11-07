from googletrans import Translator, LANGUAGES

# Ініціалізація об'єкта перекладача
translator = Translator()

def TransLate(str_text: str, lang: str) -> str:
    """
    Функція для перекладу тексту на вказану мову.
    :param str_text: Текстовий рядок для перекладу.
    :param lang: Назва мови (наприклад, 'English') або ISO-639 код (наприклад, 'en').
    :return: Перекладений текст або повідомлення про помилку.
    """
    try:
        lang_clean = lang.strip().lower()
        
        # Перевіряємо: передано код мови (наприклад, 'en') чи назву (наприклад, 'english')
        target_lang = None
        if lang_clean in LANGUAGES:
            target_lang = lang_clean
        else:
            # Шукаємо відповідний ISO-код за назвою мови
            for code, name in LANGUAGES.items():
                if name.lower() == lang_clean:
                    target_lang = code
                    break
        
        if not target_lang:
            return f"Помилка: Мову '{lang}' не знайдено в базі."

        result = translator.translate(str_text, dest=target_lang)
        return result.text
    except Exception as e:
        return f"Помилка під час перекладу: {str(e)}"

def LangDetect(txt: str) -> str:
    """
    Функція для визначення мови тексту та рівня впевненості (confidence).
    :param txt: Текст для аналізу.
    :return: Рядок формату Detected(lang=..., confidence=...).
    """
    try:
        detection = translator.detect(txt)
        return f"Detected(lang={detection.lang}, confidence={detection.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
    """
    Повертає код мови, якщо передано її назву, або назву мови, якщо передано її код.
    :param lang: Код мови або її назва.
    :return: Назва мови або її ISO-код.
    """
    lang_clean = lang.strip().lower()
    
    # Якщо передано код мови (наприклад, 'en') -> повертаємо назву ('English')
    if lang_clean in LANGUAGES:
        return LANGUAGES[lang_clean].capitalize()
    
    # Якщо передано назву мови (наприклад, 'english') -> повертаємо код ('en')
    for code, name in LANGUAGES.items():
        if name.lower() == lang_clean:
            return code
            
    return f"Помилка: Мову або код '{lang}' не знайдено."

# --- Демонстрація роботи програми (згідно із завданням) ---
if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    lang = "en"

    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))

    