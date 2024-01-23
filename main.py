from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from jinja_partials import register_starlette_extensions, render_partial

app = FastAPI()

templates = Jinja2Templates(directory="templates")

register_starlette_extensions(templates)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get('/chat_message')
async def chat_message(request: Request):
    return render_partial(
        'partials/chat_message.html', role='assistant', message='Test'
    )