from distutils.log import debug
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, id: str = "1"):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

if __name__ == '__main__':
    uvicorn.run(app)