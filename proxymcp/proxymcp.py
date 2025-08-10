from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient

# Create a proxy with full MCP feature support

#proxy = FastMCP.as_proxy(
#    ProxyClient("backend_server.py"),
#    name="MyProxy"
#)

# Multi-server configuration
config = {
    "mcpServers": {
        "omada": {
            "url": "http://omadamcp:5200/mcp",
            "transport": "http"
        },
        "ubnt": {
            "url": "http://ubntmcp:4200/mcp",
            "transport": "http"
        }
    }
}

# Create a unified proxy to multiple servers
composite_proxy = FastMCP.as_proxy(config, name="Composite Proxy")

# Run the proxy (e.g., via stdio for Claude Desktop)
if __name__ == "__main__":
    #proxy.run()
    composite_proxy.run(transport="http", host="0.0.0.0", port=6200)