# ai.py
from algo.initialize import*
from algo.apps import Discord

class Wazingai:
    try
        genai.configure(api_key=GOOGLE_API_KEY)
        
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                p(m.name)
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
    except Exception as e:
        p(e)
        
    def __init__(ai):
        pass
        
    async def to_markdown(ai, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    async def chat(ai, text):
        prompt = 'You: I am waiting for a question.\n {}'.format(text)
        try:
            r = ai.model.generate_content(prompt, safety_settings={'SEXUALLY_EXPLICIT':'block_none','HARASSMENT':'block_none','HATE_SPEECH':'block_none','DANGEROUS_CONTENT':'block_none'})
            if r:
                return r.text.replace("*", "")
            else:
                return r.candidates
        except Exception as e:
            p(e)
            await Discord().logger(f'Application log: {e}')
            return e
    
if __name__ == "__main__":
    m = Wazingai()
    content = 'what is the meaning of life'
    data = a.run(m.chat(content))
    p(data)


