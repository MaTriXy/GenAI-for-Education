from educhain import Educhain
from dotenv import load_dotenv
load_dotenv()

client = Educhain()

## Save OPENAI_API_KEY in .env

ques = client.qna_engine.generate_questions_from_data(
    source="[https://en.wikipedia.org/wiki/Big_Mac_Index",](https://en.wikipedia.org/wiki/Big_Mac_Index",) # Replace with your webpage URL
    source_type="url",
    num=5) # Specify the number of questions

print(ques)
ques.json() # or ques.dict() to get the output as a dictionary
