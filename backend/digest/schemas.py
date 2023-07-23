from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

LIMIT = int(os.getenv("LIMIT"))
OFFSET = int(os.getenv("OFFSET"))


class DigestParams(BaseModel):
    limit: int = LIMIT
    offset: int = OFFSET
    id: int
