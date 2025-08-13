# Calculator

A desktop calculator application written in **Python** with a **PyQt** GUI. It combines a **basic** and **scientific** calculator with a handy **unit converter** (length, mass, temperature, time).

---

## 🧭 Overview

**Calculator** focuses on quick everyday calculations while also offering advanced math functions and a clean, keyboard-friendly UI. The built‑in converter covers the most common unit categories so you don’t need a separate tool.

---

## ✨ Features

- **Basic calculator:** addition, subtraction, multiplication, division, parentheses
- **Scientific mode:** powers, roots, common trigonometric functions, logarithms
- **Unit converter:** length, mass, temperature, and time
- **Clear, responsive UI** optimized for desktop use

> Tip: Exact button labels and the full set of scientific functions depend on the implementation—this README describes the intent of each module.

---

## 🛠️ Tech Stack

- Python 3.x  
- PyQt (PyQt5/6 depending on `requirements.txt`)  
- *(Optional)* Qt Designer for editing `.ui` files

---

## 📁 Project Structure

```text
Calculator/
├─ main.py              # Application entry point
├─ classes/             # Core logic (operations, conversions)
├─ gui/                 # UI layer (Qt widgets / .ui files)
├─ build/               # (optional) build artifacts
└─ requirements.txt     # Python dependencies
```

> Folder names may vary slightly; the structure above reflects the intended separation of concerns.

---

## 🚀 Installation

1) **Clone the repository**
```bash
git clone https://github.com/GingerCRO/Calculator.git
cd Calculator
```

2) **Create and activate a virtual environment (recommended)**
```bash
# Windows (PowerShell)
py -m venv .venv
.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
# Windows
py main.py

# macOS / Linux
python3 main.py
```

---

## 🕹️ Usage

- Choose the desired module from the UI: **Basic**, **Advanced/Scientific**, or **Converter**.  
- In **Converter**, select a category (length/mass/temperature/time), choose **From** and **To** units, and enter a value.  
- In **Calculator**, use on‑screen buttons or your keyboard; press **=** (or **Enter**) to evaluate.

---

## ✅ Quick Smoke Tests

- **Basic:** `2 + 2 = 4`, `10 / 4`, `3 * (5 - 2)`  
- **Scientific:** `√9`, `2^8`, `sin(π/2)`, `log10(100)`  
- **Converter:** check typical conversions (e.g., `m ↔ km`, `kg ↔ g`, `°C ↔ °F`, `s ↔ min`)

---

## 🤝 Contributing

1. Fork the repository  
2. Create a branch: `git checkout -b feature/your-feature`  
3. Commit: `git commit -m "Add your feature"`  
4. Push: `git push origin feature/your-feature`  
5. Open a Pull Request

---

## 📦 Build a Standalone App (optional)

Using **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --name Calculator --onefile --windowed main.py
```

Artifacts will be available in the `dist/` directory.

---

## 📄 License

This project is released under the **MIT License**. See the `LICENSE` file for details.

---

## 🙏 Acknowledgments

Thanks to the open‑source community and the PyQt ecosystem for tools and inspiration.
