from app.ai.embeddings import generate_embedding

text = "Python developer with SQL skills"

embedding = generate_embedding(text)

print(len(embedding))
print(embedding[:10])