<div align="center">

# 🤖 AI Web & Video Summarizer

*Transform any web content into intelligent summaries with AI*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)](https://ollama.ai)

Transform lengthy articles, research papers, and YouTube videos into concise summaries using Qwen3 1.7B AI model.

</div>

## ✨ Features

- � **Web Page Summarization** - Any website content
- 🎥 **YouTube Video Analysis** - Automatic transcript extraction
- � **Turkish Translation** - Translate summaries instantly
- 📱 **Modern Web Interface** - Clean Streamlit UI
- 📥 **Export Support** - Download as markdown files

## 🚀 Quick Start

### Prerequisites
```bash
# Install Ollama
ollama pull qwen3:1.7b
ollama run qwen3:1.7b
```

### Installation
```bash
# Clone and setup
git clone https://github.com/deepakchoudhary-dc/Web-Summarizer.git
cd Web-Summarizer
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

### Test Setup
```bash
python test_setup.py  # Verify everything works
```

## 🎮 Usage

1. **Open** http://localhost:8501 in your browser
2. **Paste** any website URL or YouTube video link
3. **Click** "Generate Summary" 
4. **Translate** to Turkish (optional)
5. **Download** results as markdown

## 🛠️ Available Interfaces

| Interface | Command | Description |
|-----------|---------|-------------|
| **Streamlit** (Primary) | `streamlit run streamlit_app.py` | Modern web interface |
| **Gradio** (Legacy) | `python webui.py` | Alternative web UI |
| **CLI** (Legacy) | `python summarizer.py -u "URL"` | Command line |

## 🐳 Docker

```bash
# Quick deploy
docker build -t ai-summarizer .
docker run -p 8501:8501 ai-summarizer
```

## � Project Structure

```
Web-Summarizer/
├── streamlit_app.py      # Main Streamlit app
├── summarizer.py         # Web page processing
├── yt_summarizer.py      # YouTube processing  
├── translator.py         # Translation features
├── config.py             # Configuration
├── test_setup.py         # Setup verification
└── requirements.txt      # Dependencies
```

## � Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Qwen3 1.7B via Ollama
- **Framework**: LangChain
- **Web Scraping**: BeautifulSoup4
- **Video Processing**: YouTube Transcript API

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Test changes: `python test_setup.py`
4. Submit pull request

## � License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Made with ❤️ using AI**

[⬆️ Back to Top](#-ai-web--video-summarizer)

</div>
