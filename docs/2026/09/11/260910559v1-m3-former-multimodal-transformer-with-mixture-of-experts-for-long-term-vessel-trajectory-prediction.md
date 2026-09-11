# M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Wenzhe Jin, Haina Tang
- 机构：University of Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10559v1) · [PDF](https://arxiv.org/pdf/2609.10559v1)

## TLDR
M³-Former is an LLM-enhanced multimodal Transformer with dual-granularity Mixture-of-Experts and a steering-weighted loss that fuses vessel static attributes and navigational intent with dynamic trajectory features to improve long-term vessel trajectory prediction.

## Abstract
To address the challenges of behavioral multimodality, limited semantic utilization, and long-term error accumulation in vessel trajectory prediction, this paper proposes M3-Former, a multimodal trajectory prediction framework enhanced by large language models (LLMs). The proposed framework incorporates vessel static attributes and navigational intent as semantic priors for long-term trajectory modeling. Specifically, a unified multimodal representation space is constructed, in which static semantic information is encoded by a pre-trained LLM and aligned with dynamic trajectory features through self-attention. To jointly capture global route planning and local motion variations, a dual-granularity Mixture-of-Experts (MoE) architecture is introduced, where sequence-level experts model global navigation trends and token-level experts refine fine-grained maneuvering behaviors. In addition, a Steering-Weighted Cross-Entropy loss is designed to alleviate the long-tail distribution of sparse turning samples and improve prediction accuracy in critical maneuvering scenarios. Experiments on a real-world Danish AIS dataset demonstrate that M\textsuperscript{3}-Former consistently outperforms state-of-the-art baselines across prediction horizons from 1 to 4 hours. In the 4-hour prediction task, the proposed method reduces Average Displacement Error (ADE) and Final Displacement Error (FDE) by 4.4\% and 5.1\%, respectively, compared with the strongest baseline. Qualitative and ablation analyses further verify that semantic fusion effectively reduces long-term trajectory drift, while the dual-granularity MoE improves robustness in complex waterways and route-branching scenarios. The proposed framework establishes a semantic-guided hierarchical prediction paradigm, in which high-level navigational intent and local motion dynamics are jointly modeled for robust long-term vessel trajectory forecasting.


## 精读解读（中文）
### 一、研究动机
长时船舶轨迹预测受行为多模态、语义信息利用不足和长期误差累积影响，且随时间延长局部交互作用减弱，目的地、船型等静态语义与航行意图成为轨迹演化主导因素。现有方法多依赖动态AIS特征，难以同时建模全局航线规划与局部操纵，因此需要语义引导的层次化预测框架。

### 二、技术方案（Method）
M3-Former将船舶动态轨迹特征（经纬度、SOG、COG）与静态属性（目的地、船型、长宽、吃水、MMSI、ETA等）统一建模，把静态信息转为自然语言描述后由冻结预训练LLM编码，再经投影与轨迹嵌入拼接并输入共享Transformer自注意力融合。模型对空间坐标进行离散分箱，将连续轨迹预测转为对经纬度、SOG、COG的多变量离散概率生成。其双粒度MoE包括序列级专家（对全序列池化上下文做软门控，建模全局航向与航路趋势）和令牌级专家（对每时刻表示做软门控，细化局部机动），并采用先序列级后令牌级的S到T顺序。训练使用Steering-Weighted Cross-Entropy，在四变量交叉熵基础上对相邻时刻航向变化超过阈值tau的样本乘以1+alpha权重，以缓解转向样本长尾问题。

### 三、结果（Result）
在丹麦海事局2023年1月到3月真实AIS数据上，M3-Former在1至4小时预测时域内持续优于现有基线。4小时预测中，相较最强基线ADE降低4.4%、FDE降低5.1%。消融与定性分析表明语义融合可减少长期轨迹漂移，双粒度MoE提升复杂航道与航路分叉场景鲁棒性，且序列级先于令牌级的MoE-S到T配置优于反向配置。

### 四、结论（Conclusion）
该工作提出语义引导的层次化长时船舶轨迹预测范式，通过LLM语义先验、统一多模态表示、双粒度MoE和转向加权损失，联合建模高层航行意图与局部运动动力学。结果表明该方法能在长时域保持物理合理性与多模态覆盖，并为智能海事监控、航线规划与避碰提供支撑。

### 五、方法论与关键技术细节
数据为DMA真实AIS，覆盖2023-01-01至2023-03-31，输入含动态lat/lon/SOG/COG及静态MMSI、类型、长宽、吃水、目的地、ETA；静态文本由冻结LLM编码，动态特征线性映射。预测为离散空间分类加自回归条件概率建模，损失为lat/lon/SOG/COG四项交叉熵之和，转向权重lambda=1+alpha乘指示函数(|Delta COG|>tau)，需调tau和alpha。双粒度MoE用平均池化全局向量与逐token表示经Softmax门控选择专家，实验验证序列级MoE先于token级MoE更优。局限性包括对AIS静态语义质量与文本模板依赖、冻结LLM与空间离散化带来的表示约束、MoE路由与长时预测的计算和超参敏感性。
