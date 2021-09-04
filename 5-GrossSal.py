Basic_Salary = input("Enter Basic Salary :")

DA = (Basic_Salary * 20) / 100
HRA = (Basic_Salary * 30) / 100
Gross_Salary = Basic_Salary + DA + HRA

print("Dearness Allowance 20 % of Basic Salary :" , DA)
print("House Rent 30 % of Basic Salary :" , HRA)
print("Gross Salary :" , Gross_Salary)
