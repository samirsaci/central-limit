## Central Limit Theorem for Process Improvement with Python 📊
*Estimate the workload for returns management, assuming a normal distribution of the number of items per carton received from your stores.*

<p align="center">
  <a href="https://www.samirsaci.com/central-limit-theorem-for-process-improvement-with-python/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/1280/1*U4P-XerPaGmh2aFyIWpC2w.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

Lean Six Sigma (LSS) is a step-by-step approach to process improvement. 

This approach typically follows five steps (Define, Measure, Analyse, Improve, and Control) to address existing process problems with unknown causes.

### Article
In this [Article](https://www.samirsaci.com/central-limit-theorem-for-process-improvement-with-python/), we will see how the Central Limit Theorem can help us estimate the workload for the process of returns management using a normal distribution based on the mean and the standard deviation of historical records.

### Scenario
You are the Inbound Manager of a multinational clothing retail company known for its fast-fashion clothing for men, women, teenagers, and children.

A significant problem for you is the lack of visibility of your workload for the returns process. 

Indeed, due to system limitations, you do not receive an advance shipping notice (ASN) before receiving returns from your stores.

<p align="center">
  <a href="https://www.samirsaci.com/central-limit-theorem-for-process-improvement-with-python/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/700/1*S7tZjimTljNyyaFLfurn2g.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

For each item (shirt, dress …), your operators need to perform:
1. Quality check to ensure that the product can be restocked
2. Relabelling
3. Re-packing

You know the productivity per item, and you would like to estimate the workload in hours based on the number of cases you will receive in the week.

Based on the historical data of the last 24 months, you have:
- An average of 23 items per carton
- A standard deviation of 7 items
- 
Your team is typically sized to handle up to 30 items per case. You need to hire temporary workers to meet your daily capacity target if it goes beyond this threshold.

### Question
Can you estimate the probability of receiving fewer than 30 items per carton each week?

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Central Limit Theorem.ipynb` - Jupyter notebook with step-by-step analysis
- `central_limit_theorem.py` - Standalone Python script

### Getting Started
```bash
pip install -r requirements.txt
python central_limit_theorem.py
```

### Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels


## Go further

- **The full write-up, with the reasoning behind the code:** [Central Limit Theorem for Process Improvement with Python](https://www.samirsaci.com/central-limit-theorem-for-process-improvement-with-python/?utm_source=github&utm_medium=readme&utm_campaign=central-limit)
- **Test what you learned:** the [Supply Science App](https://supply-science.com/?utm_source=github&utm_medium=readme&utm_campaign=central-limit) has lessons on lean six sigma and the statistics quizzes, free and in the browser.
- **100+ case studies with their source code:** [samirsaci.com](https://www.samirsaci.com/?utm_source=github&utm_medium=readme&utm_campaign=central-limit)

## About me

Samir Saci, supply chain engineer and data scientist with ten years in operations across Asia and Europe. Founder of [LogiGreen](https://www.logi-green.com/), creator of [Supply Science](https://www.youtube.com/@SupplyScience).
For consulting on analytics and sustainable supply chain transformation: [LogiGreen](https://www.logi-green.com/). More about me: [samirsaci.com/about](https://www.samirsaci.com/about/) · [LinkedIn](https://www.linkedin.com/in/samir-saci/)

