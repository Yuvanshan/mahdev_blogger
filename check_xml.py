from pathlib import Path
import xml.etree.ElementTree as ET
path = Path('mahdev.xml')
text = path.read_text(encoding='utf-8', errors='replace')
try:
    ET.fromstring(text)
    print('parsed successfully')
except ET.ParseError as e:
    print('ParseError:', e)
    print('line:', e.position[0], 'column:', e.position[1])
