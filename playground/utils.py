import pandas as pd
import json


def decode_response(response: str) -> dict:
    return json.loads(response)


def write_response(response_dict: dict) -> str:
    if "answer" in response_dict:
        return response_dict["answer"]

    if "bar" in response_dict:
        data = response_dict["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        return "Show a bar graph"

    if "line" in response_dict:
        data = response_dict["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        return "Show a line graph"

    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        return "Show a table graph"
