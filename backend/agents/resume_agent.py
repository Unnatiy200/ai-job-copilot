from langchain_core.prompts import ChatPromptTemplate
from .llm import llm
import json
import re

prompt = ChatPromptTemplate.from_template("""
You are an expert resume analyzer.
Analyze this resume and return JSON with:
- name
- email
- skills (list)
- education (list)
- experience (list)
- strengths (list)
- weaknesses (list)
- ats_score (0-100)
- ats_suggestions (list)

Resume:
{resume_text}

Return only valid JSON. No extra text.
""")

chain = prompt | llm

def analyze_resume(resume_text: str) -> dict:
    response = chain.invoke({"resume_text": resume_text})
    text = response.content
    # Remove markdown code blocks if present
    text = re.sub(r'```json|```', '', text).strip()
    return json.loads(text)