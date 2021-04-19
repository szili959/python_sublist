# Wellcome to the the **List Analysis** task

You will get a list containing characters and digits.

You need to write a function in Python 3, which **identifies the longest sublist that contains the same amount of characters and digits**.
Return a tuple with the start and end indicies. Return (0, 0) if this sublist would be empty.

The function should be like:

```python
def identifySublist(digitCharList):
    ### your implementation
    return (startIndex, endIndexInclusive)
```

**Example input:** [9, 'd', 'c', 4, 1, 2, 'b', 0, 2, 3]

**Expected output:** (1, 6) because the biggest sublist is ['d', 'c', 4, 1, 2, 'b'] (which contains 3 characters and 3 digits).

**Bonus task:** Can you write a function which runtime complexity is better than O(N^2)?
