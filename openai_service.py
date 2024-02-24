import base64
import os
from io import StringIO
from typing import Optional

import pandas as pd
from pandasai import Agent
from pandasai.llm import AzureOpenAI

# The purpose of this method is for uploading files and query regading the file data to OpenAI through PandasAI.
# Therefore, at least one file and query must present.


# two files, 2 question, one related to image, another related scalar.
def make_query(buffer: bytes, query: str):
    llm = AzureOpenAI(
        # api_token=<insert-key>
        azure_endpoint="https://genai-lsr.openai.azure.com/",
        api_version="2023-08-01-preview",
        deployment_name="gpt-turbo-4k",
        api_base="https://genai-lsr.openai.azure.com/",
    )

    df = create_dataframe(buffer)
    # If array of df, put them inside [] with commas.
    agent = Agent([df], config={"llm": llm}, memory_size=10)

    response = agent.chat(query)

    print(response)

    # try:
    #     response2 = agent.chat("What is the total number of records in my data?.")
    #     print("response 2 ..")
    #     print(response2)
    # except Exception as e:
    #     print("exp-->")
    #     print(e)

    # Response either contains image or text only.
    if os.path.isfile(response):
        file = open(response, mode="rb")
        data = file.read()
        base64_encoded_image = base64.b64encode(data).decode("utf-8")
        print("Service returns image ...")
        return base64_encoded_image, True
    else:
        print("Service returns no-image ...")
        return response, False


def create_dataframe(buffer: bytes):
    s = str(buffer, "utf-8")
    data = StringIO(s)
    return pd.read_csv(data)


"""
NOTE: This is the original code. It was commented for reference.
"""
# def call_llm():
#     # map to file1 param
#     clinical = pd.read_csv("data/mutation_luad1.csv")
#     clinical = pd.read_csv("data/clinical_luad1.csv")
#     # map to file2 param
#     mutation = pd.read_csv("data/mutation_luad1.csv")

#     llm = AzureOpenAI(
#         api_token="0c6bd275471947ffa99d5a0a9f536df6",
#         azure_endpoint="https://genai-lsr.openai.azure.com/",
#         api_version="2023-08-01-preview",
#         deployment_name="gpt-turbo-4k",
#         api_base="https://genai-lsr.openai.azure.com/",
#     )

#     # Sending file1 & file2 to the request
#     agent = Agent([clinical, mutation], config={"llm": llm}, memory_size=10)

#     # response = agent.chat(
#     #     "Calculate the percentage of samples not having gene value EGFR"
#     # )

#     # response = agent.chat(
#     #     "Compare the distribution of values of EGFR for each values from primary_therapy_outcome_success"
#     # )

#     # response = agent.chat(
#     #     "Show the distribution of genes for patient id TCGA-97-7938-01A"
#     # )

#     # mapping the query
#     response = agent.chat("Show the distribution of ALK AND EGFR")
#     print(response)
