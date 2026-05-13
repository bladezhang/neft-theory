"""
NEFT论文图表生成脚本 (优化版)
优化内容：
1. 改进布局，避免文字重叠
2. 增强数据可视化的清晰度
3. 统一图表风格
4. 修正图表序号与内容对应关系
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Wedge, PathPatch, FancyBboxPatch
from matplotlib.path import Path
from mpl_toolkits.mplot3d import Axes3D

# 设置中文字体 - 尝试多个字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'STKaiti', 'KaiTi', 'FangSong', 'SimSun', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.rcParams['mathtext.fontset'] = 'cm'  # 数学公式使用Computer Modern字体
plt.rcParams['font.size'] = 10  # 默认字体大小

# 创建输出目录
import os
output_dir = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def save_figure(fig, filename):
    """保存图表到文件"""
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"生成: {filename}")
    return filepath


# ==================== 图1: 物理学统一历程时间线 (优化版) ====================
def figure1_physics_unification_timeline():
    """物理学统一历程时间线（从牛顿力学到NEFT）- 优化版，避免文字重叠"""
    fig, ax = plt.subplots(figsize=(14, 5))

    # 时间线数据 - 分成两行显示，避免重叠
    events_top = [
        ("1687年", "牛顿力学\n万有引力定律", 0.10),
        ("1865年", "麦克斯韦方程\n电磁学统一", 0.23),
        ("1905年", "狭义相对论\n时空新观念", 0.36),
        ("1915年", "广义相对论\n引力几何化", 0.49),
        ("1925年", "量子力学\n微观世界描述", 0.62),
    ]

    events_bottom = [
        ("1954年", "杨-米尔斯理论\n非阿贝尔规范场", 0.10),
        ("1964年", "希格斯机制\n质量起源", 0.28),
        ("1970s", "标准模型\n粒子物理框架", 0.46),
        ("2026年", "NEFT理论\n非平衡能量场论", 0.64),
    ]

    y_top = 0.65
    y_bottom = 0.35

    # 绘制上半部分
    for i, (year, label, x) in enumerate(events_top):
        color = plt.cm.viridis(i / len(events_top))
        circle = Circle((x, y_top), 0.03, color=color, zorder=10)
        ax.add_patch(circle)

        # 年份在上
        ax.text(x, y_top + 0.12, year, ha='center', fontsize=11, fontweight='bold')
        # 标签在下
        ax.text(x, y_top - 0.12, label, ha='center', fontsize=9, va='top', linespacing=1.2)

        # 连接线到主轴
        ax.plot([x, x], [y_bottom, y_top - 0.03], 'k-', alpha=0.2, linewidth=1)

    # 绘制下半部分
    for i, (year, label, x) in enumerate(events_bottom):
        color = plt.cm.plasma(i / len(events_bottom))
        circle = Circle((x, y_bottom), 0.03, color=color, zorder=10)
        ax.add_patch(circle)

        # 标签在下
        ax.text(x, y_bottom - 0.12, label, ha='center', fontsize=9, va='bottom', linespacing=1.2)
        # 年份在上
        ax.text(x, y_bottom + 0.12, year, ha='center', fontsize=11, fontweight='bold')

        # 连接线到主轴
        ax.plot([x, x], [y_bottom + 0.03, y_top], 'k-', alpha=0.2, linewidth=1)

    # 绘制时间主轴
    ax.plot([0.05, 0.7], [0.5, 0.5], 'k-', linewidth=2, alpha=0.6)

    # 箭头表示时间方向
    ax.arrow(0.68, 0.5, 0.03, 0, head_width=0.02, head_length=0.015,
             fc='gray', ec='gray', linewidth=2)

    ax.set_xlim(0, 0.75)
    ax.set_ylim(0, 0.8)
    ax.axis('off')
    ax.set_title("物理学统一历程时间线（从牛顿力学到NEFT）", fontsize=15, fontweight='bold', pad=15)

    return fig


# ==================== 图2: NEFT理论框架 ====================
def figure2_neft_framework():
    """NEFT理论框架：展示能量场、耗散、拓扑结构与已知理论的关联"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # 中心：能量场
    center = (0.5, 0.5)
    energy_field = Circle(center, 0.14, color='#3498db', alpha=0.85, zorder=5)
    ax.add_patch(energy_field)
    ax.text(center[0], center[1], "能量场\nE(x)", ha='center', va='center',
            color='white', fontweight='bold', fontsize=13, zorder=6, linespacing=1.3)

    # 核心组件环
    components = [
        ("耗散动力学", 0.5, 0.75, '#e74c3c'),
        ("拓扑结构", 0.25, 0.5, '#f39c12'),
        ("熵产机制", 0.5, 0.25, '#27ae60'),
        ("广义外尔算子", 0.75, 0.5, '#9b59b6')
    ]

    for name, x, y, color in components:
        circle = Circle((x, y), 0.11, color=color, alpha=0.75, zorder=4)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center',
                color='white', fontsize=10, fontweight='bold', zorder=5, linespacing=1.2)
        # 连接线
        arrow = FancyArrowPatch(center, (x, y), arrowstyle='->',
                                  color='gray', alpha=0.4, linewidth=1.5, zorder=3)
        ax.add_patch(arrow)

    # 外圈：退化的已知理论
    theories = [
        ("牛顿力学", 0.12, 0.85, '#95a5a6'),
        ("广义相对论", 0.5, 0.90, '#95a5a6'),
        ("量子力学", 0.88, 0.85, '#95a5a6'),
        ("量子场论", 0.94, 0.5, '#95a5a6'),
        ("标准模型", 0.88, 0.15, '#95a5a6'),
        ("热力学", 0.5, 0.10, '#95a5a6'),
        ("信息论", 0.12, 0.15, '#95a5a6')
    ]

    for name, x, y, color in theories:
        rect = FancyBboxPatch((x-0.09, y-0.04), 0.18, 0.08,
                              boxstyle="round,pad=0.02",
                              color=color, alpha=0.65, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center',
                color='white', fontsize=9, zorder=3)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("NEFT理论框架：能量场、耗散、拓扑结构与已知理论的关联",
            fontsize=15, fontweight='bold', pad=15)

    return fig


