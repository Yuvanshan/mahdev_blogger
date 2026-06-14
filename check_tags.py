from pathlib import Path
import re
text = Path('mahdev.xml').read_text(encoding='utf-8', errors='replace')
# Remove CDATA sections entirely because they contain literal HTML/XML content
text = re.sub(r'<!\[CDATA\[.*?\]\]>', '', text, flags=re.S)
# Remove comments
text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
# Find tags
pattern = re.compile(r'<(/?)([A-Za-z0-9:_-]+)([^>]*)>')
stack = []
errors = []
for i, line in enumerate(text.splitlines(), 1):
    for m in pattern.finditer(line):
        closing = m.group(1) == '/'
        tag = m.group(2)
        rest = m.group(3)
        self = rest.strip().endswith('/') or tag.lower() in ['br','img','input','meta','link','hr','area','base','col','param','source','track','wbr']
        if closing:
            if stack and stack[-1][0] == tag:
                stack.pop()
            else:
                errors.append((i, tag, stack[-1][0] if stack else None, list(stack[-5:])))
        elif not self:
            stack.append((tag, i))
print('errors', len(errors))
for e in errors[:20]:
    print('line', e[0], 'closing', e[1], 'expected', e[2], 'stack', e[3])
print('remaining', len(stack), stack[-20:])
