import json
import numpy
from joblib import dump, load
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report


def svm_classifier(x_train, y_train):
    """
    SVM classifier
    :param x_train: the review text
    :param y_train: label, 1 for positive, 0 for negative
    :return: the classifier
    """
    print('************ Support Vector Machine Model************')
    clf = SVC(kernel='linear', probability=True)  # default with 'rbf'
    clf.fit(x_train, y_train)  # training，for supervised learning we use fit(X, y), not fit(X)
    dump(clf, 'classifiers/SvmClassifier.jbl')
    return clf


def nb_classifier(x_train, y_train):
    """
    naive bayes model
    :param x_train:
    :param y_train:
    :return:
    """
    print('************** Naive Bayes Model ********************')
    clf = MultinomialNB(alpha=0.01).fit(x_train, y_train)
    dump(clf, 'classifiers/NbClassifier.jbl')
    return clf


def logistic_classifier(x_train, y_train):
    """
    logistic regression model
    :param x_train:
    :param y_train:
    :return:
    """
    print('************** Logistic Regression ******************')
    clf = LogisticRegression(penalty='l2')
    clf.fit(x_train, y_train)
    dump(clf, 'classifiers/LogisticClassifier.jbl')
    return clf


def knn_classifier(x_train, y_train):
    """
    KNN model
    :param x_train:
    :param y_train:
    :return:
    """
    print('************ K-nearest Neighbors Model **************')
    clf = KNeighborsClassifier()
    clf.fit(x_train, y_train)
    dump(clf, 'classifiers/KnnClassifier.jbl')
    return clf


def decision_classifier(x_train, y_train):
    """
    decision tree model
    :param x_train:
    :param y_train:
    :return:
    """
    print('************** Decision Tree Model ******************')
    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    dump(clf, 'classifiers/DeciClassifier.jbl')
    return clf


def random_forest_class(x_train, y_train):
    """
    random forest model
    :param x_train:
    :param y_train:
    :return:
    """
    print('************** Random Forest Model ******************')
    clf = RandomForestClassifier(n_estimators=8)  # n_estimators is the number of trees to be used in the forest
    clf.fit(x_train, y_train)
    dump(clf, 'classifiers/RandomFClassifier.jbl')
    return clf


def precision(clf):
    """
    the helper method to print each classifier's precision rate
    :param clf:
    :return:
    """
    doc_class_predicted = clf.predict(x_test)
    precision, recall, thresholds = precision_recall_curve(y_test, clf.predict(x_test))
    answer = clf.predict_proba(x_test)[:, 1]
    report = answer > 0.5
    from sklearn.metrics import accuracy_score
    print('Precision: %.2f' % accuracy_score(y_test, doc_class_predicted))
    print("--------------------")
    print(classification_report(y_test, report, target_names=['neg', 'pos']))


if __name__ == '__main__':
    data = []
    labels = []
    print('Reading training data set...\n')
    with open("data/train_set.json", "r", encoding='utf-8') as read_file:
        dataset = json.loads(read_file.read())
        for line in dataset:
            labels.append(dataset[line][1])
            data.append(dataset[line][0])
    x = numpy.array(data)
    labels = numpy.array(labels)
    labels = [int(i) for i in labels]
    movie_target = labels
    # convert the data into vectors
    vec = TfidfVectorizer(binary=False)
    # load the data set, set 80% of the data for training and the rest 20% for test
    x_train, x_test, y_train, y_test = train_test_split(x, movie_target, test_size=0.2)
    x_train = vec.fit_transform(x_train)
    x_test = vec.transform(x_test)
    dump(vec, 'classifiers/vectorizer.jbl')
    print('Trained vectorizer is saved to data/vectorizer.jbl\n')

    precision(svm_classifier(x_train, y_train))
    precision(nb_classifier(x_train, y_train))
    precision(knn_classifier(x_train, y_train))
    precision(logistic_classifier(x_train, y_train))
    precision(decision_classifier(x_train, y_train))
    precision(random_forest_class(x_train, y_train))
