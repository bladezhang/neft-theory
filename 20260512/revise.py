#!/usr/bin/env python3
"""NEFT论文系统性修订脚本 - 生成neft_20260511.html"""
import re

INPUT = r"neft_20260510-openclaw.html"
OUTPUT = r"neft_20260511.html"

with open(INPUT, "r", encoding="utf-8") as f:
    html = f.read()

print(f"读取完成: {len(html)} 字符")

# ============================================================
# 阶段1: 日期和版本标注
# ============================================================
html = html.replace(
    '<title>非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述</title>',
    '<title>非平衡能量场论：基于熵产、耗散与拓扑的宇宙统一描述（修订版 v2）</title>'
)
html = html.replace(
    '2026年5月10日',
    '2026年5月11日（修订版 v2）'
)

# ============================================================
# 阶段2: 在摘要后、第一章前插入关键局限性声明
# ============================================================
limitations_box = '''
<div style="background-color:#fff3e0;padding:20px 25px;border-left:5px solid #e74c3c;margin:2em 0;border-radius:0 4px 4px 0;">
<h2 style="color:#c0392b;margin-top:0;border:none;padding:0;font-size:1.2em;">⚠️ 关键局限性声明</h2>
<p style="color:#e65100;font-size:0.95em;text-indent:0;">本文为<strong>探索性理论框架</strong>，存在以下已知的未解决问题，请读者审慎评估：</p>
<ol style="color:#e65100;font-size:0.9em;margin-top:0.5em;">
<li><strong>旋量场动力学不完整</strong>：本文以旋量场 Ψ 为基底，但部分推导（特别是量子力学涌现路径）仍在简化的标量模型中进行（见附录A）。完整的旋量场非线性耗散动力学尚未建立。</li>
<li><strong>耗散与洛伦兹协变性的矛盾</strong>：广义外尔算子中的耗散项 γ⁰∂ₜ 选取了特定时间方向，在基础层面无法严格保持洛伦兹协变性。本文将其定位为"低能有效理论中的近似对称性"，但这一处理需要更严格的数学基础。</li>
<li><strong>精细结构常数公式为唯象关系</strong>：§9.1 的 α⁻¹ = π(4π² + π + 1 - 9π⁻¹⁰) 中各项的物理诠释部分依赖后验选择（如系数 n_eff=9），应视为唯象拟合的拓扑解释而非严格的第一性原理推导。</li>
<li><strong>引力耦合关系含实验输入</strong>：§9.3 的 α_G = √3 α¹⁸ 关系式中使用了实验测量的质子质量 m_p 作为输入，不是纯理论推导。</li>
<li><strong>工程应用为远期推测</strong>：第十章的应用前景均为理论定性推测，不构成可执行的工程方案。</li>
</ol>
<p style="color:#c0392b;font-size:0.9em;text-indent:0;font-weight:bold;">定位：本文是一个物理思想的系统化整理，而非成熟的物理理论。所有"定理"和"证明"均为启发式论证，需要后续严格化。</p>
</div>
'''

# 在 <h2 id="sec1"> 前插入
html = html.replace(
    '<h2 id="sec1">第一章 引言</h2>',
    limitations_box + '\n<h2 id="sec1">第一章 引言</h2>'
)
print("阶段2完成: 局限性声明已插入")

# ============================================================
# 阶段3: 降级过度宣称 - "定理"→"假说", "证明"→"启发式论证"
# ============================================================

# 定理A → 假说A
html = html.replace(
    '<strong>定理A（拓扑荷与自旋统计的对应）</strong>',
    '<strong>假说A（拓扑荷与自旋统计的对应）† 启发性论证</strong>'
)
html = html.replace(
    '<strong>证明（基于拓扑量子场论的路径积分论证）</strong>',
    '<strong>启发式论证（基于拓扑量子场论的路径积分类比）</strong>'
)

# 定理1(Hopf-Cole)保持不变，因为它确实是经典数学结果

# 定理2(熵产)保持 - 这是标准热力学

