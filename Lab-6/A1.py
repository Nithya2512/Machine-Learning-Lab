import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import unittest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_curve,roc_auc_score

df=pd.read_excel("Lab Session Data (1).xlsx",sheet_name="marketing_campaign")
df=df.drop_duplicates()
df["Response"]=pd.to_numeric(df["Response"],errors="coerce")
df=df.dropna(subset=["Response"])
df["Dt_Customer"]=pd.to_datetime(df["Dt_Customer"],errors="coerce",dayfirst=True)
df["Customer_Year"]=df["Dt_Customer"].dt.year
df["Customer_Month"]=df["Dt_Customer"].dt.month
df["Customer_Day"]=df["Dt_Customer"].dt.day
df=df.drop(columns=["Dt_Customer","ID"])

X=df.drop(columns=["Response"])
y=df["Response"].astype(int)
X=pd.get_dummies(X,drop_first=True)
X=X.apply(pd.to_numeric,errors="coerce")
X=X.fillna(X.mean())
X=X.fillna(0)

scaler=StandardScaler()
X=scaler.fit_transform(X)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)

sklearn_model=KNeighborsClassifier(n_neighbors=3)
sklearn_model.fit(X_train,y_train)
sklearn_pred=sklearn_model.predict(X_test)

sklearn_accuracy=accuracy_score(y_test,sklearn_pred)
sklearn_precision=precision_score(y_test,sklearn_pred,zero_division=0)
sklearn_recall=recall_score(y_test,sklearn_pred,zero_division=0)
sklearn_f1=f1_score(y_test,sklearn_pred,zero_division=0)
sklearn_prob=sklearn_model.predict_proba(X_test)[:,1]
sklearn_auc=roc_auc_score(y_test,sklearn_prob)

k_values=[1,3,5,7,9,11]
sklearn_k_accuracy=[]

for k in k_values:
    model=KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    prediction=model.predict(X_test)
    sklearn_k_accuracy.append(accuracy_score(y_test,prediction))

plt.plot(k_values,sklearn_k_accuracy,marker="o")
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.title("Accuracy vs k")
plt.xticks(k_values)
plt.grid()
plt.show()

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class CustomKNN:
    def __init__(self,k=3):
        self.k=k

    def fit(self,X,y):
        self.X_train=np.array(X)
        self.y_train=np.array(y)
        return self

    def predict(self,X):
        predictions=[]
        for point in X:
            distances=[]
            for i in range(len(self.X_train)):
                distance=euclidean_distance(point,self.X_train[i])
                distances.append((distance,self.y_train[i]))
            distances.sort(key=lambda x:x[0])
            neighbors=distances[:self.k]
            votes={}
            for distance,label in neighbors:
                votes[label]=votes.get(label,0)+1
            prediction=max(votes,key=votes.get)
            predictions.append(prediction)
        return np.array(predictions)

    def predict_proba(self,X):
        probabilities=[]
        for point in X:
            distances=[]
            for i in range(len(self.X_train)):
                distance=euclidean_distance(point,self.X_train[i])
                distances.append((distance,self.y_train[i]))
            distances.sort(key=lambda x:x[0])
            neighbors=distances[:self.k]
            probability=sum(label==1 for distance,label in neighbors)/self.k
            probabilities.append(probability)
        return np.array(probabilities)

    def score(self,X,y):
        prediction=self.predict(X)
        return accuracy_score(y,prediction)

custom_model=CustomKNN(k=3)
custom_model.fit(X_train,y_train)
custom_pred=custom_model.predict(X_test)

custom_accuracy=accuracy_score(y_test,custom_pred)
custom_precision=precision_score(y_test,custom_pred,zero_division=0)
custom_recall=recall_score(y_test,custom_pred,zero_division=0)
custom_f1=f1_score(y_test,custom_pred,zero_division=0)
custom_prob=custom_model.predict_proba(X_test)
custom_auc=roc_auc_score(y_test,custom_prob)

