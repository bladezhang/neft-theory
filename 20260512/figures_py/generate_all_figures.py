"""
NEFT论文图表生成脚本
生成所有论文所需的图表，确保中文正确显示
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Wedge, PathPatch
from matplotlib.path import Path

# 设置中文字体 - 尝试多个字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'STKaiti', 'KaiTi', 'FangSong', 'SimSun', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.rcParams['mathtext.fontset'] = 'cm'  # 数学公式使用Computer Modern字体

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


# ==================== 图1: 物理学统一历程时间线 ====================
def figure1_physics_unification_timeline():
    """物理学统一历程时间线（从牛顿力学到NEFT）"""
    fig, ax = plt.subplots(figsize=(12, 4))

    # 时间线数据
    events = [
        ("1687年", "牛顿力学\n万有引力定律", 0.2),
        ("1865年", "麦克斯韦方程\n电磁学统一", 0.35),
        ("1905年", "狭义相对论\n时空新观念", 0.5),
        ("1915年", "广义相对论\n引力几何化", 0.65),
        ("1925年", "量子力学\n微观世界描述", 0.75),
        ("1954年", "杨-米尔斯理论\n非阿贝尔规范场", 0.85),
        ("1964年", "希格斯机制\n质量起源", 0.9),
        ("1970s", "标准模型\n粒子物理框架", 0.95),
        ("2026年", "NEFT理论\n非平衡能量场论", 1.0)
    ]

    y = 0.5

    for i, (year, label, x) in enumerate(events):
        # 绘制时间点
        color = plt.cm.viridis(i / len(events))
        circle = Circle((x, y), 0.05, color=color, zorder=10)
        ax.add_patch(circle)

        # 绘制连接线
        if i < len(events) - 1:
            ax.plot([x, events[i+1][2]], [y, y], 'k-', alpha=0.3, linewidth=2)

        # 添加文字
        ax.text(x, y + 0.15, year, ha='center', fontsize=10, fontweight='bold')
        ax.text(x, y - 0.2, label, ha='center', fontsize=9, wrap=True)

    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("物理学统一历程时间线（从牛顿力学到NEFT）", fontsize=14, fontweight='bold')

    return fig


# ==================== 图2: NEFT理论框架 ====================
def figure2_neft_framework():
    """NEFT理论框架：展示能量场、耗散、拓扑结构与已知理论的关联"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # 中心：能量场
    center = (0.5, 0.5)
    energy_field = Circle(center, 0.12, color='#3498db', alpha=0.8, zorder=5)
    ax.add_patch(energy_field)
    ax.text(center[0], center[1], "能量场\nE(x)", ha='center', va='center',
            color='white', fontweight='bold', fontsize=11, zorder=6)

    # 核心组件环
    components = [
        ("耗散动力学", 0.5, 0.72, '#e74c3c'),
        ("拓扑结构", 0.27, 0.5, '#f39c12'),
        ("熵产机制", 0.5, 0.28, '#27ae60'),
        ("广义外尔算子", 0.73, 0.5, '#9b59b6')
    ]

    for name, x, y, color in components:
        circle = Circle((x, y), 0.1, color=color, alpha=0.7, zorder=4)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center',
                color='white', fontsize=9, fontweight='bold', zorder=5)
        # 连接线
        arrow = FancyArrowPatch(center, (x, y), arrowstyle='->',
                                  color='gray', alpha=0.5, linewidth=1.5, zorder=3)
        ax.add_patch(arrow)

    # 外圈：退化的已知理论
    theories = [
        ("牛顿力学", 0.15, 0.8, '#95a5a6'),
        ("广义相对论", 0.5, 0.85, '#95a5a6'),
        ("量子力学", 0.85, 0.8, '#95a5a6'),
        ("量子场论", 0.92, 0.5, '#95a5a6'),
        ("标准模型", 0.85, 0.2, '#95a5a6'),
        ("热力学", 0.5, 0.12, '#95a5a6'),
        ("信息论", 0.15, 0.2, '#95a5a6')
    ]

    for name, x, y, color in theories:
        rect = Rectangle((x-0.08, y-0.05), 0.16, 0.1,
                        color=color, alpha=0.6, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center',
                color='white', fontsize=8, zorder=3)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("NEFT理论框架：能量场、耗散、拓扑结构与已知理论的关联",
            fontsize=14, fontweight='bold')

    return fig


