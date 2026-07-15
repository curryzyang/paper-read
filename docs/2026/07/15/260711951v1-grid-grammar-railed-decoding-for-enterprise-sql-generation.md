# GRID: Grammar-Railed Decoding for Enterprise SQL Generation

- 区域：速读区
- 排名：10
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Mohsen Arjmandi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11951v1) · [PDF](https://arxiv.org/pdf/2607.11951v1)

## TLDR
GRID presents a grammar-constrained decoding engine that uses LALR(1) parser configurations and a byte-level trie to enforce syntactic validity, role/schema-based policies, provable guarantees, flat per-token cost, and a tamper-evident audit trail for enterprise SQL generation.

## Abstract
Large language models can write SQL, but enterprise deployment demands more than plausible text: outputs must be syntactically valid, must respect per-role and per-schema policy, must carry provable (not best-effort) guarantees, must not slow down as generations grow, and must leave a compliance-grade record of every decision. We present GRID (Grammar-Railed Decoding), a grammar-constrained decoding engine that keys exact next-token masks on parser configurations (lexer scan state x LALR(1) stack) rather than on token sequences, and uses the incrementally advanced LALR(1) parser itself as a viable-prefix oracle. LLM tokens are bridged to grammar terminals by a byte-level trie walk with a context-independent/context-dependent split that makes cache-key soundness hold by construction. Role-based access control is compiled into the language: role projections subset the grammar's productions and schema lexicons restrict identifier terminals, so forbidden verbs and identifiers are unreachable at mask level. Four guarantees (soundness, completeness, termination, and near-constant per-token cost) are stated with explicit preconditions and each paired with a test or benchmark. Rust kernels bring the per-token mask to a 3.6-6.7 us median, ahead of llguidance at p50 and p90 on two tokenizers with zero false rejects; per-token guard cost is position-flat at n=16,000. On Spider, constrained decoding is worth +13 execution-accuracy points at 0.5B, and one checker-guided repair pass over the provably mask-unenforceable residue (column-level policy) lifts a 7B model to 94.5% executable. A hash-chained per-token audit trail replays bit-identically with 100% tamper detection. We state plainly what the mask cannot do (distribution faithfulness, column-level RBAC, non-LALR(1) languages) and where measured cost remains.
