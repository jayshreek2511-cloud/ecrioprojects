import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

print("Dataset Loaded Successfully!\n")
print("Script started...")
# 1. Count survived passengers and percentage
survived_count = df['Survived'].sum()
total_passengers = len(df)
survival_percentage = (survived_count / total_passengers) * 100

print("1. Survived Count:", survived_count)
print("   Survival Percentage:", survival_percentage, "%\n")

# 2. Average age in each class
avg_age_class = df.groupby('Pclass')['Age'].mean()
print("2. Average Age per Class:\n", avg_age_class, "\n")

# 3. Count male and female in each class
gender_count_class = df.groupby(['Pclass', 'Sex']).size()
print("3. Gender Count per Class:\n", gender_count_class, "\n")

# 4. Percentage of females who survived
female_data = df[df['Sex'] == 'female']
female_survival_percentage = (female_data['Survived'].sum() / len(female_data)) * 100

print("4. Female Survival Percentage:", female_survival_percentage, "%\n")

# 5. Survival rate by gender
survival_by_gender = df.groupby('Sex')['Survived'].mean() * 100
print("5. Survival Rate by Gender:\n", survival_by_gender, "\n")

# 6. Median age of male and female
median_age_gender = df.groupby('Sex')['Age'].median()
print("6. Median Age by Gender:\n", median_age_gender, "\n")

# 7. Average age of survivors vs non-survivors
avg_age_survival = df.groupby('Survived')['Age'].mean()
print("7. Avg Age (0=Not Survived, 1=Survived):\n", avg_age_survival, "\n")

# 8. Passengers above age 40
above_40 = df[df['Age'] > 40]
avg_age_above_40 = above_40['Age'].mean()

print("8. Avg Age of Passengers > 40:", avg_age_above_40, "\n")

# 9. Create Age Group column
def age_group(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df['AgeGroup'] = df['Age'].apply(age_group)

print("9. Age Group Column Added\n")

# 10. Survivors in 1st class & avg fare
first_class_survivors = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]
avg_fare_first_class = first_class_survivors['Fare'].mean()

print("10. Avg Fare (1st Class Survivors):", avg_fare_first_class, "\n")

# 11. Clean dataset and save
# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("11. Cleaned dataset saved as 'titanic_cleaned.csv'")