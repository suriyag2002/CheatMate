import streamlit as st
import base64

CHEATSHEETS = {
    "python": """
**Python Cheatsheet**

**Basics:**
- **Variables**: Used to store data. Example: `x = 5`
- **Data Types**: Common types include `int`, `float`, `str`, `list`, `dict`
- **Functions**: Define reusable code blocks using `def`. Example:
```python
def greet(name):
    return f"Hello, {name}"
```

**Loops:**
- Used to iterate over sequences. Example:
```python
for i in range(5):
    print(i)
```

**Conditionals:**
- Perform actions based on conditions:
```python
if x > 5:
    print("Big")
else:
    print("Small")
```

**List Comprehension:**
- Compact way to generate lists:
```python
squares = [x*x for x in range(10)]
```
    """,
    "git": """
**Git Cheatsheet**

**Basics:**
- **Clone** a repository: `git clone <url>`
- **Check Status** of changes: `git status`
- **Commit** changes: `git commit -m "message"`

**Branching:**
- Create a new branch: `git branch new-feature`
- Switch to a branch: `git checkout new-feature`
- Merge changes: `git merge main`

**Push/Pull:**
- Upload code to GitHub: `git push origin main`
- Get latest code: `git pull`
    """,
    "pandas": """
**Pandas Cheatsheet with Explanations**

**Import the library:**
```python
import pandas as pd
```
This imports pandas, commonly used for data analysis.

**Create DataFrame:**
```python
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)
```
This creates a tabular data structure from a dictionary.

**Read a CSV File:**
```python
df = pd.read_csv('data.csv')
```
Reads data from a CSV file into a DataFrame.

**Basic Operations:**
- `df.head()` – shows first 5 rows.
- `df.describe()` – gives statistical summary.
- `df['col']` – accesses a specific column.
- `df.groupby('col').mean()` – groups data by a column and computes mean.

**Filter Data:**
```python
df[df['age'] > 25]
```
Returns rows where age is greater than 25.

**Add a Column:**
```python
df['salary'] = [50000, 60000]
```
Adds a new column called salary to the DataFrame.
    """
}

st.set_page_config(page_title="CheatMate", layout="wide")
st.title("📘 CheatMate – Instant Code Cheatsheet Generator")
st.markdown("Enter a topic (e.g. python, git, pandas) to view a ready-made cheatsheet with simple explanations.")

query = st.text_input("Enter a topic:", placeholder="e.g. python, git, pandas...").lower().strip()

if query:
    if query in CHEATSHEETS:
        st.markdown(CHEATSHEETS[query])

        # Optional: Export as text download
        def get_download_link(text, filename):
            b64 = base64.b64encode(text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download Cheatsheet</a>'
            return href

        st.markdown(get_download_link(CHEATSHEETS[query], f"{query}_cheatsheet.txt"), unsafe_allow_html=True)
    else:
        st.warning("❌ Sorry, no cheatsheet found for that topic. Try 'python', 'git', or 'pandas'.")

st.markdown("---")
st.caption("Made with ❤️ by @Suriya")