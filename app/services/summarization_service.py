import bentoml
from bentoml.io import Text
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("text_summarization_service")

# Create a Prometheus summary to track request durations

# Define the summarizer runner
summarizer_runner = bentoml.models.get("summarization:latest").to_runner()

# Create the BentoML service
svc = bentoml.Service(
    name="summarization_service", runners=[summarizer_runner]
)

# Start Prometheus server

@svc.api(input=Text(), output=Text())
async def summarize(text: str) -> str:
    logger.info("Received request to summarize text.")
    generated = await summarizer_runner.async_run(text, max_length=3000)
    summary = generated[0]["summary_text"]
    logger.info("Generated summary successfully.")
    return summary
