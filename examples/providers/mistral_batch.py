import os

from bespokelabs import curator

# To visualize the dataset on Curator viewer, you can set CURATOR_VIEWER=1 environment variable, or set it here:
# os.environ["CURATOR_VIEWER"]="1"


llm = curator.LLM(model_name="mistral-tiny", batch=True)
questions = [
    "What is the capital of Montana?",
    "Who wrote the novel 'Pride and Prejudice'?",
    "What is the largest planet in our solar system?",
    "In what year did World War II end?",
    "What is the chemical symbol for gold?",
]
ds = llm(questions)

# Check the first response
print(ds[0])
