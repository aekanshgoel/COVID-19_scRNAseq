## IDENTIFICATION OF COVID-19 SEVERITY AND ASSOCIATED GENE-MARKERS BASED ON SCRNA-SEQ DATA
The outbreak of coronavirus disease (COVID-19) has spread rapidly to every corner of the world in a very complex way. A key research focus is in early-detection, development and transmission trend of COVID-19 through Artificial Intelligence and Machine Learning. An AI diagnostic system using Machine Learning models trained with single-cell RNA-seq data of bronchoalveolar lavage fluid (BALF) immune cells of COVID infected and non-infected patients is a new promising method that helps in early prediction and identification of COVID infected persons. This paper `Identification of COVID-19 Severity and Associated Gene-Markers based on single-cell RNA-seq data' acquaints a system for an automatic identification of COVID-19 from sc-RNA seq data, along with the 42 gene-markers related to COVID Severity. This can be extremely useful in future treatment development and combating the COVID-19 pandemic.

## Goal
To Detect and Classify COVID using, CatBoost and RandomForest; as an asset of Machine Learning.

## Dataset Information

The dataset contains gene-expression and week labels: COVID Severity (Severe, Mild and Normal) which contains 23,189 Cells and 1,999 Genes.

## Libraries

<li>sklearn
<li>catboost
<li>pandas
<li>matplotlib
<li>numpy
<li>seaborn
<li>collections

## Algorithms

<li>Gradient Boosting Classifier (CatBoost)
<li>Random Forest Classifier
<li>Support Vector Machine

## Prediction Metrics
![alt text](https://github.com/aekanshgoel/COVID-19_scRNAseq/blob/main/boxplot.png)
![alt text](https://github.com/aekanshgoel/COVID-19_scRNAseq/blob/main/cross-validation.png)

## Prediction Results
![alt text](https://github.com/aekanshgoel/COVID-19_scRNAseq/blob/main/confusion-mat.png)
![alt text](https://github.com/aekanshgoel/COVID-19_scRNAseq/blob/main/featureimp.png)
![alt text](https://github.com/aekanshgoel/COVID-19_scRNAseq/blob/main/shap.png)
