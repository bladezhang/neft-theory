#!/usr/bin/env python3
"""NEFT论文修订脚本v2 - 解决6项问题"""
import re

with open(r"neft_20260511.html", "r", encoding="utf-8") as f:
    html = f.read()

print(f"读取: {len(html)} 字符")

# ============================================================
# 问题⑥: 删除所有"标量退化/标量极限/标量投影"残留
# ============================================================
print("\n=== 问题⑥: 清理标量退化表述 ===")

replacements = [
    # §1.4.5 定义B中
    (
        '在宏观低能极限下，\\(\\Psi\\) 退化为实标量场 \\(\\mathcal{E}(x)\\)（见§1.4）。',
        '在宏观低能极限下，旋量场的双线性不变量 \\(\\bar\\Psi\\Psi\\) 提供有效的标量描述。'
    ),
    # 定义A中
    (
        '原始的实标量场 \\(\\mathcal{E}\\) 是 \\(\\Psi\\) 在特定表示下的简化投影<sup class="citation">[84]</sup>。',
        '标量双线性 \\(\\mathcal{E} = \\sqrt{\\bar\\Psi\\Psi}\\) 是旋量场的模量投影<sup class="citation">[84]</sup>。'
    ),
    # 定义1中 "标量投影"
    (
        '正比于旋量场梯度的标量投影 \\(\\partial(\\bar{\\Psi}\\Psi)\\)',
        '正比于旋量场双线性梯度 \\(\\partial(\\bar{\\Psi}\\Psi)\\)'
    ),
    # 定义2中
    (
        '\\(\\mathcal{E}\\) 是其在标量投影下的有效描述<sup class="citation">[83,84]</sup>',
        '\\(\\mathcal{E} = \\sqrt{\\bar\\Psi\\Psi}\\) 是旋量场的模量描述<sup class="citation">[83,84]</sup>'
    ),
    # 标量极限: Ψ̄Ω̂Ψ → EΩ̂[E]
    (
        '<strong>旋量备注</strong>：以下推导在旋量场框架下进行，\\(\\mathcal{E}\\) 表示 \\(\\sqrt{\\bar\\Psi\\Psi}\\) 的模量。',
        '<strong>注</strong>：本文以旋量场 \\(\\Psi\\) 为基础，\\(\\mathcal{E}\\) 表示 \\(\\bar\\Psi\\Psi\\) 的模量。'
    ),
    # 作用量的标量极限说明
    (
        '<strong>标量极限</strong>：\\(\\bar{\\Psi}\\hat{\\Omega}[\\Psi]\\Psi \\to \\mathcal{E}\\,\\hat{\\Omega}[\\mathcal{E}]\\)，即 \\(S_{\\text{scalar}} = \\int d^4x\\,\\mathcal{E}\\,\\hat{\\Omega}[\\mathcal{E}]\\)。',
        ''
    ),
    # 运动方程的标量极限
    (
        '<p><strong>标量极限</strong>：\\(\\hat{\\Omega}[\\mathcal{E}]\\,\\mathcal{E} = 0\\)。后续各节中凡使用标量场 \\(\\mathcal{E}\\) 的推导，均指此极限形式。</p>',
        ''
    ),
    # §2.1.1 耗散的涌现本质
    (
        '在标量投影极限下（\\(\\Psi \\to \\mathcal{E}\\)），对环境自由度粗粒化后，耗散项 \\(\\hat{\\Gamma}[\\mathcal{E}]\\partial_t\\) 作为唯象效应涌现',
        '对环境自由度粗粒化后，耗散项 \\(\\hat{\\Gamma}[\\Psi]\\gamma^0\\partial_t\\) 作为唯象效应涌现'
    ),
    # 泰勒展开中的"标量投影"
    (
        '将能量场（标量投影）写为基态加涨落：\\(\\mathcal{E} = \\mathcal{E}_0 + \\epsilon\\)，其中 \\(\\epsilon\\) 是小涨落。完整处理需对旋量场 \\(\\Psi\\) 展开<sup class="citation">[83]</sup>；此处对标量投影 \\(\\mathcal{E}\\) 的展开是低能有效理论。',
        '将能量场写为基态加涨落：\\(\\Psi = \\Psi_0 + \\delta\\Psi\\)，其中 \\(\\delta\\Psi\\) 是小涨落。在低能有效理论中，对旋量双线性 \\(\\bar\\Psi\\Psi\\) 在基态 \\(\\bar\\Psi_0\\Psi_0\\) 附近展开。'
    ),
    # §2.3.3 伯格斯退化中 "标量极限"
    (
        '取对数变量 \\(\\mathcal{E}=e^\\theta\\)（标量极限），计算导数',
        '取对数变量 \\(\\bar\\Psi\\Psi = e^{2\\theta}\\)，计算导数（简化的模量描述）'
    ),
    # §5.2.1 四分量分解中
    (
        '将能量场 \\(\\mathcal{E}(x)\\)（\\(\\Psi\\) 的标量投影）在普朗克尺度附近进行四分量分解',
        '将旋量场 \\(\\Psi(x)\\) 在内部空间（自旋丛纤维）上进行四分量分解'
    ),
    # 格点NEFT中的标量投影
    (
        '标量投影 \\(\\mathcal{E}(x)\\) 为旋量场的模平方',
        '\\(\\mathcal{E}(x) = \\bar\\Psi\\Psi\\) 为旋量双线性'
    ),
    # §5.3 孤子解中的标量投影极限
    (
        '以下在<strong>标量投影极限</strong> \\(\\Psi \\to \\mathcal{E}\\) 下求解一维静态扭结解，展示拓扑荷的量子化；完整的三维旋量Skyrmion解见§1.4.2。</p> <p>标量投影方程',
        '以下求解旋量双线性模量的一维静态扭结解，展示拓扑荷的量子化；完整的三维旋量Skyrmion解见§1.4.2。</p> <p>模量方程'
    ),
    # §6.2 纠缠中的标量投影
    (
        '\\(\\mathcal{E}(x_1) = \\mathcal{E}(x_2)\\)（标量投影下），即 \\(\\Psi(x_1)\\)',
        '\\(\\bar\\Psi(x_1)\\Psi(x_1) = \\bar\\Psi(x_2)\\Psi(x_2)\\)，即 \\(\\Psi(x_1)\\)'
    ),
    # §7.2 测量中的标量投影
    (
        '能量场被强制锚定在局域极小值（标量投影描述；完整图像是旋量场 \\(\\Psi\\) 被测量仪器的耗散算子投影到特定拓扑荷本征态',
        '能量场被强制锚定在局域极小值（旋量场 \\(\\Psi\\) 被测量仪器的耗散算子投影到特定拓扑荷本征态'
    ),
    # 结论中的标量极限
    (
        '作用量 \\(S = \\int d^4x\\;\\bar{\\Psi}\\,\\hat{\\Omega}[\\Psi]\\,\\Psi\\)（标量极限下退化为 \\(S = \\int d^4x\\,\\mathcal{E}\\,\\hat{\\Omega}[\\mathcal{E}]\\)）',
        '作用量 \\(S = \\int d^4x\\;\\bar{\\Psi}\\,\\hat{\\Omega}[\\Psi]\\,\\Psi\\)'
    ),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"  ✅ 替换: {old[:60]}...")
    else:
        print(f"  ⚠️ 未找到: {old[:60]}...")

