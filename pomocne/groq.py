import os
from groq import Groq
from dotenv import load_dotenv

# isto ko na vezbama
load_dotenv()

def configure_groq_client():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY") # cita iz .env fajla a ne iz sistem putanje
    if not GROQ_API_KEY:
        raise ValueError("Postavite environment varijablu GROQ_API_KEY.")

    groq_client = Groq(api_key=GROQ_API_KEY)
    print("Groq client configured")
    return groq_client

def generate_llm_answer(query, retrieved_text, groq_client=None, llm_model="openai/gpt-oss-120b"):
    context = "\n\n".join(retrieved_text)

    response = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Answer based on context provided."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
        ],
        model=llm_model,
        temperature=0.7,
        max_tokens=2048
    )
    return response.choices[0].message.content