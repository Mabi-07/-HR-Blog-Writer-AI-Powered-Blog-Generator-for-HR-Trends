# 🛠️ HR Blog Writer - Setup & Usage Instructions

## ✅ Setup Instructions

### 1. Clone or Download the Project
Unzip the folder `hr_blog_writer_module_ready` or clone from your version control system.

### 2. Install Dependencies
Make sure Python 3.8+ is installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install:
```bash
pip install requests python-dotenv
```

### 3. Set Up Environment Variables
Create a `.env` file in the root of your project folder with the following content:

```
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here
```

Replace the placeholder values with your actual API keys:
- [Hugging Face Token](https://huggingface.co/settings/tokens)
- [SERP API Key](https://serpapi.com/manage-api-key)

---

## ▶️ Usage Instructions

### 1. Run the Blog Writing Pipeline
From your project root, run:

```bash
python -m hr_blog_writer.main
```

This will:
- Get a trending HR topic
- Gather research content
- Generate an outline and full blog post
- Optimize it for SEO
- Proofread and polish it
- Save it as `output_blog.txt` in the root directory

You can modify the pipeline or agents in the `hr_blog_writer/agents` directory.

---

## 📂 Output File
Check the generated blog in:

```
output_blog.txt
```