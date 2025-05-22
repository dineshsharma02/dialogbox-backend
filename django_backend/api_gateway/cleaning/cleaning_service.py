import re


def clean_query(text: str) -> str:
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    return cleaned