import os
import json
import logging
import sched

from dotenv import load_dotenv
from scrapingbee import ScrapingBeeClient

# for reading API key from `.env` file.
load_dotenv()

# helpful to have logs with timestamps for verification
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO)


# Refer: https://www.scrapingbee.com/documentation/
class MAPMonitor:
    api_key = os.getenv("SPB_API_KEY")  # ScrapingBee
    client = ScrapingBeeClient(api_key=api_key)
    # logging.debug(f"API KEY: {api_key}")

    def __init__(self, _price: int):
        """
        The constructor for MAPMonitor

        :param _price: The `min_price` aka Minimum Advertised Price (MAP) for monitoring
        """

        self.min_price = _price
        logging.info(f"Monitoring for MAP threshold: ${self.min_price}")

    def check_current_price(self, url: str):
        """
        Retrieves current price from given url and checks it against `min_price` (MAP)

        :param url: The website URL for scraping
        """
        if self.client and url:
            logging.info("Checking current price...")
            response = self.client.get(url, params={"wait": 100, "extract_rules": {"price": "#map1"}})
            # logging.debug(f"Resp: {response.content}")

            if response.ok:
                self._process_price(response.content.decode("utf-8"))
            else:
                logging.error(f"### Response Error - {response.status_code}: {response.content}")
        else:
            logging.error(f"### Invalid client: {self.client} or URL: {url} passed!")

    def _process_price(self, txt: str):
        """
        Processes response text for `min_price` and sends MAP alert if required

        :param txt: The text from the webpage response object
        """
        price_data = json.loads(txt)
        if price_data.get("price", "").isdigit():
            current_price = int(price_data.get("price"))
            if current_price < self.min_price:
                MAPMonitor._send_map_alert(current_price)
            else:
                # for testing only, this will be NO-OP, since price is above MAP
                logging.info(f"----->> Ignoring price above MAP: ${current_price}.")
        else:
            logging.error(f"### Invalid price-data format: {txt}")

    @staticmethod
    def _send_map_alert(current_price: int):
        """
        Sends notifications for the MAP (stub only)

        :param current_price: The retrieved current price from the web page
        """

        # send appropriate below-MAP alert via email/SMS etc.
        logging.warning(f"----->> ALERT: Current vendor price is *below* MAP: ${current_price}!")


# Sample output
"""
$ python min_adv_price_monitor.py
2023-08-14 17:33:04,523 INFO: Monitoring for MAP threshold: $60
2023-08-14 17:33:09,529 INFO: Checking current price...
2023-08-14 17:33:20,061 WARNING: ----->> ALERT: Current vendor price is *below* MAP: $53!
2023-08-14 17:34:09,528 INFO: Checking current price...
2023-08-14 17:34:23,254 INFO: ----->> Ignoring price above MAP: $64.
2023-08-14 17:34:23,258 INFO: Finished!
$ 
"""

if __name__ == '__main__':
    monitor_url = "https://reclusivecoder.com/spb-dummy/scraping-bee-map-demo.html"
    map_monitor = MAPMonitor(60)  # minimum price is $60

    # schedule 2 scraping calls 1-minute apart for MAP-Alert demo.
    # You may use Advanced Python Scheduler (apscheduler) for real-life scheduling
    sch = sched.scheduler()
    sch.enter(5, 1, map_monitor.check_current_price, argument=(monitor_url,))
    sch.enter(65, 1, map_monitor.check_current_price, argument=(monitor_url,))
    sch.run()  # blocking call
    logging.info("Finished!")
