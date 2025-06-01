import pandas as pd
import preprocessing

#Load the csv file
df = pd.read_csv("employees.csv")
print("Original DataFrame:")
print(df)

# Remove duplicates based on 'id'
df_cleaned = df.drop_duplicates(subset=["age", "salary", "department"])
print("\nAfter Removing Duplicates:")
print(df_cleaned)

# Normalize the salary column
df_normalized = preprocessing.normalize_column(df_cleaned, "salary")
print("\nAfter Normalizing Salary:")
print(df_normalized)

# Encode the department column
df_encoded, dept_mapping = preprocessing.encode_categorical(df_normalized, "department")
print("\nDepartment Mapping:", dept_mapping)
print("\nAfter Encoding Department:")
print(df_encoded)

# Save the preprocessed DataFrame to a new CSV file
df_encoded.to_csv("employees_processed.csv", index=False)
print("\nPreprocessed data saved to 'employees_preprocessed.csv'")