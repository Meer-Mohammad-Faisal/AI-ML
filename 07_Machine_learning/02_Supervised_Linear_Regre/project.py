# %% [markdown]
# # Insurance Charge Prediction

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# %% [markdown]
# # EDA

# %%
# reading data
df = pd.read_csv('insurance.csv')
df

# %%
# shape of data
df.shape

# %%
# so there are 7 column. and we have to predict last wala charges.
# information about data
df.info()

# %%
# describing the data(only numeric)
df.describe()

# %%
# is there any null values:
df.isnull().sum()
# we don't have any null values

# %%
df.columns

# %%
# distribution plot for numeric-> 'age', 'bmi', 'children', 'charges'
numeric_columns = ['age', 'bmi', 'children', 'charges']
for col in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde = True, bins = 20)

# %%
 
# count plot for children
sns.countplot(x = df['children'])

# %%
# for genders
sns.countplot(x = df['sex'])

# %%
# for smokers
sns.countplot(x = df['smoker'])

# %%

for col in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.boxenplot(x = df[col])

# %%
# now see some relation between data
# corelation -> only for numeric data
plt.Figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)

# %% [markdown]
# # Data cleaning and Preprocessing

# %%
# in this pdf, all the data is cleaned, so no need to clean data for this insurance file.
df_cleaned = df.copy()
df_cleaned.head()
# we copied our data into df_cleaned for the operation like
# first give it null or missing value than handle it

# %%
df_cleaned.shape

# %%
df_cleaned.drop_duplicates(inplace=True)

# %%
df_cleaned.shape

# %%
df_cleaned.isnull().sum()

# %%
df_cleaned.dtypes

# %%
# so we are making all the object(non-numeric) into numeric

# %%
df_cleaned['sex'].value_counts()

# %%
df_cleaned.dtypes

# %%
# so here are sex, smoker and region are object we are converting into 0's and 1's (numeric)


# %% [markdown]
# # label encoding

# %%
df_cleaned['sex'] = df_cleaned['sex'].map({"male" : 0, "female" : 1})

# %%
df_cleaned.head()

# %%
# doing same for smoker
df_cleaned['smoker'].value_counts()

# %%
df_cleaned['smoker'] = df_cleaned['smoker'].map({"no" : 0, "yes" : 1})

# %%
df_cleaned

# %%
# renaming sex-> isFemale, smoker-> isSmoker
df_cleaned.rename(columns={
    'sex': 'is_female',
    'smoker': 'is_smoker'
}, inplace=True)

# %%
df_cleaned.head()

# %%
# now encoding region
df['region'].value_counts()

# %% [markdown]
# # one hot encoding on region

# %%
# one hot coding on
df_cleaned = pd.get_dummies(df_cleaned,columns = ['region'], drop_first=True)

# %%
df_cleaned.head()

# %%
df_cleaned = df_cleaned.astype(int)
df_cleaned

# %% [markdown]
# # Feature Engineering and Extraction

# %%
sns.histplot(df['bmi'])

# %%
# categories bmi into diffrent diffrent classes...
df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[0, 18.5, 24.5, 29.9, float('inf')],
    labels=['UnderWeight', 'Normal', 'OverWeight', 'Obse']
)

# %%
df_cleaned

# %%
# so, now into bmi categories there are string, 
# so we have to change it into numeric
# so we are using one hot encoding.
df_cleaned = pd.get_dummies(df_cleaned, columns = ['bmi_category'], drop_first=True)

# %%
df_cleaned

# %%
df_cleaned = df_cleaned.astype(int)

# %%
df_cleaned

# %% [markdown]
# Feature scaling

# %%
df_cleaned.columns

# %%
# standerd scalling of age and bmi and children -> standerd deviation (-3 to +3)
from sklearn.preprocessing import StandardScaler
cols = ['age', 'bmi', 'children']
scaler = StandardScaler()

df_cleaned[cols] = scaler.fit_transform(df_cleaned[cols])

# %%
df_cleaned.head()

# %% [markdown]
# #  Feature Extraction

# %%
from scipy.stats import pearsonr
# Pearson Correlation Claculation

# list of features to check against target
selected_features = [
    'age', 'bmi', 'children', 'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Normal', 'bmi_category_OverWeight', 'bmi_category_Obse'
]

correlations = {
    feature: pearsonr(df_cleaned[feature], df_cleaned['charges'])[0]
    for feature in selected_features
}

correlations_df = pd.DataFrame(list(correlations.items()), columns=['Feature', 'Pearson Correlation'])
correlations_df.sort_values(by='Pearson Correlation', ascending=False)


# %%
cat_features = [
    'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Normal', 'bmi_category_OverWeight', 'bmi_category_Obse'
]

# %%
from scipy.stats import chi2_contingency
import pandas as pd

alpha = 0.05

df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False)  # corrected column name
chi2_result = {}

for col in cat_features:
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_result[col] = {
        'chi2_statistics': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }

chi2_df = pd.DataFrame(chi2_result).T 
chi2_df = chi2_df.sort_values(by='p_value')
chi2_df

# %%
# final data frame:
final_df = df_cleaned[['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges', 'region_southeast', 'bmi_category_Obse']]


# %%
final_df

# %% [markdown]
# # Machine Learning Start-> Linear Regression

# %%
from sklearn.model_selection import train_test_split

# %%
X = final_df.drop('charges', axis=1)
y = final_df['charges']

# %%
# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# %%
from sklearn.linear_model import LinearRegression

# %%
model = LinearRegression()
model.fit(X_train, y_train)

# %% [markdown]
# # y test(prediction)

# %%
y_pred = model.predict(X_test)

# %%
y_pred

# %%
y_test

# %%
# now comparing models
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)

# %%
# accuracy->
r2

# %%
# adjusted R2

# %%
n = X_test.shape[0] # no of row
p = X_test.shape[1] # no of col

adjusted_r2 = 1 - ((1- r2) * (n - 1) / (n - p - 1))
adjusted_r2

# %%



