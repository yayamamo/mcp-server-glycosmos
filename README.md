# An MCP Server to access GlyCosmos SPARQLet
- To setup this server please follow the instructions [here](https://github.com/modelcontextprotocol/python-sdk).
- To utilize this server from Claude Desktop please follow the instructions [here](https://modelcontextprotocol.io/quickstart/user)  
An example configuration for this server is as follows:
```
      "ask_glycosmos": {
        "command": "/Users/awsome_user/.local/bin/uv",
        "args": [
          "--directory",
          "/Users/awsome_user/git/mcp-server-glycosmos",
          "run",
          "server.py"
        ]
      }
```

