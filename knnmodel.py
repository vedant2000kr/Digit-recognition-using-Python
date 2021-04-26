from sklearn.datasets import load_digits
from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

class MLmodel:
    def trainModel():
        digits = load_digits()
        (X_train, X_test, y_train, y_test) = train_test_split(digits.data, digits.target, test_size=0.25, random_state=42)

        KNN_model = KNeighborsClassifier(n_neighbors=3)
        KNN_model.fit(X_train, y_train)
        return KNN_model
