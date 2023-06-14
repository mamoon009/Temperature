# Create the dataset
data = {
    'num_students': [500, 600, 700, 800, 900],
    'temperature': [20, 21, 22, 23, 24],
    'num_rooms': [30, 35, 40, 45, 50]
}

# Split the dataset into features (X) and target (y)
X = [[1, num_students, temperature] for num_students, temperature in zip(data['num_students'], data['temperature'])]
y = data['num_rooms']

# Calculate the coefficients using normal equations
XTX = [[sum(x[i] * x[j] for x in X) for j in range(len(X[0]))] for i in range(len(X[0]))]
XTy = [sum(X[i][j] * y[i] for i in range(len(X))) for j in range(len(X[0]))]

coefficients = [0] * len(X[0])
for i in range(len(X[0])):
    coefficients[i] = sum(XTX[i][j] * XTy[j] for j in range(len(X[0])))

# Print the coefficients
print("Coefficients:", coefficients)

# Predict the number of rooms required for a new scenario
new_students=int(input("ENTER NEW STUDENTS : "))  # Number of students in the new scenario
new_temperature=int(input("ENTER NEW TEMPERATURE : "))# Temperature in the new scenario

# Create the feature array for the new scenario
new_scenario = [1, new_students, new_temperature]

# Make the prediction
predicted_rooms = sum(coefficients[i] * new_scenario[i] for i in range(len(new_scenario)))

print("Number of students:", new_students)
print("Temperature:", new_temperature)
print("Predicted number of rooms:", predicted_rooms)