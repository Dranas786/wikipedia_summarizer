# Wikipedia Summarizer API

A FastAPI service that scrapes and summarizes Wikipedia articles using Hugging Face models.

---

## Quick Start (with Docker)

```bash
# 1. Clone the repository
git clone https://github.com/{username}/webscraper_summary.git
cd webscraper_summary

# 2. Build the Docker image
docker build -t webscraper-summary .

# 3. Run the container (takes a minute to run, open summary-api container logs to see when the server launches)
docker run -d -p 8000:8000 --name summary-api webscraper-summary

# 4. Open Swagger UI in browser
http://localhost:8000/docs

# Using Swagger UI
Navigate to the Swagger UI
Find the POST /summarize endpoint.
Click Try it out.
Enter the JSON payload shown below or any thing you want to test.
{
  "query": "Give me the history of Agentic AI"
}
Click Execute.
View the summarized response in the output section.
```

# Design Notes: How Wikipedia Results Are Chosen (scraper.py)

I experimented with using Hugging Face NLP models to semantically rank Wikipedia pages by embedding queries and comparing them with page titles or descriptions. Although this added an AI-driven layer beyond keyword matching, the accuracy improvements were minimal and inconsistent. I also tried emphasizing the end of queries (e.g., focusing on “Agentic AI” in “history of Agentic AI”), but this had little effect.

Additionally, I attempted to leverage Wikipedia sections to combine them with the query for more precise summarization. However, the section-based approach did not work reliably.

Ultimately, I decided to keep it simple by relying on Wikipedia’s built-in keyword search and prompting users to clarify ambiguous queries. This method is faster, less complex, and effective for most structured topics.
