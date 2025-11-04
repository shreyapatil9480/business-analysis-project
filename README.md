# Project Performance Analysis

This repository contains a synthetic dataset and analysis notebook intended for practicing data analytics and project management skills. It simulates tasks that a **Business Analyst**, **Program Manager**, or **Data Analyst** might perform when evaluating project outcomes.

## Dataset

The dataset (`project_data.csv`) includes 200 synthetic projects with the following fields:

| Column | Description |
|-------|-------------|
| `project_id` | Unique identifier for each project |
| `project_name` | Name of the project |
| `start_date` | Project start date (YYYY‑MM‑DD) |
| `end_date` | Project end date (YYYY‑MM‑DD) |
| `budget` | Allocated budget for the project in USD |
| `actual_spend` | Actual amount spent on the project in USD |
| `team_size` | Number of team members |
| `risk_score` | Risk score between 0 and 1 |
| `status` | Current status of the project (`Completed`, `On Track`, `Delayed`, `Cancelled`, `At Risk`) |
| `success` | Binary indicator (1 if the project was successful, 0 otherwise) |

A project is considered successful if it finishes within budget, within a reasonable duration, and with a low risk score.

## Notebook

The Jupyter notebook (`analysis.ipynb`) performs the following:

1. **Exploratory Data Analysis (EDA)**:
   - Loads the dataset and displays summary statistics.
   - Visualizes the distribution of project statuses.
   - Creates a scatter plot of budget versus actual spend, highlighting successful projects.
   - Generates a correlation heatmap of numeric features.

2. **Predictive Modeling**:
   - Derives project duration from start and end dates.
   - Splits the data into training and testing sets.
   - Standardizes numeric features.
   - Trains a logistic regression model to predict project success.
   - Evaluates model performance using classification metrics and an ROC curve.

You can run the notebook interactively in Jupyter to explore the data and extend the analysis. The synthetic nature of the data means that no sensitive or proprietary information is used.

## Usage

1. **Clone the repository** (once it is public on GitHub).
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Install dependencies** (ideally in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook analysis.ipynb
   ```
   Follow the prompts to run the cells and explore the analysis.

## Requirements

The `requirements.txt` file lists the Python packages needed to run the notebook. Major dependencies include:

- pandas
- numpy
- matplotlib
- seaborn
- scikit‑learn
- jupyter

## Contributions

Feel free to fork this repository and build upon the synthetic dataset or analysis. You could experiment with different predictive models, add more visualization techniques, or expand the dataset with additional features.

## License

This project is provided under the MIT License. You are free to use, modify, and distribute the contents of this repository for educational and professional purposes.
