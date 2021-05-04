import re

with open('nginx_logs.txt', 'r', encoding='utf=8') as f:
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s[.[]'
                         r'(\d{2}[./]\w+[./]\d{4}[.:]\d{2}[.:]\d{2}[.:]\d{2}\s[.+]\d{4})'
                         r'.\s[."](\w+)\s([./]\w+[./]\w+)\s\w+.\d+\.\d+[."]\s(\d+)\s(\d+)')
    for string in f:
        check = pattern.finditer(string)
        for i in check:
            print(i.group(1, 2, 3, 4, 5, 6))
