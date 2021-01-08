import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.optimizers import SGD
from sklearn.model_selection import KFold
from tensorflow.keras.callbacks import EarlyStopping


def load_dataset():
    """
    Loads MNIST dataset to x_train, x_test, y_train, y_test
    :return: train and test datasets
    """

    def shapex(X, threshold):
        XX = np.empty_like(X)
        XX[X < threshold] = 0
        XX[X >= threshold] = 1
        XX = XX.reshape(*XX.shape, 1)
        return XX

    mnist = tf.keras.datasets.mnist
    threshold = 125

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = shapex(x_train, threshold)
    x_test = shapex(x_test, threshold)
    # reshape to have a single color channel
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
    x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

    # one hot encode target values
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    return x_train, y_train, x_test, y_test


def normalize_data(train, test):
    """
    normalizes data values
    :param train: train data
    :param test: test data
    :return:
    """

    # convert from int to float
    train_norm = train.astype("float32")
    test_norm = test.astype("float32")
    # normalize to values between 0 and 1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    return train_norm, test_norm


def create_model(model_name=None):
    """
    Creates model for the MNIST dataset. convolution layer, pooling layer, flattening,
     dense layer, and dense layer with softmax.
    :return: model
    """
    if not model_name:
        act = "relu"
        model = Sequential([
            Conv2D(32, (3, 3), activation=act, input_shape=x_train.shape[1:]),
            MaxPooling2D(2, 2),
            Conv2D(64, (3, 3), activation=act, kernel_initializer='he_uniform'),
            MaxPooling2D(2, 2),
            Conv2D(64, (3, 3), activation=act, kernel_initializer='he_uniform'),
            Flatten(),
            Dense(128, activation="relu", kernel_initializer="he_uniform"),
            Dense(10, activation="softmax")
        ])
        opt = SGD(lr=0.025, momentum=0.9)
        model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
        return model
    else:
        model = load_model(model_name)
        return model

def train_and_save_model(dataX, dataY, n_folds=5):
    """
    Evaluates the performance of the model.
    :param dataX: x-data
    :param dataY: y-data
    :param n_folds: number of folds for KFold
    :return: score data and history data
    """
    scores, histories = list(), list()
    # prepare cross validation
    model = create_model()
    trainX, trainY, testX, testY = dataX[int(len(dataX)*0.2):], dataY[int(len(dataY)*0.2):], dataX[:int(len(dataX)*0.2)], dataY[:int(len(dataY)*.2)]
    es = EarlyStopping(monitor="val_loss", patience=10)
    # fit model
    model.fit(trainX, trainY, epochs=150, batch_size=32, validation_data=(testX, testY), verbose=1, validation_split=0.8, callbacks=[es])
    model.save("savedModels/mnist_model3")
    # evaluate model
    _, acc = model.evaluate(testX, testY, verbose=0)
    print('> %.3f' % (acc * 100.0))


def summarize_diagnostics(histories):
    for i in range(len(histories)):
        # plot loss
        plt.subplot(2, 1, 1)
        plt.title('Cross Entropy Loss')
        plt.plot(histories[i].history['loss'], color='blue', label='train')
        plt.plot(histories[i].history['val_loss'], color='orange', label='test')
        # plot accuracy
        plt.subplot(2, 1, 2)
        plt.title('Classification Accuracy')
        plt.plot(histories[i].history['accuracy'], color='blue', label='train')
        plt.plot(histories[i].history['val_accuracy'], color='orange', label='test')
    plt.show()


# summarize model performance
def summarize_performance(scores):
    # print summary
    print('Accuracy: mean=%.3f std=%.3f, n=%d' % (np.mean(scores)*100, np.std(scores)*100, len(scores)))
    # box and whisker plots of results
    plt.boxplot(scores)
    plt.show()


# run the test harness for evaluating a model
def run_test_harness():
    # load dataset
    trainX, trainY, testX, testY = load_dataset()
    # prepare pixel data
    trainX, testX = normalize_data(trainX, testX)
    train_and_save_model(trainX, trainY)


x_train, y_train, x_test, y_test = load_dataset()
model = create_model()

run_test_harness()
#model.fit(x_train, y_train, epochs=10)
#model.evaluate(x_test, y_test)
#predictions = model(x_train[:1]).numpy()
#predictions
#print(tf.nn.softmax(predictions).numpy())
