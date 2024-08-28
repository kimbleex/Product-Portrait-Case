from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uvicorn
from TOOLS import TOOLS 
import json
import os
from fastapi.staticfiles import StaticFiles
from itertools import islice

def dict_slice(d, n):
    return dict(islice(d.items(), n))

TOOLS = TOOLS()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# data_source_path = 'D:/#Scripts/googleTrends_new/'
# data_target_path = 'D:/#Scripts/googleTrendsVisualize/Dataset/'
# file_names = ['data.json']
# TOOLS.copy_files(data_source_path, data_target_path, file_names)

with open('./Dataset/data.json', "r", encoding='utf8') as f:
        if os.path.isfile('./Dataset/data.json'):
            size = os.path.getsize('./Dataset/data.json')
            if size == 0:
                data = {}
            else:
                data = json.load(f)
        else:
            data = {}

class item(BaseModel):
    topic_key: str
    country_scores: Dict[str, float]
    related_entities: Dict[str, float]
    related_queries: Dict[str, float]

@app.get("/data/{topic_key}")
async def get_data(topic_key: str):
    if topic_key in data:
        # print([dict_slice(data[topic_key]['country_scores'], 15), data[topic_key]['related_entities'], data[topic_key]['related_queries']])
        return [dict_slice(data[topic_key]['country_scores'], 15), data[topic_key]['related_entities'], data[topic_key]['related_queries']]
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/topic_keys")
async def get_all_keys():
    return list(data.keys())

@app.get("/related_entities")
async def get_data(topic_key: str):
    if topic_key in data:
        if data[topic_key]['related_entities'] == {}:
            return {'Nothing': 0}
        else:    
            return data[topic_key]['related_entities']
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.get("/related_queries")
async def get_data(topic_key: str):
    if topic_key in data:
        if data[topic_key]['related_queries'] == {}:
            return {'Nothing': 0}
        else:
            return data[topic_key]['related_queries']
    else:
        raise HTTPException(status_code=404, detail="User not found")

