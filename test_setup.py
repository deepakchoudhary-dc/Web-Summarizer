#!/usr/bin/env python3
"""
Test script for AI Web & Video Summarizer
This script tests the basic functionality of the summarization components
"""

import sys
import requests
from langchain_community.chat_models import ChatOllama

def test_ollama_connection():    """Test if Ollama is running and accessible"""
    print("🔍 Testing Ollama connection...")
    try:
        llm = ChatOllama(model="qwen3:1.7b", base_url="http://127.0.0.1:11434")
        response = llm.invoke("Hello, this is a test.")
        print("✅ Ollama connection successful!")
        return True
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        print("💡 Make sure Ollama is running: ollama run qwen3:1.7b")
        return False

def test_web_access():
    """Test if we can access web content"""
    print("\n🌐 Testing web access...")
    try:
        response = requests.get("https://httpbin.org/json", timeout=10)
        if response.status_code == 200:
            print("✅ Web access successful!")
            return True
        else:
            print(f"❌ Web access failed with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Web access failed: {e}")
        return False

def test_imports():
    """Test if all required packages can be imported"""
    print("\n📦 Testing package imports...")
    required_packages = [
        "streamlit",
        "langchain",
        "langchain_community",
        "beautifulsoup4",
        "youtube_transcript_api",
        "tiktoken"
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            if package == "beautifulsoup4":
                import bs4
            elif package == "youtube_transcript_api":
                import youtube_transcript_api
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("💡 Install missing packages: pip install -r requirements.txt")
        return False
    else:
        print("✅ All packages imported successfully!")
        return True

def run_full_test():
    """Run all tests"""
    print("🚀 Running AI Web & Video Summarizer Tests\n")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_web_access,
        test_ollama_connection
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("🚀 Run the app with: streamlit run streamlit_app.py")
        return True
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        return False

if __name__ == "__main__":
    success = run_full_test()
    sys.exit(0 if success else 1)
