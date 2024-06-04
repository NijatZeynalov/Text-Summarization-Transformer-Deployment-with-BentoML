from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>Text Summarization</title>
        </head>
        <body>
            <h1>Text Summarization</h1>
            <form action="/summarize" method="post">
                <textarea name="text" rows="10" cols="50"></textarea><br>
                <input type="submit" value="Summarize">
            </form>
        </body>
    </html>
    """

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    response = requests.post(
        "http://0.0.0.0:4000/summarize",
        headers={"accept": "text/plain", "Content-Type": "text/plain"},
        data=text
    )
    return {"summary": response.text}
