import os
import re
from pathlib import Path

#First, we import stuff

BASE_DIR = Path(__file__).resolve().parent


def load_chunks(file_name="Bees.txt"):

  full_path = BASE_DIR / file_name

  with open(full_path, "r", encoding="utf-8") as file:
    raw_text = file.read()

    My_chunks = [chunk.strip() for chunk in raw_text.split("\n\n") 
          if chunk.strip()
  ]
    
# We believe in efficiency. So, we first hope that the text is already chunked bcs... paragraphs
# We split the text into chunks based on double newlines, and remove any empty chunks.
# If the file has only one chunk, we can split it into smaller chunks based on sentences.

    if len(My_chunks) <= 1:
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', raw_text) if s.strip()]
        
        chunks = [
            " ".join(sentences[i : i + 4]) 
            for i in range(0, len(sentences), 4)
        ]
  return My_chunks

# Fours is about the sweet spot for chunk size. Not too small, not too big. 
# Like, topics ARE usually discussed in 3-5 sentences. So, we take 4.

My_chunks = load_chunks()
print("Number of chunks created:", len(My_chunks))

#There should be 10 chunks. Atleast in my Bees.txt file.
#ITS IRRITating that even a single space destroys the code.
