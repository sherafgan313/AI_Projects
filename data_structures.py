# Lists: Storing and manipulating feature data
features = [1.5, 2.3, 3.7, 4.1, 5.0]
print("Features List:", features)
features.append(6.2)  # Add a new feature
print("After Append:", features)
features.sort()  # Sort the list
print("Sorted Features:", features)
squared_features = [x**2 for x in features]  # List comprehension
print("Squared Features:", squared_features)

# Dictionaries: Storing metadata about a dataset
dataset_info = {
    "name": "Iris Dataset",
    "num_samples": 150,
    "num_features": 4,
    "target_classes": ["setosa", "versicolor", "virginica"]
}
print("\nDataset Info:", dataset_info)
print("Target Classes:", dataset_info["target_classes"])
dataset_info["num_samples"] += 10  # Update value
print("Updated Dataset Info:", dataset_info)

# Sets: Finding unique elements
labels = ["cat", "dog", "cat", "bird", "dog", "fish"]
unique_labels = set(labels)
print("\nLabels:", labels)
print("Unique Labels:", unique_labels)
unique_labels.add("rabbit")  # Add a new label
print("Updated Unique Labels:", unique_labels)

# Tuples: Storing immutable data (e.g., model configuration)
model_config = (0.01, 100, "relu")  # (learning_rate, epochs, activation)
print("\nModel Config (learning_rate, epochs, activation):", model_config)
print("Learning Rate:", model_config[0])
# model_config[0] = 0.02  # This will raise an error (tuples are immutable)