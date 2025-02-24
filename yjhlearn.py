import numpy as np

class KNeighborRegressor:
    def __init__(self,n_neighbors=5):
        self.n_neighbors=n_neighbors
    def fit(self,X_train,y_train):
        """
        learning function
        :param X: independent variable(2d array format)
        :param y: dependent variable(2d array format)
        :return: void
        """
        self.X_train=X_train
        self.y_train=y_train

    def predict(self,X_test):
        predictions = []
        for x_test in X_test:  # loop just one time in this example
            # d(P, Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
            distances = np.sqrt(np.sum((x_test - self.X_train)**2, axis=1))
            # print(distances)
            indices = np.argsort(distances)[:self.n_neighbors]
            # print(indices)
            prediction = np.mean(self.y_train[indices])
            # prediction = (self.y_train[indices[0]]+self.y_train[indices[1]]+self.y_train[indices[2]]) / self.n_neighbors
            predictions.append(prediction)

            return np.array(prediction).reshape(-1, 1)
