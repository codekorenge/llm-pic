import base64
import os
from typing import Optional

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import openai_service

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# This is similar to index method for returning the intial form.
@app.get("/query", response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse(
        "form.html", {"request": request, "queryresponse": None}
    )


# This method processes the files, query and return result to the form.
@app.post("/query", response_class=HTMLResponse)
async def post_basic_form(
    request: Request,
    querytext: str = Form(...),
    file: Optional[UploadFile] = None,
):
    print(f"Query: {querytext}")
    print(f"Filename: {file.filename}")

    if not file or not querytext:
        return templates.TemplateResponse(
            "form.html",
            {"request": request, "queryresponse": "No file or query present!"},
        )

    contents = await file.read()
    response, has_image = openai_service.make_query(contents, querytext)
    print(response)

    if has_image:
        # os.remove(response)
        print("Controller returns image ...")
        return templates.TemplateResponse(
            "form.html",
            {
                "request": request,
                "myImage": response,
                "queryresponse": "Has-Image",
            },
        )
    else:
        print("Controller returns no-image ...")
        return templates.TemplateResponse(
            "form.html", {"request": request, "queryresponse": response}
        )


"""
NOTE: Original code for reference.
"""
# @app.post("/query", response_class=HTMLResponse)
# async def post_basic_form(
#     request: Request,
#     querytext: str = Form(...),
#     file: UploadFile = File(...),
# ):
#     print(f"Query: {querytext}")
#     print(f"Filename: {file.filename}")

#     if file is not none

#     contents = await file.read()

#     response = openai_service.create_chatgpt_request(contents, querytext)

#     if os.path.isfile(response):
#         f = open(response, mode="rb")
#         # Reading file data with read() method
#         data = f.read()
#         base64_encoded_image = base64.b64encode(data).decode("utf-8")
#         return templates.TemplateResponse(
#             "form.html", {"request": request, "myImage": base64_encoded_image}
#         )
#     else:
#         return templates.TemplateResponse(
#             "form.html", {"request": request, "queryresponse": response}
#         )

#     print(response)
