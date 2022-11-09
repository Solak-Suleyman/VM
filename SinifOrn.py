class BaseClassifier(object):
    def __init__(self):
        pass
    def get_name(self):
        raise NotImplementedError()
    def fit(self, x, y):
        raise NotImplementedError()
    def predict(self, x):
        raise NotImplementedError()

class BaseTree(BaseClassifier):
    def __init__(self, height):
        super().__init__()
        self.height = height
    def get_name(self):
        return "Base Tree";
    def fit(self, x, y):
        self.X = x
        self.Y = y
    def predict(self, x):
        y = np.zeros((x.shape[0],))
        for i in range(x.shape[0]):
            y[i] = self.__predict_single(x[i, :])
        return y
