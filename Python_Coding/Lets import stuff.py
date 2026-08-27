from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Test encoding a quick sentence
vector = model.encode("Honey bees live in hives.")

print("Model loaded successfully!")
print("Vector shape:", vector.shape)  # Should output (384,)