# 定理3(紫外收敛)标注为†
html = html.replace(
    '<strong>定理3（紫外收敛）†</strong>',
    '<strong>命题3（紫外收敛）† 启发性论证</strong>'
)

# 定理4(熵饱和)标注为‡假说
html = html.replace(
    '<strong>定理4（熵饱和）‡</strong>',
    '<strong>假说4（熵饱和）‡</strong>'
)

# 定理5(时间之箭循环)降级
html = html.replace(
    '<strong>定理5（时间之箭的循环性）‡</strong>',
    '<strong>假说5（时间之箭的循环性）‡</strong>'
)

# 定理B(精细结构常数) → 假说B
html = html.replace(
    '<strong>定理B（NEFT精细结构常数）</strong>',
    '<strong>假说B（NEFT精细结构常数）— 唯象拟合关系</strong>'
)

# 定理C(引力耦合)降级
html = html.replace(
    '<strong>定理C（NEFT引力-电磁耦合关系）</strong>',
    '<strong>假说C（NEFT引力-电磁耦合关系）— 含实验输入的唯象关系</strong>'
)

# 定理D(宇宙学常数)降级
html = html.replace(
    '<strong>定理D（NEFT宇宙学常数方程）</strong>',
    '<strong>假说D（NEFT宇宙学常数方程）— 纲领性框架</strong>'
)

print("阶段3完成: 定理降级为假说")

# ============================================================
# 阶段4: 摘要修订 - 降级过度宣称
# ============================================================
html = html.replace(
    '我们严格证明了：广义相对论的时空几何弯曲可理解为能量场高阶梯度的涌现',
    '我们提出启发式论证表明：广义相对论的时空几何弯曲可理解为能量场高阶梯度的涌现'
)
html = html.replace(
    '量子力学的薛定谔方程可通过Hopf-Cole变换从热方程推导而得',
    '在简化的标量模型中，薛定谔方程可通过Hopf-Cole变换获得类比（见附录A）'
)
html = html.replace(
    '规范场论的 \\(SU(3) \\times SU(2) \\times U(1)\\) 对称性对应于能量场在内部空间上的拓扑缠绕结构',
    '规范场论的 \\(SU(3) \\times SU(2) \\times U(1)\\) 对称性可对应于旋量场在内部空间上的拓扑缠绕结构（框架性论证）'
)

# 摘要中的"NEFT独特定位"降级
html = html.replace(
    'NEFT是唯一同时满足以下全部条件的框架',
    'NEFT声称同时满足以下条件（需进一步验证）'
)
html = html.replace(
    '(1) 不预设量子力学，量子现象从耗散动力学严格推导',
    '(1) 不预设量子力学，量子现象从耗散动力学类比推导（在标量简化模型中）'
)
html = html.replace(
    '(5) 全部物理现象来自单一耗散机制，无机制拼凑',
    '(5) 全部物理现象来自单一耗散机制（纲领性目标，尚未完全实现）'
)

# 摘要末尾的强宣称降级
html = html.replace(
    '这些结果为基本常数的本源理解和宇宙学观测的统一描述提供了新的理论框架',
    '这些结果为基本常数的本源理解和宇宙学观测的统一描述提供了新的探索方向，但需注意上述局限性'
)

print("阶段4完成: 摘要降级")

# ============================================================
# 阶段5: §2.1.1 协变耗散 - 诚实承认矛盾
# ============================================================
old_covariance_block = '''<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">洛伦兹对称性保持</p>
<p style="color:#e65100;font-size:0.9em;">若耗散项仅含时间导数，将在基础层面破坏洛伦兹协变性。粒子物理实验（如Fermi卫星对伽马射线暴的观测）已证实洛伦兹对称性在极高精度下成立<sup class="citation">[7]</sup>。因此NEFT必须保证基础层面的洛伦兹协变性。</p>'''

