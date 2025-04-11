import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="g.a000uwgVWl5p39EMpKQrBHVm5y0MoYEgh1gsBmJWPTkKnPavC5JwJ2CA8f0h8ALrOtNFih0naQACgYKAcISARESFQHGX2MiY1O3Kyb1NgfNXFQZwW6T5RoVAUF8yKr8I4Eu021NHHLGwvjQBgIB0076")

model = genai.GenerativeModel("gemini-pro")

def generate_quiz(topic, num_questions=5):
    prompt = f"""
    Create a {num_questions}-question multiple-choice quiz on the topic: "{topic}".
    Each question must have 1 correct answer and 3 wrong options.
    Format like this:
    
    Q1: Question text?
    A. Option 1  
    B. Option 2  
    C. Option 3  
    D. Option 4  
    Answer: B

    Let's begin.
    """

    response = model.generate_content(prompt)
    return response.text