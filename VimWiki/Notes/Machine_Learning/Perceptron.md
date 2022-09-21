# The Perceptron algorithm

``` python

"""no-offset perceptron algo"""
# start with a null vector
# so init param:
theta = 0

# define linear classifier error as

cls_err = y*(theta*x) <= 0

# train over a range of times T
for t in range(T):
    # loop over training set
    for i in len(train_set):

        # update param according to error result
        cls_err = y[i]*(theta*x[i])
        if cls_err <= 0:
            # this is the rule to update the param
            theta += y[i]*x[i]
```

if there exist a linear classifier,
then the training error computed using the given classifier must be 0.

Note that this algo works because each iteration improves the previous one,
in terms of the error condition.


## Sklearn

```python
from sklearn.linear_model import Perceptron
```