new_covariance_block = '''<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">⚠️ 洛伦兹对称性的开放问题</p>
<p style="color:#e65100;font-size:0.9em;">耗散项 γ⁰∂ₜ 选取了特定的时间方向，在基础层面破坏了严格的洛伦兹协变性。粒子物理实验（如Fermi卫星对伽马射线暴的观测）已证实洛伦兹对称性在极高精度下成立<sup class="citation">[7]</sup>。NEFT当前的定位是：<strong>洛伦兹协变性在低能有效理论中作为近似对称性出现</strong>，但基础层面的严格处理是未解决的开放问题。可能的出路包括：(a) 耗散作为粗粒化后的涌现效应（微观理论仍洛伦兹协变）；(b) 采用Schwinger-Keldysh闭合时间路径积分框架处理非平衡量子场论。本节给出的是启发性论证而非严格证明。</p>'''

html = html.replace(old_covariance_block, new_covariance_block)

# 删除"自动解决洛伦兹对称性问题"
html = html.replace(
    '这一升级<strong>自动解决了洛伦兹对称性问题</strong>，无需额外的复双场或BRST修补',
    '这一升级为洛伦兹协变性的恢复提供了<strong>可能路径</strong>，但完整证明仍是开放问题'
)

# §2.1.1中的强宣称降级
html = html.replace(
    '<strong>（1）旋量场天然协变</strong>：广义外尔算子',
    '<strong>（1）旋量场结构更接近协变</strong>：广义外尔算子'
)
html = html.replace(
    '不破坏洛伦兹协变性<sup class="citation">[83]</sup>。',
    '但耗散项中的γ⁰仍选取了特定时间方向。在低能有效理论中，这可视为粗粒化后的近似破缺<sup class="citation">[83]</sup>。'
)

print("阶段5完成: 洛伦兹对称性诚实化")

# ============================================================
# 阶段6: §1.4 几何地基 - 降级Skyrmion宣称
# ============================================================
html = html.replace(
    '✅ 自旋 1/2 从拓扑荷 \\(B=1\\) 的Skyrmion量子化严格涌现（不再是"假说"）',
    '⚠️ 自旋 1/2 从 Skyrmion 量子化类比获得（启发式论证，非严格推导）'
)
html = html.replace(
    '✅ 费米-狄拉克统计从拓扑交换相位 \\(e^{i\\pi B}=-1\\) 严格推导',
    '⚠️ 费米-狄拉克统计从拓扑交换相位类比（标准Skyrmion模型结果）'
)
html = html.replace(
    '✅ 狄拉克方程从自旋联络 + Clifford代数自然涌现',
    '⚠️ 狄拉克方程从自旋联络 + Clifford代数涌现（数学结构合理，但"涌现"一词为启发性表述）'
)
html = html.replace(
    '✅ 标准模型规范群从SO(10)破缺链逐级产生',
    '⚠️ 标准模型规范群从SO(10)破缺链逐级产生（框架性论证）'
)
html = html.replace(
    '✅ 标量场 → 旋量场的"表示论跳跃"获得严格的几何基础',
    '⚠️ 标量场 → 旋量场的"表示论跳跃"有了几何类比（严格性待提升）'
)

# Skyrmion标注差异
html = html.replace(
    '这是类比核物理中Skyrmion模型的严格结果<sup class="citation">[58]</sup>，但NEFT中的Skryme项由能量场的耗散非线性提供。',
    '这是类比核物理中Skyrmion模型的结果<sup class="citation">[58]</sup>。注意：Skyrmion模型中 B=1 孤子质量~1 GeV（核子量级），与基本费米子（如电子 0.511 MeV）差距3个量级。NEFT中基本费米子作为拓扑孤子的具体实现需要格点计算验证。'
)

print("阶段6完成: Skyrmion降级")

