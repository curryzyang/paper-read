# Adaptive Cost-Sensitive Machine Learning for Autonomous Robot Navigation Failure Prediction: When Not All Errors Are Equal

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Rifa Ferzana
- 机构：University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05593v1) · [PDF](https://arxiv.org/pdf/2609.05593v1)

## TLDR
This paper reframes autonomous robot navigation failure prediction as consequence-sensitive forecasting by introducing an adaptive cost-sensitive learning framework that weights training samples by categorical severity and physical context (velocity, obstacle proximity, sensing uncertainty), substantially improving high-severity and collision recall at the cost of a more conservative operating point rather than better ranking.

## Abstract
Autonomous robot navigation failures differ not only in categorical severity but also in the physical context in which they occur. A near-miss at low speed under reliable sensing is not equivalent to the same event during rapid motion, close obstacle approach or degraded perception. This paper reframes navigation failure prediction as consequence-sensitive forecasting. We first establish a fixed baseline in which training weights are modulated by categorical severity, then introduce an adaptive extension defining a state-dependent consequence function combining severity with normalised velocity, obstacle proximity and sensing uncertainty, together with a risk-sensitivity term that rises as conditions deteriorate. We evaluate on 2,000 simulated differential-drive episodes (~1,000,000 timesteps) using episode-level GroupKFold, with external validation on the UCI SCITOS G5 dataset. Fixed weighting raises Logistic Regression high-severity recall from 0.851 to 0.985 and reduces missed consequence cost from 1,940 to 313; the adaptive extension reaches 0.998 and 82. Under matched false-positive conditions, however, the discriminative advantage is modest (0.986 versus 0.984), so most of the gain reflects a more conservative operating point rather than better ranking. The effect is consistent across all five folds and stable across a threefold span of context coefficients. Because the primary simulation produced no collisions, we add a controlled extension in which 108 of 600 episodes terminate in contact: collision recall rises from 0.850 to 0.966 (fixed) and 0.984 (adaptive), with missed collision cost falling from 1,000 to 105, at false-positive rates of 0.413 and 0.799, respectively. Context-dependent consequence modelling thus provides a principled mechanism for allocating conservatism by physical risk.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
