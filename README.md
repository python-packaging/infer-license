# Infer License

Heavily inspired by https://github.com/sol/infer-license/ this will provide an
API to guess what license a given file represents.

```
>>> from infer_license import guess_file
>>> print(guess_file("LICENSE"))
License(name='MIT License', shortname='MIT')
>>> guess_file("setup.py")
None
```