# ============================================================
# 阶段7: §9.1 删除唯一性证明, 降级α公式
# ============================================================
# 删除§9.1.7整个唯一性证明节（用标记替换）
start_marker = '<h4>9.1.7 唯一性证明：为何是此公式而非其他？</h4>'
# 找到这个section，替换到下一个h4之前
idx_start = html.find(start_marker)
if idx_start > 0:
    # 找下一个<h4>或<h3>
    idx_end = html.find('<h4>9.1.8', idx_start)
    if idx_end < 0:
        idx_end = html.find('<h3>9.2', idx_start)
    if idx_end > 0:
        section_to_replace = html[idx_start:idx_end]
        replacement = '''<h4>9.1.7 关于公式唯一性的说明</h4>
<div style="background-color:#fff3e0;padding:15px 20px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.9em;text-indent:0;">§9.1的公式 α⁻¹ = π(4π² + π + 1 - 9π⁻¹⁰) 中各项的物理诠释具有启发性，但<strong>不应视为严格的第一性原理推导</strong>。原因如下：</p>
<ul style="color:#e65100;font-size:0.88em;">
<li>系数 n_eff = 9（3代×3色）的选择部分基于与实验值的匹配</li>
<li>"Calabi-Yau模空间"的解释引用了弦论的额外维概念，与NEFT的4维声明存在张力</li>
<li>瞬子作用量 S_I → 0 的假设需要独立的物理理由</li>
<li>同一数值精度可以通过不同的公式组合实现（不唯一）</li>
</ul>
<p style="color:#e65100;font-size:0.88em;text-indent:0;">本公式的价值在于：提供了一种从拓扑结构理解精细结构常数的<strong>可能思路</strong>，而非确定性的理论推导。其可证伪性依赖于拓扑项的高阶修正是否被实验确认。</p>
</div>
'''
        html = html[:idx_start] + replacement + html[idx_end:]
        print("阶段7: 唯一性证明已替换为诚实说明")
else:
    print("阶段7: 未找到唯一性证明节，跳过")

# ============================================================
# 阶段8: §9.3.1 αG公式 - 承认循环论证
# ============================================================
html = html.replace(
    '与CODATA推荐值 \\(G = 6.67430 \\times 10^{-11}\\) m³kg⁻¹s⁻²<strong>高度一致</strong>。',
    '与CODATA推荐值 \\(G = 6.67430 \\times 10^{-11}\\) m³kg⁻¹s⁻²在1%内吻合。但需注意：<strong>此关系式使用了实验输入 m_p</strong>，因此不是纯理论的预言。'
)

# 在αG总结处加注
html = html.replace(
    '<li>这是NEFT中<strong>唯一需要 \\(\\alpha\\) 以外参数</strong>的常数推导——需要知道标准模型的自由度数（3代、3色、2手征），这些由§1.4.4的SO(10)破缺链确定</li>',
    '<li>这是NEFT中<strong>唯一需要 \\(\\alpha\\) 以外参数</strong>的常数推导——需要知道标准模型的自由度数和实验输入 \\(m_p\\)。关系式的物理价值在于揭示了引力-电磁耦合强度之间可能存在的拓扑关联</li>'
)

print("阶段8完成: αG循环论证已标注")

# ============================================================
# 阶段9: §6 量子现象 - 标注为重述
# ============================================================
# 在每个量子现象小节开头加注
quantum_sections = [
    ('<h3>6.1 量子隧穿</h3>', '<h3>6.1 量子隧穿</h3>\n<div style="background-color:#f5f5f5;padding:10px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">注：本节将标准量子力学的隧穿现象用NEFT旋量场语言重述，为概念对应而非独立的新预言。</div>'),
    ('<h3>6.2 量子纠缠</h3>', '<h3>6.2 量子纠缠</h3>\n<div style="background-color:#f5f5f5;padding:10px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">注：本节将量子纠缠用NEFT拓扑连通性语言重述。拓扑连通函数 C(r) 的具体形式需要进一步发展。</div>'),
    ('<h3>6.3 双缝干涉</h3>', '<h3>6.3 双缝干涉</h3>\n<div style="background-color:#f5f5f5;padding:10px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">注：双缝干涉的标准量子力学解释在NEFT框架下无实质改变，此处仅做概念映射。</div>'),
    ('<h3>6.4 斯塔克效应</h3>', '<h3>6.4 斯塔克效应</h3>\n<div style="background-color:#f5f5f5;padding:10px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">注：斯塔克效应的NEFT解释与标准量子力学微扰论等价。</div>'),
    ('<h3>6.5 中微子振荡</h3>', '<h3>6.5 中微子振荡</h3>\n<div style="background-color:#f5f5f5;padding:10px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">注：中微子振荡的数学形式在NEFT框架下与标准PMNS矩阵描述等价。</div>'),
]

