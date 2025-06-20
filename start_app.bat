@echo off
echo Starting AI Web & Video Summarizer...
echo.
echo Make sure Ollama is running with:
echo ollama run llama3:instruct
echo.
pause
echo.
echo Starting Streamlit application...
streamlit run streamlit_app.py
