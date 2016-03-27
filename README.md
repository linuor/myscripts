# myscripts
User scripts for easy use

Add the location of this repo to the PATH enviroment. So you should use them
more easily.

# generate.py

Use to generate a set of files. Usually include sub-directory.

Usage:
```
usage: generate.py [-h] [-t Template] [-a Author] [-d Date] [-v Version]
                   Destination

Generate files from jinja template.

positional arguments:
  Destination           Specify the location directory, also the name of the
                        destination.

optional arguments:
  -h, --help            show this help message and exit
  -t Template, --template Template
                        Specify the source template used for generation, also
                        the name of the sub-directory under the template
                        directory.
  -a Author, --author Author
                        Specify the author name.
  -d Date, --date Date  Specify the date.
  -v Version, --version Version
                        Specify the version.
```

# render.py

Use to render a set of files. Always change the files' name.

Usage:
```
usage: render.py [-h] [-t Template] [-n Namespace] [-a Author] [-d Date]
                 [-v Version]
                 Destination

Render files from jinja template.

positional arguments:
  Destination           Specify the location directory, also the name of the
                        destination.

optional arguments:
  -h, --help            show this help message and exit
  -t Template, --template Template
                        Specify the source template used to render, also the
                        name of the sub-directory under the template
                        directory.
  -n Namespace, --namespace Namespace
                        Specify the namespace for files to render.
  -a Author, --author Author
                        Specify the author name.
  -d Date, --date Date  Specify the date.
  -v Version, --version Version
                        Specify the version.
```
