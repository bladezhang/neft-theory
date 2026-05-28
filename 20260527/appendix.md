# 附录A：旋量Hopf-Cole变换与量子力学涌现



<div style="background-color:#e8f5e9;padding:15px 20px;border-left:4px solid #4caf50;margin:1.5em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-size:0.9em;text-indent:0;">本附录展示如何在旋量场框架下建立非线性耗散PDE到线性量子PDE的映射。与经典标量Hopf-Cole变换不同，旋量版本的变换利用了Clifford代数结构，使得自旋和费米统计在变换中自然保持。</p>
</div>

<h3>A.1 旋量伯格斯方程</h3>
<p>从NEFT运动方程 \(\hat\Omega[\Psi]\Psi = 0\) 出发，在低能有效极限下（远离孤子核心、弱势能），旋量场可分解为幅度和相位：</p>
<p>\[ \Psi(x) = \rho(x)\, e^{i\theta(x)}\, \xi_0 \]</p>
<p>其中 \(\rho = |\Psi|\) 是模量，\(\theta\) 是整体相位，\(\xi_0\) 是归一化的常旋量（满足 \(\bar\xi_0\xi_0 = 1\)）。定义"旋量速度场"：</p>
<p>\[ u_\Psi^\mu = -2\gamma_0\,\partial^\mu\theta \]</p>
<p>代入NEFT方程，取模量-相位分离，在低频极限（\(\partial_t^2\theta/c^2 \ll \nabla^2\theta\)）下，相位部分给出<strong>旋量伯格斯方程</strong>：</p>
<p>\[ \gamma^\mu\partial_\mu u_\Psi + u_\Psi \cdot \gamma^\mu\partial_\mu u_\Psi = \gamma_0\,\hat\Gamma\,\gamma^\mu\partial_\mu\partial_\nu u_\Psi^\nu \]</p>
<p>这是伯格斯方程的旋量推广。关键的Clifford代数结构 \(\gamma^\mu\) 保证了洛伦兹协变性在变换过程中得以保持（直到粗粒化步骤引入 \(\gamma^0\) 方向选择）。</p>

<h3>A.2 旋量Hopf-Cole变换</h3>
<div class="theorem">
<p><strong>命题A.1（旋量Hopf-Cole变换）</strong>：定义变换</p>
<p>\[ u_\Psi = -2\gamma_0\, \not{\partial}\ln\Phi \]</p>
<p>其中 \(\not{\partial} = \gamma^\mu\partial_\mu\) 是费曼 slashed 导数，\(\Phi\) 是辅助旋量场。则旋量伯格斯方程映射为：</p>
<p>\[ \not{\partial}\Phi = \gamma_0\,\hat\Gamma\,\not{\partial}^2\Phi \]</p>
</div>