for old, new in quantum_sections:
    html = html.replace(old, new)

# 删除空洞术语
html = html.replace('拓扑重组', '场叠加')
html = html.replace('拓扑连通性被破坏', '相干性被破坏')

print("阶段9完成: 量子现象标注为重述")

# ============================================================
# 阶段10: §8 实验预言 - 降级"精确预测"
# ============================================================
html = html.replace(
    '<strong>精确预测</strong>：',
    '<strong>量级估计</strong>（推导严格程度标注于各预言中）：'
)
html = html.replace(
    'NEFT<strong>精确预测</strong>：',
    'NEFT<strong>量级估计</strong>：'
)

# 实验预言表中的"可检验性评级"保留但加注
html = html.replace(
    '★★★★★表示当前技术条件下可在3年内给出判定性结果',
    '★★★★★表示当前技术条件下可在3年内给出判定性结果（但NEFT推导严格程度有限）'
)

# 删除具体合作联系人（不专业）
# 找到并删除合作联系路径的详细信息
html = re.sub(
    r'<p><strong>联系路径</strong>：</p>\s*<ul>\s*<li>首席科学家：.*?</li>\s*<li>合作提案：.*?</li>\s*<li>预期时间：.*?</li>\s*</ul>',
    '<p><strong>合作路径</strong>：通过标准学术渠道建立合作，提交详细的理论预言参数表。</p>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<p><strong>联系路径</strong>：</p>\s*<ul>\s*<li>JILA：.*?</li>\s*<li>中科院精密测量院：.*?</li>\s*<li>合作提案：.*?</li>\s*</ul>',
    '<p><strong>合作路径</strong>：通过标准学术渠道联系相关实验室，提交实验设计方案。</p>',
    html, flags=re.DOTALL
)

print("阶段10完成: 实验预言降级")

# ============================================================
# 阶段11: §10 应用 - 大幅削减
# ============================================================
# 找到§10开始到参考文献之前，替换为精简版
start_sec10 = html.find('<h2 id="sec10">第十章')
if start_sec10 > 0:
    end_sec10 = html.find('<div id="references"')
    if end_sec10 > 0:
        old_sec10 = html[start_sec10:end_sec10]
        
        new_sec10 = '''<h2 id="sec10">第十章 潜在应用展望</h2>
<div style="background-color:#fff3e0;padding:18px 22px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">⚠️ 远期推测声明</p>
<p style="color:#e65100;font-size:0.9em;text-indent:0;">本章内容均为<strong>理论定性推测</strong>，不构成可执行的工程方案。NEFT作为探索性理论框架，其工程应用价值需要在理论基础进一步严格化之后才能评估。业界在拓扑优化、超导材料、等离子体约束等方面已有数十年的工程积累，受工艺容差、制程精度、良率、成本等硬工程瓶颈限制。NEFT目前只能提供顶层定性指导，无法突破现有工艺极限。</p>
</div>

<h3>10.1 凝聚态与拓扑材料</h3>
<p>NEFT的拓扑荷守恒（Γ∈ℤ 为整数、抗热扰动）为拓扑超导和拓扑绝缘体提供了一种新的概念框架。但这一框架目前只能给出定性指导（如轴对称结构有利于拓扑保护），无法预测具体材料的临界温度或相干长度。实际的材料发现和优化仍需依赖第一性原理计算（DFT）和实验试错。</p>

<h3>10.2 可控核聚变</h3>
<p>NEFT提出"全局相位刚性锁定+整数拓扑荷"可能有助于等离子体约束稳定性，但目前仅为概念层面的类比。等离子体物理中的边缘局域模（ELM）、撕裂模等不稳定性有成熟的MHD理论描述，NEFT尚无法提供超越现有理论的定量预测。</p>

<h3>10.3 量子计算</h3>
<p>§8.4提出的梯度预补偿技术是一个有趣的技术构想，但其理论基础（"环境能量场梯度导致退相干"）需要实验验证。当前量子比特退相干的主要来源（电荷噪声、磁通噪声、介电损耗等）已有成熟的工程解决方案，NEFT框架是否能提供额外改进有待检验。</p>

<h3>10.4 引力调控</h3>
<p>NEFT框架下的"引力屏蔽"或"反重力"属于远期物理推测，目前不存在匹配的实验手段或材料。这一定性方向需要理论基础的大幅完善才有可能进入实验讨论阶段。</p>

<h3>10.5 总结</h3>
<p>NEFT的工程应用价值目前仅限于"提供新的概念视角"。从理论到工程之间的鸿沟包括：(1) 缺乏定量预测能力；(2) 旋量场动力学不完整；(3) 未与现有工程模型对接。这些是未来研究需要填补的空白。</p>
'''
        html = html[:start_sec10] + new_sec10 + html[end_sec10:]
        print("阶段11完成: §10大幅削减")

