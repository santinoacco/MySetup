# ROOT notes

## ROOT in python

- create a tree like:
    - m_tree=ROOT.TTree('name','name')
- add brances, notice de syntax:
    - var = array.array('var_type',[0])                 # the [0] is the 1st elem
    - m_tree.Branch('branch_name',var,'leaf_name/var_type')
- Fill the Tree, example:
    - ```python
    -   for i in range(10):
        - var[0]=var_type(i)
        - m_tree.Fill()
    -``` 
- pyROOT objects accept array.array and numpy.array types, but not python.lists
