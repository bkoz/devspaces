import gradio as gr
from transformers import AutoTokenizer
import transformers
import torch
import time

def greet(prompt):
    t0 = time.time()
    sequences = pipeline(
    prompt,
    do_sample=True,
    top_k=10,
    temperature=0.1,
    top_p=0.95,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
    )
    print(f'==> Time to inference = {time.time() - t0}')
    for seq in sequences:
        print(f"Result:\n")
        print(f"{seq['generated_text']}")

    return seq['generated_text']

model = "codellama/CodeLlama-7b-Python-hf"

t0 = time.time()
tokenizer = AutoTokenizer.from_pretrained(model)
print(f'==> Time to load tokenizer = {time.time() - t0}')

t0 = time.time()
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)
print(f'==> Time to load pipeline = {time.time() - t0}')

# Instantiate the Gradio Textbox class
textbox = gr.Textbox(label="Let's write some Python:", placeholder="Code goes here", lines=2)

gr.Interface(fn=greet, inputs=textbox, outputs="text",
    examples=["def fibonacci(n: int) -> int:", "def is_prime(n: int) -> Boolean"])\
    .launch()