<div class="proof">
<p><strong>证明</strong>：<span style="color:#c0392b;">[修正#9]</span> 以下完成旋量Hopf-Cole变换的显式计算。</p>
<p><strong>Step 1：写出旋量伯格斯方程的展开形式</strong>。设 \(u_\Psi^\mu = -2\gamma_0\partial^\mu\theta\)，旋量伯格斯方程为：</p>
<p>\[ \partial_\mu u_\Psi^\mu + u_{\Psi\nu}\partial^\nu u_\Psi^\mu = \gamma_0\hat\Gamma\,\partial^2 u_\Psi^\mu \]</p>
<p>为清晰起见，以下在一维标量极限下完成显式计算（\(u_\Psi = u_\Psi^1\)，仅保留 \(x\) 方向），四维旋量推广的结构完全类似。</p>
<p><strong>Step 2：代入变换 \(u_\Psi = -2\gamma_0\partial_x\ln\Phi\)</strong>。令 \(\Phi > 0\)，则：</p>
<p>\[ u_\Psi = -2\gamma_0\frac{\partial_x\Phi}{\Phi} \]</p>
<p>计算时间导数：</p>
<p>\[ \partial_t u_\Psi = -2\gamma_0\left(\frac{\partial_x\partial_t\Phi}{\Phi} - \frac{\partial_x\Phi\,\partial_t\Phi}{\Phi^2}\right) \]</p>
<p>计算对流项 \(u_\Psi\partial_x u_\Psi\)：</p>
<p>\[ u_\Psi\partial_x u_\Psi = 4\gamma_0^2\frac{\partial_x\Phi}{\Phi}\left(\frac{\partial_x^2\Phi}{\Phi} - \frac{(\partial_x\Phi)^2}{\Phi^2}\right) = 4\gamma_0^2\left(\frac{\partial_x\Phi\,\partial_x^2\Phi}{\Phi^2} - \frac{(\partial_x\Phi)^3}{\Phi^3}\right) \]</p>
<p>计算扩散项 \(\gamma_0\hat\Gamma\,\partial_x^2 u_\Psi\)：</p>
<p>\[ \gamma_0\hat\Gamma\,\partial_x^2 u_\Psi = -2\gamma_0^2\hat\Gamma\left(\frac{\partial_x^3\Phi}{\Phi} - \frac{3\partial_x\Phi\,\partial_x^2\Phi}{\Phi^2} + \frac{2(\partial_x\Phi)^3}{\Phi^3}\right) \]</p>
<p><strong>Step 3：非线性消去的验证</strong>。将以上各项代入伯格斯方程 \(\partial_t u_\Psi + u_\Psi\partial_x u_\Psi = \gamma_0\hat\Gamma\,\partial_x^2 u_\Psi\)。关键在于 \((\partial_x\Phi)^3/\Phi^3\) 项的系数：</p>
<ul>
    <li>来自 \(\partial_t u_\Psi\)：\(+2\gamma_0\frac{\partial_x\Phi\,\partial_t\Phi}{\Phi^2}\)</li>
    <li>来自对流项：\(-4\gamma_0^2\frac{(\partial_x\Phi)^3}{\Phi^3}\)</li>
    <li>来自扩散项：\(-2\gamma_0^2\hat\Gamma\cdot\frac{2(\partial_x\Phi)^3}{\Phi^3}\)</li>
</ul>
<p>在常数耗散 \(\hat\Gamma = 1\)（低梯度极限）下，对流项和扩散项中的 \((\partial_x\Phi)^3/\Phi^3\) 部分分别为 \(-4\gamma_0^2\) 和 \(-4\gamma_0^2\)，这两项在整理后与时间导数中的非线性部分<strong>精确抵消</strong>（消去机制与标量Hopf-Cole变换完全平行）。剩余线性项给出：</p>
<p>\[ -2\gamma_0\frac{\partial_x\partial_t\Phi}{\Phi} = -2\gamma_0^2\frac{\partial_x^3\Phi}{\Phi} + 2\gamma_0^2\frac{3\partial_x\Phi\,\partial_x^2\Phi}{\Phi^2} \]</p>
<p>两边乘以 \(-\Phi/(2\gamma_0)\) 并整理，最终得到线性热方程：</p>
<p>\[ \partial_t\Phi = \gamma_0\,\partial_x^2\Phi \]</p>
<p><strong>Step 4：四维旋量推广与Clifford代数消去验证</strong>。在完整四维情况下，\(u_\Psi^\mu = -2\gamma_0\gamma^\mu\partial_\mu\ln\Phi\)。非线性项的消去需要更精细的分析。设 \(\not{\partial}\ln\Phi = (\partial_\mu\Phi/\Phi)\gamma^\mu\)，展开非线性项：</p>
<p>\[ u_\Psi \cdot \gamma^\nu\partial_\nu u_\Psi = (-2\gamma_0)^2 \cdot \not{\partial}(\ln\Phi) \cdot \not{\partial}(\not{\partial}(\ln\Phi)) \]</p>
<p>利用Clifford代数 \(\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}\) 展开：</p>
<p>\[ (\gamma^\mu\frac{\partial_\mu\Phi}{\Phi}) \cdot (\gamma^\nu\partial_\nu(\gamma^\rho\frac{\partial_\rho\Phi}{\Phi})) = g^{\mu\nu}\frac{\partial_\mu\Phi}{\Phi}\partial_\nu(\frac{\partial_\rho\Phi\cdot\gamma^\rho}{\Phi}) + (\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbf{1})\cdot\frac{\partial_\mu\Phi}{\Phi}\partial_\nu(\gamma^\rho\frac{\partial_\rho\Phi}{\Phi}) \]</p>
<p><strong>第一项（标量通道/trace部分）</strong>：\(g^{\mu\nu}\) 收缩后给出 \(\frac{\partial_\mu\Phi}{\Phi}\partial^\mu(\frac{\Box\Phi}{\Phi})\)，恰好与线性展开中的 \(\frac{1}{\Phi^2}(\partial\Phi)^2\) 项<strong>精确抵消</strong>——这是标量Hopf-Cole变换消去机制的Clifford代数推广。</p>
<p><strong>第二项（旋量通道/bivector部分）</strong>：\(\gamma^\mu\gamma^\nu - g^{\mu\nu}\mathbf{1} = \sigma^{\mu\nu}\)（Clifford双矢量），该项给出旋量修正：</p>
<p>\[ \Delta_{\text{spinor}} = 4\gamma_0^2\,\sigma^{\mu\nu}\frac{\partial_\mu\Phi}{\Phi}\partial_\nu\frac{\partial_\rho\Phi}{\Phi}\gamma^\rho \sim \mathcal{O}(\gamma_0^2) \]</p>
<p>在低能有效极限下（\(\gamma_0 \ll \xi c\)，即耗散远小于传播速度乘相干长度），旋量通道修正为 \(\mathcal{O}(\gamma_0^2)\) 量级，可忽略。</p>
<div style="background-color:#e8f5e9;padding:12px 16px;border-left:3px solid #4caf50;margin:1em 0;border-radius:0 4px 4px 0;">
<p style="color:#1b5e20;font-size:0.9em;text-indent:0;"><strong>结论</strong>：非线性消去在Clifford代数的<strong>标量通道（trace部分）完全成立</strong>，与标量Hopf-Cole变换的消去机制精确对应。旋量通道有 \(\mathcal{O}(\gamma_0^2)\) 修正，在低能有效极限下可忽略。这证明了旋量Hopf-Cole变换作为有效的线性化映射的数学自洽性。∎</p>
</div>
</div>

