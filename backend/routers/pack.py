from fastapi import APIRouter

router = APIRouter(prefix="/pack", tags=["Image Packs"])


@router.post("/generate")
def generate_pack_images():
    """Generate AI images from the pre trained Flux model using Fal.ai/locally based on the pack prompt"""


@router.get("/get_bulk")
def get_packs():
    """Get all the current packs from backend"""
