# 🤖 AI Web & Video Summarizer

A comprehensive web application that uses artificial intelligence to summarize web pages and YouTube videos. Built with Streamlit, LangChain, and powered by LLaMA 3 through Ollama.

## ✨ Features

- **🌐 Web Page Summarization**: Analyze and summarize content from any website
- **🎥 YouTube Video Summarization**: Extract and summarize YouTube video transcripts
- **🌍 Translation Support**: Translate summaries to Turkish (more languages coming soon)
- **📱 Modern Web Interface**: Clean, responsive Streamlit interface
- **⚡ Real-time Processing**: Live progress indicators and status updates
- **📥 Download Support**: Save summaries and translations as markdown files
- **🔄 Automatic Detection**: Automatically detects content type (web page vs YouTube video)
- **📚 Example URLs**: Built-in examples for quick testing

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**: Download and install from [ollama.com](https://ollama.com/)
2. **Download LLaMA 3 Model**:
   ```bash
   ollama pull llama3:instruct
   ```
3. **Start Ollama**:
   ```bash
   ollama run llama3:instruct
   ```

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-web-video-summarizer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run streamlit_app.py
   ```

   Or use the startup script on Windows:
   ```bash
   start_app.bat
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 🖥️ Usage

### Web Interface (Recommended)

1. **Enter a URL**: Paste any website URL or YouTube video URL
2. **Generate Summary**: Click "Generate Summary" to analyze the content
3. **Translate (Optional)**: Click "Translate" to convert summary to Turkish
4. **Download**: Save your summaries and translations as markdown files

### Available Interfaces

- **Streamlit App** (Primary): `streamlit run streamlit_app.py`
- **Gradio Interface** (Legacy): `python webui.py`
- **Command Line** (Legacy): `python summarizer.py -u "URL"`

## 📁 Project Structure

```
ai-web-video-summarizer/
├── streamlit_app.py          # Main Streamlit application
├── summarizer.py             # Web page summarization logic
├── yt_summarizer.py          # YouTube video summarization
├── translator.py             # Translation functionality
├── webui.py                  # Legacy Gradio interface
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── start_app.bat            # Windows startup script
├── README.md                # This file
├── assets/
│   ├── Dockerfile           # Docker configuration
│   ├── README.md            # Original documentation
│   └── requirements.txt     # Legacy requirements
└── finance_tracker/        # Separate finance tracking project
```

## 🐳 Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker build -t ai-summarizer .

# Run the container
docker run -p 8501:8501 ai-summarizer

# If Ollama is running on host machine
docker run -d --network='host' -p 8501:8501 ai-summarizer
```

### Docker Compose (Coming Soon)

A docker-compose.yml file will be added to manage both the application and Ollama service together.

## ⚙️ Configuration

Edit `config.py` to customize:

- **Ollama Settings**: Base URL and model name
- **Text Processing**: Chunk size and overlap for long documents
- **Languages**: Add support for additional translation languages
- **Server Settings**: Port and host configuration

## 🛠️ Development

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Adding New Features

- **New Translation Languages**: Update `config.py` and modify translation prompts
- **Different AI Models**: Update Ollama model configuration
- **New Content Types**: Extend URL detection and processing logic
- **Enhanced UI**: Modify Streamlit components and styling

## 📋 Roadmap

- [x] Web page summarization
- [x] YouTube video summarization
- [x] Streamlit web interface
- [x] Turkish translation
- [x] Docker support
- [x] Download functionality
- [ ] Multiple language translation
- [ ] Batch processing
- [ ] API endpoints
- [ ] Summary quality scoring
- [ ] Content type detection improvements
- [ ] Cloud deployment guides
- [ ] Mobile-responsive design
- [ ] User authentication
- [ ] Summary history
- [ ] Custom AI model integration

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: LangChain
- **Language Model**: LLaMA 3 (via Ollama)
- **Web Scraping**: BeautifulSoup4
- **Video Processing**: YouTube Transcript API
- **Text Processing**: Tiktoken
- **Containerization**: Docker

## 📝 Requirements

- Python 3.9+
- Ollama with LLaMA 3 model
- 4GB+ RAM (for LLaMA 3)
- Internet connection (for content fetching)

## 🤝 Support

If you encounter any issues:

1. Check that Ollama is running: `ollama list`
2. Verify LLaMA 3 is installed: `ollama run llama3:instruct`
3. Check Python dependencies: `pip install -r requirements.txt`
4. Review the console output for error messages

## 📄 License

This project is open source and available under the MIT License.

## 🔄 Updates

- **v2.0.0**: Complete Streamlit rewrite with enhanced UI
- **v1.5.0**: Added Turkish translation support
- **v1.0.0**: Initial release with Gradio interface

---

**Note**: This project requires a local installation of Ollama and the LLaMA 3 model. Make sure both are properly set up before running the application.
