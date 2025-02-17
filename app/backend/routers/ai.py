from fastapi import APIRouter


router = APIRouter(prefix="/ai", tags=["AI Inference"])


@router.post("/train", )
def train_user_model():
    """Train Flux model based on user images using Fal.ai/locally"""


@router.post("/generate")
def generate_images():
    """Generate AI images from the pre trained Flux model using Fal.ai/locally"""