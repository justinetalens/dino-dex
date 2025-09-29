from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI(title="Dinodex API", description="A Pokédex-style encyclopedia for dinosaurs", version="1.0")

# Load JSON data
DATA_PATH = Path(__file__).parent.parent / "data" / "dinosaurs.json"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    dinosaurs = json.load(f)


@app.get("/dinosaurs")
def get_all_dinosaurs():
    return dinosaurs


@app.get("/dinosaurs/{dino_id}")
def get_dinosaur(dino_id: int):
    dino = next((d for d in dinosaurs if d["id"] == dino_id), None)
    if not dino:
        raise HTTPException(status_code=404, detail="Dinosaur not found")
    return dino


@app.get("/dinosaurs/search/")
def search_dinosaur(name: str):
    results = [d for d in dinosaurs if name.lower() in d["name"].lower()]
    if not results:
        raise HTTPException(status_code=404, detail="No dinosaurs match your search")
    return results
