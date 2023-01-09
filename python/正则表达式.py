import re

pattern = r'[(]p.*[)]'  # 匹配小括号
pattern = r'\d+\.?\d+'  # 匹配小数
text = 'similar deletions (p11.1p21)'
c = re.findall(pattern, text)
for p in c:
    # p = p[1:-1]
    print(p)
