# Round half away from zero. 

```
pip install round2
```

Since python's default round function uses 'bankers rounding', I made this small module that uses 'commercial rounding' instead. This means half is rounded up for positive numbers and down for negative numbers:

```python
>>> from round2 import round2
>>> round2(1.5)
2
>>> round2(2.5)
3
>>> round2(-1.5)
-2
>>> round2(-2.5)
-3
>>> round2(2.5, decimals=1)
2.5
```

If decimals=0 (default), returns an int, otherwise a float, just like Python’s round function.

Implemented in Cython with type hinting in Python.
