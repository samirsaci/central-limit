## Central Limit Theorem for Process Improvement with Python 📊
*Estimate the workload for returns management assuming a normal distribution of the number of items per carton received from your stores.*


<p align="center">
  <img align="center" src="https://miro.medium.com/max/1280/1*U4P-XerPaGmh2aFyIWpC2w.png">
</p>

Lean Six Sigma (LSS) is a method based on a stepwise approach to process improvements.This approach usually follows 5 steps 
(Define, Measure, Analyze, Improve and Control) for improving existing process problems with unknown causes.

### Article
In this [Article](https://medium.com/towards-data-science/central-limit-theorem-for-process-improvement-with-python-483126e33b07),we will see how the Central 
Limit Theorem can help us to estimate the workload for the process of returns management using a normal distribution based on the mean and the standard deviation 
of historical records.

### Scenario
You are the Inbound Manager of a multinational clothing retail company known for its fast-fashion clothing for men, women, teenagers, and children.
A major problem for you is the lack of visibility of your workload for the returns process. 
Indeed, because of system limitations, you do not get advance shipping notice (ASN) before receiving returns from your stores.

<p align="center">
  <img align="center" src="https://miro.medium.com/max/700/1*S7tZjimTljNyyaFLfurn2g.png">
</p>

For each item (shirt, dress …) your operators need to perform:
1. Quality check to ensure that the product can be restocked
2. Relabelling
3. Re-packing

You know the productivity per item and you would like to estimate the workload in hours based on the number of cases you will receive in the week.
Based on the historical data of the last 24 months, you have:
- An average of 23 items per carton
- A standard deviation of 7 items
Your team is usually sized to handle a maximum of 30 items per case. You need to hire temporary workers to meet your daily capacity target if it goes beyond this threshold.

### Question
Can you estimate the probability to have less than 30 items per carton that you will receive every week?

## Code
This repository code you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain Engineer with an international experience working on Logistics and Transportation operations. \
Have a look at my portfolio: [Data Science for Supply Chain Portfolio](https://samirsaci.com) \
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://www.logi-green.com/) \
Data Science for Warehousing📦, Transportation 🚚 and Demand Forecasting 📈 
