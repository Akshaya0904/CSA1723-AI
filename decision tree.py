from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
m=DecisionTreeClassifier().fit(X,y)
print("Accuracy:",m.score(X,y))
