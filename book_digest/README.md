# 📖 Book Digest Generator

Generate actionable insights from books tailored to your specific role or profession using AI.

## Features

- **Personalized Insights**: Get book summaries tailored to your specific role (e.g., startup founder, teacher, manager)
- **Structured Output**: Receive 3-5 key insights with actionable bullet points
- **Interactive UI**: Easy-to-use Streamlit interface
- **Download Option**: Save your summaries as text files
- **Flexible Configuration**: Choose the number of insights you want

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.streamlit/secrets.toml` file in the book_digest directory:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

## Usage

1. **Enter Book Name**: Type the name of the book you want insights from
2. **Specify Your Role**: Enter your profession or perspective (e.g., "startup founder", "teacher", "product manager")
3. **Choose Number of Insights**: Select 3-5 key insights
4. **Generate**: Click the button to create your personalized summary
5. **Download**: Save the summary as a text file

## Files Structure

- `streamlit_app.py` - Main Streamlit application
- `book_digest_core.py` - Core logic and AI processing
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Example Output

For the book "Hyperfocus" tailored for a "startup founder":

```
📚 Hyperfocus
Tailored for: startup founder
Key Theme: Directing and sustaining attention to maximize productivity and strategic impact

1. Define Your Founder's Attention Charter
• List the 3-5 high-impact activities that deserve 80% of your daily cognitive energy
• Explicitly write down everything else that you will deliberately ignore or delegate
💡 Application: Create a one-page 'Attention Charter' and revisit it every Monday morning

2. Run 90-Minute Hyperfocus Sprints
• Block 90-minute sessions for deep work on critical growth levers
• Eliminate external triggers: turn off Wi-Fi, use full-screen mode
💡 Application: Schedule two 90-minute sprints before noon every workday
```

## Requirements

- Python 3.7+
- Streamlit
- LangChain
- Pydantic
- GROQ API access

## API Usage

The app uses the GROQ API with the Kimi-k2-instruct model for generating insights. Make sure you have a valid API key and sufficient credits.