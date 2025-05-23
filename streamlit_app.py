import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = 'antioxidants.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS compounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        cid INTEGER,
        formula TEXT,
        smiles TEXT,
        source TEXT,
        mechanism TEXT,
        target TEXT,
        activity TEXT,
        reference TEXT
    )''')
    conn.commit()
    conn.close()

def insert_compound(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO compounds (name, cid, formula, smiles, source, mechanism, target, activity, reference) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def fetch_compounds():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM compounds", conn)
    conn.close()
    return df

def search_by_target(target):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM compounds WHERE target LIKE ?", conn, params=(f'%{target}%',))
    conn.close()
    return df

st.title("🧪 Antioxidant Compound Database")
create_table()

menu = ["View All", "Search by Target", "Add New Compound"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "View All":
    st.subheader("All Compounds")
    df = fetch_compounds()
    st.dataframe(df)

elif choice == "Search by Target":
    st.subheader("Search Compounds by Target")
    target = st.text_input("Enter target (e.g. Nrf2)")
    if target:
        results = search_by_target(target)
        st.dataframe(results)

elif choice == "Add New Compound":
    st.subheader("Add a New Antioxidant Compound")
    name = st.text_input("Compound Name")
    cid = st.text_input("PubChem CID")
    formula = st.text_input("Molecular Formula")
    smiles = st.text_input("SMILES")
    source = st.selectbox("Source", ["Natural", "Synthetic Drug"])
    mechanism = st.text_input("Mechanism of Action")
    target = st.text_input("Target Molecule")
    activity = st.text_input("Activity (e.g. IC50)")
    reference = st.text_input("Reference (PMID or URL)")

    if st.button("Add Compound"):
        insert_compound((name, cid, formula, smiles, source, mechanism, target, activity, reference))
        st.success(f"{name} has been added successfully!")