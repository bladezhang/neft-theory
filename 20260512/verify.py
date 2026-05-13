with open(r'neft_20260511.html','r',encoding='utf-8') as f:
    c = f.read()
print(f'文件大小: {len(c)} 字符')
checks = {
    '旋量Hopf-Cole': '旋量Hopf-Cole' in c,
    'Schwinger-Keldysh CTP证明': 'Schwinger-Keldysh' in c,
    '导航锚点s1_1': 's1_1' in c,
    '实施计划引用8.5': '§8.5' in c,
    '§10已展开(10.1.1)': '10.1.1' in c,
    '局限性已回应': '本文回应' in c,
    '参考文献完整': 'Particle Data Group' in c,
    '附录A存在': 'appendixA' in c,
}
for k,v in checks.items():
    print(f'  {"✅" if v else "❌"} {k}')
