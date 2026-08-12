# Thread Scaling of Hexaly on the TDVRPTW across Two Model Encodings. An Experimental Report: External-Function Serialization, Slice-Count Choice, and the Time-Sliced Thread Ladder

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Florian Rascoussier
- 机构：INSA Lyon, IMT Atlantique
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10079v1) · [PDF](https://arxiv.org/pdf/2608.10079v1)

## TLDR
A one-sentence TLDR: Thread scaling in Hexaly on the TDVRPTW is dominated by the model encoding, since external-function callbacks serialize evaluation regardless of thread count, while a sufficiently fine time-sliced native encoding uses extra threads to improve solution quality and reduce seed variation.

## Abstract
Thread scaling in Hexaly depends first on how the Time-Dependent Vehicle Routing Problem with Time Windows is modeled. We compare two Python encodings: one evaluates continuous travel-time functions through external callbacks, while the other approximates them with time slices evaluated natively by the solver. Independent CPU measurements show that the supported external-function interface uses a single evaluator worker regardless of the requested thread count. The native encoding, by contrast, makes effective use of the allocated cores. Across our selected benchmark panel, wider native searches produce better solutions both at the end of the run and throughout the search, while substantially reducing variation between seeds. Nearly every paired run improves from one to sixteen threads. The choice of encoding has an even larger impact than the thread count: native evaluation provides the strongest gains, at the cost of a travel-time approximation that must be sufficiently fine and independently checked. These descriptive results support multi-threading as a practical way to improve solution quality and stability when the model can exploit it, and show that the modeling approach is central to thread-scaling conclusions in time-dependent routing.
