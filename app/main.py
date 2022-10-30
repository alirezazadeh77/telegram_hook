from fastapi import FastAPI, Request, HTTPException, status

from app.telegram.send_message import send_message

app = FastAPI()


@app.post("/hooks", status_code=status.HTTP_201_CREATED)
async def github_webhook(request: Request):
    body = await request.json()
    try:
        send_message(body)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