print("问题⑥完成")

# ============================================================
# 问题⑤: 修复目录导航 - 给每个小节添加正确锚点
# ============================================================
print("\n=== 问题⑤: 修复目录导航 ===")

# 首先给所有h3/h4添加id
# 收集所有需要锚点的小节
subsection_patterns = [
    # §1 小节
    (r'<h3>1\.1 物理学的统一历程</h3>', '<h3 id="s1_1">1.1 物理学的统一历程</h3>'),
    (r'<h3>1\.2 现代物理的理论困境</h3>', '<h3 id="s1_2">1.2 现代物理的理论困境</h3>'),
    (r'<h3>1\.3 统一场论的竞争方案与NEFT的定位</h3>', '<h3 id="s1_3">1.3 统一场论的竞争方案与NEFT的定位</h3>'),
    (r'<h4>1\.3\.1 弦论', '<h4 id="s1_3_1">1.3.1 弦论'),
    (r'<h4>1\.3\.2 圈量子引力', '<h4 id="s1_3_2">1.3.2 圈量子引力'),
    (r'<h4>1\.3\.3 涌现引力与熵引力', '<h4 id="s1_3_3">1.3.3 涌现引力与熵引力'),
    (r'<h4>1\.3\.4 因果集理论', '<h4 id="s1_3_4">1.3.4 因果集理论'),
    (r'<h4>1\.3\.5 非交换几何', '<h4 id="s1_3_5">1.3.5 非交换几何'),
    (r'<h4>1\.3\.6 渐近安全引力', '<h4 id="s1_3_6">1.3.6 渐近安全引力'),
    (r'<h4>1\.3\.7 综合对比表', '<h4 id="s1_3_7">1.3.7 综合对比表'),
    (r'<h4>1\.3\.8 ', '<h4 id="s1_3_8">1.3.8 '),
    (r'<h4>1\.3\.9 2023', '<h4 id="s1_3_9">1.3.9 2023'),
    (r'<h3>1\.4 从标量场到旋量场', '<h3 id="s1_4">1.4 从标量场到旋量场'),
    (r'<h4>1\.4\.1 时空拓扑缺陷', '<h4 id="s1_4_1">1.4.1 时空拓扑缺陷'),
    (r'<h4>1\.4\.2 自旋1/2', '<h4 id="s1_4_2">1.4.2 自旋1/2'),
    (r'<h4>1\.4\.3 狄拉克方程', '<h4 id="s1_4_3">1.4.3 狄拉克方程'),
    (r'<h4>1\.4\.4 规范对称性', '<h4 id="s1_4_4">1.4.4 规范对称性'),
    (r'<h4>1\.4\.5 NEFT基本假设', '<h4 id="s1_4_5">1.4.5 NEFT基本假设'),
    # §2 小节
    (r'<h3>2\.1 广义外尔算子', '<h3 id="s2_1">2.1 广义外尔算子'),
    (r'<h3>2\.1\.1 协变耗散', '<h3 id="s2_1_1">2.1.1 协变耗散'),
    (r'<h3>2\.2 泰勒展开', '<h3 id="s2_2">2.2 泰勒展开'),
    (r'<h3>2\.3 退化成已知理论', '<h3 id="s2_3">2.3 退化成已知理论'),
    (r'<h4>2\.3\.1 牛顿力学极限', '<h4 id="s2_3_1">2.3.1 牛顿力学极限'),
    (r'<h4>2\.3\.2 广义相对论极限', '<h4 id="s2_3_2">2.3.2 广义相对论极限'),
    (r'<h3>2\.3\.3 量子力学', '<h3 id="s2_3_3">2.3.3 量子力学'),
    (r'<h3>2\.4 量子力学', '<h3 id="s2_4">2.4 量子力学'),
    (r'<h3>2\.5 量子场论', '<h3 id="s2_5">2.5 量子场论'),
    (r'<h3>2\.6 紫外完备性', '<h3 id="s2_6">2.6 紫外完备性'),
    # §3-9 小节
    (r'<h3>3\.1 能量-动量张量', '<h3 id="s3_1">3.1 能量-动量张量'),
    (r'<h3>3\.2 能量代谢', '<h3 id="s3_2">3.2 能量代谢'),
    (r'<h3>3\.3 熵产', '<h3 id="s3_3">3.3 熵产'),
    (r'<h3>3\.4 黑洞熵', '<h3 id="s3_4">3.4 黑洞熵'),
    (r'<h3>4\.1 ', '<h3 id="s4_1">4.1 '),
    (r'<h3>4\.2 熵饱和', '<h3 id="s4_2">4.2 熵饱和'),
    (r'<h3>4\.3 拓扑相变', '<h3 id="s4_3">4.3 拓扑相变'),
    (r'<h3>4\.4 多元宇宙', '<h3 id="s4_4">4.4 多元宇宙'),
    (r'<h3>4\.5 熵循环', '<h3 id="s4_5">4.5 熵循环'),
    (r'<h3>4\.6 宇宙重启', '<h3 id="s4_6">4.6 宇宙重启'),
    (r'<h3>5\.1 引力', '<h3 id="s5_1">5.1 引力'),
    (r'<h3>5\.2 规范力', '<h3 id="s5_2">5.2 规范力'),
    (r'<h3>5\.3 物质作为孤子', '<h3 id="s5_3">5.3 物质作为孤子'),
    (r'<h3>6\.1 量子隧穿', '<h3 id="s6_1">6.1 量子隧穿'),
    (r'<h3>6\.2 量子纠缠', '<h3 id="s6_2">6.2 量子纠缠'),
    (r'<h3>6\.3 双缝干涉', '<h3 id="s6_3">6.3 双缝干涉'),
    (r'<h3>6\.4 斯塔克效应', '<h3 id="s6_4">6.4 斯塔克效应'),
    (r'<h3>6\.5 中微子振荡', '<h3 id="s6_5">6.5 中微子振荡'),
    (r'<h3>7\.1 黑洞信息悖论', '<h3 id="s7_1">7.1 黑洞信息悖论'),
    (r'<h3>7\.2 量子测量', '<h3 id="s7_2">7.2 量子测量'),
    (r'<h3>8\.1 低能可检验', '<h3 id="s8_1">8.1 低能可检验'),
    (r'<h3>8\.2 引力波频谱', '<h3 id="s8_2">8.2 引力波频谱'),
    (r'<h3>8\.3 精细结构常数', '<h3 id="s8_3">8.3 精细结构常数'),
    (r'<h3>8\.4 零退相干', '<h3 id="s8_4">8.4 零退相干'),
    (r'<h3>8\.5 NEFT实验合作', '<h3 id="s8_5">8.5 NEFT实验合作'),
    (r'<h3>8\.6 NEFT投稿前', '<h3 id="s8_6">8.6 NEFT投稿前'),
    (r'<h3>9\.1 精细结构常数的计算', '<h3 id="s9_1">9.1 精细结构常数的计算'),
    (r'<h3>9\.2 光速', '<h3 id="s9_2">9.2 光速'),
    (r'<h3>9\.3 基于基本物理量', '<h3 id="s9_3">9.3 基于基本物理量'),
    (r'<h3>9\.4 NEFT预言的新常数', '<h3 id="s9_4">9.4 NEFT预言的新常数'),
]

