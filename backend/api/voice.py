from fastapi import APIRouter, Request
router=APIRouter()
@router.post("/voice")
async def voice_endpoint(request: Request):
    payload=await request.json()
    print("\n---VOICE EVENT---")
    print(payload)
    print("-------------------\n")
    return {
        "success": True
    }