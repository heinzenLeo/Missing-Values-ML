```python
import pandas as pd
from sklearn.model_selection import train_test_split
```


```python
df = pd.read_csv('train.csv', index_col='Id')

df.dropna(subset=['SalePrice'], axis=0, inplace=True)
y = df.SalePrice

X = df.drop(['SalePrice'], axis=1)
```


```python
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
```

---


```python
df2 = pd.read_csv('melb_data.csv')
df2.dropna(subset=['Price'], axis=0, inplace=True)
y2 = df2.Price

X2 = df2.drop(['Price'], axis=1)
```


```python
X_train_1, X_valid_1, y_train_1, y_valid_1 = train_test_split(X2, y2, test_size=0.2, random_state=0)
```

# Until here:
- I imported pandas as train_test_split, from sklearn
- I loaded 2 different datasets:
- (melb_data: https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot?select=melb_data.csv) -- (train: in Categorical Variables, in Intermidiate ML from: https://www.kaggle.com)
- I set X, y and X2, y2, so that there is data and target variables from 2 different datasets

---

# Next:
- Simply import the function nan_columns and use it
- Enjoy it!


```python
from main import nan_columns
```

# Using the first dataset (train.csv):


```python
nan_columns(X_train, X_valid)
```

    |X_train| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      212
    Alley           1097
    MasVnrType       707
    MasVnrArea         6
    BsmtQual          28
    BsmtCond          28
    BsmtExposure      28
    BsmtFinType1      28
    BsmtFinType2      29
    Electrical         1
    FireplaceQu      551
    GarageType        58
    GarageYrBlt       58
    GarageFinish      58
    GarageQual        58
    GarageCond        58
    PoolQC          1164
    Fence            954
    MiscFeature     1119
    dtype: int64 
    
    Number of columns with missing values: 19 
     ------------------------------------------- 
    
    
    |X_valid| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      47
    Alley           272
    MasVnrType      165
    MasVnrArea        2
    BsmtQual          9
    BsmtCond          9
    BsmtExposure     10
    BsmtFinType1      9
    BsmtFinType2      9
    FireplaceQu     139
    GarageType       23
    GarageYrBlt      23
    GarageFinish     23
    GarageQual       23
    GarageCond       23
    PoolQC          289
    Fence           225
    MiscFeature     287
    dtype: int64 
    
    Number of columns with missing values: 18 
     ------------------------------------------- 
    
    Column: |Electrical| from X_train has missing values and it is NOT in X_valid 
    
    

## Or we could do so:


```python
nan_columns(X_valid, X_train)
```

    |X_valid| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      47
    Alley           272
    MasVnrType      165
    MasVnrArea        2
    BsmtQual          9
    BsmtCond          9
    BsmtExposure     10
    BsmtFinType1      9
    BsmtFinType2      9
    FireplaceQu     139
    GarageType       23
    GarageYrBlt      23
    GarageFinish     23
    GarageQual       23
    GarageCond       23
    PoolQC          289
    Fence           225
    MiscFeature     287
    dtype: int64 
    
    Number of columns with missing values: 18 
     ------------------------------------------- 
    
    
    |X_train| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      212
    Alley           1097
    MasVnrType       707
    MasVnrArea         6
    BsmtQual          28
    BsmtCond          28
    BsmtExposure      28
    BsmtFinType1      28
    BsmtFinType2      29
    Electrical         1
    FireplaceQu      551
    GarageType        58
    GarageYrBlt       58
    GarageFinish      58
    GarageQual        58
    GarageCond        58
    PoolQC          1164
    Fence            954
    MiscFeature     1119
    dtype: int64 
    
    Number of columns with missing values: 19 
     ------------------------------------------- 
    
    Column: |Electrical| from X_train has missing values and it is NOT in X_valid
    

---

# Using the other dataset (melb_data.csv):


```python
nan_columns(X_train_1, X_valid_1)
```

    |X_train_1| --> (columns w/ nan values, number of missing values): 
    
    Car               49
    BuildingArea    5156
    YearBuilt       4307
    CouncilArea     1072
    dtype: int64 
    
    Number of columns with missing values: 4 
     ------------------------------------------- 
    
    
    |X_valid_1| --> (columns w/ nan values, number of missing values): 
    
    Car               13
    BuildingArea    1294
    YearBuilt       1068
    CouncilArea      297
    dtype: int64 
    
    Number of columns with missing values: 4 
     ------------------------------------------- 
    
    --> Both X_train_1 and X_valid_1 have nan values in the same columns
    


```python
nan_columns(X_valid_1, X_train_1)
```

    |X_valid_1| --> (columns w/ nan values, number of missing values): 
    
    Car               13
    BuildingArea    1294
    YearBuilt       1068
    CouncilArea      297
    dtype: int64 
    
    Number of columns with missing values: 4 
     ------------------------------------------- 
    
    
    |X_train_1| --> (columns w/ nan values, number of missing values): 
    
    Car               49
    BuildingArea    5156
    YearBuilt       4307
    CouncilArea     1072
    dtype: int64 
    
    Number of columns with missing values: 4 
     ------------------------------------------- 
    
    --> Both X_valid_1 and X_train_1 have nan values in the same columns
    

---

# Let's say you got something wrong, in the function's argumet:


```python
nan_columns(X_train, y_train)
```

    |X_train| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      212
    Alley           1097
    MasVnrType       707
    MasVnrArea         6
    BsmtQual          28
    BsmtCond          28
    BsmtExposure      28
    BsmtFinType1      28
    BsmtFinType2      29
    Electrical         1
    FireplaceQu      551
    GarageType        58
    GarageYrBlt       58
    GarageFinish      58
    GarageQual        58
    GarageCond        58
    PoolQC          1164
    Fence            954
    MiscFeature     1119
    dtype: int64 
    
    Number of columns with missing values: 19 
     ------------------------------------------- 
    
    
    *error* --> |y_train| --> you may have put a wrong input: only pandas DataFrame types are accepted
    

---

## Here I used 2 different data training variables (both dataframes) but from different datasets:


```python
nan_columns(X_train, X_train_1)
```

    |X_train| --> (columns w/ nan values, number of missing values): 
    
    LotFrontage      212
    Alley           1097
    MasVnrType       707
    MasVnrArea         6
    BsmtQual          28
    BsmtCond          28
    BsmtExposure      28
    BsmtFinType1      28
    BsmtFinType2      29
    Electrical         1
    FireplaceQu      551
    GarageType        58
    GarageYrBlt       58
    GarageFinish      58
    GarageQual        58
    GarageCond        58
    PoolQC          1164
    Fence            954
    MiscFeature     1119
    dtype: int64 
    
    Number of columns with missing values: 19 
     ------------------------------------------- 
    
    
    |X_train_1| --> (columns w/ nan values, number of missing values): 
    
    Car               49
    BuildingArea    5156
    YearBuilt       4307
    CouncilArea     1072
    dtype: int64 
    
    Number of columns with missing values: 4 
     ------------------------------------------- 
    
    19 Columns: |'Alley', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'BsmtQual', 'Electrical', 'Fence', 'FireplaceQu', 'GarageCond', 'GarageFinish', 'GarageQual', 'GarageType', 'GarageYrBlt', 'LotFrontage', 'MasVnrArea', 'MasVnrType', 'MiscFeature', 'PoolQC'| from X_train have missing values and they are NOT in X_train_1 
    
    4 Columns: |'BuildingArea', 'Car', 'CouncilArea', 'YearBuilt'| from X_train_1 have missing values and they are NOT in X_train 
    
    

---
