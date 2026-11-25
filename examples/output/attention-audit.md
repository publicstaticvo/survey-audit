# Attention Is All You Need

NeurIPS 2017 proceedings · https://papers.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf

**Scope (partial)** Check the reported EN–DE BLEU gain against Table 2 and the positional-encoding wavelength description against the formula. Assess comparator coverage only within the manuscript.

**Literature cutoff** Unspecified

**Conclusion** The stated EN–DE margin holds among listed comparators. Correcting the wavelength endpoint is a local repair. Literature-wide priority and score reproduction remain open.

**Reasoning and confidence (moderate)** Calculate the gain within the reported comparison, then inspect whether its benchmark and baseline boundaries support the broader claim. Separately derive the realized wavelength range from the architecture specification.

**Limitations** This audit uses the proceedings PDF and does not recompute BLEU or verify completeness of contemporaneous literature.

**Suggested next steps** Obtain archived outputs and BLEU settings for score reproduction. Resolve comparator versions and review contemporaneous WMT results for a priority check.

## Research questions, claims and contributions

- Can an attention-based architecture attain competitive machine translation quality?
- **CL1** Transformer big reports 28.4 BLEU on WMT 2014 EN–DE. Evidence E1, E2. Dependencies None recorded.
- **CL2** The EN–DE score is more than 2 BLEU above the best previously reported result, including ensembles. Evidence E1, E2. Dependencies CL1.
- **CL3** The sinusoidal wavelength range reaches 10000 × 2π. Evidence E3, E4. Dependencies None recorded.
- **CO1** An attention-based architecture with competitive machine translation results and a specified positional encoding. Claims CL1, CL2, CL3. Evidence E1, E3.

## Verified findings

### F1 · Strength

The table substantiates the reported gain against the strongest listed EN–DE comparator.

The reported 28.4 exceeds the strongest listed comparator's 26.36 by 2.04 BLEU.

**Evidence** E1, E2 · **Claims** CL1, CL2 · **Confidence** high

**Limitations** Arithmetic uses the displayed precision.

### F2 · Weakness

The exact wavelength endpoint in the prose is larger than the maximum realized by the stated formula at the reported model dimensions.

For paired coordinates, the highest pair is i = d_model / 2 − 1. Its wavelength is 2π × 10000^(1 − 2/d_model), strictly below 2π × 10000.

**Evidence** E3, E4, E5 · **Claims** CL3 · **Confidence** high

**Underlying failures** Conceptual / Theoretical Failure

**Legacy Categories** C1

**Presentation** True

**Limitations** The finding concerns the literal endpoint under the stated formula.

**Suggested next steps** State the exact endpoint or mark the bound as approximate.


## Evidence-supported findings requiring confirmation

### F3 · Weakness

The comparison may leave baseline coverage insufficient for the literature-wide priority claim.

The abstract's comparator set is broad and Table 2 enumerates specific systems. The accompanying text provides no selection criterion for the set. Its completeness within contemporaneous literature remains uncertain.

**Evidence** E1, E2, E6 · **Claims** CL2 · **Confidence** low

**Underlying failures** Scope / Generalization Failure

**Limitations** No omitted eligible system was identified in this manuscript-only audit.

**Suggested next steps** Compare Table 2 to contemporaneous WMT leaderboards and inspect differing BLEU conventions.


## Unresolved questions

### F4 · Question

Can the reported test score be reproduced from the original system outputs?

Table 2 reports the score. Reproducing it would require archived translations, test references and matching evaluation settings.

**Evidence** E2 · **Claims** CL1 · **Confidence** undetermined

**Limitations** The required run artifacts were outside the materials inspected.

**Suggested next steps** Locate the original outputs and the evaluation command.


## Non-applicable findings

None recorded.

## Audit obligations

- **Reference Integrity · Not Applicable** (outside_scope) The request excludes bibliographic identity and version checks.
- **Citation Support · Not Applicable** (outside_scope) The request limits comparator inspection to the reported table.
- **Central Claim Verification · Unresolved** (applicable) Reported figures can be checked. Independent score reproduction remains open.
  - CL1, reported value · Verified. Table 2 reports the stated score. Evidence E2.
  - CL1, evaluation reproduction · Unresolved. No evaluation artifacts were inspected. Evidence E2.
- **Method Evidence Alignment · Verified** (applicable) The displayed comparison supports the within-table numerical claim.
  - CL2, gain within Table 2 · Verified. The difference is 2.04 BLEU for the strongest displayed comparator. Evidence E1, E2.
- **Internal Consistency · Contradicted** (applicable) The prose endpoint conflicts with the finite-dimensional formula.
  - CL3, exact prose endpoint versus formula · Contradicted. The maximal exponent is smaller than one. Evidence E3, E4, E5.
