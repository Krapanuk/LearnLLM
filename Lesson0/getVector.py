from transformers import AutoTokenizer, AutoModel

# Modell und Tokenizer laden
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
model = AutoModel.from_pretrained("meta-llama/Llama-3.1-8B")

# Wort, das analysiert werden soll
word = "Cat"

# Tokenisierung durchführen
tokens = tokenizer(word, return_tensors="pt", add_special_tokens=False)  # Tokenisierung mit Tensor-Rückgabe - add_special_tokens=False entfernt das zusätzliche <|startoftext|> Token
token_ids = tokens["input_ids"].squeeze().tolist()  # Token-IDs extrahieren

# Falls nur ein einzelner Token-Index zurückkommt, in eine Liste umwandeln
if isinstance(token_ids, int):
    token_ids = [token_ids]

# Tokens in Text zurückkonvertieren
token_strings = tokenizer.convert_ids_to_tokens(token_ids)  

# Embeddings für jedes Token abrufen
embeddings = model.get_input_embeddings().weight[token_ids]

# Ergebnisse ausgeben
print(f"Wort: {word}")
print(f"Tokens: {token_strings}")
print(f"Token-IDs: {token_ids}")

# Die Embeddings für jedes Token ausgeben
for i, (token, token_id, embedding) in enumerate(zip(token_strings, token_ids, embeddings)):
    print(f"\nToken {i}: '{token}' (ID: {token_id}) → Werte im Vektor:")

    # Zahlen runden und durchnummerieren
    rounded_values = [f"{j+1}: {round(val, 3)}" for j, val in enumerate(embedding.tolist())]
    
    # Alle 10 Werte pro Zeile, um es übersichtlicher zu machen
    for k in range(0, len(rounded_values), 10):
        print("  " + " | ".join(rounded_values[k:k+10]))
