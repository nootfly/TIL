# Using Python unittest in IPython or Jupyter

To solve this issue, use the code below:

```python
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

Reference:

[Using Python unittest in IPython or Jupyter](https://medium.com/@vladbezden/using-python-unittest-in-ipython-or-jupyter-732448724e31)