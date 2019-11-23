# infer-license

Heavily inspired by https://github.com/sol/infer-license/ this will provide an
API to guess what license a given file represents.

```
>>> from infer_license import guess_file
>>> print(guess_file("LICENSE"))
License(name='MIT License', shortname='MIT', trove_classifier='License :: OSI Approved :: MIT License')
>>> guess_file("setup.py")
None
```

There's also a handy `infer_license` script that takes a filename.

```
$ infer_license LICENSE
LICENSE: MIT
```


# License

infer-license is copyright [Tim Hatch](http://timhatch.com/), and licensed under
the MIT license.  I am providing code in this repository to you under an open
source license.  This is my personal repository; the license you receive to
my code is from me and not from my employer. See the `LICENSE` file for details.
