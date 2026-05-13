import re
with open(r'C:\Users\Administrator\.openclaw\workspace\neft\20260510\neft_20260511.html','r',encoding='utf-8') as f:
    content = f.read()

# 1. 实施计划
idx = content.find('与以往的纯理论框架不同')
print(f'实施计划位置: {idx}')

# 2. 标量极限残留
for m in re.finditer(r'标量极限|退化为标量|退化.*标量|标量退化|标量投影|简化投影', content):
    start = max(0, m.start()-60)
    end = min(len(content), m.end()+60)
    ctx = content[start:end].replace('\n',' ')
    print(f'标量残留 @{m.start()}: ...{ctx}...')

# 3. 导航链接
nav_matches = list(re.finditer(r'<a href="#sec\d+">', content))
print(f'\n导航链接数: {len(nav_matches)}')
for m in nav_matches[:5]:
    print(f'  {content[m.start():m.end()+100].replace(chr(10)," ")}')

# 4. §10长度
idx10 = content.find('第十章 潜在应用展望')
idxref = content.find('附录A：标量玩具模型')
print(f'\n§10长度: {idxref-idx10} 字符')

# 5. 检查各section的id
ids = re.findall(r'id="([^"]*)"', content)
print(f'\n所有id: {ids}')
