import bentoml, transformers

model = "nijatzeynalov/mT5-based-azerbaijani-summarize"
task = "summarization"

bentoml.transformers.save_model(
    task,
    transformers.pipeline(task, model=model),
    metadata=dict(model_name=model),
)