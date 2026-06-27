from app.ai.embeddings import generate_embedding
from app.ai.vector_service import find_best_match

query = generate_embedding("Python developer")

data = [
    generate_embedding("Java developer"),
    generate_embedding("Python backend developer"),
    generate_embedding("Graphic designer")
]

result = find_best_match(query, data)

print(result)