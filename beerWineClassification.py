# Beer Vs. Wine
# Classification based on Alcoholic Content & Color

from sklearn import tree
#features = [[4,"amber"], [5,"amber"], [10,"red"], [11.5,"red"]]
features = [[4, 0], [5, 0], [9, 1],[12, 1]]
# labels = ["beer","beer","wine","wine"]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[8, 1]]))