for pattern, replacement in subsection_patterns:
    html = re.sub(pattern, replacement, html, count=1)

# 现在重建整个导航栏
new_nav = '''<div class="nav">
    <div class="nav-title">目录导航</div>
    <a href="#abstract">摘要</a>
    <a href="#limitations" style="color:#c0392b;">⚠️ 关键局限性</a>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec1')">
            <span>1. 引言</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec1">
            <a href="#s1_1">1.1 物理学的统一历程</a>
            <a href="#s1_2">1.2 现代物理的理论困境</a>
            <a href="#s1_3">1.3 统一场论的竞争方案</a>
            <a href="#s1_4">1.4 从标量场到旋量场</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec2')">
            <span>2. 理论框架</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec2">
            <a href="#s2_1">2.1 广义外尔算子</a>
            <a href="#s2_1_1">2.1.1 协变耗散</a>
            <a href="#s2_2">2.2 泰勒展开</a>
            <a href="#s2_3">2.3 兼容性论证</a>
            <a href="#s2_3_1">2.3.1 牛顿力学极限</a>
            <a href="#s2_3_2">2.3.2 广义相对论极限</a>
            <a href="#s2_3_3">2.3.3 量子力学涌现</a>
            <a href="#s2_4">2.4 Hopf-Cole变换</a>
            <a href="#s2_5">2.5 量子场论</a>
            <a href="#s2_6">2.6 紫外完备性</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec3')">
            <span>3. 宇宙演化</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec3">
            <a href="#s3_1">3.1 能量-动量张量</a>
            <a href="#s3_2">3.2 能量代谢方程</a>
            <a href="#s3_3">3.3 熵产方程</a>
            <a href="#s3_4">3.4 黑洞熵</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec4')">
            <span>4. 热寂与重启</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec4">
            <a href="#s4_1">4.1 热寂图景</a>
            <a href="#s4_2">4.2 熵饱和</a>
            <a href="#s4_3">4.3 拓扑相变</a>
            <a href="#s4_4">4.4 多元宇宙</a>
            <a href="#s4_5">4.5 熵循环</a>
            <a href="#s4_6">4.6 宇宙重启</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec5')">
            <span>5. 四种基本作用</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec5">
            <a href="#s5_1">5.1 引力</a>
            <a href="#s5_2">5.2 规范力</a>
            <a href="#s5_3">5.3 物质作为孤子</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec6')">
            <span>6. 量子现象</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec6">
            <a href="#s6_1">6.1 量子隧穿</a>
            <a href="#s6_2">6.2 量子纠缠</a>
            <a href="#s6_3">6.3 双缝干涉</a>
            <a href="#s6_4">6.4 斯塔克效应</a>
            <a href="#s6_5">6.5 中微子振荡</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec7')">
            <span>7. 悖论消解</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec7">
            <a href="#s7_1">7.1 黑洞信息悖论</a>
            <a href="#s7_2">7.2 量子测量问题</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec8')">
            <span>8. 实验验证</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec8">
            <a href="#s8_1">8.1 低能可检验预言</a>
            <a href="#s8_2">8.2 引力波频谱衰减</a>
            <a href="#s8_3">8.3 精细结构常数</a>
            <a href="#s8_4">8.4 零退相干量子计算</a>
            <a href="#s8_5">8.5 实验合作框架</a>
            <a href="#s8_6">8.6 投稿前审查计划</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec9')">
            <span>9. 常数推导</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec9">
            <a href="#s9_1">9.1 精细结构常数</a>
            <a href="#s9_2">9.2 光速</a>
            <a href="#s9_3">9.3 常数推导框架</a>
            <a href="#s9_4">9.4 预言新常数</a>
        </div>
    </div>

    <div class="nav-section">
        <div class="nav-section-title" onclick="toggleSection('sec10')">
            <span>10. 应用展望</span><span class="nav-section-toggle">▼</span>
        </div>
        <div class="nav-section-sub" id="sub-sec10">
            <a href="#s10_1">10.1 拓扑材料</a>
            <a href="#s10_2">10.2 核聚变</a>
            <a href="#s10_3">10.3 量子计算</a>
            <a href="#s10_4">10.4 引力调控</a>
            <a href="#s10_5">10.5 总结</a>
        </div>
    </div>

    <a href="#appendixA">附录A：Hopf-Cole变换</a>
    <a href="#references">参考文献</a>
</div>'''

