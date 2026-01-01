# CHAT-WITH-PDFS-RAG

A powerful Retrieval Augmented Generation (RAG) chatbot application that allows you to chat with your PDF documents using **Llama 3.3** (via Groq), LangChain, ChromaDB, and Streamlit.

Ask questions in natural language about your uploaded PDFs and get accurate, context-aware answers instantly!

## 🚀 Features

-   **Chat with Multiple PDFs**: Upload multiple documents and chat with all of them simultaneously.
-   **RAG Architecture**: Uses advanced retrieval-augmented generation to ground answers in your document content.
-   **Local Embeddings**: Uses `all-MiniLM-L6-v2` (HuggingFace) for efficient and free local text embeddings.
-   **High-Performance LLM**: Powered by `llama-3.3-70b-versatile` via Groq for lightning-fast inference.
-   **Persistent Database**: Uses ChromaDB to save your document vectors locally, so you don't have to re-process files every time.
-   **Chat History**: Remembers the context of your conversation for a natural chat experience.
-   **Source Citations**: Shows exactly which source documents and pages were used to generate the answer.
-   **Clean UI**: A simple, elegant interface built with Streamlit.

## 🛠️ Tech Stack

-   **Frontend**: Streamlit
-   **LLM**: Llama 3.3-70b (via Groq API)
-   **Orchestration**: LangChain
-   **Vector Database**: ChromaDB
-   **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
-   **PDF Processing**: PyPDF

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/MADSKULL21/CHAT-WITH-PDFS-RAG.git
cd CHAT-WITH-PDFS-RAG
```

### 2. Create a Virtual Environment (Recommended)
It is highly recommended to use a virtual environment to manage dependencies.

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
You need a **Groq API Key** to run the LLM.

1.  Go to [Groq Console](https://console.groq.com/keys).
2.  Login and create a new API Key.
3.  Copy the API Key.

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Open `.env` and add your key:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

---

## 🚀 Usage

Once installed, you can start the application with a single command:

```bash
streamlit run app/app.py
```

The app will open automatically in your browser (usually at `http://localhost:8501`).

### How to Use
1.  **Upload**: Use the sidebar to browse and upload one or multiple PDF files.
2.  **Process**: The system will chunk and embed the text (this happens locally).
3.  **Chat**: Once processed, type your question in the chat input.
4.  **Inspect**: Check the sidebar to see which documents the AI is referencing.

---

## 🧠 How It Works

1.  **Document Loading**: The app reads the PDF files and extracts text.
2.  **Splitting**: Text is split into manageable chunks to fit into the context window.
3.  **Embedding**: Each chunk is converted into a numerical vector using the `HuggingFaceEmbeddings` model.
4.  **Vector Storage**: These vectors are stored locally in a ChromaDB database (`Vector_DB - Documents` folder).
5.  **Retrieval**: When you ask a question, your query is embedded and compared against the stored vectors to find the most relevant chunks.
6.  **Generation**: The relevant chunks + your question + chat history are sent to the `Llama 3.3` model on Groq, which generates the final answer.

## 📂 Project Structure

```
CHAT-WITH-PDFS-RAG/
├── app/
│   ├── app.py                  # Main Streamlit application
│   └── utils/
│       ├── chatbot.py          # Chat logic and LLM chain
│       ├── prepare_vectordb.py # PDF processing & Vector DB logic
│       ├── save_docs.py        # Helper to manage document uploads
│       └── session_state.py    # Streamlit session state management
├── docs/                       # Folder where uploaded PDFs are stored
├── Images/                     # Images for README
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API Keys)
└── README.md                   # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
