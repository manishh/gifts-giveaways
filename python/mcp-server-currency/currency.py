import os
from typing import Any
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import logging


# Read API key from environment
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("currency")

# Constants
CURRENCY_API_BASE = "https://api.getgeoapi.com"
API_KEY = os.getenv("CURRENCY_API_KEY")
logging.info(f"Got the API key? {API_KEY != ''}")  # for debugging

async def _send_api_request(url: str) -> dict[str, Any] | None:
    """Make a request to the Currency API with proper error handling."""   

    headers = {
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as ex:
            logging.exception(ex)
            return None
        
def _format_conversion(rates: dict, to_currency: str) -> str:
    """Format currency conversion into a readable string."""
    return f"""
Converted Amount: {rates.get('rate_for_amount', 'Unknown')}
Latest {rates.get('currency_name', to_currency)} Rate: {rates.get('rate', 'Unknown')}    
"""
        
@mcp.tool()
async def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts the given amount from one currency to another.

    Args:
        amount: Amount to be converted.
        from_currency: Three letter currency code (e.g. USD, INR, GBP, EUR)
        to_currency: Three letter currency code (e.g. USD, INR, GBP, EUR)

    Returns:
        str: Converted amount with currency rate.
    """
    
    api_endpoint = f"{CURRENCY_API_BASE}/v2/currency/convert?api_key={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}&format=json"
    data = await _send_api_request(api_endpoint)

    if not data or "rates" not in data or not data["rates"]:
        return "Unable to perform currency conversion at this time."

    # get relevant data for the converted currency
    conversion_data = data.get("rates", {}).get(to_currency, {})
    return _format_conversion(conversion_data, to_currency)

@mcp.tool()
async def list_currencies() -> dict[str, str] | str:
    """Lists all the currencies available for conversion.
    
    Returns:
        dict: List of all available currencies.
    """
    
    api_endpoint = f"{CURRENCY_API_BASE}/v2/currency/list?api_key={API_KEY}&format=json"
    data = await _send_api_request(api_endpoint)

    if not data or "currencies" not in data or not data["currencies"]:
        return "Unable to list available currencies at this time."

    available_currencies = data.get("currencies", {})
    return  available_currencies


if __name__ == "__main__":
    # Initialize and run the server
    logging.info("Running MCP Currency Server...")
    mcp.run(transport='stdio')
