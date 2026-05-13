"""
图11：标准模型粒子谱（优化版）
根据论文上下文优化：清晰展示三代费米子、规范玻色子和希格斯标量的完整分类
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'STKaiti', 'KaiTi', 'FangSong', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

def figure11_standard_model_optimized():
    """标准模型粒子谱 - 优化版"""
    fig = plt.figure(figsize=(16, 11))

    # 创建网格布局
    # 左侧：费米子（三代）
    # 右侧：玻色子

    # 费米子数据（论文中的数值）
    leptons = {
        'νe': 0.0005,      # 电子中微子 (keV单位)
        'e': 0.511,       # 电子 (MeV)
        'νμ': 0.008,       # μ子中微子
        'μ': 105.7,       # μ子
        'ντ': 0.018,      # τ子中微子
        'τ': 1776         # τ子
    }

    quarks = {
        'u': 2.2,         # 上夸克 (MeV)
        'd': 4.7,         # 下夸克
        'c': 1275,        # 粲夸克
        's': 95,          # 奇异夸克
        't': 172000,      # 顶夸克
        'b': 4200         # 底夸克
    }

    # 规范玻色子数据
    gauge_bosons = {
        'γ': 0,           # 光子
        'W±': 80.4e3,    # W玻色子 (转换为MeV)
        'Z⁰': 91.2e3,    # Z玻色子
        'g': 0            # 胶子
    }

    # 希格斯玻色子
    higgs_mass = 125e3  # 125 GeV 转换为 MeV

    # 颜色方案
    gen_colors = ['#3498db', '#2ecc71', '#e74c3c']  # 蓝、绿、红
    boson_color = ['#f39c12', '#e67e22', '#9b59b6', '#27ae60']  # 橙、深橙、紫、绿
    higgs_color = '#8e44ad'  # 紫色

    # ============ 左侧：费米子区域 ============
    ax_fermions = fig.add_axes([0.03, 0.08, 0.55, 0.88])
    ax_fermions.axis('off')

    # 标题
    ax_fermions.text(0.5, 0.98, '费米子 (自旋 1/2)', fontsize=16, fontweight='bold',
                     ha='center', va='top',
                     bbox=dict(boxstyle='round', facecolor='#e8f4f8', edgecolor='#3498db', linewidth=2, pad=0.5))

    # 三代标题
    gen_titles = ['第一代', '第二代', '第三代']
    gen_x = [0.15, 0.40, 0.65]
    for i, (title, x) in enumerate(zip(gen_titles, gen_x)):
        ax_fermions.text(x, 0.88, title, fontsize=13, fontweight='bold', ha='center',
                        color=gen_colors[i],
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=gen_colors[i], linewidth=1.5))

    # 轻子部分
    lepton_y_start = 0.75
    ax_fermions.text(0.02, lepton_y_start, '轻子', fontsize=12, fontweight='bold',
                     bbox=dict(boxstyle='round', facecolor='#d6eaf8', alpha=0.7))

    lepton_items = [
        ('νe', leptons['νe'], '电子中微子'),
        ('e', leptons['e'], '电子'),
        ('νμ', leptons['νμ'], 'μ子中微子'),
        ('μ', leptons['μ'], 'μ子'),
        ('ντ', leptons['ντ'], 'τ子中微子'),
        ('τ', leptons['τ'], 'τ子')
    ]

    y_pos = lepton_y_start
    for i, (name, mass, full_name) in enumerate(lepton_items):
        gen_idx = i // 2  # 每2个粒子对应一代
        x_pos = gen_x[gen_idx]
        y_pos -= 0.07

        # 绘制粒子框
        box = FancyBboxPatch((x_pos - 0.1, y_pos - 0.025), 0.2, 0.05,
                             boxstyle='round,pad=0.02',
                             facecolor=gen_colors[gen_idx], edgecolor='black', linewidth=0.8, alpha=0.8)
        ax_fermions.add_patch(box)

        # 粒子名称
        ax_fermions.text(x_pos, y_pos, name, ha='center', va='center',
                        color='white', fontsize=11, fontweight='bold')

        # 质量标注
        if mass < 0.001:
            mass_str = f'{mass*1000:.1f} keV'
        else:
            mass_str = f'{mass:.1f} MeV'
        ax_fermions.text(x_pos + 0.12, y_pos, mass_str, ha='left', va='center',
                        fontsize=9, color='#555')

    # 夸克部分
    quark_y_start = y_pos - 0.08
    ax_fermions.text(0.02, quark_y_start, '夸克', fontsize=12, fontweight='bold',
                     bbox=dict(boxstyle='round', facecolor='#fadbd8', alpha=0.7))

    quark_items = [
        ('u', quarks['u'], '上夸克'),
        ('d', quarks['d'], '下夸克'),
        ('c', quarks['c'], '粲夸克'),
        ('s', quarks['s'], '奇异夸克'),
        ('t', quarks['t'], '顶夸克'),
        ('b', quarks['b'], '底夸克')
    ]

    y_pos = quark_y_start
    for i, (name, mass, full_name) in enumerate(quark_items):
        gen_idx = i // 2
        x_pos = gen_x[gen_idx]
        y_pos -= 0.07

        # 绘制粒子框
        box = FancyBboxPatch((x_pos - 0.1, y_pos - 0.025), 0.2, 0.05,
                             boxstyle='round,pad=0.02',
                             facecolor=gen_colors[gen_idx], edgecolor='black', linewidth=0.8, alpha=0.8)
        ax_fermions.add_patch(box)

        # 粒子名称
        ax_fermions.text(x_pos, y_pos, name, ha='center', va='center',
                        color='white', fontsize=11, fontweight='bold')

        # 质量标注
        if mass < 10:
            mass_str = f'{mass:.1f} MeV'
        elif mass < 1000:
            mass_str = f'{mass:.0f} MeV'
        else:
            mass_str = f'{mass/1000:.1f} GeV'
        ax_fermions.text(x_pos + 0.12, y_pos, mass_str, ha='left', va='center',
                        fontsize=9, color='#555')

    # 添加夸克色荷标注
    y_pos -= 0.06
    ax_fermions.text(0.5, y_pos, r'夸克色荷：红(R)、绿(G)、蓝(B) + 反色',
                     ha='center', fontsize=9, style='italic', color='#666')

    # 质量单位说明
    ax_fermions.text(0.02, 0.02, '质量单位：MeV/c² (中微子标注keV，重夸克标注GeV)',
                     fontsize=8, style='italic', color='#666')

    # ============ 右侧：玻色子区域 ============
    ax_bosons = fig.add_axes([0.62, 0.08, 0.35, 0.88])
    ax_bosons.axis('off')

    # 标题
    ax_bosons.text(0.5, 0.98, '玻色子', fontsize=16, fontweight='bold',
                   ha='center', va='top',
                   bbox=dict(boxstyle='round', facecolor='#fef9e7', edgecolor='#f39c12', linewidth=2, pad=0.5))

    # 规范玻色子部分
    ax_bosons.text(0.5, 0.88, '规范玻色子 (自旋 1)', fontsize=13, fontweight='bold',
                   ha='center', color='#e67e22',
                   bbox=dict(boxstyle='round', facecolor='white', edgecolor='#e67e22', linewidth=1.5))

    boson_items = [
        ('γ', gauge_bosons['γ'], '光子', boson_color[0], '电磁相互作用'),
        ('W±', gauge_bosons['W±'], 'W玻色子', boson_color[1], '弱相互作用'),
        ('Z⁰', gauge_bosons['Z⁰'], 'Z玻色子', boson_color[2], '弱相互作用'),
        ('g', gauge_bosons['g'], '胶子', boson_color[3], '强相互作用')
    ]

    y_pos = 0.78
    for name, mass, full_name, color, interaction in boson_items:
        x_pos = 0.3

        # 绘制粒子框
        box = FancyBboxPatch((x_pos - 0.1, y_pos - 0.03), 0.4, 0.06,
                             boxstyle='round,pad=0.02',
                             facecolor=color, edgecolor='black', linewidth=1, alpha=0.85)
        ax_bosons.add_patch(box)

        # 粒子名称
        ax_bosons.text(x_pos, y_pos, f'  {name}  ', ha='center', va='center',
                      color='white', fontsize=12, fontweight='bold')

        # 质量标注
        if mass == 0:
            mass_str = '无质量'
        else:
            mass_str = f'{mass/1000:.1f} GeV'
        ax_bosons.text(0.75, y_pos, mass_str, ha='left', va='center',
                      fontsize=10, color='#555')

        # 相互作用标注
        ax_bosons.text(0.75, y_pos - 0.04, interaction, ha='left', va='top',
                      fontsize=8, color='#666', style='italic')

        y_pos -= 0.12

    # 胶子色荷标注
    y_pos -= 0.02
    ax_bosons.text(0.5, y_pos, r'胶子色荷：8种 (R̄ḠB̄及其反色)',
                   ha='center', fontsize=9, style='italic', color='#666')

    # 希格斯玻色子部分
    higgs_y_start = y_pos - 0.1
    ax_bosons.text(0.5, higgs_y_start, '希格斯玻色子 (自旋 0)', fontsize=13, fontweight='bold',
                   ha='center', color=higgs_color,
                   bbox=dict(boxstyle='round', facecolor='white', edgecolor=higgs_color, linewidth=1.5))

    y_pos = higgs_y_start - 0.08
    x_pos = 0.5

    # 绘制希格斯框
    higgs_box = FancyBboxPatch((x_pos - 0.2, y_pos - 0.04), 0.4, 0.08,
                               boxstyle='round,pad=0.02',
                               facecolor=higgs_color, edgecolor='black', linewidth=2, alpha=0.85)
    ax_bosons.add_patch(higgs_box)

    # 希格斯名称
    ax_bosons.text(x_pos, y_pos, '  H  ', ha='center', va='center',
                  color='white', fontsize=16, fontweight='bold')

    # 希格斯质量
    ax_bosons.text(x_pos, y_pos - 0.06, f'm_H = {higgs_mass/1000:.0f} GeV',
                  ha='center', fontsize=11, color='#555')

    # 希格斯机制说明
    y_pos -= 0.12
    ax_bosons.text(0.5, y_pos, '希格斯机制：对称性自发破缺\n真空期望值 v ≈ 246 GeV',
                  ha='center', fontsize=9, color='#666', style='italic',
                  bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    # 添加图例和说明
    y_pos -= 0.15
    ax_bosons.text(0.5, y_pos,
                  '标准模型：SU(3) × SU(2) × U(1) 规范群',
                  ha='center', fontsize=11, fontweight='bold',
                  bbox=dict(boxstyle='round', facecolor='#e8f5e8', alpha=0.8, pad=0.5))

    y_pos -= 0.1
    ax_bosons.text(0.5, y_pos,
                  '• SU(3)：量子色动力学 (QCD)\n• SU(2)：弱电相互作用 (包含W±, Z⁰)\n• U(1)：电磁相互作用 (包含γ)',
                  ha='center', fontsize=9, color='#555')

    # 图表主标题
    fig.suptitle('标准模型粒子谱：展示三代费米子、规范玻色子和希格斯标量的完整分类',
                fontsize=18, fontweight='bold', y=0.995)

    return fig


if __name__ == "__main__":
    # 生成图表
    fig = figure11_standard_model_optimized()

    # 保存
    output_dir = "E:/work/projs/neft/paper/figures_py"
    filepath = f"{output_dir}/第五章_图11_标准模型粒子谱.png"
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"生成: 第五章_图11_标准模型粒子谱.png")
    plt.close(fig)
