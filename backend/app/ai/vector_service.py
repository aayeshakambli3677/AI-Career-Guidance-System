import numpy as np


def cosine_similarity(vector1, vector2):
    """
    Calculate cosine similarity.
    """

    v1 = np.array(vector1)
    v2 = np.array(vector2)

    similarity = np.dot(v1, v2) / (
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )

    return float(similarity)


def find_best_match(query_embedding, embeddings):
    """
    Find most similar embedding.
    """

    best_score = -1
    best_index = -1

    for index, embedding in enumerate(embeddings):

        score = cosine_similarity(
            query_embedding,
            embedding
        )

        if score > best_score:
            best_score = score
            best_index = index

    return {
        "index": best_index,
        "score": round(best_score, 4)
    }