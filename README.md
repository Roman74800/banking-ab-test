# Banking Onboarding A/B Test

**Portfolio project | Synthetic randomized experiment | Python + SQL**

## Business question
Does a simplified onboarding flow improve completion conversion compared with the current flow?

## Hypothesis
H0: conversion rates are equal. H1: conversion rates differ (two-sided).

## Design
12,000 simulated users randomly allocated to control and treatment. The generator sets a **+2 percentage point treatment effect** and channel-dependent baseline rates. One observation per randomized user.

## Metrics
- **Primary**: onboarding completion rate = completed users / randomized users.
- **Secondary**: revenue per randomized user (ARPU), simulated in RUB.
- **Guardrails to add with real data**: error rate, fraud rate, support tickets, latency.

## Statistical approach
Two-sided pooled two-proportion z-test, alpha=0.05; 95% unpooled Wald confidence interval for absolute rate difference. The notebook reports absolute and relative uplift and avoids treating statistical significance as a business decision by itself.

## Quick start
```bash
pip install -r requirements.txt
python generate_data.py
jupyter notebook notebooks/analysis.ipynb
```
CSV included. Notebook works from the repository root or `notebooks/`.

## Caveats
Synthetic data, **not a real T-Bank experiment**. The effect is built into the simulation; this does not prove a real product improvement. In practice, pre-register sample size and duration, monitor sample-ratio mismatch, check guardrails, and account for multiple testing when evaluating many metrics.
