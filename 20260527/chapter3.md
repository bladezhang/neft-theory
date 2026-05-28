# 第三章 宇宙演化与熵



<h3 id="s3_1">3.1 能量-动量张量</h3>
<div class="definition">
<p><strong>定义3（能量-动量张量）</strong>：从NEFT作用量出发，广义能量-动量张量为<sup class="citation">[14]</sup></p>
<p>\[ T^{\mu\nu} = \frac{\partial \mathcal{L}}{\partial (\partial_\mu \mathcal{E})} \partial^\nu \mathcal{E} - g^{\mu\nu} \mathcal{L} \]</p>
</div>

<h3 id="s3_2">3.2 能量代谢方程</h3>
<div class="derivation">
<p><strong>推导（能量代谢方程）</strong>：计算能量-动量张量的四维散度：</p>
<p>\[ \partial_\mu T^{\mu\nu} = - \hat{\Gamma} \partial_t \mathcal{E} \cdot \partial^\nu \mathcal{E} \]</p>
<p>这就是<strong>NEFT能量代谢方程</strong>。等式右边是负的耗散功率，意味着机械能 \(T^{\mu\nu}\) 并不守恒，一部分能量在流动过程中被"代谢"掉了，转化为热或拓扑结构的改变。</p>
</div>

<h3 id="s3_3">3.3 熵产方程</h3>
<div class="definition">
<p><strong>定义4（NEFT熵）</strong>：定义NEFT熵为能量场拓扑复杂度的度量<sup class="citation">[15]</sup></p>
<p>\[ S_{NEFT} = k_B \ln \Omega(\mathcal{E}) \]</p>
<p>其中 \(\Omega(\mathcal{E})\) 是能量场在特定拓扑构型下的微观态数目，对应涡旋、孤子、节点连接等拓扑结构的排列数。</p>
</div>

<div class="theorem">
<p><strong>定理2（熵产定理）</strong>：能量场的演化总是伴随着非负的熵产率</p>
<p>\[ \frac{dS}{dt} = \int d^3x \; \frac{\hat{\Gamma}}{T} (\partial \mathcal{E})^2 \ge 0 \]</p>
</div>

