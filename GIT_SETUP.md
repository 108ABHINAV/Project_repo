# Git Setup Instructions

## What to Commit

✅ **Include these files:**
- `app.py` - Main Streamlit UI
- `generate_data.py` - Data generator script
- `requirements.txt` - Dependencies
- `notebooks/*.ipynb` - All 4 analysis notebooks
- `README.md` - Documentation
- `QUICKSTART.md` - Quick start guide
- `PROJECT_SUMMARY.md` - Summary
- `.gitignore` - Git ignore rules

❌ **Exclude these (auto-ignored):**
- `data/` - Large data files (can regenerate)
- `__pycache__/` - Python cache
- `.ipynb_checkpoints/` - Jupyter checkpoints
- IDE/OS files

## Setup Instructions

### 1. Initialize Git Repository
```bash
cd d:\5-Projects\Grad_Final
git init
```

### 2. Add Files
```bash
git add .
```

### 3. Create First Commit
```bash
git commit -m "Initial commit: Crime Rate Prediction System"
```

### 4. Add Remote Repository (GitHub/GitLab)
```bash
# Replace with your repository URL
git remote add origin https://github.com/yourusername/crime-prediction.git
git branch -M main
git push -u origin main
```

## After Cloning

When someone clones your repository, they need to:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate data:**
   ```bash
   python generate_data.py
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## File Sizes

- Total project (without data): ~50 KB
- Data file (excluded): 2.3 MB
- Notebooks: ~200 KB

By excluding the data file, your repository stays lightweight and fast to clone!

---

**Ready to commit!** ✅
