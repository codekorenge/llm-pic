import base64
import os
from typing import Optional

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import openai_service

app = FastAPI()
imgList = []
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# This is similar to index method for returning the intial form.
@app.get("/query", response_class=HTMLResponse)
def get_basic_form(request: Request):
    print("get")
    return templates.TemplateResponse(
        "form.html", {"request": request, "queryresponse": None}
    )


# This method processes the files, query and return result to the form.
@app.post("/query", response_class=HTMLResponse)
async def post_basic_form(
    request: Request,
    querytext: str = Form(...),
    file1: Optional[UploadFile] = None,
    file2: Optional[UploadFile] = None,
):
    print("post")
    print(f"Query: {querytext}")
    print(f"Filename: {file1.filename}")
    print(f"Filename: {file2.filename}")

    # if os.stat(file1.file).st_size != 0 and os.stat(file2.file).st_size != 0:
    if file1.filename != "" and file2.filename != "":
        print(f"Filename: {file1.filename}")
        print(f"Filename: {file2.filename}")
        return templates.TemplateResponse(
            "form.html",
            {"request": request, "queryresponse": "File uploaded!"},
        )

    print(f"To process query ...")
    response, has_image = openai_service.make_query_only(querytext)
    print(response)
    if has_image:
        # os.remove(response)
        print("Controller returns image ...")
        # imgList.append({"appImg": response})
        # print("imglist:", len(imgList))
        # return templates.TemplateResponse(
        #     "form.html",
        #     {
        #         "request": request,
        #         "myImage": response,
        #         "queryresponse": "Has-Image",
        #         "result": imgList,
        #     },
        # )
        return templates.TemplateResponse(
            "form.html", {"request": request, "myImage": response}
        )
    else:
        print("Controller returns no-image ...")
        return templates.TemplateResponse(
            "form.html", {"request": request, "queryresponse": response.to_string}
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