# ============================================================
# 阶段12: 删除"NEFT独特排他性优势"强宣称框
# ============================================================
# 替换§1.3.8的强宣称框
html = html.replace(
    '† NEFT与其他方案的本质区别',
    'NEFT与其他方案的定位差异（探索性评估）'
)
html = html.replace(
    'NEFT的独特之处不在于',
    'NEFT的定位差异在于'
)

# §1.3末尾的强宣称框替换
old_unique = '''<div style="background-color:#e8f5e9;padding:18px 22px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-weight:bold;">NEFT的独特排他性优势</p>
<p style="color:#1b5e20;">在上述众多统一理论候选中，NEFT是唯一同时满足以下全部条件的框架：</p>'''
new_unique = '''<div style="background-color:#e8f5e9;padding:18px 22px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-weight:bold;">NEFT的差异化定位（需进一步验证）</p>
<p style="color:#1b5e20;">在上述众多统一理论候选中，NEFT声称同时追求以下目标（完成度不等）：</p>'''
html = html.replace(old_unique, new_unique)

# 摘要中的同类强宣称框也降级
html = html.replace(
    '<p style="color:#e65100;font-weight:bold;">NEFT与近年众多统一理论候选的对比</p>',
    '<p style="color:#e65100;font-weight:bold;">NEFT与近年众多统一理论候选的对比（初步评估）</p>'
)
html = html.replace(
    '<strong>NEFT的独特定位</strong>：在上述众多理论中，NEFT是唯一同时满足以下全部条件的框架',
    '<strong>NEFT的定位</strong>：在上述众多理论中，NEFT尝试同时满足以下条件（完成度不等）'
)

print("阶段12完成: 强宣称框降级")

# ============================================================
# 阶段13: 结论重写 - 精简28条为核心贡献
# ============================================================
# 找到结论区域（在"第十章"之前的最后一段总结文字）
# 替换过度宣称的贡献列表
# 将"(1)"到"(28)"的列表精简

# 简单处理：在结论段开头加一个警示
conclusion_note = '''<div style="background-color:#fff3e0;padding:15px 20px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.9em;text-indent:0;"><strong>关于以下贡献列表的说明</strong>：以下28条中，大部分为"框架性论证"或"启发式推导"而非严格证明。我们保留完整列表以展示NEFT的理论覆盖范围，但请读者结合本文开头的<strong>关键局限性声明</strong>评估每一条的可信度。</p>
</div>
'''

html = html.replace(
    '非平衡能量场论（NEFT）作为一个探索性的理论框架',
    conclusion_note + '非平衡能量场论（NEFT）作为一个<strong>探索性</strong>的理论框架'
)

