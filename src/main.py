from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5h://tor:9050',
                       'https': 'socks5h://tor:9050'}
    return session

WTTR_CALL = "https://wttr.in/Kyiv?m&format=3"

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    session = get_tor_session()
    res = session.get(WTTR_CALL).text
    return res