import json
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

website_list = json.load(open("websiteRedirectList.json", "r"))
print(website_list['0'])
app = FastAPI()

@app.get("/{websiteToRedirect}", response_class=RedirectResponse)
async def root(websiteToRedirect):
    print(websiteToRedirect)
    return website_list[websiteToRedirect]