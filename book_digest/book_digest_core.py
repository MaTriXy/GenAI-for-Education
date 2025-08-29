from langchain_core.output_parsers.pydantic import PydanticOutputParser 
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Optional, List
from langchain_openai import ChatOpenAI
import streamlit as st

def get_llm():
    """Get LLM instance with API key from Streamlit secrets"""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        return ChatOpenAI(
            model="moonshotai/kimi-k2-instruct",
            openai_api_base="https://api.groq.com/openai/v1",
            openai_api_key=api_key
        )
    except KeyError:
        st.error("GROQ_API_KEY not found in secrets. Please add it to your Streamlit secrets.")
        st.stop()

class KeyInsight(BaseModel):
    """Individual actionable insight from the book"""
    heading: str = Field(description="The main takeaway or insight title")
    bullet_points: List[str] = Field(
        description="2-3 bullet points explaining this insight in detail",
        min_items=2,
        max_items=3
    )
    application: Optional[str] = Field(
        default=None,
        description="How to apply this insight in practice"
    )

class BookSummary(BaseModel):
    """Structured summary of book insights for a specific role"""
    book_name: str = Field(description="The name of the book")
    role: str = Field(description="The role/profession this summary is tailored for")
    key_insights: List[KeyInsight] = Field(
        description="List of key insights from the book",
        min_items=3,
        max_items=5
    )
    key_theme: Optional[str] = Field(
        default=None,
        description="The overarching theme of the book"
    )

def generate_book_summary(book_name: str, role: str, num_insights: int) -> BookSummary:
    """Generate book summary using the LLM chain"""
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=BookSummary)
    
    book_learn_template = """Extract {num_insights} key insights from the book {book_name} that I can apply as a {role}.

{format_instructions}

Make sure each insight has a clear heading and 2-3 actionable bullet points."""

    book_learn_prompt = PromptTemplate(
        template=book_learn_template,
        input_variables=['num_insights', 'book_name', 'role'],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    # Create the chain with the parser
    book_chain = book_learn_prompt | llm | parser
    
    # Invoke the chain
    response = book_chain.invoke({
        "num_insights": num_insights,
        "book_name": book_name,
        "role": role
    })
    
    return response

# Example usage (for testing)
if __name__ == "__main__":
    response = generate_book_summary("Hyperfocus", "startup founder", 5)
    print(response)

## Sample Output 
#BookSummary(book_name='Hyperfocus', role='startup founder', key_insights=[KeyInsight(heading="Define Your Founder's Attention Charter", bullet_points=['List the 3-5 high-impact activities (product-market fit validation, fundraising, key hires) that deserve 80 % of your daily cognitive energy.', 'Explicitly write down everything else (email, social media, low-priority meetings) that you will deliberately ignore, delegate, or batch.'], application="Create a one-page 'Attention Charter' and revisit it every Monday morning to ensure your calendar and to-do list align with these priorities."), KeyInsight(heading='Run 90-Minute Hyperfocus Sprints', bullet_points=['Block 90-minute sessions for deep work on the most critical growth lever (e.g., building the next release, refining pitch deck).', "Eliminate external triggers: turn off Wi-Fi if possible, use full-screen mode, and set a visible 'do-not-disturb' signal."], application='Schedule two 90-minute sprints before noon every workday; treat them as investor meetings—non-negotiable and immovable.'), KeyInsight(heading='Install Mindless-Mode Triggers for Rapid Recharge', bullet_points=['Use mundane activities (walking between meetings, waiting in coffee lines) to enter scatterfocus and let the subconscious connect disparate ideas.', 'Keep a pocket notebook or voice-note app ready to capture startup insights that surface during these breaks.'], application="End each hyperfocus sprint with a 10-minute walk without your phone; use the time to ask yourself, 'What creative risk should I take next?'"), KeyInsight(heading='Build a Team-Wide Attention Contract', bullet_points=['Share your Attention Charter with co-founders and early hires; ask them to draft their own.', "Establish 'quiet hours' (e.g., 9-11 a.m.) where Slack and non-urgent messages are forbidden company-wide."], application="Add a bullet to your onboarding checklist: 'Read and sign the Attention Contract; schedule your first deep-work block within 48 hours.'"), KeyInsight(heading='Ritualize the Daily Shutdown to Prevent Burnout', bullet_points=["Set a hard stop each evening to review what moved the needle, capture tomorrow's top three tasks, and power down devices.", 'Perform a 60-second breathing exercise to signal the brain that work is complete, preserving long-term cognitive stamina.'], application="Use an automated calendar reminder titled 'Shutdown Ritual' at 6:30 p.m.; treat skipping it as seriously as missing a board meeting.")], key_theme='Directing and sustaining attention to maximize productivity and strategic impact')