# ==================== 图3: Hopf-Cole变换示意图 ====================
def figure3_hopf_cole_transform():
    """Hopf-Cole变换示意图：非线性伯格斯方程通过变换映射到线性热方程"""
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.5))

    # 左图：伯格斯方程解（冲击波）
    x = np.linspace(-2, 4, 500)
    u = 0.8 * (1 - np.exp(-x)) / (1 + np.exp(-x))
    ax1.plot(x, u, 'r-', linewidth=2.5)
    ax1.set_xlabel('位置 x', fontsize=11)
    ax1.set_ylabel('速度 u', fontsize=11)
    ax1.set_title('伯格斯方程解\n非线性冲击波', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.text(1.5, 0.5, r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \nu\frac{\partial^2 u}{\partial x^2}$',
             fontsize=11, ha='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.4, pad=0.5))

    # 中间：变换箭头
    ax2.axis('off')
    ax2.text(0.5, 0.65, 'Hopf-Cole变换', ha='center', fontsize=13, fontweight='bold')
    ax2.text(0.5, 0.52, r'$u = -2\nu \frac{\partial}{\partial x}\ln \phi$', ha='center', fontsize=14)
    ax2.text(0.5, 0.38, r'$\phi(x,t) = e^{-u/2\nu}$', ha='center', fontsize=12, color='#e74c3c')
    arrow = FancyArrowPatch((0.3, 0.5), (0.7, 0.5), arrowstyle='->',
                              color='#3498db', linewidth=2.5, mutation_scale=25)
    ax2.add_patch(arrow)
    ax2.text(0.5, 0.25, '非线性 → 线性', ha='center', fontsize=10, color='#3498db', style='italic')

    # 右图：热方程解（高斯扩散）
    x2 = np.linspace(-3, 3, 500)
    t_values = [0.1, 0.5, 1.0, 2.0]
    colors = ['blue', 'green', 'orange', 'red']
    for t, alpha, color in zip(t_values, [1.0, 0.7, 0.5, 0.3], colors):
        phi = (4*np.pi*alpha*t)**(-0.5) * np.exp(-x2**2 / (4*alpha*t))
        ax3.plot(x2, phi, color=color, alpha=0.8, linewidth=2, label=f't={t}')
    ax3.set_xlabel('位置 x', fontsize=11)
    ax3.set_ylabel(r'$\phi$', fontsize=11)
    ax3.set_title('热方程解\n线性高斯扩散', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.legend(loc='upper right', fontsize=9, framealpha=0.8)
    ax3.text(0, -0.1, r'$\frac{\partial \phi}{\partial t} = \nu\frac{\partial^2 \phi}{\partial x^2}$',
             fontsize=11, ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.4, pad=0.5))

    plt.tight_layout()
    return fig


# ==================== 图4: 紫外完备性对比 ====================
def figure4_uv_convergence():
    """紫外完备性对比：展示NEFT传播子与标准模型传播子在高动量区的行为差异"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 动量空间
    k = np.logspace(-2, 4, 300)

    # 标准模型传播子（紫外发散）
    G_SM = 1 / (k**2)

    # NEFT传播子（紫外收敛）
    k_cutoff = 100
    gamma_k = 0.005 * k**1.5
    G_NEFT = 1 / (k**2 + gamma_k * k)

    ax.loglog(k, G_SM, 'r-', linewidth=2.5, label='标准模型\n(紫外发散)')
    ax.loglog(k, G_NEFT, 'b-', linewidth=2.5, label='NEFT\n(紫外收敛)')

    # 标记截断
    ax.axvline(k_cutoff, color='gray', linestyle='--', alpha=0.6, linewidth=2)
    ax.text(k_cutoff*1.3, G_NEFT[120], '截断能标\n(普朗克尺度)', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 添加注解
    ax.annotate('标准模型: $G \sim k^{-2}$\n动量增大时\n不收敛',
               xy=(1000, G_SM[150]), xytext=(300, 1e-6),
               arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
               fontsize=9, color='darkred', ha='center')

    ax.annotate('NEFT: $G \sim (k^2 + \Gamma k)^{-1}$\n高阶耗散项\n使传播子归零',
               xy=(1000, G_NEFT[150]), xytext=(1000, 1e-10),
               arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
               fontsize=9, color='darkblue', ha='center')

    ax.set_xlabel('动量 |k|', fontsize=13)
    ax.set_ylabel('传播子 G(k)', fontsize=13)
    ax.set_title('紫外完备性对比：NEFT vs 标准模型', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

    plt.tight_layout()
    return fig


# ==================== 图5: 传播子在动量空间的衰减 ====================
def figure5_propagator_decay():
    """传播子在动量空间的衰减：展示NEFT的紫外完备性，高频分量自动归零"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    omega = np.logspace(0, 5, 400)

    # NEFT传播子幅值
    omega_P = 1e15  # 普朗克频率
    Gamma = 1e-16
    amplitude = np.abs(1 / (omega**2 + 1j * Gamma * omega**2))

    # 归一化
    amplitude_norm = amplitude / amplitude[0]

    ax.loglog(omega, amplitude_norm, 'b-', linewidth=2.5)
    ax.fill_between(omega, amplitude_norm, alpha=0.3, color='blue')

    # 标记不同频段
    ax.axvspan(1, 1e3, alpha=0.15, color='green', label='可观测区')
    ax.axvspan(1e3, 1e12, alpha=0.15, color='yellow', label='实验区')
    ax.axvspan(1e12, 1e5, alpha=0.15, color='red', label='普朗克区')

    # 标记特征点
    ax.text(10, amplitude_norm[0]*0.5, '低频\n经典', fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # 添加衰减起点标注
    decay_start = 1e12
    ax.axvline(decay_start, color='red', linestyle='--', alpha=0.7, linewidth=2)
    ax.text(decay_start*0.5, 1e-8, '快速衰减起点\n(耗散主导)', fontsize=9,
            color='darkred', ha='center',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.7))

    ax.set_xlabel('频率 ω', fontsize=13)
    ax.set_ylabel('归一化幅度', fontsize=13)
    ax.set_title('传播子在动量空间的衰减', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # 添加公式
    ax.text(5e1, 1e-12, r'$|G(\omega)| \propto \frac{1}{\omega^2 + i\Gamma\omega^2}$',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5, pad=0.5))

    plt.tight_layout()
    return fig


# ==================== 图6: 时间之箭与熵产 ====================
def figure6_entropy_arrow():
    """时间之箭与熵产：展示熵随时间的单调增长"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    t = np.linspace(0, 100, 600)

    # 熵的增长曲线（有饱和趋势）
    S = 100 * (1 - np.exp(-t/30)) * (1 + 0.05 * np.sin(t/12))

    ax.plot(t, S, 'b-', linewidth=2.5)
    ax.fill_between(t, S, alpha=0.3, color='blue')

    # 标记关键点
    ax.axhline(90, color='gray', linestyle='--', alpha=0.5, linewidth=2)
    ax.text(50, 92, '接近饱和 (S≈S_max)', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 箭头表示时间方向
    ax.annotate('', xy=(90, S[-1]), xytext=(60, S[-1]*1.08),
                arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
                fontsize=12, color='red', fontweight='bold')
    ax.text(100, S[-1]*1.15, '时间之箭', color='red',
            fontsize=12, fontweight='bold')

    # 添加阶段标注
    ax.annotate('快速增长期\n(远离平衡)', xy=(10, 25), xytext=(10, 35),
                fontsize=9, color='green', ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    ax.annotate('缓慢趋近期\n(接近平衡)', xy=(60, 85), xytext=(60, 75),
                fontsize=9, color='orange', ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

    ax.set_xlabel('时间 t', fontsize=13)
    ax.set_ylabel('熵 S', fontsize=13)
    ax.set_title('时间之箭与熵产', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 110)

    plt.tight_layout()
    return fig


# ==================== 图7: 能量场演化与熵产 ====================
def figure7_energy_entropy_evolution():
    """能量场演化与熵产：展示能量场从有序（低熵）向无序（高熵）的演化过程"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    # 能量场演化
    x = np.linspace(-5, 5, 300)
    t_values = [0, 1, 3, 5, 10]

    for t, alpha, color in zip(t_values, [0.95, 0.7, 0.5, 0.3, 0.1],
                              ['darkblue', 'green', 'orange', 'red', 'purple']):
        E = alpha * np.exp(-x**2/2) + (1-alpha) * 0.15 * np.exp(-x**2/3) * np.cos(x*0.8)
        ax1.plot(x, E, color=color, alpha=0.8, linewidth=2, label=f't={t}')

    ax1.set_xlabel('位置 x', fontsize=12)
    ax1.set_ylabel('能量场 E(x)', fontsize=12)
    ax1.set_title('能量场演化', fontsize=13, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9, framealpha=0.8)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.text(-4, 0.85, '有序状态\n(低熵)', fontsize=10, ha='center',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax1.text(4, 0.12, '无序状态\n(高熵)', fontsize=10, ha='center',
             bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.7))

    # 熵产率
    t = np.linspace(0, 10, 300)
    dS = np.exp(-t/2.5) * (1 + 0.15 * np.sin(t))
    S = 100 * (1 - np.exp(-t/3.5))

    ax2.plot(t, dS, 'r-', linewidth=2.5, label='熵产率 dS/dt')
    ax2_twin = ax2.twinx()
    ax2_twin.plot(t, S, 'b--', linewidth=2.5, label='累积熵 S')

    ax2.set_xlabel('时间', fontsize=12)
    ax2.set_ylabel('熵产率', color='red', fontsize=12)
    ax2_twin.set_ylabel('累积熵', color='blue', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='red', labelsize=10)
    ax2_twin.tick_params(axis='y', labelcolor='blue', labelsize=10)

    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=10, framealpha=0.9)
    ax2.set_title('熵随时间的演化', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()
    return fig


# ==================== 图8: 贝肯斯坦-霍金熵 (优化版) ====================
def figure8_bekenstein_hawking():
    """贝肯斯坦-霍金熵：展示黑洞视界上的普朗克像素结构与信息流动 - 优化版"""
    fig, ax = plt.subplots(figsize=(11, 11))

    # 绘制黑洞视界（更大的黑洞，更清晰的像素）
    horizon = Circle((0, 0), 1.6, color='black', zorder=5)
    ax.add_patch(horizon)

    # 视界光晕
    halo = Circle((0, 0), 1.7, color='gray', alpha=0.2, zorder=3)
    ax.add_patch(halo)

    # 普朗克像素（优化布局，更清晰）
    n_pixels = 96  # 增加像素数以显示更精细的结构
    angles = np.linspace(0, 2*np.pi, n_pixels, endpoint=False)

    # 使用热力图颜色，从中心到外圈
    for i, angle in enumerate(angles):
        # 像素颜色表示信息状态，使用更丰富的色彩
        ring = i // 8
        color = plt.cm.RdYlBu_r(ring / 12)
        wedge = Wedge((0, 0), 1.55, np.degrees(angle), np.degrees(angle) + 360/n_pixels - 1,
                     facecolor=color, edgecolor='black', linewidth=0.8, alpha=0.9, zorder=2)
        ax.add_patch(wedge)

    # 中心标注
    ax.text(0, 0, '黑洞\n视界', ha='center', va='center', color='white',
            fontsize=16, fontweight='bold', zorder=6, linespacing=1.5)

    # 信息流动箭头（优化布局）
    n_arrows = 12
    arrow_angles = np.linspace(0, 2*np.pi, n_arrows, endpoint=False)
    for angle in arrow_angles:
        x_start = 1.75 * np.cos(angle)
        y_start = 1.75 * np.sin(angle)
        x_end = 2.8 * np.cos(angle)
        y_end = 2.8 * np.sin(angle)
        arrow = FancyArrowPatch((x_start, y_start), (x_end, y_end),
                                  arrowstyle='->,head_width=0.15,head_length=0.2',
                                  color='#e74c3c', mutation_scale=25, linewidth=2, alpha=0.7, zorder=7)
        ax.add_patch(arrow)
        # 软毛发点
        ax.plot(2.3 * np.cos(angle), 2.3 * np.sin(angle), 'o',
               color='#e74c3c', markersize=6, alpha=0.6, zorder=8)

    # 信息流动标注
    ax.text(0, 3.5, '信息流动（软毛发）', ha='center',
            fontsize=13, color='#e74c3c', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8, pad=0.5))

    # 公式标注（优化布局）
    formula_box = dict(boxstyle='round', facecolor='lightblue', alpha=0.7, pad=0.8)
    ax.text(0, -3.2, r'$S = \frac{k_B c^3 A}{4G\hbar}$',
            ha='center', fontsize=15, bbox=formula_box, fontweight='bold')
    ax.text(0, -4, r'$A = 4R_s^2 = 16\pi(GM/c^2)^2$  （视界面积）',
            ha='center', fontsize=11, color='#555')

    # 添加注解
    ax.text(-4, 0, '普朗克像素\n(信息单位)', ha='center', fontsize=10,
            color='#333', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.axis('equal')
    ax.axis('off')
    ax.set_title('贝肯斯坦-霍金熵：黑洞视界的普朗克像素结构',
            fontsize=15, fontweight='bold', pad=15)

    return fig


# ==================== 图9: 黑洞信息流动示意图 (优化版) ====================
def figure9_black_hole_information():
    """黑洞信息流动示意图：展示黑洞蒸发过程中的信息守恒与软毛发机制 - 优化版"""
    fig, ax = plt.subplots(figsize=(13, 6.5))

    # 黑洞（随时间变小）- 更好的布局
    t_stages = [0, 0.25, 0.5, 0.75]
    black_hole_radii = [1.0, 0.7, 0.4, 0.1]
    masses = ['M₀', '0.75M₀', '0.5M₀', '0.1M₀']
    times = ['t=0', 't₁', 't₂', 't₃']

    for i, (t, r, m, time) in enumerate(zip(t_stages, black_hole_radii, masses, times)):
        x_pos = i * 3.5

        # 黑洞本体
        circle = Circle((x_pos, 0), r, color='black', zorder=5)
        ax.add_patch(circle)
        ax.text(x_pos, 0, m, ha='center', va='center',
                color='white', fontsize=10, fontweight='bold', zorder=6)
        ax.text(x_pos, -r-0.25, time, ha='center', fontsize=11, fontweight='bold')

        # 软毛发
        if r > 0.15:
            for angle in np.linspace(0, 2*np.pi, 10, endpoint=False):
                hair_x = x_pos + (r+0.4)*np.cos(angle)
                hair_y = (r+0.4)*np.sin(angle)
                ax.plot([x_pos + r*np.cos(angle), hair_x], [r*np.sin(angle), hair_y],
                       '#e74c3c', alpha=0.6, linewidth=1.5)
                ax.plot(hair_x, hair_y, 'o', color='#e74c3c',
                       markersize=5, alpha=0.5, zorder=4)

        # 霍金辐射箭头
        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            rad_x = x_pos + (r+0.8)*np.cos(angle)
            rad_y = (r+0.8)*np.sin(angle)
            ax.arrow(x_pos, 0, rad_x-x_pos, rad_y, head_width=0.08, head_length=0.08,
                    fc='orange', ec='orange', alpha=0.5, length_includes_head=True, zorder=3)

    # 霍金辐射标签
    ax.text(5.25, 2, '霍金辐射', fontsize=12, color='orange',
            fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, pad=0.5))

    # 信息守恒说明（优化布局）
    info_box = dict(boxstyle='round', facecolor='#e8f8f5', alpha=0.9, edgecolor='#1abc9c', linewidth=2)
    info_text = "信息守恒机制：\n\n• 黑洞内部信息编码在视界上的\n  普朗克像素（软毛发）中\n\n• 蒸发过程中，信息通过软毛发\n  辐射释放到外部\n\n• 信息总量保持守恒，\n  不违反幺正性"

    ax.text(13.5, 0, info_text, fontsize=10, va='center', ha='left',
            bbox=info_box)

    # 绘制时间轴箭头
    ax.annotate('', xy=(11.5, -1.5), xytext=(0.5, -1.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.text(6, -1.8, '时间 (黑洞蒸发过程)', ha='center', fontsize=11, color='gray')

    ax.set_xlim(-0.5, 15)
    ax.set_ylim(-2.5, 3)
    ax.axis('off')
    ax.set_title('黑洞信息流动：软毛发机制与信息守恒',
            fontsize=15, fontweight='bold', pad=15)

    plt.tight_layout()
    return fig


# ==================== 图10: 墨西哥帽势能 (优化版 - 3D) ====================
def figure10_mexican_hat():
    """墨西哥帽势能：展示希格斯机制的对称性自发破缺 - 优化版，更清晰地展示3D形状"""
    fig = plt.figure(figsize=(12, 8))

    # 创建3D子图
    ax = fig.add_subplot(111, projection='3d')

    # 墨西哥帽势能曲面 - 减少点数以避免过大
    phi1 = np.linspace(-2, 2, 60)
    phi2 = np.linspace(-2, 2, 60)
    PHI1, PHI2 = np.meshgrid(phi1, phi2)

    mu2 = -1
    lam = 1
    V = mu2 * (PHI1**2 + PHI2**2) + lam * (PHI1**2 + PHI2**2)**2

    # 绘制3D曲面
    surf = ax.plot_surface(PHI1, PHI2, V, cmap='viridis', alpha=0.85,
                         linewidth=0, antialiased=True, shade=True)

    # 标记极值点
    ax.scatter([0], [0], [0], color='red', s=100, marker='x',
               linewidths=3, label='不稳定真空 (φ=0)', zorder=10)
    ax.text(0, 0, 0.5, '不稳定真空', color='red', fontsize=11, fontweight='bold', ha='center')

    # 真空期望值圆（在底面标记）
    v = np.sqrt(-mu2/lam)
    theta = np.linspace(0, 2*np.pi, 100)
    # 在r=v的圆上标记
    ax.plot(v * np.cos(theta), v * np.sin(theta), np.ones_like(theta)*(-1),
            'r--', linewidth=3, label=f'真空期望值 |φ| = {v:.2f}')

    # 标记几个真空态
    thetas = [0, np.pi/2, np.pi, 3*np.pi/2]
    for theta in thetas:
        ax.scatter([v * np.cos(theta)], [v * np.sin(theta)], [-1],
                  color='blue', s=80, marker='o', alpha=0.8, zorder=11)

    # 设置标签和标题
    ax.set_xlabel('φ₁', fontsize=14, fontweight='bold')
    ax.set_ylabel('φ₂', fontsize=14, fontweight='bold')
    ax.set_zlabel('势能 V(φ)', fontsize=14, fontweight='bold')
    ax.set_title('墨西哥帽势能：对称性自发破缺',
                fontsize=16, fontweight='bold', pad=20)

    # 调整视角以更好地展示帽子形状
    ax.view_init(elev=35, azim=45)

    # 添加颜色条
    cbar = plt.colorbar(surf, ax=ax, shrink=0.7, pad=0.1)
    cbar.set_label('势能值', fontsize=12)

    # 添加势能公式
    ax.text2D(0.5, 0.92, r'$V(φ) = \mu^2|φ|^2 + \lambda|φ|^4$,  $\mu^2 < 0$',
              transform=ax.transAxes, fontsize=14, ha='center',
              bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # 添加说明文字
    ax.text2D(0.5, 0.05, '红色X点为局域极大值(不稳定)，蓝色圆环为全局极小值(稳定)',
              transform=ax.transAxes, fontsize=11, ha='center',
              bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    return fig


# ==================== 图11: 标准模型粒子谱 ====================
def figure11_standard_model():
    """标准模型粒子谱：展示三代费米子、规范玻色子和希格斯标量的完整分类"""
    fig, ax = plt.subplots(figsize=(15, 11))

    # 定义粒子（优化数据）
    quarks = {
        '上夸克(u)': [2.2, 1275, 172000],
        '下夸克(d)': [4.7, 95, 4200],
        '粲夸克(c)': [1275, 0, 172000],
        '奇异夸克(s)': [95, 0, 4200],
        '顶夸克(t)': [172000, 0, 0],
        '底夸克(b)': [4200, 0, 0]
    }

    leptons = {
        '电子(e)': [0.511, 105.7, 1777],
        '电子中微子': [0.0005, 0.008, 0.018]
    }

    gauge_bosons = {
        '光子(γ)': [0, 0, 0],
        'W⁺/W⁻': [80.4, 0, 0],
        'Z⁰': [91.2, 0, 0],
        '胶子(g)': [0, 0, 0]
    }

    higgs = {'希格斯(H)': 125}

    # 颜色方案
    colors_quarks = ['#e74c3c', '#e67e22', '#f1c40f', '#c0392b', '#d35400', '#7f8c8d']
    colors_leptons = ['#3498db', '#9b59b6']
    colors_bosons = ['#2ecc71', '#1abc9c', '#16a085', '#27ae60']
    color_higgs = '#e056fd'

    # 绘制费米子区域
    ax.text(7, 10, '费米子 (自旋1/2)', fontsize=14, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.axhline(9.3, color='gray', linestyle='-', linewidth=2, alpha=0.3)

    # 夸克 (左上区域)
    y_start = 8.5
    for i, (name, masses) in enumerate(quarks.items()):
        x_pos = 1 + (i % 6) * 2.5
        if i >= 6:
            x_pos = 1 + (i - 6) * 2.5
            y_pos = y_start - 1.3
        else:
            y_pos = y_start
        for gen, mass in enumerate(masses):
            if mass > 0:
                bar = Rectangle((x_pos, y_pos - 0.5), 2, 1,
                               color=colors_quarks[i], alpha=0.7, edgecolor='black', linewidth=0.5)
                ax.add_patch(bar)
                ax.text(x_pos + 1, y_pos, f'{mass:.0f}', ha='center', va='center',
                        fontsize=9, color='white', fontweight='bold')
        ax.text(x_pos + 1, y_pos + 0.6, name.split('(')[0], ha='center',
                fontsize=8.5, fontweight='bold')

    # 轻子 (右上区域)
    y_pos = 8.5
    for i, (name, masses) in enumerate(leptons.items()):
        x_pos = 8.5 + i * 2.5
        for gen, mass in enumerate(masses):
            if mass > 0:
                bar = Rectangle((x_pos, y_pos - 0.5), 2, 1,
                               color=colors_leptons[i], alpha=0.7, edgecolor='black', linewidth=0.5)
                ax.add_patch(bar)
                label = f'{mass:.1f}' if mass >= 0.1 else f'{mass*1000:.1f} keV'
                ax.text(x_pos + 1, y_pos, label, ha='center', va='center',
                        fontsize=9, color='white', fontweight='bold')
        ax.text(x_pos + 1, y_pos + 0.6, name.split('(')[0], ha='center',
                fontsize=8.5, fontweight='bold')

    # 规范玻色子 (下方左侧)
    y_pos = 5.5
    ax.text(4, y_pos + 1.2, '规范玻色子 (自旋1)', fontsize=14, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    ax.axhline(y_pos + 0.8, color='gray', linestyle='-', linewidth=2, alpha=0.3)

    boson_names = list(gauge_bosons.keys())
    for i, (name, masses) in enumerate(gauge_bosons.items()):
        x_pos = 1 + i * 2.8
        for gen, mass in enumerate(masses):
            bar = Rectangle((x_pos, y_pos - 0.5), 2.5, 1,
                           color=colors_bosons[i], alpha=0.7, edgecolor='black', linewidth=0.5)
            ax.add_patch(bar)
            ax.text(x_pos + 1.25, y_pos, f'{mass}' if mass > 0 else '0', ha='center',
                    va='center', fontsize=11, color='white', fontweight='bold')
        ax.text(x_pos + 1.25, y_pos + 0.6, name.split('(')[0], ha='center',
                fontsize=9.5, fontweight='bold')

    # 希格斯玻色子 (下方右侧)
    y_pos = 5.5
    ax.text(12.5, y_pos + 1.2, '标量玻色子 (自旋0)', fontsize=14, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='plum', alpha=0.5))
    higgs_bar = Rectangle((12, y_pos - 0.5), 2.5, 1,
                         color=color_higgs, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.add_patch(higgs_bar)
    ax.text(13.25, y_pos, '125', ha='center', va='center', fontsize=11,
            color='white', fontweight='bold')
    ax.text(13.25, y_pos + 0.6, '希格斯(H)', ha='center', fontsize=9.5, fontweight='bold')

    # 代标签
    ax.text(2.5, 9.8, '第一代', ha='center', fontsize=12, fontweight='bold', color='#555')
    ax.text(5, 9.8, '第二代', ha='center', fontsize=12, fontweight='bold', color='#555')
    ax.text(7.5, 9.8, '第三代', ha='center', fontsize=12, fontweight='bold', color='#555')

    # 质量单位标注
    ax.text(7.5, -0.5, '质量单位：MeV/c²（未标注的为0或极小）',
            ha='center', fontsize=11, style='italic', color='#666',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    ax.set_xlim(0, 15)
    ax.set_ylim(-1, 10.5)
    ax.axis('off')
    ax.set_title('标准模型粒子谱', fontsize=16, fontweight='bold', pad=15)

    return fig


# ==================== 图12: 费米子质量层级 ====================
def figure12_fermion_mass_hierarchy():
    """费米子质量层级：展示三代费米子的质量分布（对数尺度）"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 费米子质量（MeV）- 优化数据
    fermions = {
        '电子': 0.511,
        'μ子': 105.7,
        'τ子': 1776,
        '上夸克': 2.2,
        '下夸克': 4.7,
        '粲夸克': 1275,
        '顶夸克': 172000,
        '奇异夸克': 95,
        '底夸克': 4200,
        '电子中微子': 0.0005,
        'μ子中微子': 0.008,
        'τ子中微子': 0.018
    }

    categories = {
        '带电轻子': ['电子', 'μ子', 'τ子'],
        '中微子': ['电子中微子', 'μ子中微子', 'τ子中微子'],
        '上型夸克': ['上夸克', '粲夸克', '顶夸克'],
        '下型夸克': ['下夸克', '奇异夸克', '底夸克']
    }

    colors = ['#3498db', '#9b59b6', '#e74c3c', '#f39c12']

    # 重新排列以便更好显示
    fermions_ordered = {
        'ν_e': 0.0005,
        'ν_μ': 0.008,
        'ν_τ': 0.018,
        'e': 0.511,
        'μ': 105.7,
        'τ': 1776,
        'u': 2.2,
        'c': 1275,
        't': 172000,
        'd': 4.7,
        's': 95,
        'b': 4200
    }

    cat_map = {
        'ν_e': '中微子', 'ν_μ': '中微子', 'ν_τ': '中微子',
        'e': '带电轻子', 'μ': '带电轻子', 'τ': '带电轻子',
        'u': '上型夸克', 'c': '上型夸克', 't': '上型夸克',
        'd': '下型夸克', 's': '下型夸克', 'b': '下型夸克'
    }

    x = np.arange(len(fermions_ordered))
    masses = list(fermions_ordered.values())
    names = list(fermions_ordered.keys())

    # 按类别着色
    color_map = []
    for name in names:
        for i, cat in enumerate(['中微子', '带电轻子', '上型夸克', '下型夸克']):
            if cat_map[name] == cat:
                color_map.append(colors[i])
                break

    bars = ax.bar(x, masses, color=color_map, alpha=0.75, edgecolor='black', linewidth=1)

    ax.set_yscale('log')
    ax.set_xlabel('费米子', fontsize=13)
    ax.set_ylabel('质量 (MeV)', fontsize=13)
    ax.set_title('费米子质量层级（对数尺度）', fontsize=15, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--', which='both')

    # 在柱子上标注数值
    for bar, mass, name in zip(bars, masses, names):
        height = bar.get_height()
        y_pos = height * 1.5
        if mass > 100:
            label = f'{mass:.0f}'
        elif mass > 1:
            label = f'{mass:.1f}'
        else:
            label = f'{mass:.3f}'
        ax.text(bar.get_x() + bar.get_width()/2, height,
                label, ha='center', va='bottom', fontsize=8, rotation=45)

    # 添加质量区间标注
    ax.axhspan(1e-4, 1, alpha=0.05, color='purple', label='轻子区')
    ax.axhspan(1, 1e5, alpha=0.05, color='orange', label='夸克区')

    # 图例
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=colors[0], label='中微子'),
        Patch(facecolor=colors[1], label='带电轻子'),
        Patch(facecolor=colors[2], label='上型夸克'),
        Patch(facecolor=colors[3], label='下型夸克')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10, framealpha=0.9)

    plt.tight_layout()
    return fig


# ==================== 图13: 规范耦合常数的大统一 ====================
def figure13_gut_unification():
    """规范耦合常数的大统一：展示SU(3)、SU(2)、U(1)耦合常数在GUT能标处的汇聚"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 能标（对数）- 使用GeV
    energy = np.logspace(0, 17, 400)

    # 耦合常数倒数（随能标演化）- 改进公式
    # 在低能：α1⁻¹ ≈ 59, α2⁻¹ ≈ 30, α3⁻¹ ≈ 8.5

    alpha1_inv = 59 + (4.2/2*np.pi) * np.log10(energy/100)
    alpha2_inv = 30 + (1/2*np.pi) * np.log10(energy/100)
    alpha3_inv = 8.5 - (7/2*np.pi) * np.log10(energy/100)

    # 确保在低能处正确
    energy_ref = 100  # GeV, MZ mass
    scale1 = np.log10(energy/energy_ref)

    # 重新计算，使用更准确的跑动公式
    alpha1_inv = 59.0 + (41/10/2/np.pi) * scale1
    alpha2_inv = 30.0 + (-19/6/2/np.pi) * scale1
    alpha3_inv = 8.5 + (-7/2/np.pi) * scale1

    ax.plot(energy, alpha1_inv, 'b-', linewidth=2.5, label=r'$\alpha_1^{-1}$ (U(1) 超荷)')
    ax.plot(energy, alpha2_inv, 'g-', linewidth=2.5, label=r'$\alpha_2^{-1}$ (SU(2) 弱作用)')
    ax.plot(energy, alpha3_inv, 'r-', linewidth=2.5, label=r'$\alpha_3^{-1}$ (SU(3) 强作用)')

    # 标记汇聚点
    gut_energy = 1e16
    ax.axvline(gut_energy, color='purple', linestyle='--', alpha=0.7, linewidth=2)
    ax.text(gut_energy*0.8, 45, 'GUT能标\n$M_{GUT} \\approx 10^{16}$ GeV', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='plum', alpha=0.7))

    # 标记低能测量点
    mz_energy = 91.2
    ax.axvline(mz_energy, color='gray', linestyle=':', alpha=0.5)
    ax.text(mz_energy, 20, '$M_Z$', fontsize=9, ha='center', rotation=90)

    ax.set_xlabel('能标 (GeV)', fontsize=13)
    ax.set_ylabel('耦合常数倒数', fontsize=13)
    ax.set_title('规范耦合常数的大统一', fontsize=15, fontweight='bold')
    ax.set_xscale('log')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)

    # 添加说明
    ax.text(1e3, 55, '在GUT能标处，三种相互作用\n可能统一为单一作用',
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    return fig


# ==================== 图14: 孤子解 ====================
def figure14_soliton_solutions():
    """孤子解：展示能量场的扭结解和反扭结解，对应于基本粒子"""
    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.linspace(-8, 8, 600)

    # 扭结解
    tanh_kink = np.tanh(x/2)
    # 反扭结解
    tanh_anti_kink = -np.tanh(x/2)
    # 呼息子解
    sech_breather = 0.6 * np.tanh(x/2) * (1 / np.cosh(x/1.5)) * np.cos(4*x)

    ax.plot(x, tanh_kink, 'b-', linewidth=2.5, label='扭结解 (粒子)')
    ax.plot(x, tanh_anti_kink, 'r--', linewidth=2.5, label='反扭结解 (反粒子)')
    ax.plot(x, sech_breather, 'g-.', linewidth=2, label='呼吸子解 (束缚态)')

    ax.set_xlabel('位置 x', fontsize=13)
    ax.set_ylabel('能量场 E(x)', fontsize=13)
    ax.set_title('孤子解：扭结、反扭结与呼吸子', fontsize=15, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # 标注
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5, linewidth=2)
    ax.axvline(0, color='gray', linestyle=':', alpha=0.5, linewidth=2)
    ax.text(0, -1.1, 'x=0', ha='center', fontsize=10, color='#666')

    # 添加说明
    ax.text(-5, 0.85, '粒子 (扭结)\n拓扑荷 = +1', fontsize=10, color='blue',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))
    ax.text(-5, -0.85, '反粒子 (反扭结)\n拓扑荷 = -1', fontsize=10, color='red',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.6))
    ax.text(5, 0.3, '呼吸子\n(束缚态)', fontsize=10, color='green',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

    plt.tight_layout()
    return fig


# ==================== 图15: 量子隧穿示意图 ====================
def figure15_quantum_tunneling():
    """量子隧穿示意图：展示能量场在势垒中的渗透过程"""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    x = np.linspace(-4, 4, 600)

    # 势垒
    V = np.zeros_like(x)
    V[(x >= -1.2) & (x <= 1.2)] = 2

    # 粒子能量
    E = 1
    ax.axhline(E, color='green', linestyle='--', linewidth=2.5, label='粒子能量 E')

    # 势垒区域填充
    ax.fill_between(x, 0, V, where=(V > 0), alpha=0.25, color='red', label='势垒 V')
    ax.plot(x, V, 'r-', linewidth=2)

    # 波函数（在势垒内指数衰减）
    psi = np.zeros_like(x, dtype=complex)
    mask_left = x < -1.2
    mask_barrier = (x >= -1.2) & (x <= 1.2)
    mask_right = x > 1.2

    kappa = np.sqrt(2*2)  # 2*(V-E)
    psi[mask_left] = np.exp(1j * 1.2 * x[mask_left])
    psi[mask_barrier] = np.exp(-kappa * (x[mask_barrier] + 1.2))
    psi[mask_right] = np.exp(-kappa * 2.4) * np.exp(1j * 1.2 * x[mask_right])

    # 归一化
    psi_abs = np.abs(psi)
    psi_abs /= np.max(psi_abs)

    ax2 = ax.twinx()
    ax2.plot(x, psi_abs, 'b-', linewidth=2.5, label='波函数 |ψ|')
    ax2.fill_between(x, psi_abs, alpha=0.3, color='blue')

    ax.set_xlabel('位置 x', fontsize=13)
    ax.set_ylabel('势能 V', fontsize=13)
    ax2.set_ylabel('波函数幅值', color='blue', fontsize=13)
    ax2.tick_params(axis='y', labelcolor='blue', labelsize=11)
    ax.tick_params(axis='y', labelsize=11)
    ax.tick_params(axis='x', labelsize=11)

    ax.set_title('量子隧穿：能量场在势垒中的渗透', fontsize=15, fontweight='bold')

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10, framealpha=0.9)
    ax2.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # 标注
    ax.text(0, 2.3, '经典禁区\n(E < V)', ha='center', fontsize=11,
            color='darkred', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.7))

    ax2.text(-3.2, 0.9, '入射波', ha='center', fontsize=10, color='blue',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))
    ax2.text(3.2, 0.1, '透射波\n(指数衰减后)', ha='center', fontsize=10, color='blue',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

    # 添加隧穿概率公式
    ax2.text(-3.5, 0.05, r'$|T|^2 \approx e^{-2\kappa L}$',
             fontsize=11, color='darkblue',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    return fig


# ==================== 图16: 双缝干涉图样 ====================
def figure16_double_slit():
    """双缝干涉图样：展示能量场通过双缝后的干涉条纹"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    # 干涉图样
    x = np.linspace(-5, 5, 600)
    wavelength = 0.5
    slit_separation = 2
    screen_distance = 10

    # 双缝干涉强度
    k = 2 * np.pi / wavelength
    beta = k * slit_separation * x / (2 * screen_distance)
    intensity = np.cos(beta)**2 * (np.sin(k * 0.1 * x / screen_distance) /
                                      (k * 0.1 * x / screen_distance + 1e-10))**2

    ax1.plot(x, intensity, 'b-', linewidth=2)
    ax1.fill_between(x, intensity, alpha=0.4, color='blue')

    # 模拟干涉条纹
    x_img = np.linspace(-5, 5, 300)
    y_img = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(x_img, y_img)
    beta_img = k * slit_separation * X / (2 * screen_distance)
    I = np.cos(beta_img)**2

    im = ax2.imshow(I, extent=[-5, 5, -3, 3], origin='lower', cmap='Blues', aspect='auto', alpha=0.9)

    ax1.set_xlabel('屏幕位置 x', fontsize=12)
    ax1.set_ylabel('强度 I', fontsize=12)
    ax1.set_title('干涉强度分布', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')

    # 标记干涉极大值
    for i in range(-5, 6):
        pos = i * wavelength * screen_distance / slit_separation
        if abs(pos) <= 5:
            ax1.axvline(pos, color='red', linestyle=':', alpha=0.5, linewidth=1)
            ax1.text(pos, 0.1, f'n={i}', ha='center', fontsize=8, color='red')

    ax2.set_xlabel('屏幕位置 x', fontsize=12)
    ax2.set_ylabel('屏幕位置 y', fontsize=12)
    ax2.set_title('干涉条纹图样', fontsize=13, fontweight='bold')

    # 添加颜色条
    plt.colorbar(im, ax=ax2, label='强度')

    plt.tight_layout()
    return fig


# ==================== 图17: 中微子振荡概率 ====================
def figure17_neutrino_oscillation():
    """中微子振荡概率：展示不同中微子味之间的振荡模式"""
    fig, ax = plt.subplots(figsize=(12, 6.5))

    L_over_E = np.linspace(0, 500, 600)

    # 混合角（PMNS参数近似）
    theta12 = np.radians(33.5)
    theta23 = np.radians(45)
    theta13 = np.radians(8.6)

    # 两味振荡概率（改进公式）
    delta_m21_sq = 7.5e-5  # eV²
    delta_m31_sq = 2.5e-3   # eV²

    P_mue = np.sin(2 * theta12)**2 * np.sin(1.27 * delta_m21_sq * L_over_E)**2
    P_mut = np.sin(2 * theta23)**2 * np.sin(1.27 * delta_m31_sq * L_over_E)**2

    ax.plot(L_over_E, P_mue, 'b-', linewidth=2.5, label=r'$\nu_\mu \to \nu_e$ (太阳振荡)')
    ax.plot(L_over_E, P_mut, 'g-', linewidth=2.5, label=r'$\nu_\mu \to \nu_\tau$ (大气振荡)')

    # 标记完全振荡点
    max_L_mue = np.pi / (1.27 * delta_m21_sq)
    # 限制在图表范围内
    if max_L_mue <= 500:
        ax.axvline(max_L_mue, color='blue', linestyle='--', alpha=0.6, linewidth=2)
        ax.text(max_L_mue, 0.5, '第一次太阳振荡', fontsize=10, ha='center', color='blue')

    ax.set_xlabel('L/E (km/GeV)', fontsize=13)
    ax.set_ylabel('振荡概率 P', fontsize=13)
    ax.set_title('中微子振荡概率', fontsize=15, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(0, 1.1)
    ax.set_xlim(0, 500)

    # 添加说明
    formula_text = r'$P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta)\sin^2(1.27\Delta m^2 L/2E)$'
    ax.text(250, 0.2, formula_text, fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7, pad=0.5))

    # 标记参数值
    ax.text(400, 0.8, r'$\Delta m_{21}^2 = 7.5 \times 10^{-5} \text{ eV}^2$' + '\n' +
            r'$\Delta m_{31}^2 = 2.5 \times 10^{-3} \text{ eV}^2$',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # plt.tight_layout()  # 可能导致问题，暂时注释
    return fig


# ==================== 图18: 引力波频谱衰减 (优化版) ====================
def figure18_gravitational_wave():
    """引力波频谱衰减：展示NEFT预言的高频引力波振幅衰减效应 - 优化版"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    frequency = np.logspace(0, 5, 400)

    # 标准GR预言（无衰减）
    h_GR = 10 / frequency

    # NEFT预言（有衰减）- 更明显的衰减
    f_cutoff = 100
    h_NEFT = 10 / frequency * np.exp(-(frequency / f_cutoff)**0.6)

    ax.loglog(frequency, h_GR, 'r-', linewidth=2.5, label='标准GR (无衰减)')
    ax.loglog(frequency, h_NEFT, 'b-', linewidth=2.5, label='NEFT (有衰减)')

    # 标记衰减起始点
    ax.axvline(f_cutoff, color='gray', linestyle='--', alpha=0.6, linewidth=2)
    ax.text(f_cutoff*1.5, h_NEFT[150]*5, '衰减起始\n$f_c \\approx 100$ Hz', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # 标注频段
    ax.text(2, h_GR[10], 'LIGO频段\n(10-1000 Hz)', fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))
    ax.text(1000, h_GR[100], '高频段\n(>1 kHz)', fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.6))

    # 添加差异区域标注
    ax.fill_between(frequency[frequency > f_cutoff], h_GR[frequency > f_cutoff],
                   h_NEFT[frequency > f_cutoff], alpha=0.2, color='purple',
                   label='NEFT与GR的差异')

    ax.set_xlabel('频率 f (Hz)', fontsize=13)
    ax.set_ylabel('振幅 |h(f)|', fontsize=13)
    ax.set_title('引力波频谱衰减：NEFT的预言', fontsize=15, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # 添加衰减公式
    ax.text(100, 1e-9, r'$|h(f)| \propto f^{-1} \cdot e^{-(f/f_c)^{0.6}}$',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # 添加观测注解
    ax.text(1e4, 1e-7, 'NEFT预言：\n高频引力波\n振幅衰减\n可通过未来\n探测器验证',
            fontsize=9, color='#555',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    plt.tight_layout()
    return fig


# ==================== 图19: 精细结构常数的跑动 ====================
def figure19_fine_structure_constant():
    """精细结构常数的跑动：展示α在不同能标下的演化"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 能标
    mu = np.logspace(-1, 5, 500)

    # 精细结构常数的跑动（改进版）
    alpha_inv_MZ = 127.9  # Z玻色子能标处
    ln_ratio = np.log(mu / 1e5)

    # 改进的跑动公式
    alpha_inv = alpha_inv_MZ - (2/(3*np.pi)) * ln_ratio + 0.05 * (ln_ratio/10)**2

    # 转换为α
    alpha = 1 / alpha_inv

    ax.loglog(mu, alpha, 'b-', linewidth=2.5)
    ax.fill_between(mu, alpha, alpha*0.95, alpha=0.2, color='blue')

    # 标记关键能标
    key_points = [
        (0.511, 'm_e', 'green'),
        (91.1876e3, 'M_Z', 'orange'),
        (80.4e3, 'M_W', 'red')
    ]

    for value, label, color in key_points:
        idx = np.argmin(np.abs(mu - value))
        ax.axvline(value, color=color, linestyle='--', alpha=0.6, linewidth=2)
        ax.text(value*1.2, alpha[idx], label, fontsize=10, color=color,
                ha='left', va='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7, edgecolor=color))

    # 标记实验值
    alpha_exp = 1/137.035999084
    ax.axhline(alpha_exp, color='gray', linestyle=':', alpha=0.8, linewidth=2)
    ax.text(1e-1, alpha_exp*1.1, '实验值\n$\\alpha^{-1}\\approx 137.036$', fontsize=10,
            ha='center', va='bottom', color='#555',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax.set_xlabel('能标 μ (MeV)', fontsize=13)
    ax.set_ylabel('精细结构常数 α', fontsize=13)
    ax.set_title('精细结构常数的跑动', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')

    # 添加公式
    ax.text(1e4, 0.004, r'$\frac{d\alpha}{d\ln\mu} = \frac{2\alpha^2}{3\pi} + \cdots$',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7, pad=0.5))

    # 添加注解
    ax.text(1e2, 0.007, 'α随能标增大而增大\n(QED重整化群效应)',
            fontsize=10, color='#555',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    plt.tight_layout()
    return fig


# ==================== 图20: 熵饱和曲线 ====================
def figure20_entropy_saturation():
    """熵饱和曲线：展示NEFT预言的熵饱和现象"""
    fig, ax = plt.subplots(figsize=(11, 6.5))

    t = np.linspace(0, 25, 600)

    # 熵的增长（饱和曲线）- 改进公式
    S_max = 100
    S = S_max * (1 - np.exp(-t/6)) * (1 - 0.05 * np.exp(-t/2))
    dS = np.gradient(S)

    ax.plot(t, S, 'b-', linewidth=2.5, label='熵 S(t)')
    ax.fill_between(t, S, alpha=0.3, color='blue')

    # 熵产率
    ax2 = ax.twinx()
    ax2.plot(t, dS, 'r-', linewidth=2.5, label='熵产率 dS/dt')
    ax2.fill_between(t, dS, alpha=0.2, color='red')

    ax.set_xlabel('时间 t', fontsize=13)
    ax.set_ylabel('熵 S', color='blue', fontsize=13)
    ax2.set_ylabel('熵产率', color='red', fontsize=13)
    ax2.tick_params(axis='y', labelcolor='red', labelsize=11)
    ax.tick_params(axis='y', labelcolor='blue', labelsize=11)
    ax.tick_params(axis='x', labelsize=11)

    # 标记饱和点
    saturation_point = 18
    ax.axvline(saturation_point, color='green', linestyle='--', alpha=0.6, linewidth=2)
    ax.text(saturation_point, S[-1]*0.85, '接近饱和\nS ≈ S_max', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # 标记最大熵
    ax.axhline(S_max, color='gray', linestyle=':', alpha=0.8, linewidth=2)
    ax.text(5, S_max*1.02, f'S_max = {S_max}', fontsize=10, ha='center',
            color='#555', fontweight='bold')

    ax.set_title('NEFT熵饱和曲线', fontsize=15, fontweight='bold')
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2,
             loc='lower right', fontsize=10, framealpha=0.9)
    ax2.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # 添加说明
    ax.text(12, 0.5, '当熵接近最大值时，\n熵产率显著下降\n系统接近平衡态',
            fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    # 添加公式
    ax.text(2, 85, r'$\frac{dS}{dt} = \Gamma_0 (1-\frac{S}{S_{max}}) S$',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    return fig


# ==================== 主函数：生成所有图表 ====================
def main():
    """生成所有论文图表"""
    print("开始生成NEFT论文图表（优化版）...")
    print()

    # 定义所有图表生成函数
    figure_generators = [
        (figure1_physics_unification_timeline, "第一章_图1_物理学统一历程时间线.png"),
        (figure2_neft_framework, "第二章_图2_NEFT理论框架.png"),
        (figure3_hopf_cole_transform, "第二章_图3_Hopf-Cole变换示意图.png"),
        (figure4_uv_convergence, "第二章_图4_紫外完备性对比.png"),
        (figure5_propagator_decay, "第二章_图5_传播子动量空间衰减.png"),
        (figure6_entropy_arrow, "第三章_图6_时间之箭与熵产.png"),
        (figure7_energy_entropy_evolution, "第三章_图7_能量场演化与熵产.png"),
        (figure8_bekenstein_hawking, "第三章_图8_贝肯斯坦霍金熵.png"),
        (figure9_black_hole_information, "第三章_图9_黑洞信息流动示意图.png"),
        (figure10_mexican_hat, "第五章_图10_墨西哥帽势能.png"),
        (figure11_standard_model, "第五章_图11_标准模型粒子谱.png"),
        (figure12_fermion_mass_hierarchy, "第五章_图12_费米子质量层级.png"),
        (figure13_gut_unification, "第五章_图13_规范耦合常数大统一.png"),
        (figure14_soliton_solutions, "第五章_图14_孤子解.png"),
        (figure15_quantum_tunneling, "第六章_图15_量子隧穿示意图.png"),
        (figure16_double_slit, "第六章_图16_双缝干涉图样.png"),
        (figure17_neutrino_oscillation, "第六章_图17_中微子振荡概率.png"),
        (figure18_gravitational_wave, "第八章_图18_引力波频谱衰减.png"),
        (figure19_fine_structure_constant, "第九章_图19_精细结构常数跑动.png"),
        (figure20_entropy_saturation, "第四章_图20_熵饱和曲线.png")
    ]

    # 生成所有图表
    for generator, filename in figure_generators:
        try:
            fig = generator()
            save_figure(fig, filename)
        except Exception as e:
            print(f"生成 {filename} 时出错: {e}")

    print()
    print(f"共生成 {len(figure_generators)} 张图表")
    print(f"图表保存在: {output_dir}/")


if __name__ == "__main__":
    main()
