from transformers import pipeline

# Load the summarization pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_content(content: str) -> str:
    # Truncate input to 1024 tokens to fit model limit (approximate)
    max_input_length = 1024
    content = content[:max_input_length]

    try:
        summary_list = summarizer(
            content,
            max_length=300,   # max words/ tokens in summary (adjust as needed)
            min_length=30,
            do_sample=False
        )
        summary = summary_list[0]['summary_text']
        return summary.strip()
    except Exception as e:
        print(f"Exception in summarize_content: {e}")
        return "Failed to summarize content."
