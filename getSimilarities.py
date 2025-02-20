import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

# Modell laden
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
model = AutoModel.from_pretrained("meta-llama/Llama-3.1-8B")

# Funktion zur Extraktion des ersten Token-Embeddings eines Wortes (BOS-Token wird entfernt)
def get_embedding(word):
    tokens = tokenizer(word, return_tensors="pt", add_special_tokens=False)  # Kein BOS-Token
    token_ids = tokens["input_ids"].squeeze().tolist()  # Token-IDs extrahieren
    
    # Falls nur ein einzelner Token-Index zurückkommt, in eine Liste umwandeln
    if isinstance(token_ids, int):
        token_ids = [token_ids]
    
    # Embeddings für das erste Token abrufen
    embedding = model.get_input_embeddings().weight[token_ids[0]]  
    return embedding

# Embeddings für Cat, Dog und Car abrufen
embedding_cat = get_embedding("Cat")
embedding_dog = get_embedding("Dog")
embedding_car = get_embedding("Car")

# Kosinussimilarität berechnen
similarity_cat_dog = F.cosine_similarity(embedding_cat.unsqueeze(0), embedding_dog.unsqueeze(0)).item()
similarity_cat_car = F.cosine_similarity(embedding_cat.unsqueeze(0), embedding_car.unsqueeze(0)).item()

print(f"Kosinussimilarität zwischen Cat und Dog: {similarity_cat_dog:.4f}")
print(f"Kosinussimilarität zwischen Cat und Car: {similarity_cat_car:.4f}")
