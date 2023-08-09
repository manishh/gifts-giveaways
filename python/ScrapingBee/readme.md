## Demo: Minimum Advertised Price (MAP) monitor with ScrapingBee

- Install the required libraries -
```
pip install -r requirements.txt
```

- Register on ScrapingBee website and copy the API Key.
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
2023-08-14 17:33:04,523 INFO: Monitoring for MAP threshold: $60
2023-08-14 17:33:09,529 INFO: Checking current price...
2023-08-14 17:33:20,061 WARNING: ----->> ALERT: Current vendor price is *below* MAP: $53!
2023-08-14 17:34:09,528 INFO: Checking current price...
2023-08-14 17:34:23,254 INFO: ----->> Ignoring price above MAP: $64.
2023-08-14 17:34:23,258 INFO: Finished!
$ 
```

