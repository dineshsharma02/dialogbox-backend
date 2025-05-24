import re


def clean_query(text: str) -> str:
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    return cleaned



def clean_llm_output(text: str):
    text = text.strip()

    # Only strip quotes if the string STARTS AND ENDS with quotes (not mid-sentence)
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
        text = text[1:-1]

    return text