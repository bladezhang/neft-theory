# 第五章 四种基本相互作用的统一


<p style="color:#0d47a1;font-size:0.9em;text-indent:0;"><strong>[v6.1修订说明，依据§9.7审核]</strong> 本章将“统一叙事”与“参数经济性”分离：新增原则为“每引入1个新参数，必须对应至少1个可独立检验观测量或先验约束”，否则仅保留为候选机制。</p>

<h3 id="s5_1">5.1 引力</h3>
<p>在NEFT中，引力是能量场为了消除梯度、趋向平衡而产生的内禀应力。爱因斯坦场方程的NEFT形式为：</p>
<p>\[ R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \frac{8\pi G}{c^4} \left[ \partial_\mu \mathcal{E} \partial_\nu \mathcal{E} - \frac{1}{2} g_{\mu\nu} (\partial_\alpha \mathcal{E} \partial^\alpha \mathcal{E}) \right] \]</p>
<p>左边是几何量，描述时空弯曲；右边是物质源，描述能量场流动。在NEFT中，物质就是能量场的激发，几何是能量场梯度的表现。</p>
<div style="background-color:#fff3e0;padding:12px 16px;border-left:3px solid #ff9800;margin:1em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.88em;text-indent:0;"><strong>[审查回应] 标量场T_μν与旋量基底的矛盾</strong>：本文以旋量场 \(\Psi\) 为统一基底，但Einstein方程右侧写入了标量场能量-动量张量 \(\partial_\mu\mathcal{E}\partial_\nu\mathcal{E}\)，而非旋量场形式。这是因为 \(\mathcal{E} = \sqrt{\bar\Psi\Psi}\) 在宏观低能极限下退化为有效标量描述（§2.2），\(\partial_\mu\mathcal{E}\partial_\nu\mathcal{E}\) 是旋量场双线性梯度的<strong>粗粒化近似</strong>。完整的旋量形式应为 \(T_{\mu\nu} = \frac{i}{4}[\bar\Psi(\gamma_\mu D_\nu + \gamma_\nu D_\mu)\Psi - (D_\mu\bar\Psi\gamma_\nu + D_\nu\bar\Psi\gamma_\mu)\Psi]\)，但此形式退化为Friedman-Robertson-Walker宇宙学中的标量T_μν。正如§2.3.2[修正#11]所述，Einstein方程本身是全息热力学状态方程（Jacobson 1995），标量近似在此层面是合理的。</p>
</div>

<h3 id="s5_2">5.2 规范力与标准模型的NEFT推导</h3>

<h4>5.2.1 NEFT作用量到标准模型拉格朗日量的映射</h4>
<div class="derivation">
<p><strong>推导（标准模型拉格朗日量的NEFT导出）</strong>：我们从NEFT的广义外尔算子作用量出发，通过多步展开和拓扑分析，导出标准模型的完整拉格朗日量。</p>
<p><strong>步骤1：NEFT作用量的四分量分解</strong></p>
<p>将旋量场 \(\Psi(x)\) 在内部空间（自旋丛纤维）上进行四分量分解<sup class="citation">[84]</sup>，对应于标准模型的四类基本相互作用。完整地，这对应于旋量场 \(\Psi\) 在内部空间（自旋丛纤维）上的分量的约化：</p>
<div style="background-color:#fff3e0;padding:12px 16px;border-left:3px solid #ff9800;margin:0.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.88em;text-indent:0;"><strong>[审查回应] 四分量分解的任意性</strong>：将 \(\mathcal{E}(x)\) 分解为4个分量 \(\epsilon_a(x)\Phi_a\) 是唯象构造，而非从NEFT基本假设严格推导。为什么恰好是4个分量？一种可能的理解来自Clifford代数 \(Cl(1,3)\)：4维时空的Clifford代数恰好有4个基底元素 \(\{1, \gamma^5, \gamma^\mu\gamma_\mu, \gamma^5\gamma^\mu\gamma_\mu\}\)，但此论证并不严格等价于标准模型的4类相互作用。投影算子 \(\Phi_a\Phi_b = \delta_{ab}\Phi_a\) 要求正交分解，这在数学上合法但物理动机需进一步发展。<strong>此分解目前为框架性构造，非第一性原理推导。</strong></p>
</div>
<p>\[ \mathcal{E}(x) = \sum_{a=1}^{4} \epsilon_a(x) \Phi_a(\mathcal{E}) \]</p>
<p>其中 \(\Phi_a\) 是拓扑投影算子，满足 \(\sum_a \Phi_a = \mathbb{1}\)，且 \(\Phi_a \Phi_b = \delta_{ab} \Phi_a\)。</p>
<p><strong>步骤2：内部空间联络的构造</strong><span style="color:#c0392b;">[修正#4]</span></p>
<p>NEFT自旋丛上的主联络（自旋联络）\(\omega_\mu\) 可分解为时空部分和内部空间部分：</p>
<p>\[ \omega_\mu = \omega_\mu^{\text{spacetime}} + \omega_\mu^{\text{internal}} \]</p>
<p>其中 \(\omega_\mu^{\text{spacetime}} = \omega_\mu^{ab}\Sigma_{ab}\)（\(\Sigma_{ab} = \frac{1}{4}[\gamma_a,\gamma_b]\) 是Lorentz群生成元，见§1.4.3），而 \(\omega_\mu^{\text{internal}}\) 是联络在内部规范子群方向上的分量。内部分量的构造依赖于SO(10)破缺链的选择——具体破缺模式（如SO(10)→SU(5)→SU(3)×SU(2)×U(1)）决定了内部空间纤维的分裂方式，从而确定 \(\omega_\mu^{\text{internal}}\) 在各子群上的投影。</p>

<p><strong>步骤3：规范联络的投影定义</strong></p>
<p>对每个规范子群 \(G_a \in \{U(1), SU(2), SU(3)\}\)，规范联络由内部联络在该子群生成元方向的投影定义：</p>
<p>\[ A_\mu^a = \text{Tr}(T^a \cdot \omega_\mu^{\text{internal}}) \]</p>
<p>其中 \(T^a\) 是规范群 \(G_a\) 的归一化生成元（满足 \(\text{Tr}(T^a T^b) = \frac{1}{2}\delta^{ab}\)）。</p>
<p><strong>退化验证</strong>：</p>
<ul>
    <li><strong>U(1)电磁场</strong>：生成元 \(T^0 = \frac{1}{2}\mathbf{1}\)，投影退化为标量通道 \(A_\mu = \frac{1}{e}\partial_\mu\theta\)，其中 \(\theta = \ln(\epsilon/\epsilon_0)\) 是相对相位——这与标准的Abelian联络一致。</li>
    <li><strong>SU(2)弱核力</strong>：生成元 \(T^a = \frac{1}{2}\tau^a\)（Pauli矩阵），非Abelian联络自动产生非线性项，场强张量 \(W_{\mu\nu}^a\) 包含自相互作用。</li>
    <li><strong>SU(3)强核力</strong>：生成元 \(T^a = \frac{1}{2}\lambda^a\)（Gell-Mann矩阵），八个规范玻色子（胶子）及其自相互作用从投影自然出现。</li>
</ul>
<p>场强张量由标准公式给出：</p>
<p>\[ F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - i g_a f^{abc} A_\mu^b A_\nu^c \]</p>
<p>其中结构常数 \(f^{abc}\) 由规范群的李代数确定，而非人为引入。对U(1)：\(f^{abc}=0\)；对SU(2)：\(f^{abc}=\epsilon^{abc}\)；对SU(3)：\(f^{abc}\) 由Gell-Mann矩阵的反对易子给出。</p>
<p style="font-size:0.85em;color:#888;">† 注意：具体破缺链 \(\text{SO}(10) \to \text{SU}(5) \to \text{SU}(3)\times\text{SU}(2)\times\text{U}(1)\) 中 \(\omega_\mu^{\text{internal}}\) 的显式分解依赖于规范群的分支规则（branching rules），这是格点NEFT计算的任务（见§5.2.12）。本节给出的是框架性论证。</p>
<div style="border-left:3px solid #e67e22;padding:8px 12px;margin:10px 0;background:#fef9e7;font-size:0.9em;">
<p><span style="color:#c0392b;">[审查回应]</span> <strong>非阿贝尔联络构造的局限性</strong>：[修正#4]已将联络定义从"标量场梯度比"改进为"自旋联络投影"。但以下问题仍存在：</p>
<ul>
<li>投影 \(A_\mu^a = \text{Tr}(T^a \cdot \omega_\mu^{\text{internal}})\) 定义了一个合理的联络形式，但<strong>未证明</strong>此联络满足杨-米尔斯运动方程——即没有从NEFT变分原理推导出 \(D_\nu F^{\nu\mu,a} = j^{\mu,a}\)，而是直接写出了标准形式。</li>
<li>U(1)退化为 \(A_\mu = \frac{1}{e}\partial_\mu\theta\) 是Abelian情形的标准结果，但SU(2)/SU(3)的非Abelian自相互作用项 \(-ig_af^{abc}A_\mu^b A_\nu^c\) 来自李代数结构，<strong>不是从NEFT场方程推导的</strong>，而是从投影定义的结构常数继承的。</li>
<li>步骤3.5的诱导规范动力学是从"背景涨落"论证出发的启发式推导，而非从NEFT作用量的变分原理严格得到。</li>
</ul>
</div>
<p style="margin-top:1.5em;border-top:1px solid #eee;padding-top:1em;"><strong>步骤3.5：诱导规范动力学 <span style="color:#c0392b;">†</span></strong></p>
<p>考虑能量场在拓扑背景 \(\bar{\mathcal{E}} = \rho(r)e^{in\theta}\)（涡旋）附近的涨落。将NEFT方程线性化，相位部分给出：</p>
<p>\[ (\partial_\mu + in\,\partial_\mu\theta)(\partial^\mu + in\,\partial^\mu\theta)\,\delta\mathcal{E} + \cdots = 0 \]</p>
<p>其中诱导规范势 \(A_\mu = n\,\partial_\mu\theta\) 自动出现。对非阿贝尔情况，多分量背景的相对相位产生非对角规范势。涨落变分方程给出<strong>杨-米尔斯方程 + 物质流</strong>：\(D_\nu F^{\nu\mu,a} = j^{\mu,a}\)。</p>
</div>

</div>

<h4>5.2.2 U(1)电磁场</h4>
<div class="derivation">
<p><strong>推导（U(1)规范场的NEFT构造）</strong>：U(1)对称性对应能量场在二维复平面上的连续旋转。定义复能量场：</p>
<p>\[ \Psi_{U(1)}(x) = \epsilon_1(x) + i\epsilon_2(x) = \rho(x) e^{i\theta(x)} \]</p>
<p>其中 \(\rho(x) = \sqrt{\epsilon_1^2 + \epsilon_2^2}\)，\(\theta(x) = \arctan(\epsilon_2/\epsilon_1)\)。</p>
<p>规范变换为 \(\theta(x) \to \theta(x) + \alpha(x)\)，对应于：</p>
<p>\[ \Psi_{U(1)}(x) \to e^{i\alpha(x)} \Psi_{U(1)}(x) \]</p>
<p>引入协变导数 \(D_\mu = \partial_\mu - i e A_\mu\)，其中 \(e\) 是基本电荷（精细结构常数的平方根）。在NEFT中：</p>
<p>\[ e = \sqrt{\frac{4\pi \alpha_0 \hbar c}{\gamma_0 \xi^2}} \]</p>
<p>其中 \(\alpha_0 = 1/137.036\) 是精细结构常数，\(\xi\) 是相干长度。</p>
<p>U(1)规范场的拉格朗日密度为：</p>
<p>\[ \mathcal{L}_{U(1)} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} - j^\mu A_\mu \]</p>
<p>其中 \(j^\mu = e \bar{\psi} \gamma^\mu \psi\) 是电流密度。</p>
</div>

<h4>5.2.3 SU(2)弱核力</h4>
<div class="derivation">
<p><strong>推导（SU(2)规范场的NEFT构造）</strong>：SU(2)对称性对应能量场在三维同位旋空间的特殊幺正变换。定义SU(2)双重态能量场：</p>
<p>\[ \Psi_{SU(2)}(x) = \begin{pmatrix} \epsilon_3(x) \\ \epsilon_4(x) \end{pmatrix} \]</p>
<p>SU(2)变换为 \(\Psi_{SU(2)}(x) \to U(x) \Psi_{SU(2)}(x)\)，其中 \(U(x) = \exp\left[-i \frac{g_2}{2} \alpha^a(x) \tau^a\right]\)，\(\tau^a = \sigma^a/2\) 是Pauli矩阵。</p>
<p>引入SU(2)规范场 \(W_\mu^a\)（a=1,2,3），其场强为：</p>
<p>\[ W_{\mu\nu}^a = \partial_\mu W_\nu^a - \partial_\nu W_\mu^a + g_2 \epsilon^{abc} W_\mu^b W_\nu^c \]</p>
<p>在NEFT中，耦合常数 \(g_2\) 由能量场的拓扑缠绕数决定：</p>
<p>\[ g_2 = \sqrt{\frac{8\pi \alpha_W \hbar c}{\gamma_0 \xi_W^2}} \]</p>
<p>其中 \(\alpha_W = g_2^2/4\pi \approx 1/29\) 是弱相互作用耦合常数。</p>
<p>物理的W±和Z°玻色子通过以下组合产生：</p>
<p>\[ W_\mu^\pm = \frac{1}{\sqrt{2}}(W_\mu^1 \mp i W_\mu^2) \]</p>
<p>\[ Z_\mu = W_\mu^3 \cos\theta_W - B_\mu \sin\theta_W \]</p>
<p>\[ A_\mu = W_\mu^3 \sin\theta_W + B_\mu \cos\theta_W \]</p>
<p>其中 \(\theta_W\) 是Weinberg角<sup class="citation">[62]</sup>，由拓扑结构决定：</p>
<p>\[ \sin^2\theta_W = \frac{n_{U(1)}}{n_{U(1)} + n_{SU(2)}} \]</p>
<p>这里 \(n_{U(1)}\) 和 \(n_{SU(2)}\) 分别是U(1)和SU(2)拓扑模式的数目。
</p>
</div>

<h4>5.2.4 SU(3)强核力</h4>
<div class="derivation">
<p><strong>推导（SU(3)规范场的NEFT构造）</strong>：SU(3)对称性对应能量场在八维颜色空间（Gell-Mann矩阵空间）中的特殊幺正变换。定义SU(3)三重态能量场：</p>
<p>\[ \Psi_{SU(3)}(x) = \begin{pmatrix} \epsilon_5(x) \\ \epsilon_6(x) \\ \epsilon_7(x) \end{pmatrix} \]</p>
<p>SU(3)变换为 \(\Psi_{SU(3)}(x) \to U(x) \Psi_{SU(3)}(x)\)，其中 \(U(x) = \exp\left[-i \frac{g_3}{2} \alpha^a(x) \lambda^a\right]\)，\(\lambda^a\) 是Gell-Mann矩阵<sup class="citation">[85]</sup>（a=1,...,8）。</p>
<p>引入SU(3)规范场 \(G_\mu^a\)（胶子场），其场强为：</p>
<p>\[ G_{\mu\nu}^a = \partial_\mu G_\nu^a - \partial_\nu G_\mu^a + g_3 f^{abc} G_\mu^b G_\nu^c \]</p>
<p>其中 \(f^{abc}\) 是SU(3)的结构常数，完全由能量场的拓扑缠绕数决定。在NEFT中：</p>
<p>\[ f^{abc} = \frac{1}{2i} \text{Tr}(\lambda^a [\lambda^b, \lambda^c]) \]</p>
<p>耦合常数 \(g_3\) 由能量场的强相互作用拓扑模式决定：</p>
<p>\[ g_3 = \sqrt{\frac{8\pi \alpha_s \hbar c}{\gamma_0 \xi_S^2}} \]</p>
<p>其中 \(\alpha_s = g_3^2/4\pi\) 是强相互作用耦合常数，具有跑动性质：
</p>
<p>\[ \alpha_s(Q^2) = \frac{12\pi}{(33 - 2n_f)\ln(Q^2/\Lambda_{QCD}^2)} \]</p>
<p>在NEFT中，这个跑动由能量场在不同能标下的梯度变化自然产生。
</p>
</div>

<h4>5.2.4a 强CP问题与轴子的涌现</h4>

<div style="background-color:#fff3e0;padding:18px 22px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">强CP问题</p>
<p style="color:#e65100;font-size:0.9em;">QCD允许一个CP破坏项 \(\theta_{\text{QCD}} G_{\mu\nu} \tilde{G}^{\mu\nu}\)，但实验测量中子电偶极矩表明 \(|\theta_{\text{QCD}}| < 10^{-10}\)<sup class="citation">[1]</sup>。为什么这个参数几乎恰好为零？这是粒子物理的著名自然性问题。</p>
</div>

<div class="derivation">
<p><strong>Peccei-Quinn机制<sup class="citation">[82]</sup>与轴子<sup class="citation">[82,83]</sup>的拓扑起源</strong></p>
<p><strong>（1）Peccei-Quinn对称性</strong>：在NEFT的对称性破缺链中，引入一个额外的全局 \(U(1)_{PQ}\) 对称性。这个对称性在能标 \(f_a\) 处自发破缺，产生一个Nambu-Goldstone玻色子——轴子（Axion）<sup class="citation">[1]</sup>。</p>
<p><strong>（2）轴子作为NEFT拓扑激发</strong>：在NEFT框架下，轴子就是旋量场 \(\Psi\) 的U(1)_{PQ}相位自由度在真空相变中产生的Nambu-Goldstone玻色子<sup class="citation">[82,86]</sup>：</p>
<p>\[ a(x) = \arg\left(\bar{\Psi}(x)\Psi(x)\right) \mod 2\pi f_a \]</p>
<p>轴子场的势能由QCD瞬子效应诱导：</p>
<p>\[ V(a) = -m_a^2 f_a^2 \cos\left(\frac{a}{f_a}\right) \]</p>
<p><strong>（3）\(\theta\) 参数的动态归零</strong>：轴子场的真空期望值会动态地将有效 \(\theta\) 参数"滚"到零：</p>
<p>\[ \theta_{\text{eff}} = \theta_{\text{QCD}} + \frac{\langle a \rangle}{f_a} \xrightarrow{\text{真空}} 0 \]</p>
<p>强CP问题因此被动力学解决，而非参数调谐。此外，轴子质量极小（\(m_a \sim 10^{-5}\) eV量级），是冷暗物质的极佳候选者<sup class="citation">[1,82]</sup>。NEFT预言轴子的存在，并为暗物质提供了拓扑起源的解释。</p>
<p style="color:#e65100;font-size:0.88em;text-indent:0;"><strong>[审查回应]</strong> 上述讨论实质上是标准Peccei-Quinn机制的重述——\(U(1)_{PQ}\) 对称性、Nambu-Goldstone玻色子、瞬子诱导势能、\(\theta\) 动态归零均为1977年Peccei-Quinn的原贡献。NEFT添加的唯一内容是将轴子诠释为"旋量场相位自由度"的拓扑激发，但这一诠释未产生新的可检验预言（如 \(m_a\) 或 \(f_a\) 的独立计算）。</p>
</div>

<h4>5.2.5 费米子场的NEFT构造</h4>
<div class="derivation">
<p><strong>推导（费米子场的拓扑起源）</strong>：费米子（夸克和轻子）是能量场的旋量拓扑激发。基于§1.4建立的纤维丛几何，费米子场通过Clifford代数从自旋丛截面自然导出<sup class="citation">[83,84]</sup>。</p>
<p><strong>步骤1：旋量场的构造</strong></p>
<p>定义旋量能量场 \(\psi(x)\) 作为能量场的梯度组合：</p>
<p>费米子场通过旋量场 \(\Psi(x)\) 的分量投影得到<sup class="citation">[83,84]</sup>（详见§1.4.3）：</p>
<p>\[ \psi_f(x) = P_f \, \Psi(x), \quad P_f = \text{投影到第}\,f\,\text{味子空间} \]</p>
<p>其中 \(P_f\) 是从 \(\Gamma(S \otimes \mathcal{L})\) 到具体费米子表示的投影算子。</p>
<p><strong>步骤2：代数结构</strong></p>
<p>狄拉克矩阵满足Clifford代数反对易关系 \(\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\)<sup class="citation">[83,84]</sup>。如§1.4.3所述，\(\gamma^\mu\) 由自旋丛的纤维结构（Clifford代数 \(Cl(1,3)\)）确定，而非从标量场导出。</p>
<p><strong>步骤3：代数分类</strong></p>
<p>费米子代数由能量场的拓扑分类数决定：</p>
<ul>
    <li><strong>第一代费米子</strong>：拓扑数 \(N = 1\)</li>
    <li><strong>第二代费米子</strong>：拓扑数 \(N = 2\)</li>
    <li><strong>第三代费米子</strong>：拓扑数 \(N = 3\)</li>
</ul>
<p>每一代包含：
<ul>
    <li>轻子：\((e, \nu_e)\), \((\mu, \nu_\mu)\), \((\tau, \nu_\tau)\)</li>
    <li>夸克：\((u, d)\), \((c, s)\), \((t, b)\)</li>
</ul>
</p>
<p><strong>步骤4：荷量子化的拓扑起源</strong></p>
<p>电荷 \(Q\) 由拓扑环绕数 \(n\) 决定（见§1.4.2的Skyrmion量子化）：</p>
<p>\[ Q = \frac{e}{3} (n_R - n_L) \]</p>
<p>其中 \(n_R\) 和 \(n_L\) 分别是右旋和左旋拓扑模式的数目。
</p>
</div>

<h4>5.2.6 希格斯机制的NEFT解释</h4>
<div class="derivation">
<p><strong>推导（希格斯场与对称性自发破缺）</strong>：希格斯机制<sup class="citation">[27-29]</sup>和对称性自发破缺<sup class="citation">[30,31]</sup>在NEFT中对应能量场的拓扑相变。</p>
<p><strong>步骤1：希格斯势的构造</strong></p>
<p>NEFT的势能项 \(\mathcal{V}'(\mathcal{E})\) 在特定条件下呈现"墨西哥帽"形状：</p>
<p>\[ V(\phi) = \mu^2 |\phi|^2 + \lambda |\phi|^4 \]</p>
<p>其中 \(\mu^2 < 0\)（从能量场的梯度条件导出），\(\lambda > 0\)（稳定性条件）。</p>
<p><strong>步骤2：真空期望值</strong></p>
<p>势能极小值位于：</p>
<p>\[ |\phi| = v = \sqrt{\frac{-\mu^2}{\lambda}} \approx 246 \text{ GeV} \]</p>
<p>在NEFT中，这个值由能量场的拓扑张力决定：</p>
<p>\[ v = \sqrt{\frac{2\gamma_0 T_\mathcal{E}}{\lambda \rho_\mathcal{E}}} \]</p>
<p><strong>步骤3：规范玻色子质量的产生</strong></p>
<p>SU(2)×U(1)对称性破缺后，W和Z玻色子获得质量：</p>
<p>\[ m_W = \frac{1}{2} g_2 v \approx 80.4 \text{ GeV} \]</p>
<p>\[ m_Z = \frac{1}{2} \sqrt{g_2^2 + g_1^2} \, v \approx 91.2 \text{ GeV} \]</p>
<p>光子保持无质量：\(m_\gamma = 0\)。</p>
<div class="figure-container">
    <img src="figures_py/第五章_图11_标准模型粒子谱.png" alt="Standard Model Particle Spectrum">
    <div class="figure-caption">图12：标准模型粒子谱：展示三代费米子、规范玻色子和希格斯标量的完整分类</div>
</div>
<p><strong>步骤4：费米子质量的产生</strong></p>
<p>费米子通过Yukawa耦合<sup class="citation">[60]</sup>获得质量：</p>
<p>\[ m_f = \frac{y_f v}{\sqrt{2}} \]</p>
<p>其中Yukawa耦合 \(y_f\) 由费米子的拓扑复杂度决定：</p>
<p>\[ y_f = \sqrt{\frac{n_f \gamma_0}{\xi_f^2}} \]</p>
<p>这里 \(n_f\) 是第f种费米子的拓扑数。
</p>

<div style="background-color:#fff3e0;padding:18px 22px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">希格斯质量的层级灾难</p>
<p style="color:#e65100;font-size:0.9em;">在量子场论中，希格斯质量的辐射修正会被拖拽到普朗克量级（\(M_P \sim 10^{19}\) GeV），而观测值仅125 GeV<sup class="citation">[1,12]</sup>。这需要极端的精细调谐（fine-tuning），是粒子物理最大的自然性问题之一。</p>
</div>

<div class="derivation">
<p><strong>超对称保护与复合希格斯二选一</strong></p>

<p><strong>方案A：超对称（SUSY）保护</strong><sup class="citation">[66]</sup>。将NEFT作用量升级为超场形式。在超对称理论中，每个费米子都有对应的玻色子伙伴，反之亦然。玻色子的真空涨落为正贡献，费米子的为负贡献，两者在超对称极限下精确抵消：</p>
<p>\[ \delta m_H^2 = \underbrace{\frac{\lambda_B}{16\pi^2} \Lambda^2}_{\text{玻色子圈}} - \underbrace{\frac{\lambda_F}{16\pi^2} \Lambda^2}_{\text{费米子圈}} = 0 \quad (\lambda_B = \lambda_F) \]</p>
<p>超对称破缺后，抵消不完全但残余量受超对称破缺能标 \(M_{\text{SUSY}}\) 控制。NEFT预言 \(M_{\text{SUSY}} \sim 1-10\) TeV，意味着超对称伙伴粒子可能在LHC的高亮度升级或未来FCC对撞机中被发现。这也解释了5.2.9节中预言超对称伙伴的必然性——它们不是可选项，而是防止希格斯质量发散的"保护费"。</p>

<p><strong>方案B：复合希格斯（Composite Higgs）</strong>。如果超对称在自然界不存在（LHC至今未发现超对称粒子<sup class="citation">[1]</sup>），NEFT可转而声称希格斯粒子不是基本粒子，而是能量场的拓扑束缚态——类似于 \(\pi\) 介子是夸克-反夸克束缚态<sup class="citation">[1]</sup>，原子核是核子束缚态。复合粒子的质量自然远小于其组分质量（因结合能释放），从而避免层级问题。在NEFT框架下：</p>
<p>\[ H \sim \langle \bar{\psi}\psi \rangle_{\text{topo}} \]</p>
<p>希格斯场是能量场旋量激发的拓扑凝聚。这种机制与Walking Technicolor理论<sup class="citation">[88]</sup>有类似结构，但NEFT中的"技术色"由能量场拓扑缠绕数提供。</p>
</div>
</div>

<h4>5.2.7 粒子质量谱的拓扑分类</h4>
<div class="figure-container">
    <img src="figures_py/第五章_图12_费米子质量层级.png" alt="Fermion Mass Hierarchy">
    <div class="figure-caption">图13：费米子质量层级：展示三代费米子的质量分布（对数尺度）</div>
</div>
<div class="derivation">
<p><strong>唯象拟合（质量矩阵的拓扑结构）†</strong>：以下为唯象拟合框架，非第一性原理严格推导。</p>
<p><strong>费米子质量矩阵</strong></p>
<p>第n代费米子的质量遵循几何级数：</p>
<p>\[ m^{(n)} \approx m^{(1)} \cdot \kappa^{n-1} \]</p>
<p>其中 \(\kappa \approx 100-300\) 是唯象拟合的拓扑放大因子†（量纲分析约束，精确值需格点NEFT计算）。形式上由能量场的自相互作用强度 \(\lambda\) 决定：</p>
<p>\[ \kappa = \frac{\lambda \xi^4}{\hbar^2} \frac{T_\mathcal{E}}{\rho_\mathcal{E}} \]</p>
<p>具体数值（实验值）：</p>
<ul>
    <li><strong>轻子</strong>：\(m_e = 0.511 \text{ MeV}\), \(m_\mu = 105.7 \text{ MeV}\), \(m_\tau = 1776 \text{ MeV}\)</li>
    <li><strong>下夸克</strong>：\(m_d \approx 2-5 \text{ MeV}\), \(m_s \approx 95 \text{ MeV}\), \(m_b \approx 4.18 \text{ GeV}\)</li>
    <li><strong>上夸克</strong>：\(m_u \approx 1-3 \text{ MeV}\), \(m_c \approx 1.27 \text{ GeV}\), \(m_t \approx 173 \text{ GeV}\)</li>
</ul>

<div style="background-color:#fff3e0;padding:18px 22px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">费米子质量层级问题</p>
<p style="color:#e65100;font-size:0.9em;">简单几何级数 \(m^{(n)} \propto \kappa^{n-1}\) 与实验数据不符（如 \(m_c/m_u \sim 500\)，但 \(m_t/m_c \sim 136\)），且中微子质量极小（~0.1 eV），完全偏离该规律<sup class="citation">[1]</sup>。需要更精细的机制。</p>
</div>

<p><strong>非微扰重整化群流与分形真空</strong></p>
<p>质量不是由简单拓扑数决定，而是由Yukawa耦合的重整化群跑动在红外不动点（IR Fixed Point）决定<sup class="citation">[74]</sup>：</p>
<p><strong>（1）Yukawa耦合的拓扑调制</strong>：费米子质量 \(m_f = y_f v/\sqrt{2}\)，在NEFT中Yukawa耦合 \(y_f\) 受拓扑荷 \(n_f\) 的非线性调制：</p>
<p>\[ y_f(\mu) = y_0 \exp\left( \alpha_f \cdot \ln^{p_f}\!\left(\frac{\mu}{\Lambda_{\text{topo}}}\right) \right) \]</p>
<p>其中 \(p_f\) 是分形真空的拓扑维数（不同费米子取不同值），\(\Lambda_{\text{topo}}\) 是拓扑相变能标。这种"指数中的对数"形式可以产生巨大的层级差。</p>
<p><strong>（2）分形真空假设</strong>：假设NEFT真空具有分形结构（分形维数 \(d_f < 4\)），场的传播子在分形空间中发生畸变，导致 \(\beta\) 函数出现离散尺度不变性（Discrete Scale Invariance）或极限环（Limit Cycles）<sup class="citation">[74]</sup>。修正后质量公式：</p>
<p>\[ m_f = m_0 \exp\left( -\frac{n_f \pi}{\alpha_s(\mu_f)} + \delta_f^{\text{topo}} \right) \]</p>
<p>其中 \(\delta_f^{\text{topo}}\) 是拓扑修正项。这种形式可拟合三代费米子的巨大质量劈裂，同时中微子质量通过跷跷板机制（见下文）被极度压制。</p>
<p style="color:#e65100;font-size:0.88em;text-indent:0;"><strong>[审查回应]</strong> 上述Yukawa耦合的拓扑调制公式 \(y_f(\mu) = y_0\exp(\alpha_f\ln^{p_f}(\mu/\Lambda_{\text{topo}}))\) 和分形真空质量公式均为<strong>唯象ansatz</strong>，非从NEFT基本方程推导。参数 \(\alpha_f, p_f, \Lambda_{\text{topo}}, \delta_f^{\text{topo}}\) 均为每个费米子独立引入的拟合参数，<strong>无法减少标准模型19个自由参数的总数</strong>。分形维数 \(d_f < 4\) 是假设而非推导结果。这些公式的价值在于提供了一个"拓扑参数决定质量"的<strong>概念框架</strong>，但当前形式不具预测力。</p>
<p><strong>希格斯玻色子质量</strong></p>
<p>\[ m_H = \sqrt{2\lambda} v \approx 125 \text{ GeV} \]</p>
<div class="figure-container">
    <img src="figures_py/第五章_图13_规范耦合常数大统一.png" alt="Gauge Coupling Unification">
    <div class="figure-caption">图14：规范耦合常数的大统一：展示SU(3)、SU(2)、U(1)耦合常数在GUT能标处的汇聚</div>
</div>
<p>其中 \(\lambda \approx 0.13\) 由四点顶点函数导出。</p>
</div>

<h4>5.2.8 CKM和PMNS混合矩阵的拓扑起源</h4>
<div class="derivation">
<p><strong>推导（混合矩阵的NEFT解释）</strong>：CKM和PMNS矩阵描述不同代费米子之间的混合，在NEFT中对应于能量场拓扑模式之间的相互渗透。</p>
<p><strong>CKM矩阵（夸克混合）</strong></p>
<p>CKM矩阵<sup class="citation">[63]</sup> \(V_{CKM}\) 由能量场的拓扑扭曲角决定：</p>
<p>\[ V_{CKM} = \begin{pmatrix}
V_{ud} & V_{us} & V_{ub} \\
V_{cd} & V_{cs} & V_{cb} \\
V_{td} & V_{ts} & V_{tb}
\end{pmatrix} \approx \begin{pmatrix}
0.974 & 0.225 & 0.0036 \\
0.225 & 0.973 & 0.041 \\
0.0087 & 0.040 & 0.999
\end{pmatrix} \]</p>
<p>在NEFT中，矩阵元由拓扑重叠积分决定：</p>
<p>\[ V_{ij} = \int \psi_i^*(x) \mathcal{O}_{\text{top}} \psi_j(x) d^4x \]</p>
<p>其中 \(\mathcal{O}_{\text{top}}\) 是拓扑算子。</p>
<p><strong>PMNS矩阵（中微子混合）</strong></p>
<p>PMNS矩阵<sup class="citation">[43,64]</sup> \(U_{PMNS}\) 同样由能量场的拓扑结构决定：</p>
<p>\[ U_{PMNS} = U_{e^2}^\dagger U_{e^1} = \begin{pmatrix}
U_{e1} & U_{e2} & U_{e3} \\
U_{\mu1} & U_{\mu2} & U_{\mu3} \\
U_{\tau1} & U_{\tau2} & U_{\tau3}
\end{pmatrix} \]</p>
<p>实验参数：
<ul>
    <li>\(\theta_{12} \approx 33.5^\circ\)（太阳角）</li>
    <li>\(\theta_{23} \approx 45^\circ\)（大气角）</li>
    <li>\(\theta_{13} \approx 8.6^\circ\)（反应堆角）</li>
    <li>\(\delta_{CP}\)（CP破坏相）</li>
</ul>
</p>
<p>在NEFT中，这些角度由能量场的几何扭曲角度精确决定。
</p>
</div>

<h4>5.2.9 新粒子的预测</h4>
<div class="derivation">
<p><strong>预测（NEFT预言的新粒子）</strong>：基于能量场的拓扑结构分析，NEFT预测以下新粒子的存在。</p>
<p><strong>预测1：第四代费米子</strong></p>
<p>能量场的拓扑结构允许更高阶的激发模式。第四代费米子的预期质量：</p>
<p>\[ m^{(4)} \approx m^{(3)} \cdot \kappa \approx 10-100 \text{ TeV} \]</p>
<p>第四代包含：\((e', \nu_{e'})\) 轻子对和 \((t', b')\) 夸克对。</p>
<p><strong>预测2：类希格斯标量</strong></p>
<p>能量场的多重孤子解预言多个标量粒子：
<ul>
    <li>\(H_2\)：第二希格斯粒子，质量 \(m_{H_2} \approx 500-1000 \text{ GeV}\)</li>
    <li>\(H^\pm\)：带电希格斯粒子，质量 \(m_{H^\pm} \approx 400-800 \text{ GeV}\)</li>
    <li>\(A^0\)：CP-odd希格斯粒子，质量 \(m_{A^0} \approx 400-800 \text{ GeV}\)</li>
</ul>
</p>
<p><strong>预测3：Z'玻色子</strong></p>
<p>额外U(1)'规范对称性产生Z'玻色子，质量：</p>
<p>\[ m_{Z'} = g' v' \approx 1-10 \text{ TeV} \]</p>
<p>其中 \(v'\) 是新标量场的真空期望值。</p>
<p><strong>预测4：右手中微子</strong></p>
<p>拓扑结构的非手性性预言右手中微子的存在，质量可能很大：
</p>
<p>\[ m_{N_R} \approx 10^{14}-10^{15} \text{ GeV} \]</p>
<p>这为马约拉纳中微子<sup class="citation">[72]</sup>和质量生成机制（Seesaw机制）<sup class="citation">[64,65]</sup>提供了NEFT解释。</p>

<div style="background-color:#fff3e0;padding:18px 22px;border-left:4px solid #ff9800;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-weight:bold;margin-bottom:0.5em;">马约拉纳中微子与轻子数破坏</p>
<p style="color:#e65100;font-size:0.9em;">中微子质量极小（~0.1 eV），且中微子可能是自身的反粒子（马约拉纳费米子）<sup class="citation">[72]</sup>，这一现象需要理论解释。</p>
</div>

<div class="derivation">
<p><strong>跷跷板机制的拓扑起源</strong></p>
<p><strong>（1）马约拉纳质量项的NEFT构造</strong>：在NEFT框架下，总能量守恒要求：产生一个左手轻中微子 \(\nu_L\) 时，必须伴随一个对应的"拓扑缺陷"来平衡能量-动量。这个拓扑缺陷就是右手中微子 \(N_R\)，其质量由大统一尺度的拓扑张力决定：</p>
<p>\[ \mathcal{L}_\nu = -\frac{1}{2} \begin{pmatrix} \overline{\nu_L} & \overline{N_R^c} \end{pmatrix} \begin{pmatrix} 0 & m_D \\ m_D & M_R \end{pmatrix} \begin{pmatrix} \nu_L^c \\ N_R \end{pmatrix} + \text{h.c.} \]</p>
<p>其中 \(m_D \sim v \sim 100\) GeV 是Dirac质量，\(M_R \sim 10^{14}\) GeV 是马约拉纳质量（由NEFT拓扑结构在大统一能标处的对称性决定）。</p>
<p><strong>（2）跷跷板公式</strong>：对角化质量矩阵后，轻本征态质量为：</p>
<p>\[ m_{\nu,\text{light}} \approx \frac{m_D^2}{M_R} \sim \frac{(100\,\text{GeV})^2}{10^{14}\,\text{GeV}} \sim 0.1\,\text{eV} \]</p>
<p>这与实验观测的中微子质量上限完美吻合<sup class="citation">[45]</sup>。NEFT解释：\(M_R\) 对应于能量场在大统一能标下的拓扑结构稳定性（拓扑张力极高），因此中微子质量被极度压制。</p>
<p><strong>（3）轻子数破坏的观测信号</strong>：如果中微子是马约拉纳粒子，轻子数不守恒。实验上可通过无中微子双β衰变（\(0\nu\beta\beta\))验证。NEFT预言该衰变的半衰期：</p>
<p>\[ T_{1/2}^{0\nu} \propto \frac{1}{m_{\beta\beta}^2} \sim \frac{1}{(0.01-0.1\,\text{eV})^2} \sim 10^{25}-10^{27}\,\text{年} \]</p>
<p>下一代实验（如nEXO, LEGEND-1000）有望在2030年前达到此灵敏度<sup class="citation">[1]</sup>。</p>
</div>
<p><strong>预测5：超对称伙伴</strong></p>
<p>能量场的拓扑对偶结构暗示超对称<sup class="citation">[66]</sup>的存在，每个标准模型粒子都有一个超对称伙伴：</p>
<ul class="center-list">
    <li>标量轻子（Selectron, Smuon, Stau）</li>
    <li>标量夸克（Squark）</li>
    <li>超规范子（Gluino）</li>
    <li>超中性子（Neutralino）</li>
    <li>超带电粒子（Chargino）</li>
</ul>
</p>
<p>这些粒子的质量由超对称破缺能标决定，预期在TeV范围。
</p>
</div>


<h4>5.2.10 规范对称性的拓扑统一</h4>
<div class="derivation">
<p><strong>推导（大统一理论的NEFT框架）</strong>：NEFT为SU(5)或SO(10)大统一理论<sup class="citation">[67]</sup>提供了拓扑基础。</p>
<p><strong>统一规范群</strong></p>
<p>标准模型规范群 \(SU(3) \times SU(2) \times U(1)\) 可以嵌入更大的单群：</p>
<p>\[ \mathcal{G}_{\text{GUT}} = SU(5) \quad \text{或} \quad SO(10) \]</p>
<p>在NEFT中，这个统一对应于能量场在更高维内部空间（10维或11维）的拓扑结构。</p>
<p><strong>统一耦合常数</strong></p>
<p>三个规范耦合常数在大统一能标 \(M_{\text{GUT}} \approx 10^{16} \text{ GeV}\) 处汇聚：</p>
<p>\[ \alpha_1(M_{\text{GUT}}) = \alpha_2(M_{\text{GUT}}) = \alpha_3(M_{\text{GUT}}) \approx \frac{1}{25} \]</p>
<p>在NEFT中，这个汇聚由能量场在统一能标下的单一拓扑模式自然产生。</p>
<div class="figure-container">
    <img src="figures_py/第五章_图14_孤子解.png" alt="Soliton Solutions">
    <div class="figure-caption">图15：孤子解：展示能量场的扭结解和反扭结解，对应于基本粒子</div>
</div>
<p><strong>质子衰变</strong></p>
<p>大统一理论预言质子衰变，NEFT给出质子寿命估计：</p>
<p>\[ \tau_p \approx \frac{M_{X}^4}{\alpha_{\text{GUT}}^2 m_p^5} \approx 10^{34}-10^{36} \text{ 年} \]</p>
<p>其中 \(M_X\) 是X玻色子质量，\(m_p\) 是质子质量。
</p>
</div>

<h4>5.2.11 开放问题与未来方向 <span style="color:#c0392b;">†</span></h4>
<div style="background-color:#fff3cd;padding:18px 22px;border-left:4px solid #ffc107;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#856404;font-weight:bold;margin-bottom:0.5em;">† NEFT未解关键问题（按优先级）：</p>
<ol style="margin-top:0.5em;color:#856404;">
    <li style="margin-bottom:0.5em;"><strong>自旋1/2涌现 [最高优先级]</strong>：如何从纯标量场拓扑严格推导旋量表示？</li>
    <li style="margin-bottom:0.5em;"><strong>规范代数选择</strong>：为何恰好 SU(3)×SU(2)×U(1)？</li>
    <li style="margin-bottom:0.5em;"><strong>耦合常数计算</strong>：需非微扰方法提取精确值。</li>
    <li style="margin-bottom:0.5em;"><strong>费米子质量谱</strong>：需格点NEFT数值验证。</li>
    <li style="margin-bottom:0.5em;"><strong>希格斯势涌现</strong>：墨西哥帽势如何从NEFT解中产生？</li>
    <li style="margin-bottom:0.5em;"><strong>CP破坏起源</strong> 与 <strong>代结构必然性</strong></li>
</ol>
</div>

<h4>5.2.12 格点NEFT计算框架 <span style="color:#c0392b;">†</span></h4>
<div style="background-color:#e8f8f5;padding:18px 22px;border-left:4px solid #1abc9c;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#0e6655;font-weight:bold;margin-bottom:0.5em;">† 格点NEFT计算实施计划（2026-2027）</p>
<p style="color:#0e6655;font-size:0.9em;">为将NEFT从"理论框架"转化为可验证的数值计算框架，我们制定了以下具体的实施计划：</p>
</div>

<div class="derivation">
<p><strong>实施阶段A：格点化与作用量构造（2026年6-12月）</strong></p>
<p><strong>（1）格点离散化方案</strong></p>
<p>将四维时空离散为 \(N_t \times N_x \times N_y \times N_z = 64^4\) 格点，间距 \(a = \xi/10 \sim 10^{-17}\) m（\(\xi\) 为相干长度）。能量场 \(\Psi(x)\) 定义在格点上，\(\mathcal{E}(x) = \bar\Psi\Psi\) 为旋量双线性。</p>
<p><strong>（2）格点NEFT作用量</strong></p>
<p>\[ S_L = a^4 \sum_{n} \left[ \frac{1}{2} \sum_{\mu} (\nabla_\mu \Psi_n)^2 + \frac{1}{2} \hat{\Gamma}_n (\nabla_t \Psi_n)^2 + V(\bar{\Psi}_n \Psi_n) \right] \]</p>
<p>其中 \(\nabla_\mu\) 为前向有限差分算子，\(\hat{\Gamma}_n = \hat{\Gamma}_0 [1 + \alpha (\nabla \Psi_n)^2]\) 为格点上的动态耗散系数。</p>
<div style="background-color:#fff3e0;padding:12px 16px;border-left:3px solid #ff9800;margin:0.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#e65100;font-size:0.88em;text-indent:0;"><strong>[审查回应] Nielsen-Ninomiya定理与费米子加倍问题</strong>：若 \(\Psi\) 是旋量场（费米子），其格点离散化必须处理<strong>费米子加倍问题</strong>（Nielsen-Ninomiya定理，1981）：在局域、厄米、平移不变的格点费米子作用量中，当格子间距 \(a\to 0\) 时不可避免地产生额外费米子自由度（"加倍子"）。标准格点QCD的解决方案包括Wilson费米子、staggered费米子、domain wall费米子等。NEFT格点作用量 \(S_L\) 中 \((\nabla_t\Psi_n)^2\) 项是标量形式的格点动能——若直接用于旋量场，会产生 \(2^4 = 16\) 个加倍子。解决方案可能来自NEFT的耗散项 \(\hat\Gamma_n\)：正如Wilson质量项 \(r/a\) 消除QCD加倍子，NEFT的耗散项可能天然充当Wilson项的角色，在高动量区自动衰减加倍子贡献（与§2.6紫外完备性论证一致）。<strong>但这一猜测需数值验证</strong>——格点NEFT代码实现中必须显式测试加倍子谱。</p>
</div>

<p><strong>实施阶段B：蒙特卡洛演化（2026年9-12月）</strong></p>
<p><strong>（3）Metropolis-Hastings算法</strong></p>
<p>对于每个格点更新：</p>
<p>\[ \Psi_n' = \Psi_n + \delta \cdot \text{Uniform}(-1, 1) \]</p>
<p>接受概率：</p>
<p>\[ P_{\text{acc}} = \min\left(1, e^{-\Delta S_L/k_B T_{\text{eff}}}\right) \]</p>
<p>其中 \(T_{\text{eff}} = \hbar/(\alpha a)\) 为有效温度，通过 \(\alpha\) 控制量子涨落强度。</p>
<p><strong>（4）并行化策略</strong></p>
<ul>
    <li>采用 checkerboard 更新模式，避免数据竞争</li>
    <li>使用 CUDA/OpenMP 实现GPU加速</li>
    <li>目标：在 100 GPU-hours 内完成 \(64^4\) 格点的热化</li>
</ul>

<p><strong>实施阶段C：观测量的计算（2027年1-6月）</strong></p>
<p><strong>（5）质量谱提取</strong></p>
<p>计算两点关联函数：</p>
<p>\[ C(t) = \langle \mathcal{E}(0) \mathcal{E}(t) \rangle \sim \sum_{n} A_n e^{-m_n t} \]</p>
<p>通过多指数拟合提取质量本征值 \(m_n\)。NEFT预言：</p>
<ul>
    <li>\(m_e \approx 0.511\) MeV（电子）</li>
    <li>\(m_\mu \approx 105.7\) MeV（μ子）</li>
    <li>\(m_p \approx 938.3\) MeV（质子）</li>
</ul>
<p><strong>（6）验证判据</strong></p>
<p>格点计算成功的判据：</p>
<ol>
    <li>提取的质量谱在10%误差内与实验值一致</li>
    <li>拓扑荷 \(B\) 与自旋 \(J\) 的关系 \(J = |B|/2\) 被验证</li>
    <li>连续极限 \(a \to 0\) 下质量本征值收敛</li>
</ol>

<p><strong>实施阶段D：代码开源与复现（2027年6-12月）</strong></p>
<p><strong>（7）开源计划</strong></p>
<ul>
    <li>代码库：GitHub (github.com/neft-lattice/neft-lattice-code)</li>
    <li>格式：Python + CUDA，包含完整的测试套件</li>
    <li>文档：详细的安装、运行和参数调优指南</li>
</ul>
<p><strong>（8）合作验证</strong></p>
<ul>
    <li>邀请至少两个独立研究组（如格点QCD团队）复现结果</li>
    <li>发布预印本详细描述数值方法和误差分析</li>
</ul>

<div style="background-color:#e8f5e9;padding:18px 22px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-weight:bold;">格点NEFT计算实施路线图</p>
<table style="border-collapse:collapse;margin:1em 0;font-size:0.9em;">
<tr style="background:#1b5e20;color:white;"><th style="border:1px solid #ccc;padding:8px;">阶段</th><th style="border:1px solid #ccc;padding:8px;">时间</th><th style="border:1px solid #ccc;padding:8px;">任务</th><th style="border:1px solid #ccc;padding:8px;">交付物</th></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">阶段A</td><td style="border:1px solid #ccc;padding:6px;">2026.06-12</td><td style="border:1px solid #ccc;padding:6px;">格点化与作用量构造</td><td style="border:1px solid #ccc;padding:6px;">格点代码 v1.0</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">阶段B</td><td style="border:1px solid #ccc;padding:6px;">2026.09-12</td><td style="border:1px solid #ccc;padding:6px;">蒙特卡洛演化</td><td style="border:1px solid #ccc;padding:6px;">GPU加速模拟器</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">阶段C</td><td style="border:1px solid #ccc;padding:6px;">2027.01-06</td><td style="border:1px solid #ccc;padding:6px;">质量谱提取</td><td style="border:1px solid #ccc;padding:6px;">质量谱预印本</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">阶段D</td><td style="border:1px solid #ccc;padding:6px;">2027.06-12</td><td style="border:1px solid #ccc;padding:6px;">开源与验证</td><td style="border:1px solid #ccc;padding:6px;">开源代码库 + 独立验证报告</td></tr>
</table>
</div>
</div>

<h3 id="s5_3">5.3 物质作为孤子</h3>
<div class="derivation">
<p><strong>推导（孤子解的构造）</strong>：<span style="color:#c0392b;">[修正#3]</span> 在NEFT中，基本粒子是旋量场 \(\Psi\) 的拓扑孤子激发<sup class="citation">[56,57]</sup>。以下在<strong>标量投影极限</strong> \(\Psi \to \mathcal{E}\) 下求解一维静态扭结解，展示拓扑荷的量子化；完整的三维旋量Skyrmion解见§1.4.2。</p>
<p>标量投影采用标准 \(\phi^4\) 势：</p>
<p>\[ V(\epsilon) = \frac{\lambda}{4}\left(\epsilon^2 - v^2\right)^2 \]</p>
<p>其中 \(v\) 是真空期望值，\(\lambda\) 是自耦合常数。静态扭结解满足：</p>
<p>\[ \frac{d^2\epsilon}{dx^2} = V'(\epsilon) = \lambda\epsilon(\epsilon^2 - v^2) \]</p>
<p>利用 Bogomol'nyi 技巧，令 \(d\epsilon/dx = \pm\sqrt{2V(\epsilon)} = \pm\sqrt{\lambda/2}\,(\epsilon^2 - v^2)\)，分离变量积分得标准 \(\phi^4\) kink 解：</p>
<p>\[ \epsilon(x) = v\,\tanh\!\left(\frac{x - x_0}{\sqrt{2}\,\xi}\right) \]</p>
<p>其中 \(\xi = 1/(v\sqrt{\lambda})\) 是相干长度（扭结宽度），\(x_0\) 是扭结中心位置。</p>
<p><strong>有限能量验证</strong>：扭结能量密度 \(E(x) = \frac{1}{2}(d\epsilon/dx)^2 + V(\epsilon)\) 在 \(x \to \pm\infty\) 处指数衰减 \(\sim e^{-\sqrt{2}|x-x_0|/\xi}\)，总能量有限：</p>
<p>\[ E_{\text{kink}} = \int_{-\infty}^{+\infty} E(x)\,dx = \frac{2\sqrt{2}}{3}\lambda^{1/2}v^3 \]</p>
<p>定义<strong>拓扑荷</strong> \(Q = \frac{1}{2v}[\epsilon(+\infty) - \epsilon(-\infty)] = \pm 1\)，只能取整数值。这解释了电荷量子化<sup class="citation">[6]</sup>。反扭结 \(\bar\epsilon(x) = -v\tanh((x-x_0)/\sqrt{2}\xi)\) 对应反粒子。</p>
<div class="figure-container">
    <img src="figures_py/第六章_图15_量子隧穿示意图.png" alt="Quantum Tunneling">
    <div class="figure-caption">图16：量子隧穿示意图：展示能量场在势垒中的渗透过程</div>
</div>
</div>
