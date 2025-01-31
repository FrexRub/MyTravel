from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter(prefix="", tags=["Фронтенд"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Элегантная парикмахерская"}
    )


@router.get("/city", response_class=JSONResponse)
async def get_city(request: Request):
    url = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
    headers = {
        "X-RapidAPI-Key": site.api_key.get_secret_value(),
        "X-RapidAPI-Host": site.host_api
    }
    try:
        text_querystring = {"languagecode": "ru"}
        text_querystring["text"] = name_city

        response = requests.get(url, headers=headers, params=text_querystring)

        date = json.loads(response.text)
    return {"result": "ok"}
