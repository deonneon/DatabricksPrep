import mlflow
import openai
import os

os.environ["OPENAI_API_KEY"] = ""
# you must set the OPENAI_API_KEY environment variable
assert (
    "OPENAI_API_KEY" in os.environ
), "Please set the OPENAI_API_KEY environment variable."

# set the experiment id
mlflow.set_experiment(experiment_id="3480141376382286")


import mlflow
import openai
import os

os.environ["OPENAI_API_KEY"] = "sssss"
# you must set the OPENAI_API_KEY environment variable
assert (
    "OPENAI_API_KEY" in os.environ
), "Please set the OPENAI_API_KEY environment variable."

# set the experiment id
mlflow.set_experiment(experiment_id="3480141376382286")

system_prompt = (
    "The following is a conversation with an AI assistant."
    + "The assistant is helpful and very friendly."
)

# start a run
mlflow.start_run()
mlflow.log_param("system_prompt", system_prompt)

# Create a question answering model using prompt engineering
# with OpenAI. Log the model to MLflow Tracking
logged_model = mlflow.openai.log_model(
    model="gpt-4o-mini",
    task=openai.ChatCompletion,
    artifact_path="model",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "{question}"},
    ],
)

# Evaluate the model on some example questions
questions = pd.DataFrame(
    {
        "question": [
            "How do you create a run with MLflow?",
            "How do you log a model with MLflow?",
            "What is the capital of France?",
        ]
    }
)
mlflow.evaluate(
    model=logged_model.model_uri,
    model_type="question-answering",
    data=questions,
)
mlflow.end_run()
