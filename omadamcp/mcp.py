from fastmcp import FastMCP
from sdn_tools.OmadaAPI import OmadaAPI

mcp = FastMCP(name="SDNAutomationServer")

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=5200,
        log_level="debug",
    )