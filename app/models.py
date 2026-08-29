from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):
    title: str
    description: str
    platform: str

    budget: Optional[float] = None
    connects: Optional[int] = None

    remote: bool = True
    recurring: bool = False
    raw_footage_provided: bool = False
    creative_freedom: bool = False
    paid_test: bool = False

    clips_per_month: Optional[int] = None