## IDENTIFICATION OF COVID-19 SEVERITY AND ASSOCIATED GENE-MARKERS BASED ON SCRNA-SEQ DATA
Bio-marker identification for COVID-19 remains a vital research area to improve current and future pandemic responses. Innovative artificial intelligence and machine learning-based systems may leverage the large quantity and complexity of single cell sequencing data to quickly identify disease with high sensitivity. In this study, we developed a novel approach to classify patient COVID-19 infection severity using single-cell sequencing data derived from patient BronchoAlveolar Lavage Fluid (BALF) samples. We also identified key genetic biomarkers associated with COVID-19 infection severity. Feature importance scores from high performing COVID-19 classifiers were used to identify a set of novel genetic biomarkers that are predictive of COVID-19 infection severity. Treatment development and pandemic reaction may be greatly improved using our novel big-data approach. Our implementation is available on https://github.com/aekanshgoel/COVID-19_scRNAseq.

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