# ==================== 图3: Hopf-Cole变换示意图 ====================
def figure3_hopf_cole_transform():
    """Hopf-Cole变换示意图：非线性伯格斯方程通过变换映射到线性热方程"""
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4))

    # 左图：伯格斯方程解（冲击波）
    x = np.linspace(-2, 4, 500)
    u = 1 - np.exp(-x) / (1 + np.exp(-x))
    ax1.plot(x, u, 'r-', linewidth=2)
    ax1.set_xlabel('位置 x')
    ax1.set_ylabel('速度 u')
    ax1.set_title('伯格斯方程解\n非线性冲击波', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.text(1.5, 0.5, r'$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \nu\frac{\partial^2 u}{\partial x^2}$',
             fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # 中间：变换箭头
    ax2.axis('off')
    ax2.text(0.5, 0.6, 'Hopf-Cole变换', ha='center', fontsize=12, fontweight='bold')
    ax2.text(0.5, 0.5, r'$u = -2\nu \frac{\partial}{\partial x}\ln \phi$', ha='center', fontsize=14)
    ax2.text(0.5, 0.35, r'$\phi(x,t) = e^{-u/2\nu}$', ha='center', fontsize=12, color='#e74c3c')
    arrow = FancyArrowPatch((0.3, 0.5), (0.7, 0.5), arrowstyle='->',
                              color='#3498db', linewidth=2, mutation_scale=20)
    ax2.add_patch(arrow)

    # 右图：热方程解（高斯扩散）
    x2 = np.linspace(-3, 3, 500)
    t_values = [0.1, 0.5, 1.0, 2.0]
    for t, alpha in zip(t_values, [1.0, 0.6, 0.4, 0.2]):
        phi = (4*np.pi*alpha*t)**(-0.5) * np.exp(-x2**2 / (4*alpha*t))
        ax3.plot(x2, phi, label=f't={t}', alpha=min(alpha+0.3, 1), linewidth=2)
    ax3.set_xlabel('位置 x')
    ax3.set_ylabel(r'$\phi$')
    ax3.set_title('热方程解\n线性高斯扩散', fontsize=11, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper right', fontsize=9)
    ax3.text(0, -0.1, r'$\frac{\partial \phi}{\partial t} = \nu\frac{\partial^2 \phi}{\partial x^2}$',
             fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 图4: 紫外完备性对比 ====================
def figure4_uv_convergence():
    """紫外完备性对比：展示NEFT传播子与标准模型传播子在高动量区的行为差异"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # 动量空间
    k = np.logspace(-2, 4, 200)

    # 标准模型传播子（紫外发散）
    G_SM = 1 / (k**2)

    # NEFT传播子（紫外收敛）
    k_cutoff = 100
    gamma_k = 0.01 * k**1.5
    G_NEFT = 1 / (k**2 + gamma_k * k)

    ax.loglog(k, G_SM, 'r-', linewidth=2.5, label='标准模型\n(紫外发散)')
    ax.loglog(k, G_NEFT, 'b-', linewidth=2.5, label='NEFT\n(紫外收敛)')

    # 标记截断
    ax.axvline(k_cutoff, color='gray', linestyle='--', alpha=0.5)
    ax.text(k_cutoff*1.2, G_NEFT[100], '截断能标', fontsize=9)

    ax.set_xlabel('动量 |k|', fontsize=12)
    ax.set_ylabel('传播子 G(k)', fontsize=12)
    ax.set_title('紫外完备性对比：NEFT vs 标准模型', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=11)

    plt.tight_layout()
    return fig


# ==================== 图5: 传播子在动量空间的衰减 ====================
def figure5_propagator_decay():
    """传播子在动量空间的衰减：展示NEFT的紫外完备性，高频分量自动归零"""
    fig, ax = plt.subplots(figsize=(10, 6))

    omega = np.logspace(0, 5, 300)

    # NEFT传播子幅值
    omega_P = 1e15  # 普朗克频率
    Gamma = 1e-16
    amplitude = np.abs(1 / (omega**2 + 1j * Gamma * omega**2))

    # 归一化
    amplitude_norm = amplitude / amplitude[0]

    ax.loglog(omega, amplitude_norm, 'b-', linewidth=2)
    ax.fill_between(omega, amplitude_norm, alpha=0.3, color='blue')

    # 标记不同频段
    ax.axvspan(1, 1e3, alpha=0.1, color='green', label='可观测区')
    ax.axvspan(1e3, 1e12, alpha=0.1, color='yellow', label='实验区')
    ax.axvspan(1e12, 1e5, alpha=0.1, color='red', label='普朗克区')

    # 标记特征点
    ax.text(1, amplitude_norm[0], '低频\n经典', fontsize=9, ha='center', va='bottom')
    ax.text(omega_P, amplitude_norm[-1]*10, '普朗克频率', fontsize=9, ha='center')

    ax.set_xlabel('频率 ω', fontsize=12)
    ax.set_ylabel('归一化幅度', fontsize=12)
    ax.set_title('传播子在动量空间的衰减', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    return fig


# ==================== 图6: 时间之箭与熵产 ====================
def figure6_entropy_arrow():
    """时间之箭与熵产：展示熵随时间的单调增长"""
    fig, ax = plt.subplots(figsize=(10, 6))

    t = np.linspace(0, 100, 500)

    # 熵的增长曲线（有饱和趋势）
    S = 100 * (1 - np.exp(-t/30)) * (1 + 0.1 * np.sin(t/10))

    ax.plot(t, S, 'b-', linewidth=2.5)
    ax.fill_between(t, S, alpha=0.3, color='blue')

    # 标记关键点
    ax.axhline(90, color='gray', linestyle='--', alpha=0.5)
    ax.text(50, 92, '接近饱和', fontsize=10)

    # 箭头表示时间方向
    ax.annotate('', xy=(90, S[-1]), xytext=(50, S[-1]*1.1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red', fontweight='bold')
    ax.text(100, S[-1]*1.15, '时间之箭', color='red',
            fontsize=12, fontweight='bold')

    ax.set_xlabel('时间', fontsize=12)
    ax.set_ylabel('熵 S', fontsize=12)
    ax.set_title('时间之箭与熵产', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 105)

    plt.tight_layout()
    return fig


# ==================== 图7: 能量场演化与熵产 ====================
def figure7_energy_entropy_evolution():
    """能量场演化与熵产：展示能量场从有序（低熵）向无序（高熵）的演化过程"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # 能量场演化
    x = np.linspace(-5, 5, 200)
    t_values = [0, 1, 3, 5, 10]

    for t, alpha, color in zip(t_values, [0.8, 0.6, 0.4, 0.2, 0.05],
                              ['blue', 'green', 'orange', 'red', 'purple']):
        E = alpha * np.exp(-x**2) + (1-alpha) * 0.2 * np.exp(-x**2/4) * np.cos(x)
        ax1.plot(x, E, color=color, alpha=0.7, linewidth=2, label=f't={t}')

    ax1.set_xlabel('位置 x')
    ax1.set_ylabel('能量场 E(x)')
    ax1.set_title('能量场演化', fontsize=11, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.text(-4, 0.8, '有序状态', fontsize=10, ha='center')
    ax1.text(4, 0.15, '无序状态', fontsize=10, ha='center')

    # 熵产率
    t = np.linspace(0, 10, 200)
    dS = np.exp(-t/2) * (1 + 0.2 * np.sin(t))
    S = 100 * (1 - np.exp(-t/3))

    ax2.plot(t, dS, 'r-', linewidth=2, label='熵产率 dS/dt')
    ax2_twin = ax2.twinx()
    ax2_twin.plot(t, S, 'b--', linewidth=2, label='累积熵 S')

    ax2.set_xlabel('时间')
    ax2.set_ylabel('熵产率', color='red')
    ax2_twin.set_ylabel('累积熵', color='blue')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2_twin.tick_params(axis='y', labelcolor='blue')

    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=9)
    ax2.set_title('熵随时间的演化', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


# ==================== 图8: 贝肯斯坦-霍金熵 ====================
def figure8_bekenstein_hawking():
    """贝肯斯坦-霍金熵：展示黑洞视界上的普朗克像素结构与信息流动"""
    fig, ax = plt.subplots(figsize=(10, 10))

    # 绘制黑洞视界
    horizon = Circle((0, 0), 1.5, color='black', zorder=3)
    ax.add_patch(horizon)

    # 普朗克像素（模拟）
    n_pixels = 64
    angles = np.linspace(0, 2*np.pi, n_pixels, endpoint=False)
    for i, angle in enumerate(angles):
        # 像素颜色表示不同的信息状态
        color = plt.cm.viridis((i % 8) / 8)
        wedge = Wedge((0, 0), 1.4, np.degrees(angle), np.degrees(angle) + 360/n_pixels - 2,
                     facecolor=color, edgecolor='black', alpha=0.8, zorder=2)
        ax.add_patch(wedge)

    # 标注
    ax.text(0, 0, '黑洞', ha='center', va='center', color='white',
            fontsize=14, fontweight='bold', zorder=4)

    # 信息流动箭头
    for i in range(8):
        angle = angles[i]
        x = 2.2 * np.cos(angle)
        y = 2.2 * np.sin(angle)
        arrow = FancyArrowPatch((1.6*np.cos(angle), 1.6*np.sin(angle)),
                                  (x, y), arrowstyle='->',
                                  color='red', mutation_scale=20, linewidth=2)
        ax.add_patch(arrow)

    ax.text(0, 2.5, '信息流动\n（软毛发）', ha='center',
            fontsize=11, color='red', fontweight='bold')

    # 公式标注
    ax.text(0, -2.5, r'$S = \frac{k_B c^3 A}{4G\hbar}$',
            ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(0, -3.2, r'$A = 4R_s^2 = 16\pi(GM/c^2)^2$（视界面积）',
            ha='center', fontsize=11)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3.5, 3.5)
    ax.axis('equal')
    ax.axis('off')
    ax.set_title('贝肯斯坦-霍金熵：黑洞视界的普朗克像素结构',
            fontsize=14, fontweight='bold')

    return fig


# ==================== 图9: 黑洞信息流动示意图 ====================
def figure9_black_hole_information():
    """黑洞信息流动示意图：展示黑洞蒸发过程中的信息守恒与软毛发机制"""
    fig, ax = plt.subplots(figsize=(12, 6))

    # 黑洞（随时间变小）
    t_stages = [0, 0.3, 0.6, 0.9]
    black_hole_radii = [1.0, 0.7, 0.3, 0.05]

    for i, (t, r) in enumerate(zip(t_stages, black_hole_radii)):
        circle = Circle((t*4, 0), r, color='black', zorder=5)
        ax.add_patch(circle)
        ax.text(t*4, 0, f'M={1-i*0.25}M₀', ha='center', va='center',
                color='white', fontsize=9, zorder=6)
        ax.text(t*4, -r-0.3, f't={t}', ha='center', fontsize=10)

        # 软毛发
        if r > 0.1:
            for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
                hair_x = t*4 + (r+0.3)*np.cos(angle)
                hair_y = (r+0.3)*np.sin(angle)
                ax.plot([t*4 + r*np.cos(angle), hair_x], [r*np.sin(angle), hair_y],
                       'r-', alpha=0.5, linewidth=1)
                ax.plot(hair_x, hair_y, 'ro', markersize=4, alpha=0.5)

    # 霍金辐射
    radiation_angles = np.linspace(0.4*np.pi, 0.6*np.pi, 20)
    for angle in radiation_angles:
        x = 2 + 5 * np.cos(angle)
        y = 5 * np.sin(angle)
        ax.arrow(0, 0, x, y, head_width=0.1, head_length=0.1,
                fc='orange', ec='orange', alpha=0.6, length_includes_head=True)

    ax.text(6, 1, '霍金辐射', fontsize=11, color='orange', fontweight='bold')

    # 信息守恒说明
    info_text = "信息守恒：\n• 黑洞内部信息 → 软毛发\n• 视界信息编码在长波长激发中\n• 熵在蒸发过程中保持连续性"
    ax.text(12, 0, info_text, fontsize=10, va='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

    ax.set_xlim(-1, 18)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    ax.set_title('黑洞信息流动：软毛发机制与信息守恒',
            fontsize=14, fontweight='bold')

    plt.tight_layout()
    return fig


# ==================== 图10: 墨西哥帽势能 ====================
def figure10_mexican_hat():
    """墨西哥帽势能：展示希格斯机制的对称性自发破缺"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # 墨西哥帽势能曲面
    phi1 = np.linspace(-2, 2, 100)
    phi2 = np.linspace(-2, 2, 100)
    PHI1, PHI2 = np.meshgrid(phi1, phi2)

    mu2 = -1
    lam = 1
    V = mu2 * (PHI1**2 + PHI2**2) + lam * (PHI1**2 + PHI2**2)**2

    # 绘制等高线图
    levels = np.linspace(-1, 1.5, 30)
    contour = ax.contour(PHI1, PHI2, V, levels=levels, cmap='viridis', linewidths=1)
    ax.clabel(contour, inline=True, fontsize=8)

    # 标记极值点
    ax.plot(0, 0, 'rx', markersize=15, markeredgewidth=3, label='不稳定真空（φ=0）')

    # 真空期望值圆
    v = np.sqrt(-mu2/lam)
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(v * np.cos(theta), v * np.sin(theta), 'r--', linewidth=2,
            label=f'真空期望值 |φ| = {v:.2f}')

    # 标记几个真空态
    thetas = [0, np.pi/2, np.pi, 3*np.pi/2]
    for theta in thetas:
        ax.plot(v * np.cos(theta), v * np.sin(theta), 'bo', markersize=8)

    # 添加图例和标注
    ax.set_xlabel('φ₁', fontsize=12)
    ax.set_ylabel('φ₂', fontsize=12)
    ax.set_title('墨西哥帽势能：对称性自发破缺', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    # 添加势能公式
    ax.text(0, -2.8, r'$V(φ) = \mu^2|φ|^2 + \lambda|φ|^4$',
            ha='center', fontsize=13, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 图11: 标准模型粒子谱 ====================
def figure11_standard_model():
    """标准模型粒子谱：展示三代费米子、规范玻色子和希格斯标量的完整分类"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # 定义粒子
    quarks = {
        '上': [2.2, 1.27, 172000],
        '下': [4.7, 2.9, 4200],
        '粲': [1275, 127, 171000]
    }
    leptons = {
        '电子': [0.511, 105.7, 1777],
        '中微子': [0, 7.5e-4, 17.7e-3]
    }
    gauge_bosons = {
        '光子': [0, 0, 0],
        'W玻色子': [80.4, 91.2, 0],
        'Z玻色子': [91.2, 0, 0],
        '胶子': [0, 0, 0]
    }

    colors_quarks = ['#e74c3c', '#e67e22', '#f1c40f']
    colors_leptons = ['#3498db', '#9b59b6']
    colors_bosons = ['#2ecc71', '#1abc9c', '#16a085', '#27ae60']
    colors_higgs = ['#e056fd', '#8e44ad']

    y_pos = 0
    bar_height = 0.6

    # 费米子
    y_pos = 8
    ax.text(-0.5, y_pos, '费米子', fontsize=12, fontweight='bold', va='center')
    ax.axhline(y_pos - bar_height*1.5, color='gray', linestyle='-', alpha=0.3)

    # 夸克
    y_pos = 7
    for i, (quark, masses) in enumerate(quarks.items()):
        for gen, mass in enumerate(masses):
            bar = Rectangle((gen*2.5, y_pos - bar_height/2), 2, bar_height,
                           color=colors_quarks[i], alpha=0.7, label=f'{quark}' if gen==0 else '')
            ax.add_patch(bar)
            ax.text(gen*2.5 + 1, y_pos, f'{mass:g}', ha='center', va='center',
                    fontsize=9, color='white')
        y_pos -= 1

    # 轻子
    y_pos = 7
    for i, (lepton, masses) in enumerate(leptons.items()):
        for gen, mass in enumerate(masses):
            bar = Rectangle((gen*2.5 + 7.5, y_pos - bar_height/2), 2, bar_height,
                           color=colors_leptons[i], alpha=0.7, label=f'{lepton}' if gen==0 else '')
            ax.add_patch(bar)
            label = f'{mass:g}' if mass > 0 else '未测'
            ax.text(gen*2.5 + 8.5, y_pos, label, ha='center', va='center',
                    fontsize=9, color='white')
        y_pos -= 1

    # 规范玻色子
    y_pos = 7
    ax.text(14.5, y_pos, '规范玻色子', fontsize=12, fontweight='bold', va='center')
    ax.axhline(y_pos - bar_height*4.5, color='gray', linestyle='-', alpha=0.3)

    boson_names = list(gauge_bosons.keys())
    boson_masses = list(gauge_bosons.values())
    for i, (name, masses) in enumerate(gauge_bosons.items()):
        for gen, mass in enumerate(masses):
            bar = Rectangle((15, y_pos - bar_height/2), 2.5, bar_height,
                           color=colors_bosons[i], alpha=0.7, label=name if gen==0 else '')
            ax.add_patch(bar)
            ax.text(16.25, y_pos, f'{mass}' if mass > 0 else '0', ha='center',
                    va='center', fontsize=10, color='white')
        y_pos -= 1.1

    # 希格斯玻色子
    y_pos = 2
    higgs = Rectangle((15, y_pos - bar_height/2), 2.5, bar_height,
                    color=colors_higgs[0], alpha=0.7, label='希格斯')
    ax.add_patch(higgs)
    ax.text(16.25, y_pos, '125', ha='center', va='center', fontsize=10, color='white')

    ax.set_xlim(-1, 20)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('标准模型粒子谱', fontsize=14, fontweight='bold')

    # 添加代标签
    ax.text(1, 9.2, '第一代', ha='center', fontsize=11)
    ax.text(3.5, 9.2, '第二代', ha='center', fontsize=11)
    ax.text(6, 9.2, '第三代', ha='center', fontsize=11)

    # 图例
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=colors_quarks[0], label='上型夸克'),
        Patch(facecolor=colors_quarks[1], label='下型夸克'),
        Patch(facecolor=colors_quarks[2], label='粲型夸克'),
        Patch(facecolor=colors_leptons[0], label='带电轻子'),
        Patch(facecolor=colors_leptons[1], label='中微子'),
        Patch(facecolor=colors_bosons[0], label='光子'),
        Patch(facecolor=colors_bosons[1], label='W/Z玻色子'),
        Patch(facecolor=colors_bosons[3], label='胶子'),
        Patch(facecolor=colors_higgs[0], label='希格斯')
    ]
    ax.legend(handles=legend_elements, loc='lower left', ncol=3, fontsize=9)

    # 质量单位标注
    ax.text(10, -0.5, '质量单位：MeV（未标注的为0或极小）',
            ha='center', fontsize=10, style='italic')

    plt.tight_layout()
    return fig


# ==================== 图12: 费米子质量层级 ====================
def figure12_fermion_mass_hierarchy():
    """费米子质量层级：展示三代费米子的质量分布（对数尺度）"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # 费米子质量（MeV）
    fermions = {
        '电子': 0.511,
        'μ子': 105.7,
        'τ子': 1777,
        '上夸克': 2.2,
        '下夸克': 4.7,
        '粲夸克': 1275,
        '顶夸克': 172000,
        '奇异夸克': 95,
        '底夸克': 4200,
        '电子中微子': 1e-5,
        'μ子中微子': 0.17,
        'τ子中微子': 17.7
    }

    categories = {
        '带电轻子': ['电子', 'μ子', 'τ子'],
        '中微子': ['电子中微子', 'μ子中微子', 'τ子中微子'],
        '上型夸克': ['上夸克', '粲夸克', '顶夸克'],
        '下型夸克': ['下夸克', '奇异夸克', '底夸克']
    }

    colors = ['#3498db', '#9b59b6', '#e74c3c', '#f39c12', '#27ae60']

    x = np.arange(len(fermions))
    masses = list(fermions.values())
    names = list(fermions.keys())

    # 按类别着色
    color_map = []
    for name in names:
        for i, (cat, parts) in enumerate(categories.items()):
            if name in parts:
                color_map.append(colors[i])
                break

    bars = ax.bar(x, masses, color=color_map, alpha=0.7, edgecolor='black')

    ax.set_yscale('log')
    ax.set_xlabel('费米子', fontsize=12)
    ax.set_ylabel('质量', fontsize=12)
    ax.set_title('费米子质量层级（对数尺度）', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, which='both', axis='y')

    # 在柱子上标注数值
    for bar, mass in zip(bars, masses):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
                f'{mass:.1e}', ha='center', va='bottom', fontsize=7)

    # 添加质量区间标注
    ax.axhspan(1e-3, 1, alpha=0.05, color='gray', label='轻子区')
    ax.axhspan(1, 1e5, alpha=0.05, color='yellow', label='夸克区')

    # 图例
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=colors[0], label='带电轻子'),
        Patch(facecolor=colors[1], label='中微子'),
        Patch(facecolor=colors[2], label='上型夸克'),
        Patch(facecolor=colors[3], label='下型夸克')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

    plt.tight_layout()
    return fig


# ==================== 图13: 规范耦合常数的大统一 ====================
def figure13_gut_unification():
    """规范耦合常数的大统一：展示SU(3)、SU(2)、U(1)耦合常数在GUT能标处的汇聚"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # 能标（对数）
    energy = np.log10(np.array([10, 100, 1000, 1e4, 1e5, 1e6, 1e7, 1e8, 1e10, 1e12, 1e14, 1e16]))

    # 耦合常数倒数（随能标演化）
    # α1 = 5/3 * α_Y, α2 = α_weak, α3 = α_strong
    # 在低能：α1⁻¹ ≈ 59, α2⁻¹ ≈ 30, α3⁻¹ ≈ 8.5

    alpha1_inv = 59 + 10 * energy / energy[-1]
    alpha2_inv = 30 + 8 * energy / energy[-1]
    alpha3_inv = 8.5 - 3 * energy / energy[-1] + 5 * (energy/energy[-1])**2

    ax.plot(energy, alpha1_inv, 'b-', linewidth=2.5, label=r'$\alpha_1^{-1}$ (U(1))')
    ax.plot(energy, alpha2_inv, 'g-', linewidth=2.5, label=r'$\alpha_2^{-1}$ (SU(2))')
    ax.plot(energy, alpha3_inv, 'r-', linewidth=2.5, label=r'$\alpha_3^{-1}$ (SU(3))')

    # 标记汇聚点
    ax.axvline(16, color='gray', linestyle='--', alpha=0.5)
    ax.text(16, 50, 'GUT能标', fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

    # 标记低能测量点
    ax.text(2, alpha1_inv[0], 'α⁻¹≈59', fontsize=9, color='blue')
    ax.text(2, alpha2_inv[0], 'α⁻¹≈30', fontsize=9, color='green')
    ax.text(2, alpha3_inv[0], 'α⁻¹≈8.5', fontsize=9, color='red')

    ax.set_xlabel('能标', fontsize=12)
    ax.set_ylabel('耦合常数倒数', fontsize=12)
    ax.set_title('规范耦合常数的大统一', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


# ==================== 图14: 孤子解 ====================
def figure14_soliton_solutions():
    """孤子解：展示能量场的扭结解和反扭结解，对应于基本粒子"""
    fig, ax = plt.subplots(figsize=(12, 5))

    x = np.linspace(-8, 8, 500)

    # 扭结解
    tanh_kink = np.tanh(x)
    # 反扭结解
    tanh_anti_kink = -np.tanh(x)
    # 呼息子解
    sech_breather = 0.5 * np.tanh(x) * (1 / np.cosh(x)) * np.cos(5*x)

    ax.plot(x, tanh_kink, 'b-', linewidth=2.5, label='扭结解')
    ax.plot(x, tanh_anti_kink, 'r--', linewidth=2.5, label='反扭结解')
    ax.plot(x, sech_breather, 'g-.', linewidth=2, label='呼吸子解')

    ax.set_xlabel('位置 x', fontsize=12)
    ax.set_ylabel('能量场 E(x)', fontsize=12)
    ax.set_title('孤子解：扭结、反扭结与呼吸子', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)

    # 标注
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(0, color='gray', linestyle=':', alpha=0.5)
    ax.text(0, -1.2, 'x=0', ha='center', fontsize=10)
    ax.text(5, 0.8, '粒子', fontsize=10, color='blue', fontweight='bold')
    ax.text(-5, -0.8, '反粒子', fontsize=10, color='red', fontweight='bold')

    plt.tight_layout()
    return fig


# ==================== 图15: 量子隧穿示意图 ====================
def figure15_quantum_tunneling():
    """量子隧穿示意图：展示能量场在势垒中的渗透过程"""
    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.linspace(-4, 4, 500)

    # 势垒
    V = np.zeros_like(x)
    V[(x >= -1) & (x <= 1)] = 2

    # 粒子能量
    E = 1
    ax.axhline(E, color='g', linestyle='--', linewidth=2, label='粒子能量 E')

    # 势垒区域填充
    ax.fill_between(x, 0, V, where=(V > 0), alpha=0.2, color='red', label='势垒 V')
    ax.plot(x, V, 'r-', linewidth=2)

    # 波函数（在势垒内指数衰减）- 修复数组索引问题
    psi = np.zeros_like(x, dtype=complex)
    mask_left = x < -1
    mask_barrier = (x >= -1) & (x <= 1)
    mask_right = x > 1

    psi[mask_left] = np.exp(1j * np.sqrt(2) * (x[mask_left] + 1))
    psi[mask_barrier] = np.exp(-np.sqrt(2) * (x[mask_barrier] + 1))
    psi[mask_right] = np.exp(-np.sqrt(2) * 2) * np.exp(1j * np.sqrt(2) * (x[mask_right] - 1))

    # 归一化
    psi_abs = np.abs(psi)
    psi_abs /= np.max(psi_abs)

    ax2 = ax.twinx()
    ax2.plot(x, psi_abs, 'b-', linewidth=2, label='波函数 |ψ|²')
    ax2.fill_between(x, psi_abs, alpha=0.3, color='blue')

    ax.set_xlabel('位置 x', fontsize=12)
    ax.set_ylabel('势能 V', fontsize=12)
    ax2.set_ylabel('波函数幅值', color='blue', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='blue')

    ax.set_title('量子隧穿：能量场在势垒中的渗透', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)

    # 标注
    ax.text(0, 2.3, '经典禁区 (E < V)', ha='center', fontsize=10,
            color='red', fontweight='bold')
    ax2.text(-3, 0.8, '入射波', ha='center', fontsize=10, color='blue')
    ax2.text(3, 0.1, '透射波', ha='center', fontsize=10, color='blue')

    plt.tight_layout()
    return fig


# ==================== 图16: 双缝干涉图样 ====================
def figure16_double_slit():
    """双缝干涉图样：展示能量场通过双缝后的干涉条纹"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # 干涉图样
    x = np.linspace(-5, 5, 500)
    wavelength = 0.5
    slit_separation = 2
    screen_distance = 10

    # 双缝干涉强度
    k = 2 * np.pi / wavelength
    beta = k * slit_separation * x / (2 * screen_distance)
    intensity = np.cos(beta)**2 * (np.sin(k * 0.1 * x / screen_distance) /
                                      (k * 0.1 * x / screen_distance))**2

    ax1.plot(x, intensity, 'b-', linewidth=1.5)
    ax1.fill_between(x, intensity, alpha=0.5, color='blue')

    # 模拟干涉条纹
    x_img = np.linspace(-5, 5, 300)
    y_img = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(x_img, y_img)
    beta_img = k * slit_separation * X / (2 * screen_distance)
    I = np.cos(beta_img)**2

    ax2.imshow(I, extent=[-5, 5, -3, 3], origin='lower', cmap='Blues', aspect='auto')

    ax1.set_xlabel('屏幕位置 x', fontsize=12)
    ax1.set_ylabel('强度 I', fontsize=12)
    ax1.set_title('干涉强度分布', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    ax2.set_xlabel('屏幕位置 x', fontsize=12)
    ax2.set_ylabel('屏幕位置 y', fontsize=12)
    ax2.set_title('干涉条纹', fontsize=11, fontweight='bold')

    # 标记干涉极大值
    max_positions = []
    for i in range(-5, 6):
        pos = i * wavelength * screen_distance / slit_separation
        if abs(pos) <= 5:
            max_positions.append(pos)
            ax1.axvline(pos, color='red', linestyle=':', alpha=0.5)

    plt.tight_layout()
    return fig


# ==================== 图17: 中微子振荡概率 ====================
def figure17_neutrino_oscillation():
    """中微子振荡概率：展示不同中微子味之间的振荡模式"""
    fig, ax = plt.subplots(figsize=(12, 6))

    L_over_E = np.linspace(0, 500, 500)

    # 混合角（PMNS参数近似）
    theta12 = np.radians(33.5)
    theta23 = np.radians(45)
    theta13 = np.radians(8.6)

    # 两味振荡概率简化版
    P_mue = np.sin(2 * theta12)**2 * np.sin(1.27 * 7.5e-5 * L_over_E)**2
    P_mut = np.sin(2 * theta12)**2 * np.sin(1.27 * 0.0025 * L_over_E)**2

    ax.plot(L_over_E, P_mue, 'b-', linewidth=2.5, label=r'$\nu_\mu \to \nu_e$')
    ax.plot(L_over_E, P_mut, 'g-', linewidth=2.5, label=r'$\nu_\mu \to \nu_\tau$')

    # 标记完全振荡点
    max_L_mue = np.pi / (1.27 * 7.5e-5) / 1.27
    ax.axvline(max_L_mue * 1.27 / 1.27, color='blue', linestyle='--', alpha=0.5)
    ax.text(max_L_mue * 1.27 / 1.27, 0.5, '第一次振荡', fontsize=9, ha='center')

    ax.set_xlabel('L/E (km/GeV)', fontsize=12)
    ax.set_ylabel('振荡概率', fontsize=12)
    ax.set_title('中微子振荡概率', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)

    # 添加说明
    ax.text(250, 0.2, r'$P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta)\sin^2(1.27\Delta m^2 L/2E)$',
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 图18: 引力波频谱衰减 ====================
def figure18_gravitational_wave():
    """引力波频谱衰减：展示NEFT预言的高频引力波振幅衰减效应"""
    fig, ax = plt.subplots(figsize=(10, 6))

    frequency = np.logspace(0, 4, 300)

    # 标准GR预言（无衰减）
    h_GR = 1 / frequency

    # NEFT预言（有衰减）
    f_cutoff = 100
    h_NEFT = 1 / frequency * np.exp(-(frequency / f_cutoff)**0.5)

    ax.loglog(frequency, h_GR, 'r-', linewidth=2.5, label='标准GR (无衰减)')
    ax.loglog(frequency, h_NEFT, 'b-', linewidth=2.5, label='NEFT (有衰减)')

    # 标记衰减起始点
    ax.axvline(f_cutoff, color='gray', linestyle='--', alpha=0.5)
    ax.text(f_cutoff*1.5, h_NEFT[150]*10, '衰减起始', fontsize=9)

    # 标注频段
    ax.text(2, h_GR[10], 'LIGO频段', fontsize=9)
    ax.text(1000, h_GR[100], '高频段', fontsize=9)

    ax.set_xlabel('频率', fontsize=12)
    ax.set_ylabel('振幅 |h(ω)|', fontsize=12)
    ax.set_title('引力波频谱衰减：NEFT的预言', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)

    # 添加衰减公式
    ax.text(500, 1e-7, r'$|h(\omega)| \propto \omega^{-1} e^{-\sqrt{\omega/\omega_c}}$',
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 图19: 精细结构常数的跑动 ====================
def figure19_fine_structure_constant():
    """精细结构常数的跑动：展示α在不同能标下的演化"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # 能标
    mu = np.logspace(-1, 5, 500)

    # 精细结构常数的跑动（简化版）
    alpha_inv_MZ = 127.9  # Z玻色子能标处
    ln_ratio = np.log(mu / 1e5)  # 相对于电质量的能标比

    # 单圈近似 + NEFT修正
    alpha_inv = alpha_inv_MZ - (2/(3*np.pi)) * ln_ratio + 0.1 * np.sin(ln_ratio/10)

    # 转换为α
    alpha = 1 / alpha_inv

    ax.loglog(mu, alpha, 'b-', linewidth=2.5)
    ax.fill_between(mu, alpha, alpha*0.95, alpha*1.05, alpha=0.2, color='blue')

    # 标记关键能标
    ax.axvline(0.511, color='green', linestyle='--', alpha=0.5)
    ax.text(0.5, alpha[10], 'm_e', ha='center', fontsize=9, color='green')

    ax.axvline(91.1876e3, color='orange', linestyle='--', alpha=0.5)
    ax.text(91.1876e3*2, alpha[200], 'M_Z', ha='center', fontsize=9, color='orange')

    ax.axvline(1.7e5, color='red', linestyle='--', alpha=0.5)
    ax.text(1.7e5*2, alpha[300], 'M_W', ha='center', fontsize=9, color='red')

    # 标记实验值
    alpha_exp = 1/137.035999084
    ax.axhline(alpha_exp, color='gray', linestyle=':', alpha=0.7)
    ax.text(1e-1, alpha_exp*1.05, '实验值 α⁻¹≈137.036', fontsize=9,
            ha='center', va='bottom')

    ax.set_xlabel('能标 μ (MeV)', fontsize=12)
    ax.set_ylabel('精细结构常数 α', fontsize=12)
    ax.set_title('精细结构常数的跑动', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # 添加公式
    ax.text(1e4, 0.005, r'$\frac{d\alpha}{d\ln\mu} = \frac{2\alpha^2}{3\pi} + \cdots$',
            fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 图20: 熵饱和曲线 ====================
def figure20_entropy_saturation():
    """熵饱和曲线：展示NEFT预言的熵饱和现象"""
    fig, ax = plt.subplots(figsize=(10, 6))

    t = np.linspace(0, 20, 500)

    # 熵的增长（饱和曲线）
    S_max = 100
    S = S_max * (1 - np.exp(-t/5)) * (1 - 0.1 * np.exp(-t/2))
    dS = np.gradient(S)

    ax.plot(t, S, 'b-', linewidth=2.5, label='熵 S')
    ax.fill_between(t, S, alpha=0.3, color='blue')

    # 熵产率
    ax2 = ax.twinx()
    ax2.plot(t, dS, 'r-', linewidth=2, label='熵产率 dS/dt')

    ax.set_xlabel('时间 t', fontsize=12)
    ax.set_ylabel('熵 S', color='blue', fontsize=12)
    ax2.set_ylabel('熵产率', color='red', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='red')

    # 标记饱和点
    saturation_point = 15
    ax.axvline(saturation_point, color='green', linestyle='--', alpha=0.5)
    ax.text(saturation_point, S[-1]*0.9, '接近饱和', ha='center', fontsize=10)

    # 标记最大熵
    ax.axhline(S_max, color='gray', linestyle=':', alpha=0.7)
    ax.text(5, S_max*1.02, f'S_max = {S_max}', fontsize=10, ha='center')

    ax.set_title('NEFT熵饱和曲线', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=11)
    ax2.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)

    # 添加说明
    ax.text(10, 0.005, '当熵接近最大值时，\n熵产率显著下降',
            fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

    plt.tight_layout()
    return fig


# ==================== 主函数：生成所有图表 ====================
def main():
    """生成所有论文图表"""
    print("开始生成NEFT论文图表...")
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
        fig = generator()
        save_figure(fig, filename)

    print()
    print(f"共生成 {len(figure_generators)} 张图表")
    print(f"图表保存在: {output_dir}/")


if __name__ == "__main__":
    main()
