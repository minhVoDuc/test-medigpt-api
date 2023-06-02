import gpt4free
from gpt4free import Provider

def get_response(prompt):
    reponse = gpt4free.Completion.create(Provider.You, prompt=prompt)
    return reponse