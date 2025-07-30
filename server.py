import sys
import requests
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GlyCosmos MCP Server")

print("Starting MCP server...", file=sys.stderr)

class GlycanInfo(BaseModel):
    position: Optional[int] = Field(None, description="Position of the glycosylation site.")
    description: str = Field(..., description="Description of the glycosylation site.")
    pubmed_ids: List[str] = Field(..., description="List of PubMed IDs associated with the glycosylation site.")
    glytoucan_ids: List[Dict[str, str]] = Field(..., description="List of GlyToucan IDs and their masses.")
    source: List[Dict[str, str]] = Field(..., description="Source information for the glycosylation site.")

class get_sequon_and_glycanOutput(BaseModel):
    result: List[GlycanInfo] = Field(
        ...,
        description="List of glycosylation sites and their associated glycan information."
    ) 

@mcp.tool()
async def get_sequon_and_glycan(uniprot_id: str) -> get_sequon_and_glycanOutput:
    """
    Get the glycosylation site and glycan information for a given UniProt ID.

    Args:
        UniProt ID (str): The UniProt ID to query.
        Example: "Q9NR99"

    Returns:
        str: The JSON-formatted result of the request conforming to the GlycanInfo model.
        Example response:
```JSON
  {
    "position": 702,
    "description": "O-linked (Xyl...) (chondroitin sulfate) serine",
    "pubmed_ids": [
      "25326458",
      "32337544",
      "36213313"
    ],
    "glytoucan_ids": [
      {
        "gtc": "",
        "mass": "0.00"
      }
    ],
    "source": [
      {
        "label": "UniProt",
        "id": "https://www.uniprot.org/uniprot/Q9NR99#ptm_processing"
      },
      {
        "label": "GlyGen",
        "id": "https://glygen.org/protein/Q9NR99"
      }
    ]
  },
```
    """
    url = "https://api.glycosmos.org/sparqlist/Glycoprotein-glycosylation"
    params = { 'id': uniprot_id }
    headers = { 'Accept': 'application/json' }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return {"result": response.json()}

if __name__ == "__main__":
   mcp.run()