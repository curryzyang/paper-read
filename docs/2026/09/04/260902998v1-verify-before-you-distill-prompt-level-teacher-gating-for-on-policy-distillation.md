# Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Zhiwei Zhang, Zechen Sun, Fei Zhao, Kang Peng, Bin Liang, Huayu Deng, Yao Hu, Kam-Fai Wong, Mu Chuan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02998v1) · [PDF](https://arxiv.org/pdf/2609.02998v1)

## TLDR
TLDR: This paper proposes Teacher-Gated On-Policy Distillation (TGOPD), which uses verifier-scored teacher probes to check teacher reliability at the prompt level and gates between dense OPD supervision and verifier-grounded GRPO, outperforming vanilla OPD across single- and multi-domain math, code, and instruction-following tasks at 4B and 35B scales while also raising teacher-node GPU utilization from 9.8% to 78.9%.

## Abstract
On-policy distillation (OPD) accelerates post-training by providing dense token-level supervision from a frozen teacher on the student's own rollouts. Vanilla OPD applies this supervision uniformly across prompts, without checking whether the teacher is reliable for each prompt. Because reverse KL is mode-seeking, a confidently wrong teacher can induce a strong yet misleading update. Distributional proxies, such as entropy or teacher-student likelihood agreement, measure uncertainty or agreement but do not directly verify outcome correctness. We introduce Teacher-Gated On-Policy Distillation (TGOPD), built on the principle that teacher reliability should be verified at the prompt level before dense supervision is admitted. TGOPD estimates reliability from a small set of verifier-scored teacher probes and routes each prompt exclusively to dense OPD when the reliability check passes or to verifier-grounded GRPO otherwise. Across 4B and 35B students in mathematics, code, and instruction following, TGOPD outperforms Vanilla OPD in all six single-domain settings and achieves higher seven-benchmark averages at both scales under multi-domain training. By using otherwise-idle teacher capacity for reliability estimation, TGOPD also reduces teacher-side compute waste in asynchronous OPD, increasing teacher-node GPU utilization from 9.8% to 78.9% in the measured 4B single-domain run.


## 精读解读（中文）
### 一、研究动机
Vanilla on-policy distillation对每个提示词无差别地施加教师密集token级监督，未验证教师在该提示上的可靠性，而反向KL的模式寻找特性会使自信但错误的教师产生强误导更新，熵或师生似然一致等分布指标不能直接验证结果正确性，因此需要在密集监督之前进行提示级教师可靠性验证。

### 二、技术方案（Method）
提出Teacher-Gated On-Policy Distillation，对每个提示先让教师生成少量probe输出，用verifier为其评分，据此估计教师在该提示级上的可靠性；可靠性检查通过时，将提示路由至密集OPD，教师基于学生自身rollout提供token级反向KL监督；检查失败时，路由至verifier-grounded GRPO，以verifier信号作为偏好奖励优化学生。在异步OPD中，利用原本空闲的教师节点来计算可靠性估计。

### 三、结果（Result）
在4B和35B学生模型上，覆盖数学、代码和指令遵循三个领域，TGOPD在全部六个单域设置中均优于Vanilla OPD；多域训练下两个规模的平均七基准分数也更高。在异步OPD的4B单域运行中，教师节点GPU利用率从9.8%提升至78.9%。

### 四、结论（Conclusion）
TGOPD通过提示级验证教师可靠性来决定是否接受密集蒸馏或改用verifier-grounded GRPO，有效克服了Vanilla OPD的盲目监督问题，同时提升性能并减少教师端计算浪费，验证了先验证再蒸馏原则的有效性。

### 五、方法论与关键技术细节
方法通过verifier对教师少量probe输出评分来估计每个提示上的可靠性，门控作为二元路由：通过检查的提示使用反向KL密集蒸馏，未通过的提示使用verifier-grounded GRPO；该估计利用异步OPD中本会空闲的教师计算资源，降低教师节点算力浪费。实现细节中未给出probe数量、评分阈值等具体超参数，也未讨论verifier误差对可靠性估计的鲁棒性影响。