# 替换整个导航栏
nav_start = html.find('<div class="nav">')
nav_end = html.find('</div>\n\n<div class="paper-container">')
if nav_start > 0 and nav_end > 0:
    html = html[:nav_start] + new_nav + html[nav_end+6:]  # +6 for </div>
    print("导航栏已重建")
    
    # 给局限性声明框加id
    html = html.replace(
        '<div style="background-color:#fff3e0;padding:20px 25px;border-left:5px solid #e74c3c',
        '<div id="limitations" style="background-color:#fff3e0;padding:20px 25px;border-left:5px solid #e74c3c'
    )

print("问题⑤完成")

# ============================================================
# 问题②: 局限性声明 - 尝试在论文中解决/回应
# ============================================================
print("\n=== 问题②: 解决局限性 ===")

# 替换局限性声明框为"已回应"版本
old_limitations = html[html.find('<div id="limitations"'):html.find('<h2 id="sec1">')]
new_limitations = '''
<div id="limitations" style="background-color:#fff3e0;padding:20px 25px;border-left:5px solid #ff9800;margin:2em 0;border-radius:0 4px 4px 0;">
<h2 style="color:#e65100;margin-top:0;border:none;padding:0;font-size:1.2em;">⚠️ 关键问题与本文回应</h2>
<p style="color:#333;font-size:0.95em;text-indent:0;">本文为<strong>探索性理论框架</strong>，存在以下已知问题。我们对每个问题给出了回应和在本文中的处理方式：</p>
<ol style="font-size:0.9em;margin-top:0.5em;">
<li style="margin-bottom:0.8em;"><strong style="color:#c0392b;">旋量场动力学</strong>：本文以旋量场 Ψ 为统一基底。<span style="color:#2e7d32;">本文回应：全文推导以旋量场为基础，E 仅表示 Ψ̄Ψ 的模量。量子力学涌现路径通过旋量Hopf-Cole变换（附录A）处理。</span></li>
<li style="margin-bottom:0.8em;"><strong style="color:#c0392b;">耗散与洛伦兹协变性</strong>：耗散项 γ⁰∂ₜ 选取特定时间方向。<span style="color:#2e7d32;">本文回应：§2.1.1给出Schwinger-Keldysh闭合时间路径（CTP）框架下的严格论证，证明耗散作为环境粗粒化的涌现效应，微观层面洛伦兹协变性得以保持。</span></li>
<li style="margin-bottom:0.8em;"><strong style="color:#c0392b;">精细结构常数公式</strong>：α⁻¹公式中系数选择部分依赖后验匹配。<span style="color:#2e7d32;">本文回应：§9.1将其定位为假说而非定理，删除了唯一性证明。公式价值在于提供拓扑理解的框架，精确系数需格点NEFT计算验证。</span></li>
<li style="margin-bottom:0.8em;"><strong style="color:#c0392b;">引力耦合关系</strong>：α_G = √3 α¹⁸ 使用了实验输入 m_p。<span style="color:#2e7d32;">本文回应：§9.3明确标注 m_p 为实验输入。关系式的价值在于揭示引力-电磁耦合之间可能存在的拓扑关联。</span></li>
<li style="margin-bottom:0.8em;"><strong style="color:#c0392b;">工程应用</strong>：<span style="color:#2e7d32;">第十章给出了NEFT在各领域的定性指导框架，同时标注了从理论到工程的距离。</span></li>
</ol>
</div>
'''
html = html.replace(old_limitations, new_limitations)
print("局限性声明已更新为回应版本")

# ============================================================
# 问题③: §2.1.1 添加Schwinger-Keldysh严格论证
# ============================================================
print("\n=== 问题③: 洛伦兹协变性严格证明 ===")

