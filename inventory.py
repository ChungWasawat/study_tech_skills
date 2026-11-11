from pathlib import Path
from csv import DictWriter
import argparse
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class File:
    path_name: str
    extension: str
    size_bytes: float
    modified_time: datetime

def top5_biggest(folder: str) -> str:
    folder_path = Path(folder)


    return 