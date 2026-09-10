# DiffLUT-Net: Differentiable Training of FPGA LUT Networks with Learnable Connectivity

- 区域：精读区
- 排名：10
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Jiaqi Ye, Xinrui Gong, Jingcun Wang, Olga Kondrateva, Bing Li, Grace Li Zhang
- 机构：TU Darmstadt, TU Ilmenau
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09254v1) · [PDF](https://arxiv.org/pdf/2609.09254v1)

## TLDR
DiffLUT-Net is an FPGA-native neural network that jointly learns each six-input LUT’s truth table and input connectivity from scratch through differentiable relaxations, then discretizes and exports the trained network as synthesizable Verilog, achieving favorable accuracy–resource trade-offs across five benchmarks.

## Abstract
Field-programmable gate arrays (FPGAs) enable efficient neural-network inference, but most deployment flows either accelerate multiply-accumulate operations or convert pretrained quantized models into lookup tables (LUTs). We present DiffLUT-Net, an FPGA-native network connected by six-input LUTs that are trained from scratch. We jointly learn the 64 truth-table entries of a LUT and the source to each of its six input ports using a differentiable LUT function relaxation and hardware source selection. After training, the truth tables and connections are discretized, unused logic can be pruned, and the network is exported directly as synthesizable Verilog. Across five benchmarks, DiffLUT-Net achieves favorable accuracy-resource trade-offs. These results demonstrate the effectiveness of jointly learning LUT functions and sparse connectivity for compact FPGA-native inference. The code is available at https://github.com/TUDa-HWAI/DiffLUT-Network.


## 精读解读（中文）
### 一、研究动机
FPGA推理部署常将训练与硬件实现分离，先训练MAC网络再量化或映射为LUT，导致学习到的模型与FPGA原语之间存在鸿沟；已有真值表转换方法受输入位宽指数增长限制，而直接训练逻辑或LUT网络的方法又未必同时优化LUT函数与物理连接并走通完整硬件流程。

### 二、技术方案（Method）
DiffLUT-Net以六输入LUT6为基本计算单元从零训练，流程包括温度计编码将实值特征转为二进制信号、一个或多个可训练LUT6层、GroupSum按类别分组累加最后层LUT输出并取最大和为预测。每个LUT的64个真值表项用参数lambda_j经sigmoid得到omega_j，并以K输入LUT的多线性松弛 y=sum_{u=0}^{2^K-1} omega_j prod_i x_i^{a_i}(1-x_i)^{1-a_i} 进行可微训练；层间连接用连接矩阵A学习，每个LUT输入端口在训练时考虑上一层所有输出，训练后每个端口保留一个源进行硬选择。训练完成后将真值表二值化、固定连接、剪除未用逻辑，并导出可综合Verilog，再做布局布线后FPGA评估。

### 三、结果（Result）
在五个基准上，DiffLUT-Net取得有利的精度-资源权衡；摘要给出的代表性结果包括紧凑JSC CERNBox模型达到72.5%精度，以及在MNIST上相当精度下紧凑配置的资源占用显著更优。与算术加速器、训练后真值表方法以及直接训练的逻辑或LUT网络相比，联合学习LUT函数与稀疏连接可实现更紧凑的FPGA原生推理。完整训练到硬件流程在Vivado布局布线后得到验证。

### 四、结论（Conclusion）
结果表明，将LUT真值表与输入端口连接作为可微参数联合优化，可在保持FPGA合法布线的同时获得紧凑且精度可接受的FPGA原生网络；DiffLUT-Net提供了从训练、离散化、剪枝到可综合Verilog导出的端到端路径，说明硬件原生LUT网络是低延迟FPGA推理的可行方向。

### 五、方法论与关键技术细节
关键实现点包括：输入采用分布感知的温度计二进制编码；每个LUT6有64个可训练参数，经sigmoid约束到[0,1]，推理时以0.5阈值二值化；连接矩阵A的a_{i,j}连接上一层输出y_j与当前层输入端口x_i，每六个连续行对应一个LUT6的六个输入端口，训练后每端口选一个源并暴露未用上游逻辑以供剪枝；最后层LUT输出由GroupSum分到类别组并取最大组和分类。局限是LUT真值表随输入位数指数增长，因此方法依赖LUT6固定扇入、低精度或稀疏连接和剪枝；预览未给出损失函数、优化器、超参、直通估计及离散化误差处理细节，完整复现需参考原文与开源代码。
