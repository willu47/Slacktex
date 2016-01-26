import re

def textraction(message):
    latex = re.search(r'\$[\S\s]+\$', message['text'], re.MULTILINE)
    latex = latex.group()
    latex = re.sub(r'\\\\', r'\\', latex)
    latex = re.sub(r'\$', '', latex)
    return latex
