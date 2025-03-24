# HR Blog Writer

## 📌 System Architecture

The system is built as a **modular multi-agent architecture**, where each agent is responsible for a distinct part of the HR blog writing process:
- **Research Agent**: Gathers trending topics and supporting content.
- **Planner Agent**: Outlines the blog post structure.
- **Writer Agent**: Writes the initial draft using Hugging Face models.
- **SEO Agent**: Optimizes content for search engines.
- **Review Agent**: Proofreads and improves grammar/style.

## 🔁 Agent Workflow

1. **Research Agent** gets a trending HR topic.
2. **Planner Agent** generates a structured outline.
3. **Writer Agent** writes the draft using the outline and research.
4. **SEO Agent** refines the content for SEO.
5. **Review Agent** finalizes the article.

## 🧰 Tools and Frameworks Used

- **Python 3.9+**
- **Hugging Face Transformers API**
- **SERP API** for live topic/research data
- **Requests** for API communication
- **VS Code / Terminal** for local development

## 🛠️ Installation

1. Clone the repo or extract the project zip.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your API keys in `config.py`:
    ```python
    HUGGINGFACE_API_KEY = "your_huggingface_key"
    SERPAPI_API_KEY = "your_serpapi_key"
    ```

## 🚀 Usage

Run the pipeline from the project root:
```bash
python -m hr_blog_writer.main
```

The final blog post will be saved as `output_blog.txt`.

---