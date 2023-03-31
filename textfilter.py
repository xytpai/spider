import re


def replace_multiple_newlines(text):
    pattern = r'\n{3,}'
    replacement = '\n\n'
    return re.sub(pattern, replacement, text)


def get_filtered_text(text):
    text = replace_multiple_newlines(text)
    return text
