the = {
    'dump': False,
    'go': None,
    'seed': 937162211,
    "file": "../../etc/data/auto93.csv",
    "Far": 0.95,
    "min": 0.5,
    "p": 2,
    "Sample": 512
}
egs = {}
help = '''USAGE: python main.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../etc/data/auto93.csv
  -F  --Far     distance to "faraway"  = .95
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -m  --min     stop clusters at N^min = .5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512
    '''

egs = {}

Seed = 937162211

n = 0