[![Python CI](https://github.com/shreyapatil9480/business-analysis-project/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shreyapatil9480/business-analysis-project/actions/workflows/python-ci.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC)

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


## Testing

```bash
pip install -r requirements.txt
pytest tests/ --cov=src
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

## Next Steps

Deploy Streamlit dashboard for business self-service.

---
*Analytics portfolio project — 2025-11*

<!-- build 7 -->
