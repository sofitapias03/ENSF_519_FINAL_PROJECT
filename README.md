# ENSF 519 Final Project – Garbage Classification

## Project Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the dataset

```bash
python Scripts/download_dataset.py
```

The Garbage Classification V2 dataset will be downloaded using KaggleHub and stored in a local cache. If the dataset has already been downloaded, the cached version will be reused.

### 5. Run the notebook

1. Open `notebooks/recycling_classification.ipynb` in VS Code.
2. Click **Select Kernel** in the top-right corner.
3. Select the `.venv` Python environment.
4. Run the notebook cells.