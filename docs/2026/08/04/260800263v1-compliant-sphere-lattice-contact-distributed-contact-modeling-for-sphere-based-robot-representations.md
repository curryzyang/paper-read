# Compliant Sphere Lattice Contact: Distributed Contact Modeling for Sphere-Based Robot Representations

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Nataliya Nechyporenko, Ava Abderezaei, Alessandro Roncone
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00263v1) · [PDF](https://arxiv.org/pdf/2608.00263v1)

## TLDR
CSLC is a distributed contact model that uses a compliant lattice of surface spheres to generate spatially distributed contact patches, improving physical accuracy and grasp stability for sphere-based robot representations.

## Abstract
Contact planning in robotics requires models that are both computationally efficient and physically accurate. Sphere-based robot representations satisfy the first requirement by enabling fast collision checking and differentiable geometry, but sacrifice physical accuracy by relying on point contact which cannot capture contact patch area, pressure distributions, rotational stiffness, or frictional moments. We introduce Compliant Sphere Lattice Contact (CSLC), a distributed contact model that operates natively on sphere representations by modeling the robot interface as a compliant lattice of surface spheres connected through anchor and lateral springs. When pressed against an object, the lattice deforms to produce a spatially distributed contact patch that improves the physical accuracy of sphere-based contact. We validate CSLC across two independent solvers and show preliminary results demonstrating contact patch formation and improved grasp stability.
