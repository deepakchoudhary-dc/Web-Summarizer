import streamlit as st
import re
from langchain.chains.llm import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import TokenTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader

# Page configuration
st.set_page_config(
    page_title="AI Web & Video Summarizer",
    page_icon="📄",
    layout="wide"
)

@st.cache_resource
def get_llm():
    """Initialize and cache the LLM model"""
    return ChatOllama(model="qwen3:1.7b", base_url="http://127.0.0.1:11434")

def check_youtube_link(link):
    """Check if the link is a valid YouTube video link"""
    yt_regex = r"^(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]+)(?:\?.*)?$"
    return re.match(yt_regex, link) is not None

def load_web_document(url):
    """Load document from web URL"""
    try:
        loader = WebBaseLoader(url)
        return loader.load()
    except Exception as e:
        st.error(f"Error loading web document: {str(e)}")
        return None

def get_youtube_transcript(video_link):
    """Get transcript from YouTube video"""
    try:
        loader = YoutubeLoader.from_youtube_url(video_link, language=["en", "en-US"])
        transcript = loader.load()
        return transcript
    except Exception as e:
        st.error(f"Error getting YouTube transcript: {str(e)}")
        return None

def split_text_chunks(transcript):
    """Split transcript into manageable chunks"""
    splitter = TokenTextSplitter(
        chunk_size=7500, 
        chunk_overlap=100
    )
    chunks = splitter.split_documents(transcript)
    return chunks

def setup_web_summarization_chain():
    """Setup the web summarization chain"""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer, create a detailed and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
        
        1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity.
        2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.
        3. Rely strictly on the provided text, without including external information.
        4. Format the summary in paragraph form for easy understanding.
        5. Optimize output as markdown format.

        "{text}"

        DETAILED SUMMARY:""",
        input_variables=["text"],
    )
    
    llm = get_llm()
    return LLMChain(llm=llm, prompt=prompt_template)

def setup_youtube_summarization_chain():
    """Setup the YouTube video summarization chain"""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer specialized in video content, create a detailed and comprehensive summary of the YouTube video transcript provided. While crafting your summary, adhere to these guidelines:
        
        1. Capture the essence of the video, focusing on main ideas and key details. Ensure the summary is in-depth and insightful, reflecting any narrative or instructional elements present in the video.
        2. Exclude any redundant expressions and non-critical details to enhance the clarity and conciseness of the summary.
        3. Base the summary strictly on the transcript provided, avoiding assumptions or additions from external sources.
        4. Present the summary in a well-structured paragraph form, making it easy to read and understand.

        "{text}"

        DETAILED SUMMARY:""",
        input_variables=["text"],
    )
    
    llm = get_llm()
    return load_summarize_chain(llm=llm, prompt=prompt_template, verbose=False)

def setup_translation_chain():
    """Setup the translation chain"""
    prompt_template = PromptTemplate(
        template="""As a professional translator, provide a detailed and comprehensive translation of the provided text into Turkish, ensuring that the translation is accurate, coherent, and faithful to the original text.

        "{text}"

        DETAILED TRANSLATION:""",
        input_variables=["text"],
    )
    
    llm = get_llm()
    return LLMChain(llm=llm, prompt=prompt_template)

def summarize_content(url):
    """Main function to summarize content based on URL type"""
    if check_youtube_link(url):
        # YouTube video summarization
        with st.spinner("Extracting YouTube transcript..."):
            transcript = get_youtube_transcript(url)
            if transcript is None:
                return None
        
        with st.spinner("Processing video content..."):
            chunks = split_text_chunks(transcript)
            sum_chain = setup_youtube_summarization_chain()
            result = sum_chain.run(chunks)
            return result
    else:
        # Web document summarization
        with st.spinner("Loading web document..."):
            docs = load_web_document(url)
            if docs is None:
                return None
        
        with st.spinner("Generating summary..."):
            llm_chain = setup_web_summarization_chain()
            result = llm_chain.run(docs)
            return result

def translate_text(text):
    """Translate text to Turkish"""
    with st.spinner("Translating to Turkish..."):
        llm_chain = setup_translation_chain()
        result = llm_chain.run(text)
        return result

# Main Streamlit App
def main():
    st.title("🤖 AI Web & Video Summarizer")
    st.markdown("Easily summarize any web page or YouTube video with AI-powered analysis")
      # Sidebar
    with st.sidebar:
        st.header("📋 Instructions")
        st.markdown("""
        1. **Web Pages**: Enter any website URL
        2. **YouTube Videos**: Enter YouTube video URL
        3. **Translation**: Use the translate button for Turkish translation
        """)
        
        st.header("🔧 Requirements")
        st.markdown("""
        - Ollama must be running locally
        - Qwen3 1.7B model must be available
        
        ```bash
        ollama run qwen3:1.7b
        ```
        """)
        
        st.header("✨ Features")
        st.markdown("""
        - Web page summarization
        - YouTube video summarization
        - Turkish translation
        - Markdown formatted output
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # URL input
        url = st.text_input(
            "Enter URL (Web page or YouTube video)",
            placeholder="https://example.com or https://youtube.com/watch?v=...",
            help="Paste any web page URL or YouTube video URL"
        )
        
        # Example URLs
        with st.expander("📌 Example URLs"):
            example_urls = [
                "https://en.wikipedia.org/wiki/Artificial_intelligence",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "https://techcrunch.com/",
                "https://www.bbc.com/news"
            ]
            
            for example_url in example_urls:
                if st.button(f"📎 {example_url}", key=example_url):
                    st.session_state.example_url = example_url
            
            if 'example_url' in st.session_state:
                url = st.session_state.example_url
    
    with col2:
        st.info("💡 **Tip**: The app automatically detects if your URL is a YouTube video or web page!")
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
            if url:
                summary = summarize_content(url)
                if summary:
                    st.session_state.summary = summary
                    st.session_state.url_type = "YouTube Video" if check_youtube_link(url) else "Web Page"
                    st.success(f"✅ {st.session_state.url_type} summarized successfully!")
            else:
                st.warning("⚠️ Please enter a URL first!")
    
    with col2:
        if st.button("🇹🇷 Translate", use_container_width=True):
            if 'summary' in st.session_state:
                translation = translate_text(st.session_state.summary)
                if translation:
                    st.session_state.translation = translation
                    st.success("✅ Translation completed!")
            else:
                st.warning("⚠️ Please generate a summary first!")
    
    # Display results
    if 'summary' in st.session_state:
        st.header(f"📄 Summary ({st.session_state.url_type})")
        st.markdown(st.session_state.summary)
        
        # Download button for summary
        st.download_button(
            label="📥 Download Summary",
            data=st.session_state.summary,
            file_name=f"summary_{st.session_state.url_type.lower().replace(' ', '_')}.md",
            mime="text/markdown"
        )
    
    if 'translation' in st.session_state:
        st.header("🇹🇷 Turkish Translation")
        st.markdown(st.session_state.translation)
        
        # Download button for translation
        st.download_button(
            label="📥 Download Translation",
            data=st.session_state.translation,
            file_name="translation_turkish.md",
            mime="text/markdown"
        )
    
    # Clear results
    if st.button("🗑️ Clear Results"):
        for key in ['summary', 'translation', 'url_type', 'example_url']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

if __name__ == "__main__":
    main()
