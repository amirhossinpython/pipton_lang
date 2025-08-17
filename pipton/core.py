import re

def preprocess_braces(code):
    # جدا کردن { و } از کدهایی که چسبیده هستند
    code = re.sub(r'([^\s]){', r'\1 {', code)
    code = re.sub(r'{([^\s])', r'{ \1', code)
    code = re.sub(r'([^\s])}', r'\1 }', code)
    code = re.sub(r'}([^\s])', r'} \1', code)
    return code

def translate(code):
    code = preprocess_braces(code)  
    lines = code.split('\n')
    output = []
    indent = 0
    in_multiline_comment = False

    def clean_line(line):
        line = line.replace('entry(', 'input(')
        line = line.replace('true', 'True')
        line = line.replace('false', 'False')
        line = line.replace('null', 'None')
        return line

    block_start_keywords = ('fun ', 'class ', 'if ', 'elif ', 'else', 'while ', 'for ', 'try', 'except', 'finally')

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            output.append('')
            continue

        if stripped.startswith("'''") or stripped.startswith('"""'):
            in_multiline_comment = not in_multiline_comment
            output.append('    ' * indent + stripped)
            continue
        if in_multiline_comment:
            output.append('    ' * indent + stripped)
            continue

        if stripped.startswith('#'):
            output.append('    ' * indent + stripped)
            continue

        if stripped == '}':
            indent -= 1
            if indent < 0:
                raise SyntaxError(f"⛔ unmatched '}}' at line {idx}")
            continue

        if stripped.endswith('{'):
            stmt = stripped[:-1].strip()

            if stmt.startswith('async fun '):
                stmt = 'async def ' + stmt[10:].strip()
            elif stmt.startswith('fun '):
                stmt = 'def ' + stmt[4:].strip()
            elif stmt.startswith('class '):
                stmt = stmt
            elif any(stmt.startswith(kw) for kw in block_start_keywords):
                stmt = stmt
            else:
                stmt = clean_line(stmt)

            output.append('    ' * indent + stmt + ':')
            indent += 1
            continue

        if any(stripped.startswith(kw) for kw in ('if ', 'elif ', 'else', 'try', 'except', 'finally')):
            if not stripped.endswith(':'):
                stripped += ':'
            output.append('    ' * indent + stripped)
            continue

        if stripped.startswith('print>>'):
            content = clean_line(stripped[7:].strip())
            stmt = f'print({content})'

        elif stripped.startswith('var '):
            var_line = stripped[4:].strip()
            if '=' in var_line:
                stmt = clean_line(var_line)
            else:
                stmt = f"{var_line} = None"

        else:
            stmt = clean_line(stripped)

        output.append('    ' * indent + stmt)

    if indent != 0:
        raise SyntaxError("⛔ بلاک‌ها به درستی بسته نشده‌اند")

    return '\n'.join(output)
