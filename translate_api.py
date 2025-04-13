from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import argostranslate.package
import argostranslate.translate
import os
import redis
import hashlib
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("ARGOS_API_KEY", "bb52f440-f0e5-4a48-aecb-c8a1d7d54bb9")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
CACHE_TTL_SECONDS = 60 * 60 * 24 * 30  # 30 dias

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)


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

    key_hash = hashlib.sha256(f"{payload.from_lang}:{payload.to_lang}:{payload.text}".encode()).hexdigest()
    cached = r.get(key_hash)

    if cached:
        return {"translated": cached}

    ensure_model(payload.from_lang, payload.to_lang)
    translated = argostranslate.translate.translate(payload.text, payload.from_lang, payload.to_lang)

    r.setex(key_hash, CACHE_TTL_SECONDS, translated)
    return {"translated": translated}
