
from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel
import argostranslate.package
import argostranslate.translate
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("ARGOS_API_KEY", "default-insecure-key")

class TranslationRequest(BaseModel):
    text: str
    from_lang: str = "pt"
    to_lang: str = "es"

def ensure_model(from_code, to_code):
    available_packages = argostranslate.package.get_available_packages()
    match = list(filter(lambda p: p.from_code == from_code and p.to_code == to_code, available_packages))
    if match:
        pkg = match[0]
        download_path = pkg.download()
        argostranslate.package.install_from_path(download_path)

@app.post("/translate")
def translate_text(payload: TranslationRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    ensure_model(payload.from_lang, payload.to_lang)
    translated = argostranslate.translate.translate(payload.text, payload.from_lang, payload.to_lang)
    return {"translated": translated}
