import requests
from bs4 import BeautifulSoup
import json

# List of Capillary documentation URLs
urls = [
    "https://docs.capillarytech.com/docs/introduction",
    "https://docs.capillarytech.com/reference/apioverview",
    "https://docs.capillarytech.com/docs/sdks",
    "https://docs.capillarytech.com/docs/dev-console",
    "https://docs.capillarytech.com/docs/vulcan"
]

all_docs = []

# Scrape each page
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content_blocks = [tag.get_text(" ", strip=True) for tag in soup.find_all(['h1','h2','h3','p','li','code']) if tag.get_text(strip=True)]
    all_docs.append({"url": url, "content": "\n".join(content_blocks)})

# Add admin & customer activity logs manually
all_docs.append({
    "url": "admin_logs",
    "content": (
        "Session Logs allow tracking admin user actions. "
        "Access from Member Care -> Session History. Shows date, time, user, reason for changes.\n"
        "Entity Audit Logs API provides programmatic access to admin changes. "
        "Fields include updatedBy, userContextDetails, createdOn, events array."
    )
})

all_docs.append({
    "url": "customer_logs",
    "content": (
        "Customer activities can be tracked via Member Care Overview, Behavioral Events, "
        "Customer Activity History API (GET /v2/partnerProgram/customerActivityHistory), "
        "Subscription Status Change Log (GET /v2/customers/{userid}/subscriptionStatusChangelog), "
        "Customer Data Audit Logs."
    )
})

# Save all scraped + structured content to JSON
with open("capillary_docs.json", "w", encoding="utf-8") as f:
    json.dump(all_docs, f, ensure_ascii=False, indent=2)

print("✅ Scraping complete. Saved to capillary_docs.json")
