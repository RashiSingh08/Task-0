from sentence_transformers import SentenceTransformer
from Chunker import load_chunks
import os
import numpy as np
from pathlib import Path
import re


def calculate_cosine_similarity(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b)

def generate_embeddings(text_list, model):
    return model.encode(text_list)

# We define calculate_cosine_similarity and generate_embeddings sabse pehle, so that they can be used in other files.

bees_path = Path(__file__).parent / "Bees.txt"
My_chunks = load_chunks(bees_path)

# I still haven't understood the path stuff much. But I know that this is the most famous way to do it. 
# It works. So, I don't care right now. Will learn later.

print(f"Imported {len(My_chunks)} chunks!")

model = SentenceTransformer('all-MiniLM-L6-v2')

#Sentence transformers are pretty cool. Text to vectors, huh...

chunk_embeddings = generate_embeddings(My_chunks, model)

print("Embeddings shape:", chunk_embeddings.shape)