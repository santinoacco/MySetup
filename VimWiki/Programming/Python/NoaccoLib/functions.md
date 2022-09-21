# Functions and Methods in Python


```python3
def fill_with_nan(DataFrame,to_replace,from_col,to_col=None):
    if to_col == None: to_col = len(DataFrame.columns)
    for col in DataFrame.columns[from_col:to_col]:
        DataFrame.loc[:,col].replace(
            to_replace=to_replace,
            value=np.NaN,
            inplace=True
        )
```
