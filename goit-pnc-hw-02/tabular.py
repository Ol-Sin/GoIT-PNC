def tabular_encrypt(text, key):
    columns = sorted(list(key))
    col_order = [key.index(c) for c in columns]
    rows = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    
    # Pad the last row
    if len(rows[-1]) < len(key):
        rows[-1] += ' ' * (len(key) - len(rows[-1]))

    encrypted = ''.join(''.join(row[col] for row in rows) for col in col_order)
    return encrypted

def tabular_decrypt(text, key):
    columns = sorted(list(key))
    col_order = [key.index(c) for c in columns]
    num_rows = len(text) // len(key)
    grid = [''] * len(key)

    for i, col in enumerate(col_order):
        grid[col] = text[i * num_rows:(i + 1) * num_rows]

    decrypted = ''.join(''.join(row[i] for row in grid) for i in range(num_rows)).rstrip()
    return decrypted

# Example usage
key = "MATRIX"
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
encrypted_text = tabular_encrypt(text, key)
decrypted_text = tabular_decrypt(encrypted_text, key)

print(f"Encrypted: {encrypted_text}")
print("\n")
print(f"Decrypted: {decrypted_text}")
