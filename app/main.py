import uvicorn
from fastapi import FastAPI
from .services import frontend
from bentoml import load
import logging

# Initialize the FastAPI app
app = FastAPI()

# Mount the frontend service
app.mount("/", frontend.app)

# Load and start the BentoML service
def start_bentoml_service():
    # Load the BentoML service from the build directory
    svc = load("service:latest")
    svc_runner = svc.to_runner()
    svc_runner.start()

    return svc_runner

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("text_summarization_project")

    logger.info("Starting BentoML service...")
    svc_runner = start_bentoml_service()
    logger.info("BentoML service started successfully.")

    logger.info("Starting FastAPI application...")
    uvicorn.run(app, host="0.0.0.0", port=8002)
    logger.info("FastAPI application started successfully.")
