# SVM

aims at solving **classification** problems by finding good 'decision boundaries' between two sets of points belonging to two different categories.

decision boundaries: line or surface separating your training data into two spaces corresponding to two categories

SVMs proceed to find these boundaries in two steps:

* First, the data is mapped to a new high-dimensional representation where the decision boundary can be expressed as an hyperplane.

* Then a good decision boundary (a separation hyperplane) is computed by trying to maximize the distance between the hyperplane and the closest data points from each class, a step called "maximizing the margin".
This allows the boundary to generalize well
to new samples outside of the training dataset.

For finding a good descision hyperplane in the new representation space,
you don't have to explicityly compute the coordinates of your points in the new space,
you just need to compute the **distance** between pairs of points intat space,
which can be done very efficiently using what is called a **'kernel function'**.








