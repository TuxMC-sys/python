import json
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

website_list = json.load(open("websiteRedirectList.json", "r"))
app = FastAPI()

@app.get("/{websiteToRedirect}", response_class=RedirectResponse)
async def root(websiteToRedirect):
    return website_list[websiteToRedirect]