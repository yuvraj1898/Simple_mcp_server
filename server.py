"""
Info Server - A FastMCP service providing Wikipedia and Arxiv search functionality.
This script exposes tools to search Wikipedia and Arxiv research papers.
"""

from typing import Any

from mcp.server.fastmcp import FastMCP
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun



# Initialize FastMCP
mcp = FastMCP("info-server")

# Set up Wikipedia search
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Set up Arxiv search
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

@mcp.tool()
async def get_info(searchterm: str) -> str:
    """Get information from Wikipedia for the search term.

    Args:
        searchterm: The term to search for on Wikipedia

    Returns:
        Information about the search term from Wikipedia
    """
    try:
        print(f"Searching Wikipedia for: {searchterm}")
        result = wiki_tool.run(searchterm)
        return result or "No information found on Wikipedia for this search term."
    except Exception as e:
        print(f"Wikipedia search error: {str(e)}")
        return f"Error fetching Wikipedia information: {str(e)}"

@mcp.tool()
async def get_research_paper(searchterm: str) -> str:
    """Get research paper information from Arxiv.

    Args:
        searchterm: Title or paper ID to search for on Arxiv

    Returns:
        Information about the requested research paper
    """
    try:
        print(f"Searching Arxiv for: {searchterm}")
        result = arxiv_tool.run(searchterm)
        return result or "No research papers found on Arxiv for this search term."
    except Exception as e:
        print(f"Arxiv search error: {str(e)}")
        return f"Error fetching research paper information: {str(e)}"

if __name__ == "__main__":
    # Run the server
    print("Starting Info Server...")
    mcp.run(transport='stdio')