from langchain.llms import GPT4All

# Use a small local model
llm = GPT4All(model="gpt4all-lora-quantized.bin")  # put your model path here


def british_to_american(text):
    prompt = f"Translate this British English text to American English:\n\n{text}"
    return llm(prompt)


brit_text = "I fancy a cup of tea and a biscuit."
us_text = british_to_american(brit_text)
print(us_text)
from langchain.llms import GPT4All

# Use a small local model
llm = GPT4All(model="gpt4all-lora-quantized.bin")  # put your model path here


def british_to_american(text):
    prompt = f"Translate this British English text to American English:\n\n{text}"
    return llm(prompt)


brit_text = "I fancy a cup of tea and a biscuit."
us_text = british_to_american(brit_text)
print(us_text)
