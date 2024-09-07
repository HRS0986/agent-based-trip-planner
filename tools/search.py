import json
import os
from langchain.tools import tool
import requests


class SearchTool:
    @tool("Search the internet")
    def search(query: str):
        """
        Useful to search the internet about any given topic and return relevant results.
        """
        result_limit = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ.get("SERPER_API_KEY"),
            "Content-Type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        if "organic" not in response.json():
            return "No results found."
        else:
            results = response.json()["organic"]
            string = []
            for result in results[:result_limit]:
                try:
                    string.append(
                        "\n".join(
                            [
                                f"{result['title']}", f"{result['link']}", f"{result['snippet']}", "\n\n"
                            ]
                        )
                    )
                except KeyError:
                    next
            
            return "\n".join(string)
