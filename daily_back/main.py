from typing import Union
from fastapi import FastAPI
import datetime
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

now_time = datetime.datetime.now().strftime('%Y%m%d')

path = './news_txt/ele_bank/%s.json' % (now_time)

with open(path, 'r', encoding='utf8') as f:
    json_data = json.load(f)

@app.get("/posts")
def read_root():
    return json_data