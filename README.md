git_by_a_lion
=============

A visualizer for [tomheon/git_by_a_bus](https://github.com/tomheon/git_by_a_bus).

**Please Note:** git_by_a_lion uses git_by_a_bus V2!

# Dependencies

In order to run git_by_a_lion you must have [PyGal](http://pygal.org) installed.
The easiest way to do that is with pip, just use the following command.

```
pip install pygal
```


# Using

In order to use git_by_a_lion you need to be running git_by_a_bus-v2 which can
be found on [GitHub](https://github.com/tomheon/git_by_a_bus/tree/v2). After
running git_by_a_bus you will have a generated output directory with the rough
structure as follows.

```
.
├── files
│   ├── 1.html
│   ├── 1.json
│   ├── 2.html
│   ├── 2.json
│   ├── 3.html
│   ├── 3.json
│   ├── 4.html
│   ├── 4.json
│   ├── 5.html
│   ├── 5.json
│   ├── 6.html
│   ├── 6.json
│   ├── 7.html
│   ├── 7.json
│   ├── 8.html
│   ├── 8.json
│   ├── pygments.css
│   └── summary.json
└── summary.db

1 directory, 19 files
```

To generate some awesome pie charts that visualize your repo just run the
following command!

```
python gbal.py <path-to-summary.json>
```