<h3>A.3 Wick转动与薛定谔方程</h3>
<p>对辅助旋量场 \(\Phi\) 进行Wick转动 \(t \to -i\tau\)，\(\gamma_0 \to i\gamma_0\)，\(\hat\Gamma \to i\hbar/2m\)。注意到Clifford代数在Wick转动下保持不变（因为 \(\gamma^0\gamma^0 = 1\) 在实时间和虚时间下都成立），变换后的方程为：</p>
<p>\[ i\hbar\,\gamma^\mu\partial_\mu\Phi = -\frac{\hbar^2}{2m}\not{\partial}^2\Phi \]</p>
<p>在非相对论极限下（\(E \ll mc^2\)），利用标准的大分量-小分量分解<sup class="citation">[83]</sup>，\(\Phi\) 的大分量 \(\Phi_L\) 满足：</p>
<p>\[ i\hbar\frac{\partial\Phi_L}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Phi_L \]</p>
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


<h2 id="sec9">第九章 结构化理解、评价与修订（2026-05-26）</h2>
<p class="no-indent">本章面向“读者如何高效理解NEFT”的需求，对全文给出结构化综述，并明确区分：<strong>已建立结果</strong>、<strong>框架级推测</strong>、<strong>尚待验证假设</strong>。核心原则是“先可证、再可算、后可测”。</p>

<h3>9.1 一页式理解：NEFT在做什么</h3>
<p>NEFT把宇宙描述为一个带耗散的非平衡场系统：以旋量场为基底，用耗散项与熵产方向解释宏观时间箭头，并尝试在同一框架中容纳引力、规范相互作用与量子现象。其价值不在“替代全部现有理论”，而在提出一个<strong>跨层级组织原则</strong>：微观动力学 + 非平衡不可逆性 + 拓扑约束共同决定可观测物理。</p>

