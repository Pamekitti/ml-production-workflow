import json
import requests

SERVICE_URL = "http://localhost:3000/summarize"

message = 'A large language model (LLM) is a computerized language model, embodied by an artificial neural network using an enormous amount of "parameters" (i.e. "neurons" in its layers with up to tens of millions to billions "weights" between them), that are (pre-)trained on many GPUs in relatively short time due to massive parallel processing of vast amounts of unlabeled texts containing up to trillions of tokens (i.e. parts of words) provided by corpora such as Wikipedia Corpus and Common Crawl, using self-supervised learning or semi-supervised learning, resulting in a tokenized vocabulary with a probability distribution. LLMs can be upgraded by using additional GPUs to (pre-)train the model with even more parameters on even vaster amounts of unlabeled texts.'

response = requests.post(
        SERVICE_URL,
        data=json.dumps(message),
        headers={"content-type": "application/json"}
    )

print(response.text)