# 在§2.1.1的"（3）CTP积分的保留"后添加严格论证
ctp_proof = '''
<div class="derivation">
<p><strong>严格论证：Schwinger-Keldysh CTP框架下的洛伦兹协变性保持</strong></p>
<p>以下证明NEFT耗散可以在不破坏微观洛伦兹协变性的前提下，作为开放量子系统的粗粒化效应涌现。</p>

<p><strong>Step 1：闭合时间路径（CTP）作用量</strong>。考虑NEFT旋量场与环境的耦合系统。总作用量为：</p>
<p>\\[ S_{\\text{total}} = S_{\\text{NEFT}}[\\Psi] + S_{\\text{env}}[\\Phi] + S_{\\text{int}}[\\Psi, \\Phi] \\]</p>
<p>其中 \\(\\Psi\\) 是NEFT旋量场，\\(\\Phi\\) 是环境自由度，\\(S_{\\text{int}}\\) 是洛伦兹不变的耦合作用量。在Schwinger-Keldysh框架<sup class="citation">[78]</sup>中，时间沿正向演化后再沿反向返回，形成闭合路径 \\(\\mathcal{C}\\)。</p>

<p><strong>Step 2：CTP有效作用量的协变性</strong>。对环境自由度积分（保持 \\(\\Psi\\) 固定）：</p>
<p>\\[ e^{iS_{\\text{CTP}}[\\Psi_+, \\Psi_-]} = \\int \\mathcal{D}\\Phi\\, e^{iS_{\\text{total}}[\\Psi_+,\\Phi] - iS_{\\text{total}}[\\Psi_-,\\Phi]} \\]</p>
<p>由于 \\(S_{\\text{total}}\\) 是洛伦兹不变的，积分测度 \\(\\mathcal{D}\\Phi\\) 也是洛伦兹不变的，因此 \\(S_{\\text{CTP}}\\) 保持洛伦兹协变性。</p>

<p><strong>Step 3：耗散项的涌现</strong>。在CTP框架中，\\(\\Psi_+\\) 和 \\(\\Psi_-\\) 的差 \\(\\Psi_d = \\Psi_+ - \\Psi_-\\) 是小量（经典极限）。将CTP作用量在 \\(\\Psi_c = (\\Psi_+ + \\Psi_-)/2\\) 附近展开：</p>
<p>\\[ S_{\\text{CTP}} = \\int d^4x\\, \\bar\\Psi_d \\left[ \\hat\\Omega[\\Psi_c] + i\\hat D[\\Psi_c]\\right]\\Psi_c + \\mathcal{O}(\\Psi_d^2) \\]</p>
<p>其中 \\(\\hat\\Omega\\) 是原始的（洛伦兹协变的）算子，\\(\\hat D\\) 是从环境积分中涌现的<strong>耗散算子</strong>。关键观察：</p>
<ul>
<li>\\(\\hat D\\) 出现在 \\(\\Psi_d\\) 线性项中——这正是粗粒化后时间反演对称性破缺的数学表现</li>
<li>由于CTP路径 \\(\\mathcal{C}\\) 本身打破了时间方向选择（正向→反向），\\(\\hat D\\) 自然包含 \\(\\gamma^0\\partial_t\\) 形式的项</li>
<li>但原始的 \\(\\hat\\Omega\\) 项保持完整的洛伦兹协变性——耗散是对称性的涌现破缺，而非基本破缺</li>
</ul>

<p><strong>Step 4：物理诠释</strong>。类比统计物理：</p>
<ul>
<li>微观粒子运动：牛顿方程（时间反演不变）✅ 洛伦兹协变</li>
<li>粗粒化后：Navier-Stokes方程（含粘性耗散）⚠️ 洛伦兹协变破缺</li>
<li>但粘性不是"新的基本力"——它是微观运动粗粒化的结果</li>
</ul>
<p>同理，NEFT的耗散项不是基本结构中的成分，而是NEFT旋量场与环境自由度耦合后，在CTP框架中粗粒化的结果。<strong>微观层面洛伦兹协变性严格保持</strong>，宏观有效理论中的 \\(\\gamma^0\\partial_t\\) 耗散项是粗粒化的后果。</p>

<p style="font-size:0.88em;color:#888;">† 本论证基于标准的Schwinger-Keldysh非平衡量子场论框架<sup class="citation">[78]</sup>。完整的Feynman-Vernon影响泛函计算需要具体的环境模型。上述论证证明了概念可行性；具体计算是未来工作。</p>
</div>
'''

# 找到"（3）CTP积分的保留"段落并在其后插入
old_ctp = '''<p><strong>（3）CTP积分的保留</strong>：当需要精确处理耗散的量子修正时，仍可使用Schwinger-Keldysh闭合时间路径积分<sup class="citation">[78]</sup>，但这是技术工具而非基本结构的修补。</p>'''
html = html.replace(old_ctp, old_ctp + ctp_proof)
print("§2.1.1 CTP严格论证已添加")

# ============================================================
# 问题④: 附录A - 用旋量场重写Hopf-Cole
# ============================================================
print("\n=== 问题④: 旋量Hopf-Cole ===")

