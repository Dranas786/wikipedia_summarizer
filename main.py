from fastapi import FastAPI, HTTPException
from models import QueryRequest, QueryResponse
from scraper import fetch_wikipedia_article
from summarizer import summarize_content

app = FastAPI()

@app.post("/summarize", response_model=QueryResponse)
def summarize(request: QueryRequest):
    content, source = fetch_wikipedia_article(request.query)
    
    # if there are valid suggestions
    if not content and isinstance(source, list):
        raise HTTPException(
            status_code=400,
            detail=f"Ambiguous query. Did you mean one of: {', '.join(source[:5])}?"
        )
    # if there are also no suggestions
    elif not content:
        raise HTTPException(status_code=404, detail="Wikipedia page not found.")

    summary = summarize_content(content)
    return QueryResponse(query=request.query, summary=summary, source_url=source)

@app.get("/health")
def health():
    return {"status": "ok"}
