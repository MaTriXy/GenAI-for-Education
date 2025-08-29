import os
from educhain import Educhain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# custom_template = """
# दिए गए विषय और स्तर के आधार पर {num} बहुविकल्पीय प्रश्न (MCQ) उत्पन्न करें। प्रश्न, चार उत्तर विकल्प और सही उत्तर प्रदान करें।
# विषय: {topic}

# Generate questions in hindi.
# """

# gpt_4o_mini = ChatOpenAI(model= "gpt-4o-mini")


# ## Generate questions in Hindi
# client = Educhain()
# result = client.qna_engine.generate_questions(
#                                   topic="भारतीय भूगोल",
#                                   num=3,
#                                   llm = gpt_4o_mini,
#                                   prompt_template=custom_template
#                                   )

# result.show()
     

# custom_template = """
# ఇచ్చిన అంశం మరియు స్థాయిని బట్టి {num} బహుళ ఎంపిక ప్రశ్నలు (MCQ) రూపొందించండి. ప్రశ్న, నాలుగు సమాధాన ఎంపికలు మరియు సరైన సమాధానాన్ని అందించండి.
# అంశం: {topic}
# ప్రశ్నలను తెలుగులో రూపొందించండి.
# """

# result = client.qna_engine.generate_questions(
#                                   topic="భారతదేశ భౌగోళికం", 
#                                   num=3,
#                                   llm = gpt_4o_mini,
#                                   prompt_template=custom_template,
#                                   )

# result.show()

from educhain import Educhain, LLMConfig
from langchain_openai import ChatOpenAI

custom_template = """
ఇచ్చిన అంశం మరియు స్థాయిని బట్టి {num} బహుళ ఎంపిక ప్రశ్నలు (MCQ) రూపొందించండి. ప్రశ్న, నాలుగు సమాధాన ఎంపికలు మరియు సరైన సమాధానాన్ని అందించండి.
అంశం: {topic}
ప్రశ్నలను తెలుగులో రూపొందించండి.
"""

sutra = ChatOpenAI(
    model="sutra-v2",
    openai_api_key=os.getenv("SUTRA_API_KEY"),
    openai_api_base="https://api.two.ai/v2",
)

sutra_config = LLMConfig(custom_model=sutra)

client_sutra = Educhain(sutra_config)

result = client_sutra.qna_engine.generate_questions(
    topic="Indian Geography",
    num=5,
    prompt_template=custom_template
)

result.show()