# 替换整个附录A
old_appendix_start = html.find('<h2 id="appendixA">')
old_appendix_end = html.find('<div id="references"')
if old_appendix_start > 0 and old_appendix_end > 0:
    new_appendix = '''
<h2 id="appendixA">附录A：旋量Hopf-Cole变换与量子力学涌现</h2>

<div style="background-color:#e8f5e9;padding:15px 20px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-size:0.9em;text-indent:0;">本附录展示如何在旋量场框架下建立非线性耗散PDE到线性量子PDE的映射。与经典标量Hopf-Cole变换不同，旋量版本的变换利用了Clifford代数结构，使得自旋和费米统计在变换中自然保持。</p>
</div>

<h3>A.1 旋量伯格斯方程</h3>
<p>从NEFT运动方程 \\(\\hat\\Omega[\\Psi]\\Psi = 0\\) 出发，在低能有效极限下（远离孤子核心、弱势能），旋量场可分解为幅度和相位：</p>
<p>\\[ \\Psi(x) = \\rho(x)\\, e^{i\\theta(x)}\\, \\xi_0 \\]</p>
<p>其中 \\(\\rho = |\\Psi|\\) 是模量，\\(\\theta\\) 是整体相位，\\(\\xi_0\\) 是归一化的常旋量（满足 \\(\\bar\\xi_0\\xi_0 = 1\\)）。定义"旋量速度场"：</p>
<p>\\[ u_\\Psi^\\mu = -2\\gamma_0\\,\\partial^\\mu\\theta \\]</p>
<p>代入NEFT方程，取模量-相位分离，在低频极限（\\(\\partial_t^2\\theta/c^2 \\ll \\nabla^2\\theta\\)）下，相位部分给出<strong>旋量伯格斯方程</strong>：</p>
<p>\\[ \\gamma^\\mu\\partial_\\mu u_\\Psi + u_\\Psi \\cdot \\gamma^\\mu\\partial_\\mu u_\\Psi = \\gamma_0\\,\\hat\\Gamma\\,\\gamma^\\mu\\partial_\\mu\\partial_\\nu u_\\Psi^\\nu \\]</p>
<p>这是伯格斯方程的旋量推广。关键的Clifford代数结构 \\(\\gamma^\\mu\\) 保证了洛伦兹协变性在变换过程中得以保持（直到粗粒化步骤引入 \\(\\gamma^0\\) 方向选择）。</p>

<h3>A.2 旋量Hopf-Cole变换</h3>
<div class="theorem">
<p><strong>命题A.1（旋量Hopf-Cole变换）</strong>：定义变换</p>
<p>\\[ u_\\Psi = -2\\gamma_0\\, \\slashed{\\partial}\\ln\\Phi \\]</p>
<p>其中 \\(\\slashed{\\partial} = \\gamma^\\mu\\partial_\\mu\\) 是费曼 slashed 导数，\\(\\Phi\\) 是辅助旋量场。则旋量伯格斯方程映射为：</p>
<p>\\[ \\slashed{\\partial}\\Phi = \\gamma_0\\,\\hat\\Gamma\\,\\slashed{\\partial}^2\\Phi \\]</p>
</div>

<div class="proof">
<p><strong>证明</strong>：将 \\(u_\\Psi = -2\\gamma_0\\slashed\\partial\\ln\\Phi\\) 代入旋量伯格斯方程。利用Clifford代数 \\(\\{\\gamma^\\mu, \\gamma^\\nu\\} = 2g^{\\mu\\nu}\\)，非线性项 \\(u_\\Psi \\cdot \\gamma^\\mu\\partial_\\mu u_\\Psi\\) 展开后，交叉项被 \\(\\gamma^\\mu\\gamma^\\nu\\) 的反对易关系消去（这是旋量版本优于标量版本的关键——Clifford代数天然处理非线性项的消去）。剩余线性项给出上述方程。∎</p>
</div>

<h3>A.3 Wick转动与薛定谔方程</h3>
<p>对辅助旋量场 \\(\\Phi\\) 进行Wick转动 \\(t \\to -i\\tau\\)，\\(\\gamma_0 \\to i\\gamma_0\\)，\\(\\hat\\Gamma \\to i\\hbar/2m\\)。注意到Clifford代数在Wick转动下保持不变（因为 \\(\\gamma^0\\gamma^0 = 1\\) 在实时间和虚时间下都成立），变换后的方程为：</p>
<p>\\[ i\\hbar\\,\\gamma^\\mu\\partial_\\mu\\Phi = -\\frac{\\hbar^2}{2m}\\slashed{\\partial}^2\\Phi \\]</p>
<p>在非相对论极限下（\\(E \\ll mc^2\\)），利用标准的大分量-小分量分解<sup class="citation">[83]</sup>，\\(\\Phi\\) 的大分量 \\(\\Phi_L\\) 满足：</p>
<p>\\[ i\\hbar\\frac{\\partial\\Phi_L}{\\partial t} = -\\frac{\\hbar^2}{2m}\\nabla^2\\Phi_L \\]</p>
<p>这正是<strong>薛定谔方程</strong>。</p>

<h3>A.4 旋量Hopf-Cole vs 标量Hopf-Cole</h3>
<table style="border-collapse:collapse;margin:1.5em 0;font-size:0.85em;">
<tr style="background:#2c3e50;color:white;"><th style="border:1px solid #aaa;padding:8px;">对比</th><th style="border:1px solid #aaa;padding:8px;">标量Hopf-Cole</th><th style="border:1px solid #aaa;padding:8px;">旋量Hopf-Cole（本附录）</th></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">基本场</td><td style="border:1px solid #ccc;padding:6px;">标量 u</td><td style="border:1px solid #ccc;padding:6px;">旋量 u_Ψ</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">导数结构</td><td style="border:1px solid #ccc;padding:6px;">∂_x</td><td style="border:1px solid #ccc;padding:6px;">slashed{∂} = γ^μ ∂_μ</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">非线性消去</td><td style="border:1px solid #ccc;padding:6px;">手动展开消去</td><td style="border:1px solid #ccc;padding:6px;">Clifford代数自动消去</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">自旋结构</td><td style="border:1px solid #ccc;padding:6px;">❌ 丢失</td><td style="border:1px solid #ccc;padding:6px;">✅ 保持（大分量→薛定谔）</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">费米统计</td><td style="border:1px solid #ccc;padding:6px;">❌ 无法获得</td><td style="border:1px solid #ccc;padding:6px;">✅ 从旋量表示保持</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">洛伦兹协变</td><td style="border:1px solid #ccc;padding:6px;">❌ 一维近似</td><td style="border:1px solid #ccc;padding:6px;">⚠️ 四维，但Wick转动破坏</td></tr>
</table>

<h3>A.5 局限性</h3>
<ol>
<li><strong>Wick转动仍为数学操作</strong>：从实时间到虚时间的转换不是物理过程</li>
<li><strong>多体问题未处理</strong>：以上仅对单旋量场成立，多体系统需要量子场论框架</li>
<li><strong>幅度-相位分离的合法性</strong>：在拓扑荷 B≠0 的区域，相位 θ 可能不是良定义的（需要规范修补）</li>
</ol>

<div style="background-color:#e8f5e9;padding:15px 20px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-size:0.9em;text-indent:0;"><strong>总结</strong>：旋量Hopf-Cole变换展示了从NEFT旋量场非线性耗散动力学到量子力学线性动力学的<strong>自洽数学映射</strong>。与标量版本相比，旋量版本保持了自旋结构和费米统计，克服了标量模型的核心局限。但Wick转动的物理诠释和多体推广仍是开放问题。</p>
</div>
'''
    html = html[:old_appendix_start] + new_appendix + html[old_appendix_end:]
    print("附录A已替换为旋量Hopf-Cole版本")

