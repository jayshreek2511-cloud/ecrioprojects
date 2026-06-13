import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

print("Dataset Loaded!\n")

# 1. Group by Pclass → avg age & survival rate
group_pclass = df.groupby('Pclass').agg({
    'Age': 'mean',
    'Survived': 'mean'
})
print("1. Avg Age & Survival Rate by Pclass:\n", group_pclass, "\n")


# 2. Normalize Age (Min-Max) and Z-score
# Fill missing first (needed for normalization)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Min-Max normalization
df['Age_MinMax'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

# Z-score normalization
df['Age_Zscore'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()

print("2. Normalization done (Min-Max & Z-score)\n")


# 3. Handle missing values in Age (already done above)
print("3. Missing Age values handled using mean\n")


# 4. Group by SexCode and count survivors
# Create SexCode (male=0, female=1)
df['SexCode'] = df['Sex'].map({'male': 0, 'female': 1})

survivors_by_sexcode = df.groupby('SexCode')['Survived'].sum()
print("4. Survivors by SexCode:\n", survivors_by_sexcode, "\n")


# 5. Create Child/Adult column
df['AgeGroup'] = df['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult')

print("5. AgeGroup column created\n")


# 6. Pivot table (Pclass vs SexCode survival rate)
pivot_table = pd.pivot_table(
    df,
    values='Survived',
    index='Pclass',
    columns='SexCode',
    aggfunc='mean'
)

print("6. Pivot Table (Survival Rate):\n", pivot_table, "\n")


# Save updated dataset
df.to_csv("titanic_project5_output.csv", index=False)

print("Final dataset saved as 'titanic_project5_output.csv'")