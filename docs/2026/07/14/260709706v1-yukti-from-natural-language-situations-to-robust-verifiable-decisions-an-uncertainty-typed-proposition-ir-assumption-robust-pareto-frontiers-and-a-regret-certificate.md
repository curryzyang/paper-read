# YUKTI: From Natural-Language Situations to Robust, Verifiable Decisions An Uncertainty-Typed Proposition IR, Assumption-Robust Pareto Frontiers, and a Regret Certificate

- 区域：精读区
- 排名：1
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Suyash Mishra
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09706v1) · [PDF](https://arxiv.org/pdf/2607.09706v1)

## TLDR
YUKTI transforms natural-language situations into robust, verifiable decisions by representing assumptions as uncertainty-typed propositions and using assumption-robust Pareto frontiers to produce a compromise with a proven regret certificate and auditable traceability.

## Abstract
Language models turn a worded situation into a numeric plan, and the dominant pipelines (NL4Opt, OptiMUS, ORLM, OR-LLM-Agent) commit to a single objective and point-valued coefficients, then solve once. For decisions that allocate real budget, effort, or clinical attention, that confidence is the failure mode: every objectified number is an assumption, and a plan optimal only if the guesses are exactly right is fragile -- mimicry of computation. YUKTI changes the target of autoformulation. Its representation is a typed-proposition graph whose relationships carry shape priors, coefficient uncertainty, and provenance. YUKTI routes each stage to an exact, nonlinear, or evolutionary solver; couples stages by a distributional Pareto hand-off; and introduces Assumption-Robust Pareto Frontiers (ARPF), resampling assumptions (including structural epsilon-contamination) to score how often each action survives (rho). We prove a bound making rho an exact factor of decision regret, add auditable traceability, and synthesize a benchmark-faithful data foundation when none exists (SRJANA). We validate three ways: under controlled misspecification the robust compromise cuts mean and tail regret by over 90% versus a naive point plan; on a regulated commercial decision we optimize inside a lawful action space and price the downside in euros; and on a real public dataset of 41,188 decisions an out-of-sample backtest beats the logged status quo by 34% and a naive point rule by 4% while reducing the optimizer's curse. The solvers are standard; we claim no benchmark-SOTA win. A head-to-head shows an LLM given the correct numbers, and single-objective optimization, both incur about 47x the held-out regret of YUKTI -- an LLM is a formulator, not a solver. Under long-range causal coupling, the forward hand-off becomes unsound, locating where it must become a backward-induction causal policy.


## 精读解读（中文）
### 一、研究动机
现有自然语言到数值规划的管线（如NL4Opt、OptiMUS、ORLM）通常采用单目标、点值系数并一次性求解，这在实际资源分配决策中非常脆弱：每个物化数字都是一个假设，仅当猜测完全正确时才最优的规划是危险的。YUKTI旨在改变自动公式化的目标，通过引入带不确定性的中间表示和鲁棒性评估来避免这种脆性。

### 二、技术方案（Method）
YUKTI的流水线输入为自然语言决策简报，首先构建一个带类型命题图（Typed Proposition IR），其中每个量化关系带有形状先验、系数的不确定性分布和来源标签。然后，结构感知路由器根据问题结构将每个阶段导向精确求解器（如HiGHS）、非线性求解器或进化多目标优化器（如NSGA-III）。阶段之间通过分布帕累托交接传递信号值。核心模块是假设鲁棒帕累托边界（ARPF），它对假设进行重采样（包括结构ε-污染误设定），评估每个候选动作在采样假设下保持可行且非支配的概率ρ。当无数据可用时，SRJANA模块从提取的规范和网络基准锚点合成上下文数据集。最终输出稳健折衷方案和决策可追溯性报告（分段归因与影子价格）。

### 三、结果（Result）
在受控结构误设定下，YUKTI的鲁棒折衷将平均和尾部遗憾相比天真点规划降低超过90%。在包含41188个市场营销决策的真实数据集上，样本外回测表明YUKTI的鲁棒规则超过历史现状34%，并比天真点规则好4%，同时减少了优化者诅咒。与给定正确数字的LLM和单目标优化头对头比较显示，两者都产生约47倍于YUKTI的遗憾，证明LLM是公式化者而非求解者。

### 四、结论（Conclusion）
YUKTI是一个完整的决策框架，通过带类型命题图和假设鲁棒帕累托边界实现了鲁棒、可追溯的自动公式化。它表明在进入高风险决策时，不应仅依赖LLM的一次性求解，而应保持目标冲突明确、系数不确定性被处理，并报告推荐在自身假设下的存活概率。该方法在多种真实场景中验证了有效性，但长期因果耦合下其前向交接变得不可靠，需要反向归纳因果策略。

### 五、方法论与关键技术细节
关键点：1）带类型命题图包含形状先验（如线性、指数、S形）和系数分布（例如均匀、正态）；2）ARPF重采样包括结构ε-污染，使得ρ成为遗憾的精确因子；3）求解器使用标准库（HiGHS、pymoo等），不追求算法创新；4）SRJANA在网络锚点基础上合成数据，使得系统能处理全新场景；5）决策可追溯性通过分段归因和影子价格实现，增强了审计能力；6）局限性：在具有长期因果耦合的行动下，前向多阶段交接不再合理，需要过渡到向后归纳因果策略；7）整体计算需求因重采样次数增大而增加，但通过并行可缓解。
