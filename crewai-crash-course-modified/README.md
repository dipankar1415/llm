# CrewAI Crash Course

A comprehensive crash course tutorial for the CrewAI framework with practical examples and working scripts.

## 📚 Reference
- **Google Reference Article**: https://ai.google.dev/gemini-api/docs/crewai-example

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd crewai-crash-course
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Install all dependencies
   pip install -r requirements.txt
   
   # Or install individually
   pip install crewai[tools]>=0.157.0
   pip install google-generativeai>=0.8.0
   pip install python-dotenv>=1.0.0
   ```

4. **Set up environment variables**
   ```bash
   # Copy the sample environment file
   cp .sample_env .env
   
   # Edit .env file with your API keys
   GEMINI_API_KEY=your_gemini_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## 🔑 API Keys Setup

### Google Gemini API Key
1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key and add it to your `.env` file

### Serper API Key (Optional - for web search)
1. Visit: https://serper.dev/
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## 📁 Project Structure

```
crewai-crash-course/
├── 1_email_agent.ipynb          # Basic email agent
├── 2_email_agent_with_tool.ipynb # Email agent with tools
├── 3_crew.ipynb                 # Multi-agent crew
├── 4_crew_with_tools.ipynb      # Crew with tools
├── 5_yaml.py                    # YAML configuration
├── 6_memory.py                  # Memory system
├── 6_memory_fixed.py            # Fixed memory script
├── 6_memory_alternative_tools.py # Alternative tools version
├── main.py                      # Main entry point
├── requirements.txt              # Dependencies
├── config/                      # Configuration files
└── marketing-crew/              # Marketing crew example
```

## 🎯 Running Examples

### Basic Memory Script
```bash
python 6_memory_fixed.py
```

### Alternative Tools Version
```bash
python 6_memory_alternative_tools.py
```

### Jupyter Notebooks
```bash
jupyter notebook
# Then open any of the .ipynb files
```

## 🛠️ Troubleshooting

### Common Issues

1. **Google Generative AI Error**
   ```bash
   pip install google-generativeai>=0.8.0
   ```

2. **Serper API Issues**
   - The project includes alternative tools that work without Serper
   - Use `6_memory_fixed.py` or `6_memory_alternative_tools.py`

3. **Memory System Errors**
   - Ensure you have the latest version of crewai-tools
   - Check that your API keys are properly set in `.env`

## 📖 Learning Path

1. Start with `1_email_agent.ipynb` for basic concepts
2. Progress through the numbered notebooks
3. Try the memory examples in `6_memory_*.py` files
4. Explore the marketing-crew example for advanced usage

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is for educational purposes.