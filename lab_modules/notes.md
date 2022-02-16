
## Challenge 1
1. Create `python_packages` in my usr's home directory 
2. Copy `jokes` directory into `python_packages` 
3. Modify terminal initialization by add these lines to the file below

#### `.zshrc`
```
PYTHONPATH="/Users/craigmckeachie/python_packages:$PYTHONPATH"
export PYTHONPATH

```
4. Restart the terminal or source the `.zshrc` file.

```
source ~/.zshrc
```

5. Check $PYTHONPATH by running `mypath.py` or the script below

```
python3 -c 'import sys; print(sys.path)'
```
6. Verify this directory `/Users/craigmckeachie/python_packages` is now in the Python Path.

## Reference
- [Setting PYTHONPATH](
https://stackoverflow.com/a/3387737/48175
)