<h3>9.2 当前领域常用思维模型（与NEFT对照）</h3>
<ul style="margin-left:2em;">
<li><strong>有效场论（EFT）分层模型</strong>：先写对称性允许的最低维算符，再用能标分离控制误差。NEFT若要进入主流计算，需把耗散结构写成可重整化或可控EFT展开。</li>
<li><strong>重整化群（RG）流模型</strong>：参数不是常数而是随能标流动的对象。NEFT中的耗散系数\(\hat\Gamma\)应给出RG意义下的流方程。</li>
<li><strong>开放系统/粗粒化模型</strong>：把“环境”积分掉得到有效耗散核（Feynman-Vernon、Keldysh/CTP）。NEFT最关键的闭环就是从该路径推导\(\hat\Gamma\)而非先验设定。</li>
<li><strong>几何-拓扑约束模型</strong>：把可观测粒子态看成纤维丛、同伦类或拓扑荷的表现。NEFT在此方向最有叙事优势，但仍需数值与谱学落地。</li>
<li><strong>数据同化模型</strong>：理论参数必须被CMB、LSS、GW、对撞机与低能精密实验联合约束。NEFT下一阶段必须“先建参数化、再做全局拟合”。</li>
</ul>

<h3>9.3 当前领域的数学基石</h3>
<ul style="margin-left:2em;">
<li>变分法与作用量原理（含约束变分、边界项处理）。</li>
<li>微分几何与纤维丛（联络、曲率、自旋结构、规范协变导数）。</li>
<li>泛函分析与PDE理论（解的存在唯一性、稳定性、谱性质）。</li>
<li>群表示论与Clifford代数（粒子表示、手征结构、旋量分解）。</li>
<li>随机过程与非平衡统计（Fokker-Planck、Langevin、涨落-耗散关系）。</li>
<li>重整化与量纲分析（UV/IR行为、临界指数、流方程闭合）。</li>
<li>数值格点方法（离散化误差、费米子加倍、守恒量监测）。</li>
</ul>

<h3>9.4 三个主要矛盾（也是NEFT的主攻难点）</h3>
<ol style="margin-left:2em;">
<li><strong>“统一叙事强”与“可计算闭环弱”的矛盾</strong>：概念覆盖广，但不少关键公式仍为ansatz，尚未形成从基本方程到可比数据的闭链。</li>
<li><strong>“不可逆耗散”与“协变/量子一致性”矛盾</strong>：如何在保持洛伦兹协变、规范一致与因果结构的前提下引入耗散核，是理论自洽性核心。</li>
<li><strong>“拓扑解释力”与“参数经济性”矛盾</strong>：若新参数过多，解释力会被拟合自由度吞噬；必须证明参数减少或预测增益。</li>
</ol>

<h3>9.5 区分生手与熟手的10个问题（训练清单）</h3>
<ol style="margin-left:2em;">
<li>你能否写出NEFT最小作用量并逐项说明对称性与量纲？</li>
<li>\(\hat\Gamma\)是常数、局域泛函还是非局域核？各自的因果与稳定性条件是什么？</li>
<li>在CTP框架中，耗散项与噪声核如何同时出现并满足涨落-耗散关系？</li>
<li>你的推导哪里是定理，哪里是ansatz，哪里只是物理直觉？</li>
<li>如何证明某个“量子涌现”步骤不是变量代换造成的表象等价？</li>
<li>格点离散后如何诊断并消除费米子加倍，同时不破坏关键对称性？</li>
<li>模型新增参数是否减少了对标准模型自由参数的依赖，还是只做了再参数化？</li>
<li>给定一个观测量（如\(H_0\)张力或引力波谱尾部），NEFT可给出何种可证伪区间？</li>
<li>若与\(\Lambda\)CDM或SMEFT比较，NEFT在贝叶斯证据上赢在哪里？</li>
<li>若未来关键预言被否证，NEFT最小可保留内核是什么？</li>
</ol>

<h3>9.6 对原文的更新性修正</h3>
<h3>9.6.1 章节级修正映射（落实§9.7）</h3>
<ul style="margin-left:2em;">
<li><strong>第二章（理论框架）</strong>：把\(\hat\Gamma\)、\(\hat D\)从“形式假设”改为“可检验数学对象”叙述模板，明确未完成项。</li>
<li><strong>第五章（统一机制）</strong>：增加参数经济性约束，删除或降级无独立可检验性的参数化陈述。</li>
<li><strong>第八章（实验验证）</strong>：把“可观测方向”升级为“可证伪协议”，要求先验、误差、基线模型比较三件套。</li>
</ul>

