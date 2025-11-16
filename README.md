# Business Analysis Project

What predicts satisfied enterprise clients?

**Stakeholder:** Account Director

## Key Insights

- Response times over 24 hours reduce satisfaction by 19 points NPS.
- More than 2 escalations per quarter predicts dissatisfaction.
- Clients with NPS above 40 rarely escalate support issues.

## Dataset

Primary file: `data/client_satisfaction.csv`  
Target variable: `satisfied`

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## CLI Usage

```bash
python src/train.py
python src/predict.py --input data/sample_input.csv
```
## Tests

```bash
pytest tests/
```
