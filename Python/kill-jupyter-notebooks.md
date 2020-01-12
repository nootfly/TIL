# Kill jupyter notebooks

```sh
# get jupyter used port-number.
jupyter notebook list

# get PID, The PID is the second field.
lsof -n -i4TCP:[port-number]

# to kill this process.
kill -9 [PID]
```

## Reference

[https://github.com/jupyter/notebook/issues/2844#issuecomment-385882596](https://github.com/jupyter/notebook/issues/2844#issuecomment-385882596)