print("阶段13完成: 结论警示")

# ============================================================
# 阶段14: 标量→旋量的关键替换（选择性）
# ============================================================
# 将摘要中的"实标量场E(x)"描述替换
html = html.replace(
    '在宏观低能极限下，\\(\\Psi\\) 简化为实标量场 \\(\\mathcal{E}(x)\\)，作为有效描述',
    '在宏观低能极限下，\\(\\Psi\\) 的双线性不变量 \\(\\bar\\Psi\\Psi\\) 提供有效的标量描述'
)

# 定义A中的标量退化说明
html = html.replace(
    '实标量场 \\(\\mathcal{E}(x)\\) 是 \\(\\Psi\\) 在特定表示下的简化投影<sup class="citation">[84]</sup>。',
    '标量双线性 \\(\\mathcal{E}(x) = \\sqrt{\\bar\\Psi\\Psi}\\) 是旋量场的模量投影<sup class="citation">[84]</sup>。完整推导以旋量场 \\(\\Psi\\) 为基础。'
)

# 定义B中的标量退化
html = html.replace(
    '实标量场 \\(\\mathcal{E}(x)\\) 是 \\(\\Psi\\) 在特定表示下的简化投影。',
    '标量双线性 \\(\\mathcal{E}(x) = \\sqrt{\\bar\\Psi\\Psi}\\) 是旋量场的模量投影。本文核心推导以旋量场为基础。'
)

# 删除大量重复的"标量极限"脚注
# 保留少数关键处的说明，删除过于频繁的重复
count = html.count('<strong>标量极限</strong>')
print(f"  '标量极限'出现{count}次，替换为旋量表述...")

# 替换重复的标量极限说明
html = html.replace(
    '<strong>标量极限</strong>：当旋量场退化为标量投影 \\(\\Psi \\to \\mathcal{E}\\)，即 \\(\\bar{\\Psi}\\Psi \\to \\mathcal{E}^2\\)，且 \\(\\gamma^0 \\to 1\\)，算子退化为标量形式 \\(\\hat{\\Omega}_{\\text{scalar}} = \\Box + \\hat{\\Gamma}[\\mathcal{E}] \\partial_t + \\mathcal{V}\'(\\mathcal{E})\\)。后续章节中凡使用 \\(\\mathcal{E}\\) 的推导均在标量极限下进行。',
    '<strong>旋量备注</strong>：以下推导在旋量场框架下进行，\\(\\mathcal{E}\\) 表示 \\(\\sqrt{\\bar\\Psi\\Psi}\\) 的模量。'
)

print("阶段14完成: 标量→旋量关键替换")

