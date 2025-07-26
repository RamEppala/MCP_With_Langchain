from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    return a*b

#transport stdio tell the mcp server to use the standard input and output
#and respond to tool function calls
if __name__ == "__main__":
    mcp.run(transport="stdio")