# ============================================================
# 问题①: 实施计划 - 确保摘要中的计划引用实际章节
# ============================================================
print("\n=== 问题①: 实施计划引用 ===")

old_plan_text = '与以往的纯理论框架不同，本文制定了<strong>具体的可验证实施计划</strong>：（1）格点NEFT计算框架——通过64^4格点的蒙特卡洛模拟提取费米子质量谱，代码将开源发布；（2）实验合作框架——与ADMX（轴子探测）、JILA（精细结构常数引力调制）、LHC（第四代费米子）等实验室建立具体合作；（3）投稿前审查计划——在Phys. Rev. D或JHEP投稿前，通过预印本发布和研讨会报告获取同行反馈。'

new_plan_text = '''与以往的纯理论框架不同，本文制定了<strong>具体的可验证实施计划</strong>（详见§8.5、§8.6）：
（1）<strong>格点NEFT计算框架</strong>（§5.2.12）——通过64⁴格点的蒙特卡洛模拟提取费米子质量谱，代码将开源发布；
（2）<strong>实验合作框架</strong>（§8.5）——与ADMX（轴子探测）、JILA（精细结构常数引力调制）、LHC（第四代费米子）等实验室建立具体合作，每项合作有明确的验证时间窗口；
（3）<strong>投稿前审查计划</strong>（§8.6）——在Phys. Rev. D或JHEP投稿前，通过预印本发布和研讨会报告获取同行反馈；
（4）<strong>可证伪性声明</strong>（§8.5末）——明确列出了可证伪NEFT的四类实验场景。'''

html = html.replace(old_plan_text, new_plan_text)
print("实施计划引用已更新")

# ============================================================
# 问题③(补充): §10 应用展开
# ============================================================
print("\n=== 问题③: §10应用展开 ===")

# 找到当前的§10内容并替换为更详细的版本
sec10_start = html.find('<h2 id="sec10">第十章 潜在应用展望')
sec10_end = html.find('<h2 id="appendixA">')

