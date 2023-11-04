"""
source: https://docs.bentoml.com/en/latest/quickstarts/deploy-a-transformer-model-with-bentoml.html
"""

import bentoml
from bentoml.io import Text

summarizer_runner = bentoml.models.get("summarization:latest").to_runner()

summarizer_service = bentoml.Service(
    name="summarization", runners=[summarizer_runner]
)

@summarizer_service.api(input=Text(), output=Text())
async def summarize(text: str) -> str:
    generated = await summarizer_runner.async_run(text, max_length=3000)
    return generated[0]["summary_text"]
