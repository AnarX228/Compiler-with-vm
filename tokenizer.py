import re

def tokenize(text):
    token_patterns = [
        (r'[ \t\n]+', None),
        (r'[0-9]+\.[0-9]+', 'NUMF'),
        (r'[0-9]+', 'NUM'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
        (r'\+', 'ADD'),
        (r'\-', 'SUB'),
        (r'\*', 'MUL'),
        (r'/', 'DIV'),
        (r'\==', 'EQUALS'),
        (r'\=', 'EQUAL'),
        (r'\>', 'GREATER'),
        (r'\<', 'LESS'),
        (r'"([^"\\]*(\\.[^"\\]*)*)"', 'QUOTIONS'),
        (r'\((.*?)\)', 'BRACKETS'),
        (r'\{(.*?)\}', 'FBRACKETS'),
    ]

    master_pattern = '|'.join(f'(?P<{name}>{pattern})' for pattern, name in token_patterns if name is not None)

    tokens = []
    
    for match in re.finditer(master_pattern, text):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type in ['QUOTIONS','BRACKETS','FBRACKETS']:
            token_value = token_value[1:-1]

        if token_type:
            tokens.append((token_type, token_value))
    
    return tokens