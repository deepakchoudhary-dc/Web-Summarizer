# AI Web & Video Summarizer

A comprehensive Streamlit web application designed to summarize webpages and YouTube videos using advanced AI models. Built with LangChain framework and ChatOllama model, it provides an intuitive web interface for content summarization and translation.

## Requirements

[Ollama](https://ollama.com/) must be installed and running locally:

```bash
ollama run llama3:instruct
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Features

- **Web Page Summarization**: Summarize any website content from URLs
- **YouTube Video Summarization**: Extract and summarize YouTube video transcripts
- **Turkish Translation**: Translate summaries to Turkish language
- **Modern Web Interface**: Built with Streamlit for easy use
- **AI-Powered**: Uses LLaMA 3 model via Ollama for high-quality summaries
- **Download Support**: Download summaries and translations as markdown files

## Usage

### Streamlit Web Application (Recommended)

Launch the comprehensive web interface:

```bash
streamlit run streamlit_app.py
```

The web application will open in your browser with the following features:
- Automatic detection of web pages vs YouTube videos
- Real-time summarization with progress indicators
- Translation capabilities
- Download summaries as markdown files
- Example URLs for quick testing

### Command Line Interface (Legacy)

For command-line usage, you can still use the original scripts:

```bash
python summarizer.py -u "http://example.com/document"
```

### Legacy Gradio Interface

The original Gradio interface is still available:

```bash
python webui.py
```

## Docker

Build and run with Docker:

```bash
docker build -t ai-summarizer .
docker run -p 8501:8501 ai-summarizer

# Run if you have ollama running on host
docker run -d --network='host' -p 8501:8501 ai-summarizer
```

## Development

This project is open for contributions. To contribute:

1. Clone the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

### Roadmap

- [x] Web page summarization
- [x] YouTube video summarization  
- [x] Streamlit web interface
- [x] Turkish translation
- [ ] Multiple language translation support
- [ ] Streaming text output
- [ ] Summary quality scoring
- [ ] Batch processing
- [ ] API endpoints
- [ ] Cloud deployment options

## Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: LangChain
- **Language Model**: LLaMA 3 via Ollama
- **Web Scraping**: BeautifulSoup4
- **Video Processing**: YouTube Transcript API
- **Text Processing**: Tiktoken


