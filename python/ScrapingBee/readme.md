## Demo: Minimum Advertised Price (MAP) monitor with ScrapingBee

- Install the required libraries -
```
pip install -r requirements.txt
```

- Register on ScrapingBee website and add the API Key.
> [https://app.scrapingbee.com/account/register](https://app.scrapingbee.com/account/register)

- Rename `env.example` file as `.env` and paste the API key there.

- Run the python script -
```
python min_adv_price_monitor.py
```
- Modify the Python script as required. :)

---

### Sample Output

```
$ python min_adv_price_monitor.py
2023-08-14 10:00:03,941 INFO: Monitoring for MAP threshold: $100
2023-08-14 10:00:08,942 INFO: Checking current price...
2023-08-14 10:01:08,968 INFO: Checking current price...
2023-08-14 10:01:25,006 WARNING: ----->> ALERT: Current retailer price is *below* MAP: $91!
2023-08-14 10:01:25,010 INFO: Finished!
$
```

