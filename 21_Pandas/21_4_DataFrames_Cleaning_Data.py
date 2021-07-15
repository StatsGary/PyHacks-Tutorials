# =============================================================================
# Title             PyHacks - Pandas - DataFrames - Cleaning Data
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      14/07/2021
# =============================================================================

# Function to convert tuple to list 

def get_df_structure_list(df):
    rows, columns = df.shape
    listed = [rows, columns]
    return listed

import pandas as pd
df = pd.read_csv("Data/Stranded/stranded.csv")#, index_col=[0])

#---------------------DATA CLEANING ON ROWS------------------------------------

# Remove empty rows
drop_df = df.dropna()
# To change the original data frame we would use the inplace=True method
# of the dropna statement
print(drop_df.to_string())
print(drop_df.info())

# Replace empty values
filled_df = df.copy()
filled_df.fillna(0, inplace=True)

#Replace only specific columns
spec_df = df.copy()
spec_df["periods_of_previous_care"].fillna(0, inplace=True)

#Replace columns using mean, median or modal imputation 
mean_df = df.copy()
mean_ppc = mean_df["periods_of_previous_care"].mean() #Compute the mean
mean_df["periods_of_previous_care"].fillna(mean_ppc, inplace=True)


#---------------------REFORMATTING--------------------------------------
# Convert the admit_date to the correct format
df = mean_df.copy()
# Delete objects, as we are going to use the mean imputed frame
del drop_df, filled_df, mean_df, mean_ppc, spec_df

#Convert to date
df["admit_date"] = pd.to_datetime(df['admit_date'])
print(df.info())
print(df)

# We aren't going to use this column in our analysis, but
# I will cover how we could engineer these features further

df = df.drop("admit_date", axis=1)

#---------------------REPLACING VALUES-----------------------------------
#One label was a long wait patient, so we will use loc to replace that
df.loc[0, "stranded.label"] = "Stranded"



print(get_df_structure_list(df)) #Unpack the tuple () to seperate variables
# Remove rows with a greater that 9 previous periods of care
for row in df.index:
    if df.loc[row, "periods_of_previous_care"] > 9:
        df.drop(row, inplace=True)
        
print(get_df_structure_list(df))

# This loops through every row in the index for the period of previous
# care and if the value is greater than 9, it drops the rows from the frame


#---------------------REPLACING DUPLICATES OR FINDING--------------------
print(df.duplicated())
# Removing duplicates
df.drop_duplicates(inplace=True)
print(df.columns)

#--------------------CREATING DUMMY ENCODING FOR CAT VARIABLES-----------
frail = df['frailty_index']
dummies_frail = pd.get_dummies(frail, prefix="frailidx",
                               dummy_na=False, drop_first=False)

# Drop original column, as we now have binary encodings we could work with in models
df = df.drop("frailty_index", axis=1) #Axis 0 is rows and axis 1 is columns

# Use column concatenation: see: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
df_new = df.copy()
df_new = pd.concat([df_new, dummies_frail],axis=1)

#--------------------DROP MULTIPLE COLUMNS -------------------------------

# I don't want the control dummy encoding or the the hcop flag
df_reduced = df_new.drop(["frailidx_Activity Limitation",
                          "frailidx_No index item"], axis=1)


#--------------------WRITE FINAL ML DATASET READY---------------------------
df_reduced.to_csv("Data/Stranded/stranded_reduced.csv", index=False)
