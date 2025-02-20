import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

# Modell und Tokenizer laden
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
model = AutoModel.from_pretrained("meta-llama/Llama-3.1-8B")

# Funktion zur Extraktion des ersten Token-Embeddings eines Wortes
def get_embedding(word):
    tokens = tokenizer(word, return_tensors="pt", add_special_tokens=False)
    token_ids = tokens["input_ids"].squeeze().tolist()
    if isinstance(token_ids, int):
        token_ids = [token_ids]
    embedding = model.get_input_embeddings().weight[token_ids[0]]
    return embedding

# Embedding für "Cat" holen
embedding_cat = get_embedding("Cat")

# Alle Token-IDs aus dem Vokabular holen
vocab = tokenizer.get_vocab()
vocab_tokens = list(vocab.keys())
vocab_ids = list(vocab.values())

# Ähnlichkeitswerte berechnen
min_similarity = float("inf")
most_distant_token = None
most_distant_embedding = None

for token, token_id in zip(vocab_tokens, vocab_ids):
    token_embedding = model.get_input_embeddings().weight[token_id]  # Embedding für das aktuelle Token
    similarity = F.cosine_similarity(embedding_cat.unsqueeze(0), token_embedding.unsqueeze(0)).item()

    # Prüfen, ob dies der am weitesten entfernte Wert ist
    if similarity < min_similarity:
        min_similarity = similarity
        most_distant_token = token
        most_distant_embedding = token_embedding

# Ergebnis ausgeben
print(f"Token, das am weitesten von 'Cat' entfernt ist: '{most_distant_token}'")
print(f"Kosinussimilarität: {min_similarity:.4f}")