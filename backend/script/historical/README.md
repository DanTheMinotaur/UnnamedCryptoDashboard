# historical.py

Script to scrape historical crypto data from `coinmarketcap.com` and store in an sqlite database.

Main purpose for this is to precollect and distribute data with the app.

Using this will result in a `429` http response, but it will calm down after a few minutes. 

```shell
python historical.py
```