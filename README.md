# 🚀 RAM Page Replacement Algorithms Toolkit

**RAM-page-replacement** is a simple, modern Python toolkit for simulating classic page replacement strategies in operating systems.  
Great for students, educators, and anyone interested in how memory management works under the hood!

---

## ✨ Features

- **Easy-to-use API**: One class, three algorithms (`FIFO`, `LRU`, `Optimal`)
- **Customizable**: Simulate with any page sequence and frame size
- **MIT Licensed & Open Source**
- **Ready-to-run examples**

---

## 📦 Algorithms Included

| Name   | Strategy Summary                                    |
|--------|-----------------------------------------------------|
| FIFO   | Evicts the oldest loaded page                       |
| LRU    | Evicts the least recently accessed page             |
| Optimal| Evicts the page not needed for the longest future   |

---

## 🛠 How To Run?

### 1. Clone the repository

```bash
git clone https://github.com/Adam-ZS/RAM-page-replacement.git
cd RAM-page-replacement
```

### 2. Run the Example

```bash
python example_run.py
```

### 3. Use in Your Own Code

```python
from page_replacement import PageReplacementSimulator

pages = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
sim = PageReplacementSimulator(capacity=4)
print("FIFO faults:", sim.fifo(pages))
print("LRU faults:", sim.lru(pages))
print("Optimal faults:", sim.optimal(pages))
```

---

## 🧪 Example Output

```
RAM Page Replacement Results
--------------------------------
Page sequence: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
Frame capacity: 4

   FIFO page faults: 11
    LRU page faults: 10
Optimal page faults: 8
```

---

## 📖 License

MIT License – see LICENSE file.

---

## 💡 Contributing

Pull requests welcome!  
For questions, ideas, or improvements, open an issue or PR.
