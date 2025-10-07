# Capillary DocBot: Efficient Documentation Q&A Chatbot 💬

## Project Overview

This project implements an efficient Question-Answering (Q&A) chatbot using CapillaryTech's public documentation. The goal is to provide fast, accurate responses to user queries by leveraging a pre-scraped knowledge base.

The solution is divided into two parts:
1.  **Documentation Scraping:** A script to fetch and structure data from specified URLs.
2.  **Chatbot Application:** A Gradio interface that uses an optimized, whole-word search algorithm against the scraped data to deliver relevant answers with source citations.

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Scraping** | Python, `requests`, `BeautifulSoup4` | To fetch HTML content and parse it into a structured JSON knowledge base. |
| **Chatbot Interface** | Python, `Gradio` | To create a simple, browser-based, interactive user interface (UI). |
| **Search Engine** | Python, `re` (Regular Expressions) | For high-accuracy, whole-word keyword matching. |

---

## 🚀 Setup and Installation

Follow these steps to set up and run the Capillary DocBot locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_LINK]
    cd [repository-name]
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You may need to create a `requirements.txt` file containing: `gradio`, `requests`, `beautifulsoup4`.)*

### Running the Application

1.  **Scrape/Prepare Data (If `capillary_docs.json` is missing or outdated):**
    ```bash
    python scrape_docs.py
    ```
    This generates the `capillary_docs.json` file used as the chatbot's knowledge base.

2.  **Launch the Chatbot:**
    ```bash
    python capillary_chatbot.py
    ```
    The application will launch and provide a local URL (e.g., `http://127.0.0.1:7860`). Open this link in your web browser.

---

## 💡 Design & Efficiency Rationale

### 1. Efficient Retrieval
* **Methodology:** The chatbot operates entirely on an **in-memory JSON knowledge base** (`capillary_docs.json`), eliminating the need for slow external API calls or database lookups during query time. This design makes the chatbot highly efficient and delivers near-instantaneous responses.

### 2. High Accuracy Search
* **Implementation:** The search function utilizes **Python's `re` module** (Regular Expressions) to perform **whole-word matching** against the documentation lines.
* **Benefit:** By enforcing word boundaries (`\b`), the search dramatically reduces false positives, ensuring that only highly relevant documentation lines are returned for the user's query.

### 3. User-Friendly Output
* **Gradio & Markdown:** The output is formatted using Markdown, which renders the relevant documentation line in **bold** and provides the original **source URL as a clickable link** for verification, boosting user trust and response clarity.

---

