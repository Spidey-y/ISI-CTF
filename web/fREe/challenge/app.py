import re
from fastapi import FastAPI, Query
import os


app = FastAPI()
strings = ["apple", "banana", "this", "application", "does", "nothing",
           "bla", "blabla", "oranges", "mangoes", "grapes", "strawberry"]

strings.append("!"+os.environ.get("FLAG"))
blacklist = " 0123456789-_*+&@`|#\"~,;:[]\\()^=!?/\{\}"


@app.get("/")
def fetch(query: str = Query(..., description="Query string")):
    if any([i in blacklist for i in query]):
        return {"error": "input not allowed, try again!"}
    results = []
    for s in strings:
        if re.search(f"^{query}$", s):
            results.append(s)
    return results
