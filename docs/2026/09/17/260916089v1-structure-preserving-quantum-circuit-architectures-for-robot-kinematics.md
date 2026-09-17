# Structure-Preserving Quantum Circuit Architectures for Robot Kinematics

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Andrea Morghen, Pierluigi Arpenti, Roberto Schiattarella, Giovanni Acampora, Bruno Siciliano
- 机构：University of Naples Federico II
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16089v1) · [PDF](https://arxiv.org/pdf/2609.16089v1)

## TLDR
This paper presents structure-preserving quantum circuit architectures that encode Denavit–Hartenberg robot kinematics by separating classical metric magnitudes from qubit-encoded directions and using selector-based readout to reconstruct end-effector position and orientation, with validation under simulation, noise, and real hardware without claiming quantum advantage.

## Abstract
Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite-depth hardware. This work introduces a quantum representation and circuit architecture for rigid-body transformations and specializes it to Denavit--Hartenberg kinematics of serial open-chain manipulators. Each translational contribution is factorized into a classical metric magnitude and a signed unit direction encoded by a single-qubit Bloch vector, while parameterized rotations reproduce the ordered propagation of frame directions. A selector register prepares probabilities proportional to the contribution magnitudes, and the reduced state of a designated readout qubit encodes their normalized weighted sum. The retained classical scale then reconstructs the metric end-effector position. Two additional readout qubits encode terminal-frame axes, providing a compact and geometrically interpretable pose interface. At the ideal expectation-value level, measured Pauli observables reproduce the corresponding classical kinematic quantities. Alternative circuit architectures realize the same representation with different tradeoffs in qubit count, circuit depth, controlled operations, and measurement requirements. Validation on a serial manipulator yields numerically negligible position and orientation reconstruction errors under ideal simulation. Finite-shot simulations, noisy executions, transpilation analysis, and a hardware demonstration further characterize statistical error, noise sensitivity, and implementation overhead without asserting computational advantage.
