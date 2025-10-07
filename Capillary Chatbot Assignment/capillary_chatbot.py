import json
import gradio as gr
import re

# Load scraped documentation
with open("capillary_docs.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

def chatbot_response(query):
    query = query.lower()
    results = []
    
    # 1. Prepare search terms for whole-word matching (Mising in your snippet)
    # Escapes special characters and adds word boundaries (\b)
    search_terms = [r"\b" + re.escape(word) + r"\b" for word in query.split() if word] 
    
    # If the query is empty or only whitespace, return an empty result
    if not search_terms:
        return "Please enter a question to search the documentation."

    for doc in docs:
        for line in doc["content"].split("\n"):
            line_lower = line.lower()
            
            # 2. Use re.search for whole-word matching
            if any(re.search(term, line_lower) for term in search_terms): 
                # Format the line as a bold list item with a markdown hyperlink for the source.
                results.append(f"• **{line.strip()}**\n[Source: {doc['url']}]({doc['url']})") 

    if results:
        # Return the top 10 results joined by two newlines
        return "\n\n".join(results[:10])
    else:
        return f"Sorry, I couldn't find relevant information for '{query}' in the Capillary documentation."


# Modify the Gradio Interface setup:
demo = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="markdown", # This enables Markdown formatting in the output
    title="Capillary DocBot",
    description="Ask questions about Capillary SDKs, Dev Console, Vulcan, APIs, and user/admin activity logs.",
    examples=[
        ["How do I view admin session logs?"],
        ["What is the Entity Audit Logs API?"],
        ["Get customer activity history"],
        ["How to track subscription status changes?"],
        ["How to integrate Capillary SDK?"],
        ["What is Vulcan?"]
    ]
)

demo.launch()