- **Counterevidence Awareness · Unresolved** (applicable) The strongest listed comparator was examined. External candidates were outside the requested inspection.
  - CL2, possible contrary results beyond Table 2 · Unresolved. The strongest listed baseline does not rule out an omitted stronger baseline. Evidence E2.
- **Scope Verification · Unresolved** (applicable) The within-table result is established and the wider comparator scope is open.
  - CL2, previously reported comparator coverage · Unresolved. The table establishes the comparison over its displayed rows. Evidence E1, E2.
- **Uncertainty Reporting · Verified** (applicable) Residual comparison and reproducibility limits are linked to the affected claims.
  - CL1 and CL2 uncertainty · Verified. F3 and F4 state limitations and what would resolve them. Evidence E1, E2.

## Quality assessment

- **Scholarly Value** The reported benchmark gain adds value to the architectural proposal within the checked comparison. Findings F1, F3. **Uncertainty** The wider priority claim remains open.
- **Epistemic Credibility** The table supports the stated magnitude within the displayed comparison. The endpoint wording needs correction. Findings F1, F2. **Uncertainty** Independent BLEU verification is outside the available evidence.
- **Verifiability** Table entries and equations make the arithmetic and wavelength derivation inspectable. Findings F1, F2, F4. **Uncertainty** End-to-end score reproduction remains unresolved.

### Impact of F1 · Noncritical

Supports the benchmark component of the architecture contribution. Claims CL1, CL2. Contributions CO1.

**Repair** None for the within-table arithmetic.

**Compensation** Independent of the wavelength description. Related strengths None recorded.

### Impact of F2 · Noncritical

Changes the exact stated range, with no demonstrated effect on benchmark scores. Claims CL3. Contributions CO1.

**Repair** Correct or qualify the endpoint in §3.5.

**Compensation** The exact claim relies on the formula and finite dimension. Related strengths None recorded.

### Impact of F3 · Noncritical

The wider historical priority claim depends on eligible comparator coverage. Claims CL2. Contributions CO1.

**Repair** Verify comparator coverage or narrow the claim to the evaluated set.

**Compensation** F1 preserves the narrower within-table result. Wider priority requires additional evidence. Related strengths F1.

## Investigation trace

1. **paper-understanding** Identified the numerical benchmark claim and the wavelength statement as independently checkable. Evidence E1, E3.
1. **scientific-verification** Compared the table values. The wording for the wavelength endpoint prompted a derivation from the finite coordinate index. Evidence E2, E3, E4, E5.
1. **critical-reasoning** The table establishes the numerical margin. The abstract's broader comparator wording prompted a scope check and a record of the uninspected literature. Evidence E1, E2.
1. **quality-synthesis** Traced the endpoint issue to the architectural description and the coverage issue to the priority claim. Evidence E2, E5.

## Evidence

### E1 · Passage

Attention Is All You Need · NeurIPS 2017 proceedings · Abstract, PDF page 1

including ensembles, by over 2 BLEU

**Role** Anchors the scope and magnitude of the comparison.

### E2 · Artifact

Attention Is All You Need · NeurIPS 2017 proceedings · Table 2, PDF page 8, EN–DE column

Transformer (big) 28.4 and ConvS2S Ensemble 26.36, the highest displayed non-Transformer EN–DE score.

**Role** Provides the reported score and strongest listed comparison.

### E3 · Passage

Attention Is All You Need · NeurIPS 2017 proceedings · §3.5, PDF page 6

The wavelengths form a geometric progression from 2π to 10000 · 2π.

**Role** States the endpoint examined.

### E4 · Artifact

Attention Is All You Need · NeurIPS 2017 proceedings · §3.5 formulas and Table 3 model dimensions, PDF pages 6 and 9

The sinusoid argument divides position by 10000^(2i/d_model). Table 3 reports d_model = 512 for base and 1024 for big.

**Role** Establishes the formula and finite coordinate ranges.

### E5 · Artifact

Audit derivation using E4 · v0.1 example · Largest paired coordinate 2i = d_model − 2

2i/d_model = 1 − 2/d_model, hence the largest period is 2π × 10000^(1 − 2/d_model).

**Role** Shows the bound is strictly below the prose endpoint.

### E6 · Bounded Absence

Attention Is All You Need · NeurIPS 2017 proceedings · Table 2 and §6.1, PDF page 8

Table 2 names comparators and §6.1 summarizes their results. Neither passage states a procedure for identifying all eligible previously reported WMT 2014 EN–DE systems.

**Role** Bounds the uncertainty about comparator completeness to the inspected reporting.

**Criterion** Explicit rules or a source for identifying the set of eligible prior comparators.

**Coverage** Table 2 caption, table entries and the machine translation results in §6.1.
