# MicroLesson Generator

A Streamlit web application that generates bite-sized learning content with interactive questions using the Educhain library and AI models.

## Features

- **Interactive Input Controls**: Select topic, concept, and customize question types
- **Multiple Question Types**: 
  - Multiple Choice Questions (MCQ)
  - True/False Questions
  - Fill in the Blank
  - Matching Questions
  - Ordering/Sequencing Questions
- **Rich Content**: Pre-read sections, detailed explanations, summaries, and tags
- **Mobile-First Design**: Content optimized for quick consumption
- **Export Functionality**: Download generated content as text file

## Setup

### Prerequisites

1. Python 3.8+ installed
2. Required packages (install via pip):
   ```bash
   pip install streamlit langchain educhain python-dotenv langchain-openai
   ```

### API Configuration

You need to set up an API key using Streamlit's secrets management:

1. **Create the secrets file:**
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

2. **Edit `.streamlit/secrets.toml` and add your API key:**

   **Option 1: OpenRouter API (recommended)**
   ```toml
   OPENROUTER_API_KEY = "your_openrouter_key_here"
   ```

   **Option 2: Cerebras API**
   ```toml
   CEREBRAS_API_KEY = "your_cerebras_key_here"
   ```

3. **Add to .gitignore (important for security):**
   ```bash
   echo ".streamlit/secrets.toml" >> .gitignore
   ```

**Note:** You only need ONE API key from either provider.

## Running the Application

1. Navigate to the micro_lessons directory:
   ```bash
   cd micro_lessons
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

3. Open your browser to the provided URL (usually `http://localhost:8501`)

## How to Use

### 1. Configure Your Content
In the sidebar, enter:
- **Topic**: The main subject area (e.g., "Psychology", "Technology")
- **Concept**: The specific concept to learn (e.g., "The Zeigarnik Effect")
- **Concept Description**: A brief description or teaser

### 2. Customize Questions
Set the number of questions for each type:
- **Multiple Choice**: Traditional 4-option questions
- **True/False**: Single statement to evaluate
- **Fill in the Blank**: Complete the sentence
- **Matching**: Match terms to definitions
- **Ordering**: Arrange items in correct sequence

### 3. Generate Content
Click "🚀 Generate MicroLesson" to create your personalized learning content.

### 4. Review and Export
- Review the generated pre-read, questions, and summary
- Download the content as a text file for offline use

## Content Structure

Each generated MicroLesson includes:

1. **Pre-Read** (250-350 words): Engaging introduction with real-world examples
2. **Interactive Questions**: Various question types with detailed explanations
3. **Key Takeaways**: 3-5 concise bullet points summarizing main concepts
4. **Tags**: Relevant keywords for content discovery

## Example Topics and Concepts

- **Psychology**: Growth Mindset, Cognitive Biases, The Zeigarnik Effect
- **Technology**: Machine Learning, Blockchain, API Design
- **Science**: Quantum Physics, Climate Change, DNA Structure
- **Business**: Customer Acquisition, Market Research, Leadership

## Troubleshooting

### API Configuration Issues
**Problem**: "No API key found" error
- **Solution**: Create `.streamlit/secrets.toml` and add your API key
- **Check**: Ensure the file path is correct: `micro_lessons/.streamlit/secrets.toml`
- **Verify**: Restart the Streamlit app after adding your key

**Problem**: "API-related error"
- **Solution**: Check that your API key has sufficient credits/permissions
- **Check**: Verify the API service status (OpenRouter/Cerebras)
- **Try**: Switch to a different API provider if one is down

### Content Generation Errors
**Problem**: "Validation error" or empty response
- **Cause**: LLM didn't return properly formatted content
- **Solution**: Try again in a moment (sometimes LLM responses vary)
- **Check**: Ensure your API key is valid and has credits

**Problem**: Connection timeouts
- **Solution**: Check your internet connection
- **Try**: Use shorter concept descriptions for faster processing
- **Check**: Verify the API service isn't experiencing outages

### Testing Your Setup
Before using the full app, run the test script:
```bash
python3 test_app.py
```
This will verify that all components work without requiring an API key.

### Performance Tips
- Start with fewer questions (2-3 total) for faster generation
- Use concise concept descriptions (1-2 sentences)
- Experiment with different question type combinations
- If one API is slow, try switching to the other provider

## File Structure

```
micro_lessons/
├── microlesson.py          # Core MicroLesson generation logic
├── streamlit_app.py        # Streamlit web application
└── README.md              # This file
```

## Technical Details

- **Framework**: Streamlit for web interface
- **AI Engine**: Educhain library with OpenRouter/Cerebras APIs
- **Models**: Qwen-3-235b for content generation
- **Response Format**: Structured Pydantic models for consistent output

## Contributing

Feel free to extend the application with:
- Additional question types
- Enhanced UI components
- Export formats (PDF, JSON)
- Content templates for specific domains