# 🌳 Daily Reflection Tree (DT Fellowship)

A deterministic, data-driven reflection agent designed to help employees evaluate their day through the lens of management science and organizational psychology.

## 🚀 Overview
This project is a **Deterministic Reflection Tool**. Unlike generic AI chatbots, this system follows a pre-defined branching logic to guide users through rigorous thinking without the risk of LLM hallucinations. It translates fuzzy human emotions into structured, auditable decision paths.

### The Three Axes of Reflection:
1.  **Locus (Victim ↔ Victor):** Internal vs. External locus of control (based on Julian Rotter & Carol Dweck).
2.  **Orientation (Entitlement ↔ Contribution):** Focus on value creation vs. perceived lack of support.
3.  **Radius (Self-Centrism ↔ Altrocentrism):** Zooming out from personal stress to team and customer value (Maslow’s Self-Transcendence).

---

## 📂 Project Structure

| Folder / File | Content |
| :--- | :--- |
| [`/tree`](./tree) | **The Knowledge Base:** Contains the `reflection-tree.json` and the logic diagram. |
| [`/agent`](./agent) | **The Engine:** A Python CLI tool that executes the deterministic logic. |
| [`/transcripts`](./transcripts) | **Proof of Concept:** Sample runs showing different persona paths. |
| [`write-up.md`](./write-up.md) | **Deep Dive:** Detailed design rationale and psychological grounding. |

---

## ⚙️ Technical Architecture
- **Deterministic Routing:** Uses a node-based system where every user selection leads to a fixed next state.
- **Signal Tallying:** The system captures "Signals" (e.g., `axis1:internal`) throughout the session.
- **Zero-LLM Runtime:** Built to be predictable, auditable, and secure.
- **Dynamic Synthesis:** The final summary interpolates user data into a personalized reflection.

---

## 🛠️ Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/daily-reflection-tree.git](https://github.com/YOUR_USERNAME/daily-reflection-tree.git)
   cd daily-reflection-tree