class GenAIKNN:
    def __init__(self,k=3):
        self.k=k

    def fit(self,X,y):
        self.X_train=np.array(X)
        self.y_train=np.array(y)
        return self

    def predict(self,X):
        predictions=[]
        for point in X:
            distances=[]
            for i in range(len(self.X_train)):
                distance=np.linalg.norm(point-self.X_train[i])
                distances.append((distance,self.y_train[i]))
            distances.sort(key=lambda x:x[0])
            neighbors=distances[:self.k]
            votes={}
            for distance,label in neighbors:
                votes[label]=votes.get(label,0)+1
            prediction=max(votes,key=votes.get)
            predictions.append(prediction)
        return np.array(predictions)

    def predict_proba(self,X):
        probabilities=[]
        for point in X:
            distances=[]
            for i in range(len(self.X_train)):
                distance=np.linalg.norm(point-self.X_train[i])
                distances.append((distance,self.y_train[i]))
            distances.sort(key=lambda x:x[0])
            neighbors=distances[:self.k]
            probability=sum(label==1 for distance,label in neighbors)/self.k
            probabilities.append(probability)
        return np.array(probabilities)

    def score(self,X,y):
        prediction=self.predict(X)
        return accuracy_score(y,prediction)

genai_model=GenAIKNN(k=3)
genai_model.fit(X_train,y_train)
genai_pred=genai_model.predict(X_test)

genai_accuracy=accuracy_score(y_test,genai_pred)
genai_precision=precision_score(y_test,genai_pred,zero_division=0)
genai_recall=recall_score(y_test,genai_pred,zero_division=0)
genai_f1=f1_score(y_test,genai_pred,zero_division=0)
genai_prob=genai_model.predict_proba(X_test)
genai_auc=roc_auc_score(y_test,genai_prob)

results=pd.DataFrame({
    "Model":["Custom kNN","Scikit-learn kNN","GenAI kNN"],
    "Accuracy":[custom_accuracy,sklearn_accuracy,genai_accuracy],
    "Precision":[custom_precision,sklearn_precision,genai_precision],
    "Recall":[custom_recall,sklearn_recall,genai_recall],
    "F1 Score":[custom_f1,sklearn_f1,genai_f1],
    "AUC":[custom_auc,sklearn_auc,genai_auc]
})

print(results)

custom_times=[]
sklearn_times=[]
genai_times=[]

for i in range(10):
    start=time.perf_counter()
    model=CustomKNN(k=3)
    model.fit(X_train,y_train)
    model.predict(X_test)
    end=time.perf_counter()
    custom_times.append(end-start)

for i in range(10):
    start=time.perf_counter()
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,y_train)
    model.predict(X_test)
    end=time.perf_counter()
    sklearn_times.append(end-start)

for i in range(10):
    start=time.perf_counter()
    model=GenAIKNN(k=3)
    model.fit(X_train,y_train)
    model.predict(X_test)
    end=time.perf_counter()
    genai_times.append(end-start)

timing_results=pd.DataFrame({
    "Model":["Custom kNN","Scikit-learn kNN","GenAI kNN"],
    "Average Time":[np.mean(custom_times),np.mean(sklearn_times),np.mean(genai_times)]
})

print(timing_results)

results.plot(x="Model",y=["Accuracy","Precision","Recall","F1 Score","AUC"],kind="bar")
plt.ylabel("Score")
plt.title("kNN Performance Comparison")
plt.ylim(0,1)
plt.xticks(rotation=0)
plt.show()

timing_results.plot(x="Model",y="Average Time",kind="bar")
plt.ylabel("Time (seconds)")
plt.title("10-Run Execution Time Comparison")
plt.xticks(rotation=0)
plt.show()

sklearn_fpr,sklearn_tpr,_=roc_curve(y_test,sklearn_prob)
custom_fpr,custom_tpr,_=roc_curve(y_test,custom_prob)
genai_fpr,genai_tpr,_=roc_curve(y_test,genai_prob)

plt.plot(sklearn_fpr,sklearn_tpr,label="Scikit-learn kNN")
plt.plot(custom_fpr,custom_tpr,label="Custom kNN")
plt.plot(genai_fpr,genai_tpr,label="GenAI kNN")
plt.plot([0,1],[0,1],linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()

class TestKNN(unittest.TestCase):
    def test_distance(self):
        result=euclidean_distance(np.array([0,0]),np.array([3,4]))
        self.assertEqual(result,5)

    def test_custom_knn(self):
        X=np.array([[0,0],[0,1],[5,5],[5,6]])
        y=np.array([0,0,1,1])
        model=CustomKNN(k=1)
        model.fit(X,y)
        prediction=model.predict(np.array([[0,0]]))
        self.assertEqual(prediction[0],0)

    def test_genai_knn(self):
        X=np.array([[0,0],[0,1],[5,5],[5,6]])
        y=np.array([0,0,1,1])
        model=GenAIKNN(k=1)
        model.fit(X,y)
        prediction=model.predict(np.array([[0,0]]))
        self.assertEqual(prediction[0],0)

unittest.main(argv=[""],exit=False)