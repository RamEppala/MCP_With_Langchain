from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    return "It's always rainy"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
