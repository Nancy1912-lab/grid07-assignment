from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from personas import personas

model = SentenceTransformer("all-MiniLM-L6-v2")

persona_texts = [p["description"] for p in personas]

embeddings = model.encode(persona_texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))


def find_best_persona(user_query):

    query_lower = user_query.lower()

    if "bitcoin" in query_lower or "crypto" in query_lower:
        return personas[2]

    if "ai" in query_lower or "software" in query_lower:
        return personas[1]

    if "marketing" in query_lower or "branding" in query_lower:
        return personas[3]

    query_embedding = model.encode([user_query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        1
    )

    matched_persona = personas[indices[0][0]]

    return matched_persona
