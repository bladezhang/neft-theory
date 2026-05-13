"""
图19：精细结构常数的跑动（简化优化版）
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

def figure19_fine_structure():
    """精细结构常数的跑动"""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    # 能标范围
    mu = np.logspace(-1, 5, 400)

    # 精细结构常数的跑动
    alpha_inv_m_e = 137.036
    ln_ratio = np.log(mu / 0.511)
    alpha_inv = alpha_inv_m_e - (2/(3*np.pi)) * ln_ratio + 0.05 * (ln_ratio / 10)**2
    alpha = 1 / alpha_inv

    # 绘制曲线
    ax.loglog(mu, alpha, 'b-', linewidth=3)
    ax.fill_between(mu, alpha, alpha*0.95, alpha*1.05, alpha=0.2, color='blue')

    # 标记关键能标点
    points = [(0.511, 'm_e', 'green'), (105.7, 'm_mu', 'darkgreen'),
              (1776, 'm_tau', 'teal'), (91.1876e3, 'M_Z', 'orange'),
              (80.4e3, 'M_W', 'darkorange'), (125e3, 'M_H', 'red')]

    for value, label, color in points:
        idx = np.argmin(np.abs(mu - value))
        ax.axvline(value, color=color, linestyle='--', alpha=0.6, linewidth=2, zorder=1)
        ax.text(value*0.8, alpha[idx]*0.9, label, fontsize=9, color=color, ha='left')

    # 实验值
    alpha_exp = 1/137.035999084
    ax.axhline(alpha_exp, color='gray', linestyle=':', linewidth=2, alpha=0.8, zorder=1)
    ax.text(1e-1, alpha_exp*1.08, '实验值 alpha = 1/137.036', fontsize=10, color='#333')

    # NEFT理论值
    alpha_neft = 1 / (np.pi * (4*np.pi**2 + np.pi + 1 - 9*np.pi**(-10)))
    ax.axhline(alpha_neft, color='red', linestyle='-.', linewidth=2, alpha=0.8, zorder=1)
    ax.text(1e3, alpha_neft*1.1, 'NEFT理论值 alpha = 1/137.036', fontsize=10, color='#c0392b')

    ax.set_xlabel('能标 mu (MeV)', fontsize=13)
    ax.set_ylabel('精细结构常数 alpha', fontsize=13)
    ax.set_title('精细结构常数的跑动：展示alpha在不同能标下的演化',
                fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')

    # 添加说明文字
    ax.text(1e3, 0.0075, 'QED跑动: alpha随能标增大\nNEFT第一性原理: pi*(4*pi^2 + pi + 1 - 9*pi^-10)',
             fontsize=9, bbox=dict(boxstyle='round', facecolor='#e8f4f8', alpha=0.7))

    return fig

if __name__ == "__main__":
    fig = figure19_fine_structure()
    fig.savefig("E:/work/projs/neft/paper/figures_py/第九章_图19_精细结构常数跑动.png",
               dpi=300, bbox_inches='tight', facecolor='white')
    print("生成: 第九章_图19_精细结构常数跑动.png")
    plt.close(fig)