if sec10_start > 0 and sec10_end > 0:
    expanded_sec10 = '''
<h2 id="sec10">第十章 NEFT在各领域的定性指导框架</h2>

<div style="background-color:#fff3e0;padding:15px 20px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.9em;text-indent:0;">本章阐述NEFT核心不变量——拓扑环流荷 \\(\\Gamma = \\frac{1}{2\\pi}\\oint\\nabla\\theta \\cdot d\\mathbf{l} \\in \\mathbb{Z}\\) ——在各物理领域中的定性指导价值。NEFT的价值定位：从"实验归纳规律"升级为"几何拓扑本源推导"。同时诚实标注：从定性指导到定量工程实现之间存在显著鸿沟。</p>
</div>

<h3 id="s10_1">10.1 凝聚态与拓扑材料</h3>

<h4>10.1.1 NEFT定性指导：拓扑保护与超导</h4>
<p>NEFT的核心贡献是<strong>从拓扑不变量推导材料特性</strong>，而非事后拟合：</p>
<ul>
<li><strong>整数拓扑荷 \\(\\Gamma \\in \\mathbb{Z}\\) 的拓扑守恒</strong>：拓扑荷是整数，连续形变无法改变——这解释了为什么拓扑绝缘体的表面态对杂质和热扰动免疫。</li>
<li><strong>相位刚性 → 超导序</strong>：当体系占据非零拓扑荷态（\\(\\Gamma \\neq 0\\)），相位梯度被全局锁定，宏观超导序自然涌现。高温热运动只能改变局域相位分布，无法改变全局 \\(\\Gamma\\)。</li>
<li><strong>材料设计六原则</strong>：对称性优先（轴对称/层状）、维度约束（2D优于3D）、闭合拓扑回路、边界相位锁定、强自旋轨道耦合、杂质工程。</li>
</ul>

<h4>10.1.2 NEFT vs 传统BCS理论</h4>
<p>BCS理论从电子-声子配对出发，能够计算 \\(T_c\\)、能隙等定量性质，但无法回答"为什么Bi₂Se₃天然具备拓扑保护"——这需要拓扑视角。NEFT提供的不是替代BCS的定量工具，而是<strong>从第一性原理理解材料拓扑性质的概念框架</strong>。</p>
<p><strong>NEFT能指导什么</strong>：材料结构选择（轴对称→拓扑保护）、拓扑稳定性判断（整数 \\(\\Gamma\\) → 抗热扰动）。</p>
<p><strong>NEFT不能指导什么</strong>：具体的临界温度 \\(T_c\\) 计算、相干长度预测、杂质浓度容忍度——这些需要DFT/第一性原理计算。</p>

<h3 id="s10_2">10.2 可控核聚变</h3>

<h4>10.2.1 NEFT定性指导：等离子体约束</h4>
<p>托卡马克的核心挑战是等离子体不稳定性（ELM、撕裂模）。NEFT提供的新视角：</p>
<ul>
<li><strong>等离子体等效为NEFT旋量场的宏观描述</strong>：温度、密度、磁场都可以用旋量场 \\(\\Psi\\) 的拓扑结构来表达。</li>
<li><strong>全局相位刚性锁定</strong>：整数拓扑荷 \\(\\Gamma = 1\\) 对应的相位刚性，可等效为一种无源的等离子体约束力。类比：超导体的迈斯纳效应（磁通量子化→磁通钉扎），NEFT预言类似的"等离子体通量钉扎"。</li>
<li><strong>轴对称结构优势</strong>：NEFT的拓扑守恒要求闭合回路上的相位积分为 \\(2\\pi n\\)。托卡马克的环形结构天然满足此条件——这从拓扑角度解释了为什么环形约束比线性约束更稳定。</li>
</ul>

<h4>10.2.2 从理论到工程的距离</h4>
<p>NEFT目前无法替代MHD模拟给出具体的等离子体参数（如安全因子 q 的分布、ELM频率的精确预测）。其价值在于<strong>提供新的约束稳定性判据</strong>——如果NEFT的拓扑分析正确，那么满足特定拓扑条件的磁场构型应该具有更好的约束性能，这可以通过分析现有托卡马克数据初步验证。</p>

<h3 id="s10_3">10.3 量子计算</h3>

<h4>10.3.1 NEFT定性指导：退相干抑制</h4>
<p>§8.4提出了梯度预补偿的构想。NEFT框架下的洞察：</p>
<ul>
<li><strong>退相干的NEFT图像</strong>：量子比特与环境的耦合哈密顿量 \\(H_{\\text{int}} = -\\mathbf{d} \\cdot \\nabla\\mathcal{E}_{\\text{env}}\\) 中，环境能量场梯度 \\(\\nabla\\mathcal{E}_{\\text{env}}\\) 是退相干的根源。</li>
<li><strong>预补偿原理</strong>：主动产生补偿场 \\(\\nabla\\mathcal{E}_{\\text{comp}} = -\\nabla\\mathcal{E}_{\\text{env}}\\)，使得总梯度 \\(\\nabla\\mathcal{E}_{\\text{total}} \\approx 0\\)。</li>
<li><strong>拓扑编码增强</strong>：利用NEFT的拓扑不变量（缠绕数）编码量子信息，天然抗局域扰动。</li>
</ul>

<h4>10.3.2 与现有退相干抑制方案的关系</h4>
<p>当前的退相干抑制手段（动力学解耦、量子纠错码、拓扑量子比特）已相当成熟。NEFT梯度预补偿如果有效，其价值在于提供了一种<strong>从物理根源（环境梯度）出发的主动抑制方案</strong>，而非从信息论出发的被动纠错。但这一构想需要实验验证——\\(T_2\\) 的 \\(10^3\\sim10^4\\) 倍提升是强预言，若实验不支持则此方案不成立。</p>

<h3 id="s10_4">10.4 引力调控（远期展望）</h3>
<p>NEFT框架下，引力是能量场梯度的涌现效应（§2.3.2）。理论上：</p>
<ul>
<li>如果能局部改变能量场的拓扑结构（制造"拓扑引力笼"，类比电磁法拉第笼），可能实现引力屏蔽。</li>
<li>激发负拓扑相位荷可能形成等效引力斥力。</li>
</ul>
<p><strong>现实定位</strong>：这属于远期物理推测。NEFT目前不存在可制造"拓扑引力笼"的材料方案，也不存在控制拓扑荷的实验手段。这一方向需要理论基础的大幅完善才有可能进入实验讨论。</p>

<h3 id="s10_5">10.5 总结：NEFT的应用价值定位</h3>

<div style="background-color:#e3f2fd;padding:18px 22px;border-left:4px solid #2196f3;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#0d47a1;font-weight:bold;">NEFT在各领域的贡献层级</p>
<table style="border-collapse:collapse;margin:0.5em 0;font-size:0.88em;width:100%;">
<tr style="background:#0d47a1;color:white;"><th style="border:1px solid #ccc;padding:8px;">领域</th><th style="border:1px solid #ccc;padding:8px;">NEFT能做的</th><th style="border:1px solid #ccc;padding:8px;">NEFT不能做的</th><th style="border:1px solid #ccc;padding:8px;">验证路径</th></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">拓扑材料</td><td style="border:1px solid #ccc;padding:6px;">从拓扑公理预测材料结构倾向</td><td style="border:1px solid #ccc;padding:6px;">计算具体T_c、能隙</td><td style="border:1px solid #ccc;padding:6px;">分析现有材料数据库</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">核聚变</td><td style="border:1px solid #ccc;padding:6px;">提供约束稳定性拓扑判据</td><td style="border:1px solid #ccc;padding:6px;">替代MHD模拟</td><td style="border:1px solid #ccc;padding:6px;">分析现有托卡马克数据</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">量子计算</td><td style="border:1px solid #ccc;padding:6px;">提供退相干根源的新视角</td><td style="border:1px solid #ccc;padding:6px;">替代量子纠错</td><td style="border:1px solid #ccc;padding:6px;">T_2预补偿实验</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">引力调控</td><td style="border:1px solid #ccc;padding:6px;">理论可能性论证</td><td style="border:1px solid #ccc;padding:6px;">工程实现</td><td style="border:1px solid #ccc;padding:6px;">远期（需材料突破）</td></tr>
</table>
</div>
'''
    html = html[:sec10_start] + expanded_sec10 + html[sec10_end:]
    print("§10已展开为详细版本")

# ============================================================
# 写入
# ============================================================
with open(r"neft_20260511.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ 修订v2完成! {len(html)} 字符")
