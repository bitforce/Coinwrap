# CoinMarketCap Python Wrapper

[![Run Status][3]][4]
[![Coverage Badge][5]][6]

Overview
---
A Python wrapper for the [https://coinmarketcap.com/]() [api][1] that provides concise 
functionality for extracting crypto-market data. 

_This project was inspired by Martin Simon's_ [coinmarketcap-api][2] _; make sure to 
hit his Gitub up and check out other cool projects_.

[1]: https://coinmarketcap.com/api/
[2]: https://github.com/mrsmn/coinmarketcap-api
[4]: https://app.shippable.com/github/bitforce/wrapper-py-coinmarketcap
[6]: https://app.shippable.com/github/bitforce/wrapper-py-coinmarketcap
[3]: https://api.shippable.com/projects/59a83c3685d3e007008b9d10/badge?branch=master
[5]: https://api.shippable.com/projects/59a83c3685d3e007008b9d10/coverageBadge?branch=master

Dependencies
---
- python `requests`
- python `pytest`

Setup
---
`pip install cmcwrap` _or_ `python setup.py install`

Usage
---
```
from cmcwrap import Market
market = Market()
market.coin('bitcoin')
market.coin('bitcoin', limit=2)
market.coin('bitcoin', limit=2, convert='EUR')
market.stats()
```

Test
---
`pytest [-s]`

Note
---
If you do decide to pull the git repo (download it), you type the latter setup command in 
the top-level dir where the _setup.py_ file is. The _-s_ option for `pytest` prints the 
output along with the test results.

License
---
Licensed under the WTFPL - see [LICENSE](./doc/LICENSE) for explicit details.

Version
---
1.0.0

Author
---
[LinkedIn](https://www.linkedin.com/in/brandonjohnsonxyz/)
[Personal](https://brandonjohnson.life)
[GitHub](https://github.com/bitforce)
