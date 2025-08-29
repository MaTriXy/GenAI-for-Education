import streamlit as st
from book_digest_core import BookSummary, generate_book_summary

def display_book_summary(summary: BookSummary):
    """Display the book summary in a formatted way"""
    st.subheader(f"📚 {summary.book_name}")
    st.write(f"**Tailored for:** {summary.role}")
    
    if summary.key_theme:
        st.write(f"**Key Theme:** {summary.key_theme}")
    
    st.write("---")
    
    for i, insight in enumerate(summary.key_insights, 1):
        st.subheader(f"{i}. {insight.heading}")
        
        for bullet in insight.bullet_points:
            st.write(f"• {bullet}")
        
        if insight.application:
            st.write(f"**💡 Application:** {insight.application}")
        
        st.write("")

def main():
    st.title("📖 Book Digest Generator")
    st.write("Generate actionable insights from books tailored to your specific role!")
    
    # Sidebar for inputs
    with st.sidebar:
        st.header("Configuration")
        book_name = st.text_input("Book Name", value="Hyperfocus", help="Enter the name of the book you want insights from")
        role = st.text_input("Your Role", value="startup founder", help="Enter your profession or role")
        num_insights = st.slider("Number of Insights", min_value=3, max_value=5, value=5, help="How many key insights do you want?")
    
    # Main content area
    if st.button("Generate Book Insights", type="primary"):
        if not book_name or not role:
            st.error("Please enter both book name and your role.")
            return
        
        with st.spinner("Generating insights... This may take a moment."):
            try:
                summary = generate_book_summary(book_name, role, num_insights)
                display_book_summary(summary)
                
                # Download option
                summary_text = f"Book Summary: {summary.book_name}\n"
                summary_text += f"Role: {summary.role}\n"
                if summary.key_theme:
                    summary_text += f"Key Theme: {summary.key_theme}\n"
                summary_text += "\n"
                
                for i, insight in enumerate(summary.key_insights, 1):
                    summary_text += f"{i}. {insight.heading}\n"
                    for bullet in insight.bullet_points:
                        summary_text += f"   • {bullet}\n"
                    if insight.application:
                        summary_text += f"   Application: {insight.application}\n"
                    summary_text += "\n"
                
                st.download_button(
                    label="📄 Download Summary",
                    data=summary_text,
                    file_name=f"{book_name}_{role}_summary.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    
    # Instructions
    with st.expander("ℹ️ How to use"):
        st.write("""
        1. **Enter Book Name**: Type the name of the book you want insights from
        2. **Specify Your Role**: Enter your profession, role, or perspective (e.g., "startup founder", "teacher", "manager")
        3. **Choose Number of Insights**: Select how many key insights you want (3-5)
        4. **Generate**: Click the button to generate your personalized book summary
        5. **Download**: Save your summary as a text file for future reference
        
        The app will extract actionable insights specifically tailored to your role!
        """)

if __name__ == "__main__":
    main()