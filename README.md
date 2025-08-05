# Heart-Disease-Risk-Prediction-Using-Patient-Records

Cardiovascular disease (CVD) remains the top contributor of death globally, highlighting the urgent need for precise, data-driven risk prediction systems. This research aims to implement AI methods to estimate the possibility of heart diseases using the structured clinical dataset Heart.csv, which includes information of the patients namely age_group, gender, lipid profile, pressure of blood flow, and electrocardiographic findings.
I developed and evaluated multiple predictive systems, including Random_Forest, Naïve-Bayes, & ensemble techniques, specifically XGBoost. These models were tuned to categorize patient risk levels and identify patterns associated with cardiovascular events. The random_forest achieves the highest precision and robustness across validation sets.
To ensure clinical relevance and trust, we incorporated model explainability tools such as LIME values and feature importance analysis, which consistently highlighted features like ST_segment, MaxHR, Oldpeak, and resting ECG results as top contributors to predictions.
Additionally, a user-centric web interface was created to allow medical practitioners to add individual-specific data and obtain real-time, individualized risk assessments. This approach demonstrates the potential of intelligent health systems to support proactive cardiovascular support and facilitate timely clinical interventions.


Dataset Overview:
The Heart Failure Prediction dataset is commonly utilized in clinical data science to assess the chances of Heart_Disease by examining a mix of demographic and physiological characteristics. In this project, we utilize a polished version called heart.csv, containing 918 patient entries with pertinent medical characteristics. The dataset originates from Kaggle and has been processed and normalized for application in machine learning classification projects. Our goal is to utilize artificial intelligence methods to help in the initial diagnosis of cardiovascular diseases, enabling healthcare practitioners to identify at-risk patients through organized data. The dataset contains categorical and numerical variables, including age, gender, lipid level, type of chest-pain, & ECG outcomes—vital factors in clinical decision-making.
This real-world data-set was constructed by combining 5 previously independent Heart_Disease data samples that had not been merged before. The resulting dataset integrates 11 common features across all sources, which makes the biggest dataset exist at present for research purposes. These 5 data samples curated for this compilation are:

Location	Number of Records
Cleveland	303
Hungary	294
Switzerland	123
Long Beach VA	200
Stalog (Heart) Data Set	270

 
Overall: 1190 records
Duplicated: 272 records
Result: 918 records 
 



