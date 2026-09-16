import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_excel("Lab Session Data (1).xlsx", sheet_name="marketing_campaign")

df = df.drop_duplicates()
df["Response"] = pd.to_numeric(df["Response"], errors="coerce")
df = df.dropna(subset=["Response"])

df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], errors="coerce", dayfirst=True)
df["Customer_Year"] = df["Dt_Customer"].dt.year
df["Customer_Month"] = df["Dt_Customer"].dt.month
df["Customer_Day"] = df["Dt_Customer"].dt.day
df = df.drop(columns=["Dt_Customer"])

df = df.drop(columns=["ID"])

X = df.drop(columns=["Response"])
y = df["Response"].astype(int)

X = pd.get_dummies(X, drop_first=True)
X = X.apply(pd.to_numeric, errors="coerce")
X = X.fillna(X.mean())
X = X.fillna(0)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def bubble_sort(distances):
    n = len(distances)
    for i in range(n):
        for j in range(0, n-i-1):
            if distances[j][0] > distances[j+1][0]:
                distances[j], distances[j+1] = distances[j+1], distances[j]
    return distances

def selection_sort(distances):
    n = len(distances)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if distances[j][0] < distances[min_index][0]:
                min_index = j
        distances[i], distances[min_index] = distances[min_index], distances[i]
    return distances

def insertion_sort(distances):
    for i in range(1, len(distances)):
        key = distances[i]
        j = i - 1
        while j >= 0 and distances[j][0] > key[0]:
            distances[j+1] = distances[j]
            j -= 1
        distances[j+1] = key
    return distances

def get_neighbors(X_train, y_train, test_point, k, sorting="insertion"):
    distances = []
    for i in range(len(X_train)):
        distance = euclidean_distance(test_point, X_train[i])
        distances.append((distance, y_train.iloc[i]))
    if sorting == "bubble":
        distances = bubble_sort(distances)
    elif sorting == "selection":
        distances = selection_sort(distances)
    else:
        distances = insertion_sort(distances)
    return distances[:k]

def majority_vote(neighbors):
    votes = {}
    for distance, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    return max(votes, key=votes.get)

def weighted_vote(neighbors):
    weights = {}
    for distance, label in neighbors:
        weight = 1 / (distance + 1e-10)
        weights[label] = weights.get(label, 0) + weight
    return max(weights, key=weights.get)

class CustomKNN:
    def __init__(self, k=3, sorting="insertion", weighted=False):
        self.k = k
        self.sorting = sorting
        self.weighted = weighted

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y.reset_index(drop=True)
        return self

    def predict(self, X):
        predictions = []
        for point in X:
            neighbors = get_neighbors(
                self.X_train,
                self.y_train,
                point,
                self.k,
                self.sorting
            )
            if self.weighted:
                predictions.append(weighted_vote(neighbors))
            else:
                predictions.append(majority_vote(neighbors))
        return np.array(predictions)

    def predict_proba(self, X):
        probabilities = []
        for point in X:
            neighbors = get_neighbors(
                self.X_train,
                self.y_train,
                point,
                self.k,
                self.sorting
            )
            probability = sum(label == 1 for distance, label in neighbors) / self.k
            probabilities.append(probability)
        return np.array(probabilities)

    def score(self, X, y):
        return accuracy_score(y, self.predict(X))

model = CustomKNN(k=3, sorting="insertion")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=0))

y_prob = model.predict_proba(X_test)
auc = roc_auc_score(y_test, y_prob)

print("AUC:", auc)

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr, label="AUC = {:.3f}".format(auc))
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

k_values = [1, 3, 5, 7, 9, 11]
accuracies = []

for k in k_values:
    model = CustomKNN(k=k)
    model.fit(X_train, y_train)
    accuracies.append(model.score(X_test, y_test))

plt.plot(k_values, accuracies, marker="o")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.title("Accuracy vs k")
plt.show()

normal_accuracy = []
weighted_accuracy = []

for k in k_values:
    model1 = CustomKNN(k=k, weighted=False)
    model1.fit(X_train, y_train)
    normal_accuracy.append(model1.score(X_test, y_test))

    model2 = CustomKNN(k=k, weighted=True)
    model2.fit(X_train, y_train)
    weighted_accuracy.append(model2.score(X_test, y_test))

plt.plot(k_values, normal_accuracy, marker="o", label="Normal")
plt.plot(k_values, weighted_accuracy, marker="o", label="Weighted")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.legend()
plt.show()