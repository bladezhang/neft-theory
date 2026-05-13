"""
图20：熵饱和曲线（优化版）
根据论文上下文优化：展示NEFT预言的熵饱和现象
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'STKaiti', 'KaiTi', 'FangSong', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

def figure20_entropy_saturation_optimized():
    """熵饱和曲线 - 优化版"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # 时间范围
    t = np.linspace(0, 30, 600)

    # 熵的增长（饱和曲线）- 改进公式
    S_max = 100
    S = S_max * (1 - np.exp(-t/6)) * (1 - 0.05 * np.exp(-t/2.5))
    dS = np.gradient(S, t)

    # 绘制熵曲线
    ax.plot(t, S, 'b-', linewidth=3, label='熵 S(t)', zorder=5)
    ax.fill_between(t, S, alpha=0.25, color='blue', zorder=4)

    # 熵产率（使用双y轴）
    ax2 = ax.twinx()
    ax2.plot(t, dS, 'r-', linewidth=3, label='熵产率 dS/dt', zorder=6)
    ax2.fill_between(t, dS, alpha=0.15, color='red', zorder=3)

    # 设置标签
    ax.set_xlabel('时间 t', fontsize=14, fontweight='bold')
    ax.set_ylabel('熵 S', color='blue', fontsize=14, fontweight='bold')
    ax2.set_ylabel('熵产率', color='red', fontsize=14, fontweight='bold')

    # 设置刻度标签颜色
    ax.tick_params(axis='y', labelcolor='blue', labelsize=11, width=2)
    ax2.tick_params(axis='y', labelcolor='red', labelsize=11, width=2)
    ax.tick_params(axis='x', labelsize=11, width=2)

    # 标记饱和点
    saturation_point = 22
    ax.axvline(saturation_point, color='green', linestyle='--', alpha=0.7, linewidth=2.5, zorder=2)
    ax.text(saturation_point, S[-1]*0.88, '接近饱和\nS ≈ S_max', ha='center', fontsize=11,
            color='green', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8, pad=0.6))

    # 标记最大熵
    ax.axhline(S_max, color='gray', linestyle=':', alpha=0.8, linewidth=2, zorder=1)
    ax.text(6, S_max*1.03, f'S_max = {S_max}', ha='center',
            fontsize=11, color='#555', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7, pad=0.4))

    # 标记相变点（熵达到50%的时间）
    t_half = -6 * np.log(0.5)  # Logistic函数的半值点
    ax.axvline(t_half, color='purple', linestyle='-.', alpha=0.7, linewidth=2, zorder=1)
    ax.text(t_half, S_max*0.5, '相变临界点\n(S = S_max/2)', ha='center', fontsize=10,
            color='purple',
            bbox=dict(boxstyle='round', facecolor='plum', alpha=0.6, pad=0.4))

    # 图例
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2,
             loc='lower right', fontsize=11, framealpha=0.95, title='变量说明', title_fontsize=10)

    # 添加标注说明
    # 快速增长期
    ax.annotate('快速增长期\n(远离平衡态)',
                xy=(3, S[20]), xytext=(5, 60),
                fontsize=10, ha='center', color='darkblue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

    # 饱和趋近期
    ax.annotate('饱和趋近期\n(接近平衡态)',
                xy=(20, S[-1]), xytext=(18, 85),
                fontsize=10, ha='center', color='darkred',
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.6))

    # 添加公式说明
    formula_box = dict(boxstyle='round', facecolor='#fff3cd', edgecolor='#ffc107', linewidth=1.5, alpha=0.9)
    ax.text(15, 95,
             r'NEFT熵饱和方程:' + '\n' +
             r'$\frac{dS}{dt} = \Gamma_0 (1-\frac{S}{S_{max}}) S$' + '\n' +
             r'解: $S(t) = \frac{S_{max}}{1+e^{-\Gamma_0(t-t_*)}}$',
             fontsize=11, ha='left',
             bbox=formula_box)

    # 添加物理意义说明
    meaning_box = dict(boxstyle='round', facecolor='#e8f4f8', edgecolor='#3498db', linewidth=1.5, alpha=0.9)
    ax.text(15, 70,
             '物理意义:' + '\n' +
             '• 熵存在上限 S_max，由拓扑自由度决定\n' +
             '• 接近 S_max 时，熵产率下降\n' +
             '• 达到饱和态时，系统可能触发拓扑相变',
             fontsize=10, ha='left',
             bbox=meaning_box)

    # 图表标题
    ax.set_title('NEFT熵饱和曲线：展示熵随时间的演化与饱和现象',
                fontsize=16, fontweight='bold', pad=15)

    ax.grid(True, alpha=0.3, linestyle='--', zorder=0)

    plt.tight_layout()
    return fig


if __name__ == "__main__":
    # 生成图表
    fig = figure20_entropy_saturation_optimized()

    # 保存
    output_dir = "E:/work/projs/neft/paper/figures_py"
    filepath = f"{output_dir}/第四章_图11_熵饱和曲线.png"
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"生成: 第四章_图11_熵饱和曲线.png")
    plt.close(fig)
