# CoinMarketCap Python Wrapper

[![Run Status][3]][4]
[![Coverage Badge][5]][4]
[![PyPI version][b]][c]
[![License][9]][a]

Overview
---
A Python wrapper for the [https://coinmarketcap.com/]() [api][1] that provides concise 
functionality for extracting crypto-market data. 

[a]: http://www.wtfpl.net/
[1]: https://coinmarketcap.com/api/
[c]: https://badge.fury.io/py/coinwrap
[b]: https://badge.fury.io/py/coinwrap.svg 
[7]: https://github.com/bitforce/Coinwatch
[2]: https://github.com/mrsmn/coinmarketcap-api
[4]: https://app.shippable.com/github/bitforce/Coinwrap
[9]: https://img.shields.io/badge/license-WTFPL-blue.svg
[8]: https://img.shields.io/badge/Issues-0-brightgreen.svg
[3]: https://api.shippable.com/projects/59a83c3685d3e007008b9d10/badge?branch=master
[5]: https://api.shippable.com/projects/59a83c3685d3e007008b9d10/coverageBadge?branch=master

Dependencies
---
- python `requests`
- python `pytest`

Setup
---
`pip install coinwrap` _or_ `python setup.py install`

Usage
---
```
from coinwrap import Market
market = Market()
market.coin('bitcoin')
market.coin('bitcoin', limit=2)
market.coin('bitcoin', limit=2, convert='EUR')
market.stats()
```

Test
---
```
python -m coinwrap.test.test_core
pytest [-s]
```

Note
---
The _-s_ option for `pytest` prints the output along with the test results. The `-m` 
option and following line format is necessary for Python to interpret the files as 
modules/packages and then run them as scripts. The distinction here stemming from 
the use of relative imports (as can be seen in the coinwrap/\_\_init\_\_.py and 
coinwrap/test/test\_core.py files).

_The test only applies if you are within the_ __coinwrap__ _directory that_ `pip` 
_installs source distributions in_.


_To see a useful implementation of this project, check out_ [Coinwatch][7].

_This project was inspired by Martin Simon's_ [coinmarketcap-api][2]

License
---
Licensed under the WTFPL - see [LICENSE](./LICENSE) for explicit details.

Version
---
1.0.0

Author
---
[LinkedIn](https://www.linkedin.com/in/brandonjohnsonxyz/)
[Personal](https://brandonjohnson.life)
[GitHub](https://github.com/bitforce)
