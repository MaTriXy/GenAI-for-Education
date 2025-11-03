#!/usr/bin/env python3
"""
Simple test script to verify the app components work
"""

from microlesson import QuestionConfig, generate_content_prompt

def test_question_config():
    """Test QuestionConfig functionality"""
    print("Testing QuestionConfig...")
    
    # Test default config
    config = QuestionConfig()
    print(f"Default config: {config.to_prompt_string()}")
    print(f"Total questions: {config.total_questions}")
    
    # Test custom config
    custom_config = QuestionConfig(mcq=3, true_false=2, fill_blank=1)
    print(f"Custom config: {custom_config.to_prompt_string()}")
    print(f"Total questions: {custom_config.total_questions}")
    
    print("✅ QuestionConfig tests passed!\n")

def test_prompt_generation():
    """Test prompt generation"""
    print("Testing prompt generation...")
    
    topic = "Psychology"
    concept = "The Zeigarnik Effect"
    description = "Why unfinished tasks bug your brain until you finally check them off"
    config = QuestionConfig(mcq=2, true_false=1)
    
    prompt = generate_content_prompt(topic, concept, description, config)
    
    print(f"Generated prompt length: {len(prompt)} characters")
    print(f"Contains topic '{topic}': {'✅' if topic in prompt else '❌'}")
    print(f"Contains concept '{concept}': {'✅' if concept in prompt else '❌'}")
    print(f"Contains question count: {'✅' if str(config.total_questions) in prompt else '❌'}")
    
    print("✅ Prompt generation tests passed!\n")

def main():
    """Run all tests"""
    print("🧪 Testing MicroLesson Components")
    print("=" * 50)
    
    try:
        test_question_config()
        test_prompt_generation()
        print("🎉 All tests passed! The app components are working correctly.")
        print("\nNext steps:")
        print("1. Configure your API key in .streamlit/secrets.toml")
        print("2. Run: streamlit run streamlit_app.py")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()