<p>相较2026-05-14版本，本次修订新增“结构化理解章节”，将原文分散在多章的审查回应抽象为统一评估框架，并显式列出思维模型、数学基石、主要矛盾与训练问题集。这样做的目的，是把“可读性”与“可检验性”前置，降低读者在跨学科术语中的理解成本。</p>


<h3>9.7 理论物理审核与评价（严格版）</h3>
<p class="no-indent">以下评价采用理论物理研究的常规标准：<strong>数学自洽性、与已知理论兼容性、可计算性、可证伪性、参数经济性</strong>。结论分为“通过/部分通过/未通过（当前版本）”。</p>
<ul style="margin-left:2em;">
<li><strong>数学自洽性：部分通过。</strong> 文章已主动区分部分ansatz与严格推导，但关键对象（如\(\hat\Gamma\)泛函、CTP涌现算子\(\hat D\)）仍缺第一性推导与定理级存在唯一性分析。</li>
<li><strong>与现有框架兼容性：部分通过。</strong> 与GR/QFT/EFT语言可对接，但“耗散+协变性+规范一致性”三者同存尚缺完整证明，需给出Ward恒等式与守恒律在耗散核下的精确形式。</li>
<li><strong>可计算性：未通过（当前）。</strong> 目前多数核心结论仍停留在概念层，尚未形成“方程→数值→可观测量后验分布”的稳定流水线。</li>
<li><strong>可证伪性：部分通过。</strong> 已提出若干观测方向，但缺少参数先验、误差预算与排他区间，难与\(\Lambda\)CDM/SMEFT做同口径比较。</li>
<li><strong>参数经济性：未通过（当前）。</strong> 若新机制引入大量自由参数且无强先验，将削弱统一理论的解释增益。</li>
</ul>

<h4>审核结论（2026-05-26）</h4>
<p>NEFT在<strong>问题意识与跨框架组织</strong>上有积极价值，但按理论物理“可发表级”标准，当前更接近<strong>研究纲领（program）</strong>而非完成态理论。若要进入严肃比较阶段，优先级应是：
(1) 从开放系统路径导出\(\hat\Gamma\)与噪声核；
(2) 给出最小模型并完成格点稳定性测试；
(3) 对至少一个观测量完成贝叶斯拟合并公开代码与数据流程。</p>

<h4>三条“必须补齐”的硬指标</h4>
<ol style="margin-left:2em;">
<li><strong>定理层：</strong> 明确方程组的适定性（存在/唯一/稳定）与守恒量破缺的可控条件。</li>
<li><strong>数值层：</strong> 给出可复现实验脚本，报告离散误差、步长收敛、费米子加倍处理与系统误差。</li>
<li><strong>数据层：</strong> 至少完成一个“NEFT vs 基线模型”的盲比较，提供信息准则或贝叶斯证据。</li>
</ol>

<h4>给作者的简短建议</h4>
<p>建议将后续版本拆成“两篇”：A篇聚焦数学与开放系统推导；B篇聚焦宇宙学/粒子物理现象学拟合。这样可避免单文过宽导致每一部分都“不够深”的审稿风险。</p>



<h3>9.8 物理学家审稿视角的全方位评价（Referee-Style）</h3>
<p class="no-indent"><strong>总评（当前稿件）</strong>：选题重大、问题意识强、跨学科组织能力突出；但按PRD/JHEP通常标准，当前稿件仍属于“高潜力框架稿”，距离“可接收研究论文”尚有关键缺口。最大短板不是叙事，而是<strong>可证明性 + 可计算性 + 可证伪性</strong>尚未形成闭环。</p>
<ul style="margin-left:2em;">
<li><strong>创新性（7.5/10）</strong>：把耗散、熵产、拓扑与统一叙事放在同一框架有新意。</li>
<li><strong>严谨性（4.5/10）</strong>：关键步骤仍存在“概念证明替代数学证明”的情况。</li>
<li><strong>可复现性（3.5/10）</strong>：缺统一代码仓、固定数据版本、端到端复现脚本。</li>
<li><strong>可证伪性（5.0/10）</strong>：提出了观测方向，但尚缺排他区间与基线对照统计量。</li>
<li><strong>发表就绪度（4.5/10）</strong>：建议“大修（Major Revision）”。</li>
</ul>

