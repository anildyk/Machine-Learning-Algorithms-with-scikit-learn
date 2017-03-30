# Digits Identification from digits dataset from scikit-learn datasets
# import datasets and required matplotlib library to plot images of digits stored in digits dataset.
from sklearn import datasets
import matplotlib.pyplot as plt 

# Get digits dataset from scikit-learn datasets
digits = datasets.load_digits()
# Make a classifier fron SVM with linear kernel. 
clf = svm.SVC(kernel='linear', gamma=0.001, C=100)
# Learn from n_samples-2 samples
clf.fit(digits.data[:-2], digits.target[:-2].astype(int))
# Predict digit images for remained 2 samples or test data.
p = clf.predict(digits.data[-2:])
print p
# Print image of last two digits in digits dataset.
plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
plt.imshow(digits.images[-1], cmap = plt.cm.gray_r, interpolation='nearest')
plt.show()
print "Mean Accuracy: ", clf.score(digits.data, digits.target.astype(int))
