# Model Context Protocol (MCP) Currency Server

This is a simple MCP server built with Python and [UV](https://docs.uv.dev/) that provides two AI-callable tools for currency conversion:

- `convert_currency`: Converts an amount from one currency to another.
- `list_currencies`: Lists all supported currencies via the external [Currency API](https://currency.getgeoapi.com).

It is provided on _"as-is"_ basis for the tutorial: **Your First MCP: From Concept to Call**. 

---

## Quick Setup

Make sure you have [npx](https://docs.npmjs.com/cli/v9/commands/npx?v=true), Python 3.10+ and [UV](https://docs.uv.dev/) installed on your computer/laptop.

Then run:

```bash
# Create a new project directory
uv init mcp-server-currency
cd mcp-server-currency

# Create a virtual environment and activate it
uv venv
source .venv/bin/activate

# Install required dependencies
uv add "mcp[cli]" httpx python-dotenv
```

---

## Configuration

1. Get a free API key for [Currency API](https://currency.getgeoapi.com/register/)
2. Export the API key in your environment, run this in a terminal:

    ```bash
    export CURRENCY_API_KEY=your_api_key_here
    ```

## Download Code

- Download or  copy all the code from [this Github repo](https://github.com/manishh/gifts-giveaways/tree/master/python/mcp-server-currency) to your project directory: `mcp-server-currency`


## Run the Server

This server uses `stdio` as the transport mechanism, making it easy to integrate with local AI agents like Claude for Desktop.

To run the server, use:

```bash
 uv run currency.py
```

If al goes well, you'll see output like this in the terminal:

```bash
$ uv run currency.py
[07/21/25 15:29:32] INFO     Got the API key? True                                                                          
                    INFO     Running MCP Currency Server...            
```

## Integrating with Claude for Desktop:

Ensure you have [Claude Desktop](https://claude.ai/download) available on your computer/laptop. Use the following configuration for Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "currency": {
      "command": "/absolute-path-to-executable/uv",
      "args": [
	"--directory",
	"/absolute-path-to/mcp-server-currency",
        "run",       
        "currency.py"
      ],
      "env": {
	"CURRENCY_API_KEY": "<your-API-key>"
      }
    }
  }
}
```

> **Note:** You will be able to use locally running MCP server with Claude's free plan as well.

## Currency MCP Server In Action:

![Demo: Currency Conversion MCP Tool in action at Wimbledon](https://i.postimg.cc/xCxKHW39/wimbledon-currency-conversion.png)


---

**Author:** Manish Hatwalne

