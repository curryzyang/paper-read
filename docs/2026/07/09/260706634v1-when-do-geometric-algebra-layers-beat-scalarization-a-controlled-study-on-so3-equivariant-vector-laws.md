# When Do Geometric Algebra Layers Beat Scalarization? A Controlled Study on SO(3)-Equivariant Vector Laws

- 区域：速读区
- 排名：5
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Fabien Polly
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06634v1) · [PDF](https://arxiv.org/pdf/2607.06634v1)

## TLDR
Geometric algebra layers are not a general shortcut for low-data 3D learning but become useful precisely when the target involves deep compositions of group elements, as they significantly outperform scalarization on such tasks.

## Abstract
Compact networks built from Clifford algebra Cl(3,0) primitives are exactly SO(3)-equivariant and learn synthetic 3D vector laws from few samples. We ask whether the geometric algebra structure itself contributes anything beyond exact equivariance. We compare against a minimal scalarization baseline: invariant dot products fed to a small MLP that outputs coefficients on the equivariant basis {v_i, v_i x v_j}, which is also exactly equivariant. On single-stage laws (rotation by axis-angle, cross product, central force), scalarization matches or beats the Cl(3,0) network at a fraction of the training cost, so the geometric algebra adds nothing there. On compositional targets whose computation graph nests group operations (apply R2 R1 to a point; map a local force through an orientation, then take a torque), the Cl(3,0) network beats scalarization by an order of magnitude in the low-data regime, reaching with 100 samples what the baseline needs 3000 for, and the gap survives strengthening the baseline with the triple-product invariant and 17x more parameters, external Vector Neurons and e3nn baselines, and a multiplicative coefficient network. Ablations show the required network depth tracks the rotation chain length, and scalarization falls below the constant predictor on chains of four rotations. The advantage is not composition per se: on a rotation-free nested cross product, which flattens into polynomial invariant coefficients, scalarization wins by 24x. No tested model, equivariant or not, extrapolates invariant magnitudes: on radius and separation shifts every model is worse than a constant predictor once errors are normalized. We conclude that geometric algebra layers are not a general shortcut for low-data 3D learning, but become useful precisely when the target composes group elements in depth.
