# Dandelion: A Spherical Flower for Neural Simulation of Planetary Dynamics

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Till Muser, Giovanni Abati, Ivan Dokmanić
- 机构：University of Basel
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27521v1) · [PDF](https://arxiv.org/pdf/2608.27521v1)

## TLDR
Dandelion is a spherical, convolution-free neural PDE solver that uses tangent-plane warp displacements and great-circle transport with spherical-harmonic pooling, and it outperforms existing spherical architectures on a newly introduced benchmark suite of diverse planetary dynamics datasets.

## Abstract
Many dynamical processes unfold on the sphere but the default scientific machine learning architectures are Euclidean. Applying these architectures on a regular lat-lon grid causes problems: Cartesian convolutions become distorted at high latitude; 2D FFTs in Fourier neural operators incorrectly assume double periodicity; Cartesian positional encodings in ViTs distort spherical geodesic distances. Recent work moves towards natively spherical primitives, including spherical convolutions (e.g., DeepSphere or DISCO), Spherical Fourier Neural Operators (SFNOs), and geodesic attention. Here we propose Dandelion, a spherical version of Flower, a warp-based neural PDE solver. Layers of Dandelion predict a tangent-plane displacement and transport features along great circles. We obtain a U-Net-like structure by implementing hierarchical pooling entirely in the spherical-harmonic domain. There are thus no convolutions: spatial mixing is achieved only through spherical coordinate changes, or warps. To compare Dandelion with existing spherical architectures, we release an evolving benchmark suite of challenging, natively-spherical PDE datasets including a modified Galewsky jet, anomalous chained turbulence, Cahn-Hilliard decomposition, spherical Riemann shocks, Held-Suarez dry atmospheric transport and global ocean dynamics. This new benchmark fills the gap in existing spherical datasets which are either too small and stylized, or much too large (ERA5) for model iteration. Dandelion is best or second-best on every dataset, and the gap to non-warp baselines widens with resolution: at $256\times 512$, Dandelion and Flower2D occupy the top two slots in both single-step prediction and rollout.


## 精读解读（中文）
### 一、研究动机
许多行星尺度动力学过程本质发生在球面上，但主流科学机器学习架构默认面向欧氏网格：在规则经纬网格上应用笛卡尔卷积会导致高纬畸变，二维FFT错误假设双周期性，ViT的笛卡尔位置编码扭曲球面测地距离。现有球面数据集又处于两个极端：要么太小且风格化，要么如ERA5过大而难以迭代，因此需要原生球面架构和中等规模球面PDE基准。

### 二、技术方案（Method）
Dandelion是warp式神经PDE求解器Flower的球面版本。输入为球面经纬网格上的多变量物理场，经球谐变换构建U-Net式多尺度结构；每一层是一个多头可学习的warp，在切空间预测逐像素位移，并将特征沿球面大圆（测地线）传输到新位置；下采样/池化完全在球谐域通过谱截断实现，不使用任何卷积，空间混合仅由球面坐标变换完成。训练采用监督学习，评估包括单步预测和自回归滚动预测。

### 三、结果（Result）
在包含6个新数据集加planetswe共7个球面PDE数据集上，Dandelion全部取得最好或第二好的性能；与SFNO、FNO、球面/平面Transformer及2D Flower等基线相比优势稳定，且随分辨率提高而扩大。在256×512分辨率下，Dandelion与Flower2D在单步预测和滚动预测中占据前两名。

### 四、结论（Conclusion）
Dandelion验证了无卷积的球面warp机制能够有效建模球面PDE，通过切空间位移与大圆传输保持几何一致性，结合球谐域层级池化兼顾表达力与计算效率；同时本文发布的中等规模球面基准填补了玩具问题与ERA5级业务数据之间的空白，适合快速迭代和系统比较球面架构。

### 五、方法论与关键技术细节
关键细节包括：位移定义在切空间并沿大圆插值，天然适合球面几何；池化完全在球谐域进行，避免了经纬网格高纬畸变；没有卷积、FFT或笛卡尔位置编码，空间混合只依赖warp坐标变换；计算复杂度关于网格尺寸线性。数据方面新增六个数据集：修改的Galewsky急流、异常链式湍流、Cahn-Hilliard相分离、球面Riemann激波、Held-Suarez干大气传输和全球海洋动力过程，加上The Well的planetswe，覆盖多种物理机制并扫描物理参数与随机种子。当前验证主要在中高分辨率（如256×512）及中等规模数据上，更高分辨率或业务级数据下的表现留待后续工作。
