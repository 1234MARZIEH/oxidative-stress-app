# 🧪 Antioxidant Compound Web App

This web application allows users to manage a database of natural and synthetic compounds effective in reducing oxidative stress.

## 🔧 Features

- View all antioxidant compounds
- Search by molecular target (e.g. Nrf2)
- Add new compounds with details
- Data stored in SQLite database

## ▶️ How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501/`.

## 📁 Files

- `streamlit_app.py` – Main Streamlit app
- `requirements.txt` – Python package requirements
- `antioxidants.db` – SQLite database (auto-created)

## 📚 Sources

- PubChem
- Research papers (PMID references)