import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_files(notes_dir, bookmarks_file):
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for file in os.listdir(notes_dir):
        if file.endswith(".md"):
            with open(os.path.join(notes_dir, file), 'r') as f:
                text = f.read()
                chunks.extend(splitter.split_text(text))

    with open(bookmarks_file) as f:
        bookmarks = json.load(f)
        for bm in bookmarks:
            note = f"{bm['title']}: {bm['notes']}"
            chunks.extend(splitter.split_text(note))

    return chunks