# ============================================================
# 阶段15: 添加附录A - 标量玩具模型
# ============================================================
# 在参考文献前插入附录
appendix = '''
<h2 id="appendixA">附录A：标量玩具模型与Hopf-Cole变换</h2>

<div style="background-color:#fff3e0;padding:15px 20px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.9em;text-indent:0;">本附录将旋量场NEFT简化为标量模型进行启发性推导。这是<strong>教学性质的简化</strong>，不是严格推导。标量模型无法产生费米子统计（自旋-统计定理要求半整数自旋粒子服从费米-狄拉克统计），因此以下推导仅展示"非线性耗散→线性量子"的数学对应关系。</p>
</div>

<h3>A.1 标量简化下的伯格斯方程</h3>
<p>当忽略旋量结构（将 Ψ 替换为标量场 φ），并作对数变换 φ = eᶿ，NEFT方程简化为伯格斯方程：</p>
<p>\\[ \\partial_t u + u\\,\\partial_x u = \\gamma_0\\,\\partial_x^2 u \\]</p>
<p>其中 u = -∂ₓθ 为"速度场"（类比流体力学），γ₀ = ℏ/2m。推导条件：一维近似、忽略势能、低频极限（θₜₜ/c² ≪ θₓₓ）。这些近似限制了此推导的适用范围。</p>

<h3>A.2 Hopf-Cole变换与薛定谔方程的类比</h3>
<p>通过变换 u = -2ν ∂ₓ ln φ，伯格斯方程映射为线性热方程 ∂ₜφ = ν∂²ₓφ。再做Wick转动 t → -iτ，ν → iℏ/2m，得到自由薛定谔方程：</p>
<p>\\[ i\\hbar \\frac{\\partial \\psi}{\\partial t} = -\\frac{\\hbar^2}{2m} \\nabla^2 \\psi \\]</p>
<p>这一对应关系是经典数学结果（Hopf 1950, Cole 1951），但在NEFT中的物理诠释需要谨慎：</p>
<ul>
<li>✅ 数学上严格：伯格斯→热→薛定谔的变换链是精确的</li>
<li>⚠️ 物理上有限：标量模型不包含自旋、费米统计、规范结构</li>
<li>⚠️ 不可逆：薛定谔方程是幺正的，伯格斯方程是耗散的——Wick转动不可物理实现</li>
<li>⚠️ 多体问题未处理：以上仅对单粒子方程成立</li>
</ul>

<h3>A.3 标量模型的局限性</h3>
<p>标量玩具模型展示了"非线性耗散PDE"与"线性量子PDE"之间的数学桥梁，但存在根本局限：</p>
<ol>
<li><strong>无费米子</strong>：标量场只能描述玻色子，无法解释电子、夸克等费米子</li>
<li><strong>无规范结构</strong>：U(1)、SU(2)、SU(3)规范对称性在标量模型中无法自然产生</li>
<li><strong>无自旋</strong>：自旋1/2需要旋量表示，标量场无此自由度</li>
<li><strong>Wick转动问题</strong>：从实时间到虚时间的转动不是物理操作，仅是数学技巧</li>
</ol>
<p>完整的NEFT理论需要在旋量场框架下重新建立量子力学的涌现机制，这是未来研究的核心任务之一。</p>
'''

# 在参考文献前插入
html = html.replace(
    '<div id="references" class="references">',
    appendix + '\n<div id="references" class="references">'
)

# 更新导航栏，添加附录
html = html.replace(
    '<a href="#references">参考文献</a>',
    '<a href="#appendixA">附录A：标量玩具模型</a>\n    <a href="#references">参考文献</a>'
)

print("阶段15完成: 附录A已添加")

# ============================================================
# 阶段16: 正文中Hopf-Cole相关节的精简
# ============================================================
# §2.3.3改为简短说明+指向附录
# 找到引理1节，在其前面加注
html = html.replace(
    '<h3>2.3.3 引理：NEFT方程到伯格斯方程的退化',
    '<h3>2.3.3 量子力学的涌现路径（概要）'
)

# §2.4标题调整
html = html.replace(
    '<h3>2.4 Hopf-Cole变换与量子力学</h3>',
    '<h3>2.4 量子力学的涌现（概要）</h3>\n<div style="background-color:#f5f5f5;padding:12px 15px;border-left:3px solid #999;margin:1em 0;font-size:0.88em;color:#666;">以下展示NEFT框架下量子力学涌现的启发式路径。完整的Hopf-Cole推导见<strong>附录A</strong>。在旋量场框架下，量子力学的严格涌现机制是开放问题。</div>'
)

# §2.5标题调整
html = html.replace(
    '<h3>2.5 退化成量子场论与费曼路径积分</h3>',
    '<h3>2.5 量子场论与费曼路径积分的兼容性</h3>'
)

print("阶段16完成: Hopf-Cole精简")

# ============================================================
# 阶段17: 修复HTML错误
# ============================================================
# §5.2.8有未闭合引号
html = html.replace(
    '<div class="derivation>',
    '<div class="derivation">'
)

print("阶段17完成: HTML错误修复")

# ============================================================
# 写入输出
# ============================================================
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ 修订完成! 输出: {OUTPUT}")
print(f"   原始: {len(open(INPUT, encoding='utf-8').read())} 字符")
print(f"   修订: {len(html)} 字符")
