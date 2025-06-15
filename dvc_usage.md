

### 📄 `dvc usage`

````markdown
# 🗃️ Data Versioning with DVC

This project uses [**DVC (Data Version Control)**](https://dvc.org/) to manage datasets in a reproducible and auditable way, especially important for projects in regulated environments like insurance.

---

## 🔧 Setup Instructions

### 1. Install DVC

```bash
pip install dvc
```
````

---

### 2. Initialize DVC in the Project

```bash
dvc init
```

This creates a `.dvc/` folder and modifies `.gitignore`.

---

### 3. Track the Dataset

```bash
dvc add data/raw/insurance_data.txt
```

This creates `insurance_data.txt.dvc`, a metadata file for Git.

---

### 4. Configure Local Remote Storage

```bash
mkdir .dvc_storage
dvc remote add -d localstore .dvc_storage
```

---

### 5. Push Data to Remote

```bash
dvc push
```

The dataset content is moved to `.dvc_storage/` and excluded from Git.

---

## 🔁 Workflow Summary

| Action          | Command                         |
| --------------- | ------------------------------- |
| Add new data    | `dvc add <file>`                |
| Update metadata | `git add <file>.dvc .gitignore` |
| Save to remote  | `dvc push`                      |
| Restore data    | `dvc pull`                      |
| Check status    | `dvc status`                    |

---

## 📂 Tracked Data Files

| Path                          | Description                          |
| ----------------------------- | ------------------------------------ |
| `data/raw/insurance_data.txt` | Main dataset used for analysis       |
| `.dvc_storage/`               | Local DVC remote (not pushed to Git) |

---

💡 To collaborate:

1. Pull latest Git changes
2. Run `dvc pull` to retrieve the dataset

````

---

### ✅ Save it

You can save this with:

```python
with open("dvc_usage.md", "w") as f:
    f.write("""[paste the above content here]""")
````
