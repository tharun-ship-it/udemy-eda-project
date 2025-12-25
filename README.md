<p align="center">
  <img src="https://img.icons8.com/fluency/96/combo-chart.png" alt="Udemy EDA Logo" width="100"/>
</p>

<h1 align="center">📊 Udemy Courses: Exploratory Data Analysis</h1>

<p align="center">
  <strong>An in-depth analysis of Udemy's online course catalog uncovering pricing strategies, subscriber patterns, and market trends</strong>
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-live-demo">Live Demo</a> •
  <a href="#-key-findings">Key Findings</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-results">Results</a> •
  <a href="#-methodology">Methodology</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge" alt="Seaborn"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-00D9A5?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Data-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle"/>
  <img src="https://img.shields.io/badge/Courses_Analyzed-3,682-E94560?style=for-the-badge" alt="Courses"/>
</p>

---

## 🎯 Overview

This project analyzes **3,682 courses** across four major subjects (Web Development, Business Finance, Graphic Design, Musical Instruments) to uncover insights about the dynamics of online education platforms. The analysis employs statistical methods and visualization techniques to identify factors associated with course popularity and learner engagement.

<p align="center">
  <img src="figures/banner.png" alt="Dashboard Preview" width="800"/>
</p>

---

## 🚀 Live Demo

Run this notebook instantly in your browser - no installation required!

<p align="center">
  <a href="https://colab.research.google.com/github/tharun-ship-it/udemy-eda-project/blob/main/notebooks/udemy_eda.ipynb">
    <img src="https://img.shields.io/badge/▶_OPEN_IN_COLAB-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Open In Colab" height="50"/>
  </a>
</p>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tharun-ship-it/udemy-eda-project/main?labpath=notebooks%2Fudemy_eda.ipynb)

---

## 📈 Key Findings

| Metric | Value |
|--------|-------|
| **Total Courses Analyzed** | 3,682 |
| **Total Subscribers** | 11.9M+ |
| **Median Course Price** | $50 |
| **Free Course Percentage** | ~8.4% |
| **Top Subject** | Web Development |

### 💡 Notable Insights

- Price shows **weak correlation** (ρ ≈ 0.05) with subscriber count
- Web Development courses capture **3.4x more subscribers per course** than Business Finance
- Course publication rates **increased 400%** between 2013-2016
- Free courses exhibit distinct engagement patterns despite representing only 8% of catalog

---

## 📁 Project Structure

```
udemy-eda-project/
├── data/
│   ├── udemy_courses.csv          # Raw dataset
│   └── README.md                  # Dataset documentation
├── notebooks/
│   └── udemy_eda.ipynb            # Main analysis notebook
├── figures/
│   ├── banner.png
│   ├── correlation_matrix.png
│   ├── subject_distribution.png
│   ├── price_vs_subscribers.png
│   ├── yearly_trend.png
│   └── ...
├── src/
│   ├── __init__.py
│   ├── utils.py                   # Helper functions
│   └── generate_figures.py        # Visualization script
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📊 Dataset

**Source:** [Kaggle - Udemy Courses](https://www.kaggle.com/andrewmvd/udemy-courses)

| Feature | Description | Type |
|---------|-------------|------|
| `course_id` | Unique identifier | int |
| `course_title` | Course name | str |
| `url` | Course URL | str |
| `is_paid` | Payment status | bool |
| `price` | Course price (USD) | float |
| `num_subscribers` | Subscriber count | int |
| `num_reviews` | Review count | int |
| `num_lectures` | Number of lectures | int |
| `level` | Difficulty level | str |
| `content_duration` | Course length (hours) | float |
| `published_timestamp` | Publication date | datetime |
| `subject` | Course category | str |

---

## 🔬 Methodology

### 1. Data Cleaning
- Missing value analysis and imputation
- Duplicate detection and removal
- Data type conversion and validation

### 2. Feature Engineering
- Temporal feature extraction (year, month, day of week)
- Engagement metrics computation (reviews per subscriber)
- Revenue estimation for paid courses

### 3. Analysis Dimensions
| Dimension | Description |
|-----------|-------------|
| **Univariate** | Distribution analysis of numerical and categorical features |
| **Bivariate** | Correlation analysis, cross-tabulations |
| **Temporal** | Publication trends, seasonal patterns |
| **Comparative** | Free vs. paid, subject-level comparisons |

---

## 📸 Results

### Subject Distribution

<p align="center">
  <img src="figures/subject_distribution.png" alt="Subject Distribution" width="700"/>
</p>

Web Development and Business Finance dominate the platform with nearly equal course counts, but Web Development generates significantly higher subscriber engagement.

### Price-Subscriber Relationship

<p align="center">
  <img src="figures/price_vs_subscribers.png" alt="Price vs Subscribers Analysis" width="700"/>
</p>

The weak correlation between price and subscribers suggests that course quality signals (reviews, instructor reputation) outweigh price sensitivity in purchase decisions.

### Temporal Growth

<p align="center">
  <img src="figures/yearly_trend.png" alt="Yearly Trends" width="700"/>
</p>

Platform growth accelerated significantly post-2013, coinciding with mobile app launches and Series C funding.

### Correlation Matrix

<p align="center">
  <img src="figures/correlation_matrix.png" alt="Correlation Matrix" width="600"/>
</p>

### Free vs Paid Courses

<p align="center">
  <img src="figures/free_vs_paid.png" alt="Free vs Paid Comparison" width="700"/>
</p>

---

## 📦 Installation

### Prerequisites

```bash
Python >= 3.8
pip >= 21.0
```

### Quick Start

```bash
# Clone the repository
git clone https://github.com/tharun-ship-it/udemy-eda-project.git
cd udemy-eda-project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

```bash
# Launch Jupyter Notebook
jupyter notebook notebooks/udemy_eda.ipynb
```

Or run directly:

```bash
cd notebooks
jupyter nbconvert --execute --to notebook udemy_eda.ipynb
```

---

## 🛠 Technologies

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core analysis |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computing |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat) | Visualizations |
| ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat) | Statistical plots |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) | Interactive notebook |

---

## 🛣 Future Work

- [ ] Sentiment analysis of course reviews
- [ ] Predictive modeling for subscriber count
- [ ] Time series forecasting for course publications
- [ ] NLP analysis of course titles and descriptions
- [ ] Integration with additional datasets (instructor info, ratings over time)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/udemy-eda-project.git

# Create branch
git checkout -b feature/amazing-feature

# Commit and push
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature

# Open Pull Request
```

---

## 📄 License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Dataset provided by [Larxel](https://www.kaggle.com/andrewmvd) on Kaggle
- Visualization inspiration from [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

---

## 👤 Author

**Tharun Ponnam**

* GitHub: [@tharun-ship-it](https://github.com/tharun-ship-it)
* Email: tharunponnam007@gmail.com

---

**⭐ If you find this project useful, please consider giving it a star!**

* [🔗 Live Demo](https://colab.research.google.com/github/tharun-ship-it/udemy-eda-project/blob/main/notebooks/udemy_eda.ipynb)
* [🐛 Report Bug](https://github.com/tharun-ship-it/udemy-eda-project/issues)
* [✨ Request Feature](https://github.com/tharun-ship-it/udemy-eda-project/pulls)
