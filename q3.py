import numpy as np
from scipy.stats import chi2_contingency

# Step 1: Create a Contingency Table
# Example data: Survey responses of two categorical variables (e.g., Gender and Preference)
# Contingency table of observed frequencies
# Rows: Gender (Male, Female)
# Columns: Preference (A, B, C)
observed = np.array([[20, 30, 50],
                     [30, 10, 40]])

# Step 2: Perform the Chi-Square Test
chi2_stat, p_val, dof, expected = chi2_contingency(observed)

# Step 3: Interpret the Results
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_val}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Step 4: Determine if the association is significant
alpha = 0.05  # Significance level
if p_val < alpha:
    print("The variables are associated (reject the null hypothesis).")
else:
    print("The variables are not associated (fail to reject the null hypothesis).")
