# NomadBBO: A direct-search framework for constrained mixed-variable blackbox optimization in Python

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Edward Hallé-Hannan, Christophe Tribes
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19333v1) · [PDF](https://arxiv.org/pdf/2609.19333v1)

## TLDR
NomadBBO is a user-friendly Python library for inequality-constrained mixed-variable blackbox optimization that integrates a new CatADS direct-search method with Nomad’s efficient C++ backend via Cython, enabling theoretically grounded optimization over continuous, integer, binary, and categorical variables with surrogate and Bayesian hybrid strategies.

## Abstract
Mixed-variable blackbox optimization arises in simulation-based engineering and machine learning, where objective and constraint functions are expensive to evaluate and variables may be continuous, integer, binary, or categorical. Several software libraries are available for derivative-free optimization, but few combine ease of use, computational efficiency, flexibility, and theoretical convergence guarantees. This work presents NomadBBO, a user-friendly Python library for inequality-constrained mixed-variable blackbox optimization built around Nomad. Its core optimization framework is CatADS, a new direct-search method that extends Adaptive Direct Search (ADS) to mixed-variable problems. CatADS combines the mechanisms of ADS for quantitative variables with neighborhoods for handling categorical variables. These neighborhoods use Gaussian process-based or empirical Wasserstein distances derived from available data. Inequality constraints are handled through the progressive barrier. The mixed-variable and surrogate-based mechanisms are implemented in Python and connected to the efficient C++ backend of Nomad via Cython. This integration allows Nomad to handle categorical variables. It also enables the use of external libraries and hybrid optimization strategies, including Gaussian process models from SMT 2.0 and Bayesian optimization. Numerical experiments compare NomadBBO with other solvers on constrained and unconstrained mixed-variable problems from the Cat-Suite benchmark collection. The beta release is available at https://test.pypi.org/project/NomadBBO/
