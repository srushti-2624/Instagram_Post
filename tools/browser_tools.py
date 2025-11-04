import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from langchain_community.llms import Ollama

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(website: str):
        """Scrape and summarize website content."""
        url = f"https://chrome.browserless.io/content?token={os.environ.get('BROWSERLESS_API_KEY')}"
        payload = json.dumps({"url": website})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        
        response = requests.post(url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])

        chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        summaries = []

        for chunk in chunks:
            agent = Agent(
                role='Principal Researcher',
                goal='Summarize and extract insights.',
                backstory="Research expert summarizing web content.",
                llm=Ollama(model=os.environ.get('MODEL')),
                allow_delegation=False
            )
            task = Task(
                agent=agent,
                description=f"Summarize this content:\n{chunk}"
            )
            summaries.append(task.execute())

        return "\n\n".join(summaries)

    @tool("Search the web")
    def web_search(query: str):
        """Search the web via browserless."""
        url = f"https://chrome.browserless.io/function?token={os.environ.get('BROWSERLESS_API_KEY')}"
        payload = json.dumps({
"code": f"async ({{ page, context }}) => {{"

                    f"await page.goto('https://www.google.com/search?q={query}');"
                    f"return await page.content(); }}"
        })
        headers = {'content-type': 'application/json'}

        response = requests.post(url, data=payload, headers=headers)
        return response.text[:2000]
