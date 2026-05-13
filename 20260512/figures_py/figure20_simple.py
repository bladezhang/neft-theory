"""
图20：熵饱和曲线（简化优化版）
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

def figure20_entropy():
    """熵饱和曲线"""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    t = np.linspace(0, 30, 500)
    S_max = 100
    S = S_max * (1 - np.exp(-t/6)) * (1 - 0.05 * np.exp(-t/2.5))
    dS = np.gradient(S, t)

    ax.plot(t, S, 'b-', linewidth=3, label='熵 S(t)', zorder=5)
    ax.fill_between(t, S, alpha=0.25, color='blue', zorder=4)

    ax2 = ax.twinx()
    ax2.plot(t, dS, 'r-', linewidth=3, label='熵产率 dS/dt', zorder=6)
    ax2.fill_between(t, dS, alpha=0.15, color='red', zorder=3)

    ax.set_xlabel('时间 t', fontsize=13)
    ax.set_ylabel('熵 S', color='blue', fontsize=13)
    ax2.set_ylabel('熵产率', color='red', fontsize=13)
    ax.tick_params(axis='y', labelcolor='blue', labelsize=11)
    ax2.tick_params(axis='y', labelcolor='red', labelsize=11)
    ax.tick_params(axis='x', labelsize=11)

    # 标记饱和点
    saturation_point = 22
    ax.axvline(saturation_point, color='green', linestyle='--', alpha=0.6, linewidth=2, zorder=1)
    ax.text(saturation_point, S[-1]*0.88, '接近饱和', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    ax.axhline(S_max, color='gray', linestyle=':', alpha=0.8, linewidth=2, zorder=1)
    ax.text(5, S_max*1.02, f'S_max = {S_max}', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2,
             loc='lower right', fontsize=10, framealpha=0.9, title='变量')
    ax2.legend(loc='upper right', fontsize=10, framealpha=0.9)

    ax.set_title('NEFT熵饱和曲线：展示熵随时间的演化与饱和现象',
                fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--', zorder=0)

    # 添加说明文字
    ax.text(8, 20, 'NEFT熵饱和方程:\ndS/dt = Gamma_0 * (1 - S/S_max) * S',
             fontsize=9, bbox=dict(boxstyle='round', facecolor='#fef9e7', alpha=0.7))

    return fig

if __name__ == "__main__":
    fig = figure20_entropy()
    fig.savefig("E:/work/projs/neft/paper/figures_py/第四章_图11_熵饱和曲线.png",
               dpi=300, bbox_inches='tight', facecolor='white')
    print("生成: 第四章_图11_熵饱和曲线.png")
    plt.close(fig)
