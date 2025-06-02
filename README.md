# zettel-graph

A visual graph interface for Zettelkasten-style notes, integrating Emacs with D3.js to provide an interactive visualization of your interconnected notes.

---

## 📂 Project Structure

```bash
zettel-graph/
├── data/                  # Auto-generated JSON graph data
├── notes/                 # Your markdown notes
├── script/
│   └── build_graph.py     # Python script to generate graph data
├── index.html             # D3.js-based graph visualization
├── zettel-graph.el        # Emacs integration script
├── .gitignore
└── README.md
```


---

## 🚀 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/hasantkbs/zettel-graph.git
cd zettel-graph
```

### 2. Set Up Your Notes

Place your Zettelkasten-style markdown notes in the notes/ directory. Ensure that links between notes are properly formatted to reflect their connections.

### 3. Generate the Graph Data
Ensure you have Python 3 installed. Then, install the required Python package:

```
pip install networkx
```

Run the script to generate the graph data:

```
python script/build_graph.py
```

This will create a graph.json file inside the data/ directory.

### 4. View the Graph Visualization
Open index.html in your preferred web browser to explore the interactive graph of your notes.



## 🧠 Emacs Integration
### 1. Load the Emacs Script
Add the following to your Emacs configuration to load the zettel-graph.el script:

```
(add-to-list 'load-path "~/path/to/zettel-graph/")
(require 'zettel-graph)
```

Replace "~/path/to/zettel-graph/" with the actual path to your cloned repository.

### 2. Usage within Emacs
After loading the script:

Use the provided functions to interact with your Zettelkasten notes.

Customize keybindings and functions as needed to fit your workflow.

## 🛠️ Dependencies
### Python 3: For running the build_graph.py script.

networkx: Python package for creating and manipulating complex networks.

Emacs: For note-taking and integration with the visualization tool.

D3.js: Included via CDN in index.html for rendering the graph.

## 📄 License

This project is open-source software developed by **Algorix Studio** and distributed under the terms of the **MIT License**.

You are free to use, modify, and distribute this project for both personal and commercial purposes.

> ✅ Contributions are welcome! Feel free to fork the repository, open issues, and submit pull requests.

Copyright © 2025 Algorix Studio.


## 🙌 Acknowledgments
Inspired by the Zettelkasten method of note-taking and the desire to visualize interconnected ideas effectively.


---

Would you like assistance in enhancing the Emacs integration further or perhaps packaging it for distribution via MELPA? Let me know, and we can work on that together!
::contentReference[oaicite:0]{index=0}
 
