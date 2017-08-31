# CoinMarketCap Python Wrapper

Overview
---
A Python wrapper for [www.coinmarketcap.com]() that provides concise functionality for 
extracting crypto market data. This software is meant to be used in conjunction with a 
larger, more complicated project involving the extraction of the sites data.

[coinmarketcap-api]('https://github.com/mrsmn/coinmarketcap-api')


[1]: 

Setup
---
```
pip install wrapper-py-coinmarketcap
```
_or_
```
python setup.py install
```

Usage
---
You have a few option for using the wrapper:

1. Run Python shell and enter:

    ```
    >>> from wrapper-py-coinmarketcap import Market
    >>> market = Market()
    >>> market.coin('ethereum')
    >>> market.stats()
    ```

2. You can apply the code above to a py-file you're writing an work with that.
3. You can copy&paste and/or run `test.py` from the git repo.

Note
---
This alone is not a project, but more a library of functions that one can apply. PyPi 
installation is most preferred.

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