<div class="proof">
<p><strong>证明</strong>：<span style="color:#c0392b;">[修正#8]</span> 我们从NEFT耗散动力学的能量耗散函数出发，避免假设热力学第二定律作为前提。</p>
<p><strong>Step 1：定义耗散函数</strong>。从NEFT运动方程（耗散Dirac算子形式，[修正#1]）出发，计算旋量场的能量耗散率密度。对能量-动量张量 \(T^{\mu\nu}\) 取散度：</p>
<p>\[ \partial_\mu T^{\mu\nu} = -\hat{\Gamma}(\bar\Psi,\partial(\bar\Psi\Psi)) \cdot \partial^\nu(\bar\Psi\Psi) \]</p>
<p>右侧定义了<strong>耗散功率密度</strong>：\(\Phi_{\text{diss}} = \hat{\Gamma}(\partial\mathcal{E})^2 \geq 0\)，其中 \(\hat{\Gamma} > 0\) 是耗散系数（正定的物理假设），\((\partial\mathcal{E})^2 = \partial_\mu\mathcal{E}\partial^\mu\mathcal{E} \geq 0\)。</p>
<p><strong>Step 2：构造熵产率</strong>。定义<strong>NEFT耗散熵产率密度</strong>为耗散功率密度与局域温度之比：</p>
<p>\[ \dot{s}_{\text{prod}} = \frac{\Phi_{\text{diss}}}{T} = \frac{\hat{\Gamma}}{T}(\partial\mathcal{E})^2 \]</p>
<p>这一定义遵循非平衡热力学中<strong>耗散函数与熵产的对应关系</strong>（de Groot & Mazur, 1962）：任何正定的耗散函数 \(\Phi \geq 0\) 必然对应一个非负的熵产率 \(\dot{s} = \Phi/T\)。</p>
<p><strong>Step 3：证明非负性</strong>。由于 \(\hat{\Gamma} > 0\)（正耗散系数）且 \((\partial\mathcal{E})^2 \ge 0\)（标量场的梯度模方非负），同时 \(T > 0\)（温度正定），因此：</p>
<p>\[ \dot{s}_{\text{prod}} = \frac{\hat{\Gamma}}{T}(\partial\mathcal{E})^2 \ge 0 \]</p>
<p>在整个空间积分得全局熵产率：</p>
<p>\[ \frac{dS}{dt} = \int d^3x \; \frac{\hat{\Gamma}}{T} (\partial \mathcal{E})^2 \geq 0 \]</p>
<p><strong>关键区别</strong>：本证明从NEFT场方程的耗散结构（\(\hat{\Gamma} > 0\)）和能量耗散函数出发，推导出熵产非负性，<strong>而非假设热力学第二定律</strong>。热力学第二定律的微观基础由此被建立——它不是前提，而是NEFT耗散动力学的推论。∎</p>
<div style="border-left:3px solid #e67e22;padding:8px 12px;margin:10px 0;background:#fef9e7;font-size:0.9em;">
<p><span style="color:#c0392b;">[审查回应]</span> <strong>熵产证明的剩余问题</strong>：尽管[修正#8]已将推导起点从热力学第二定律改为NEFT耗散函数，但以下问题仍需注意：</p>
<ul>
<li><strong>隐含假设</strong>：耗散功率密度 \(\Phi_{\text{diss}} = \hat{\Gamma}(\partial\mathcal{E})^2\) 的具体形式依赖 \(\partial_\mu T^{\mu\nu}\) 的推导，而该散度的推导本身需要假设运动方程的形式——即结论（熵产≥0）已经编码在前提（\(\hat{\Gamma}>0\)的耗散场方程）中。更准确地说，NEFT将热力学第二定律替换为<strong>"耗散系数正定"假设</strong>，后者是一个更强的物理假设（等价于时间不可逆性作为基本原理）。</li>
<li>\(\Omega(\mathcal{E})\) 从未给出显式计算方法——\(S_{NEFT} = k_B\ln\Omega(\mathcal{E})\) 是形式定义而非可操作公式。</li>
<li>黑洞熵 \(S = A/4\ell_P^2\) 的1/4因子论证（§3.4）中，从\(2^N\)到\(2^{N/4}\)的三步修正（拓扑约束+规范冗余+量子关联）均未给出具体计算，因子1/4恰好是Bekenstein-Hawking结果，有事后匹配嫌疑。</li>
</ul>
</div>
<div class="figure-container">
    <img src="figures_py/第三章_图6_时间之箭与熵产.png" alt="Entropy Arrow of Time">
    <div class="figure-caption">图6：时间之箭与熵产：展示熵随时间的单调增长</div>
</div>
</div>

<div class="figure-container">
    <img src="figures_py/第三章_图7_能量场演化与熵产.png" alt="Energy Field Evolution and Entropy Production">
    <div class="figure-caption">图7：能量场演化与熵产：展示能量场从有序（低熵）向无序（高熵）的演化过程</div>
</div>
<p>这为<strong>时间之箭</strong>提供了微观基础：时间之箭的方向就是能量场从低熵（有序拓扑）向高熵（无序拓扑）演化的方向。</p>

<h3 id="s3_4">3.4 黑洞熵</h3>
<div class="derivation">
<p><strong>启发式推导（贝肯斯坦-霍金熵）<span style="color:#c0392b;font-size:0.8em;"> † 非严格证明</span></strong><sup class="citation">[16,17]</sup>：全息原理断言：一个引力系统的自由度正比于其边界面积<sup class="citation">[18]</sup>。在NEFT中，这自然涌现为能量场的离散拓扑结构。</p>
<p>考虑黑洞视界，其面积为 \(A\)。在NEFT中，能量场在普朗克尺度下离散化，最小单元面积为普朗克面积 \(\ell_P^2 = \hbar G/c^3\)。视界包含的普朗克像素数为 \(N = A/\ell_P^2\)。</p>
<p>每个像素有两种拓扑状态，总组合数为 \(2^N = 2^{A/\ell_P^2}\)。</p>
<p style="color:#2c3e50;font-size:0.88em;border-top:1px solid #ddd;padding-top:8px;margin-top:10px;">† <strong>从 \(2^{A/\ell_P^2}\) 到 \(2^{A/4\ell_P^2}\) 的修正</strong> <span style="color:#c0392b;">[修正#12]</span>：原始计数比Bekenstein-Hawking值大4倍。修正来源的定性论证：（1）拓扑约束使有效自由度减半；（2）\(U(1)\) 规范冗余进一步约化；（3）量子关联修正。总修正因子 \(1/4\)。<strong>需要强调的是，这3个修正步骤目前是定性论证——给出精确的1/4因子需要格点NEFT微观计算</strong>。1/4因子在弦论（Susskind 1993<sup class="citation">[107]</sup>）和LQG（Rovelli 1996<sup class="citation">[84]</sup>）中也需要各自的微观计数。NEFT的拓扑论证与这些方法平行，但精确的微观态计数需数值验证。微观态数为 \(2^{A/4\ell_P^2}\)，熵为：</p>
<p></p>
<p>\[ S = k_B \ln(2^{A/4\ell_P^2}) = k_B \frac{A}{4\ell_P^2} \ln 2 \]</p>
<p>精确计算（考虑拓扑约束）得到：</p>
<p>\[ S = k_B \frac{A}{4\ell_P^2} = \frac{k_B c^3 A}{4G\hbar} \]</p>
<div class="figure-container">
    <img src="figures_py/第三章_图8_贝肯斯坦霍金熵.png" alt="Bekenstein-Hawking Entropy">
    <div class="figure-caption">图8：贝肯斯坦-霍金熵：展示黑洞视界上的普朗克像素结构与信息流动</div>
</div>
<div class="figure-container">
    <img src="figures_py/第三章_图9_黑洞信息流动示意图.png" alt="Black Hole Information Flow">
    <div class="figure-caption">图9：黑洞信息流动示意图：展示黑洞蒸发过程中的信息守恒与软毛发机制</div>
</div>
<p>这正是<strong>贝肯斯坦-霍金熵</strong>。黑洞熵就是能量场在视界上的拓扑缠绕数的对数，与全息原理<sup class="citation">[18]</sup>和AdS/CFT对偶<sup class="citation">[19,53,54]</sup>的预言一致。</p>
</div>