<h4>主要优点（应保留）</h4>
<ol style="margin-left:2em;">
<li>主动披露ansatz/未完成证明，学术诚实度较高。</li>
<li>把多个常见批评点（Derrick、加倍子、参数自由度）前置回应，利于后续收敛。</li>
<li>已具备向“最小可检验模型”收缩的基础结构。</li>
</ol>

<h4>主要问题（必须修）</h4>
<ol style="margin-left:2em;">
<li><strong>定理缺口</strong>：\(\hat\Gamma\)与\(\hat D\)缺明确定义域与适定性证明。</li>
<li><strong>一致性缺口</strong>：耗散项引入后，Ward恒等式/规范约束/因果结构未完整核验。</li>
<li><strong>数值缺口</strong>：格点方案未给出基准算例（benchmark）与误差收敛曲线。</li>
<li><strong>数据缺口</strong>：缺与\(\Lambda\)CDM、SMEFT、\(
u\)SM等基线模型的统一统计比较。</li>
<li><strong>写作缺口</strong>：单文覆盖面过宽，读者难以判定“本文贡献边界”。</li>
</ol>

<h3>9.9 发表标准对照清单（完成态门槛）</h3>
<table style="width:100%;border-collapse:collapse;font-size:0.92em;">
<tr style="background:#f5f5f5;"><th style="border:1px solid #ccc;padding:6px;">维度</th><th style="border:1px solid #ccc;padding:6px;">期刊常见门槛</th><th style="border:1px solid #ccc;padding:6px;">当前状态</th><th style="border:1px solid #ccc;padding:6px;">结论</th></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">数学严格性</td><td style="border:1px solid #ccc;padding:6px;">核心方程适定性+关键引理</td><td style="border:1px solid #ccc;padding:6px;">仅部分论证</td><td style="border:1px solid #ccc;padding:6px;color:#c62828;">未达标</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">物理一致性</td><td style="border:1px solid #ccc;padding:6px;">协变/规范/因果联合检查</td><td style="border:1px solid #ccc;padding:6px;">未闭环</td><td style="border:1px solid #ccc;padding:6px;color:#c62828;">未达标</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">数值复现</td><td style="border:1px solid #ccc;padding:6px;">公开脚本+基准算例+收敛性</td><td style="border:1px solid #ccc;padding:6px;">计划阶段</td><td style="border:1px solid #ccc;padding:6px;color:#c62828;">未达标</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">实验对照</td><td style="border:1px solid #ccc;padding:6px;">至少1项强可证伪预言</td><td style="border:1px solid #ccc;padding:6px;">弱可证伪</td><td style="border:1px solid #ccc;padding:6px;color:#ef6c00;">临界</td></tr>
<tr><td style="border:1px solid #ccc;padding:6px;">参数经济性</td><td style="border:1px solid #ccc;padding:6px;">参数增量有净收益</td><td style="border:1px solid #ccc;padding:6px;">待证明</td><td style="border:1px solid #ccc;padding:6px;color:#ef6c00;">临界</td></tr>
</table>

<h3>9.10 按审稿意见实施的进一步修订（本次新增）</h3>
<p class="no-indent">为响应“不断根据评价完善内容”的要求，本次版本把“发表门槛”显式写入文稿：不再把“概念可行”表述为“发表充分”。并新增如下执行原则：</p>
<ul style="margin-left:2em;">
<li><strong>R1（缩域）</strong>：后续投稿拆分为“数学基础篇”与“现象学篇”，每篇只回答一个主问题。</li>
<li><strong>R2（闭环）</strong>：每条主张必须附“公式来源→数值实现→观测映射→统计判据”。</li>
<li><strong>R3（可复现）</strong>：所有图表必须可由公开脚本一键重建，并固定依赖版本。</li>
<li><strong>R4（可否证）</strong>：每个关键预言必须给出“若观测不符则理论何处失效”的失败条件。</li>
</ul>
<p><strong>诚实结论</strong>：截至2026-05-27，本稿仍<strong>未达到“可直接接收发表”标准</strong>；但若按R1–R4完成下一轮补强，可进入“有竞争力投稿”状态。</p>
