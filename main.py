from fastapi import FastAPI, Response, Query

app = FastAPI()

# This is a secret password you invent. You will give it to Facebook later.
VERIFY_TOKEN = "SUCF_UNIUYO_SECRET_TOKEN_2026"

@app.get("/webhook")
def verify_webhook(
    mode: str = Query(None, alias="hub.mode"),
    token: str = Query(None, alias="hub.verify_token"),
    challenge: str = Query(None, alias="hub.challenge")
):
    # Checks if Facebook is sending the correct token
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return Response(content=challenge, media_type="text/plain")
    
    return Response(content="Verification failed", status_code=403)

@app.post("/webhook")
async def receive_message():
    # This is where your code will process incoming messages later
    return {"status": "success"}