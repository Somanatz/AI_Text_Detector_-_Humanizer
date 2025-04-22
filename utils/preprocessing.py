def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9. ]", "", text)
    return text.strip()