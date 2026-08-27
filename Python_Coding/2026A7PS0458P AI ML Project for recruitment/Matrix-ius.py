from Vectory import calculate_cosine_similarity, generate_embeddings
import numpy as np
import os
import re
from pathlib import Path
from Chunker import load_chunks
from sentence_transformers import SentenceTransformer


TARGET_FILE = "Bees.txt"
SIMILARITY_THRESHOLD = 0.55

# Target file is where you guys put in your test files. 
# If you're in a good mood, please put one in with defined paragraphs. 

chunks = load_chunks(TARGET_FILE)
model = SentenceTransformer('all-MiniLM-L6-v2')

chunk_vectors = generate_embeddings(chunks, model)

user_query = input("Ask a question about the document: ")
query_vector = model.encode(user_query)

# Question is converted to a vector, and then compared with the chunk vectors.

scored_results = []
for idx, chunk_vec in enumerate(chunk_vectors):
    score = calculate_cosine_similarity(query_vector, chunk_vec)
    scored_results.append((score, chunks[idx]))

scored_results.sort(key=lambda x: x[0], reverse=True)

above_threshold = [item for item in scored_results if item[0] >= SIMILARITY_THRESHOLD]

# We have a threshold for similarity. If the score is above that, we consider it a match.
# But becauHo wse the threshold is high, we might not get any matches. 
# So, we have a fallback to show the top match if nothing passes the threshold.

if above_threshold:
    final_matches = above_threshold
    print(f"\n--- Found {len(final_matches)} result(s) above threshold ({SIMILARITY_THRESHOLD}) ---")
else:
    # Fallback: If nothing passes threshold, pick the top 1 highest score match
    final_matches = [scored_results[0]]
    print(f"\n--- No chunks passed threshold {SIMILARITY_THRESHOLD}. Showing top match ---")

for score, text in final_matches:
    print(f"\n[Similarity Score: {score:.4f}]")
    print(text)
    print("-" * 50)