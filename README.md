# 🌳 Daily Reflection Tree (DT Fellowship)

A deterministic, data-driven reflection tool designed to help employees navigate their daily experiences through the lens of management science and organizational psychology.

## 🚀 The Core Philosophy
Unlike standard AI chatbots, this tool is **fully deterministic**. It uses a structured ontology to guide users through three critical psychological axes. There are no LLM calls at runtime—ensuring a predictable, auditable, and high-quality reflection every single time.

### The Three Axes of Reflection:
1.  **Locus (Victim ↔ Victor):** Shifting from "Why me?" to "What can I control?" based on Julian Rotter’s Locus of Control.
2.  **Orientation (Entitlement ↔ Contribution):** Moving from "What do I get?" to "What did I give?" focusing on Organizational Citizenship Behavior.
3.  **Radius (Self-Centrism ↔ Altrocentrism):** Expanding concern from personal stress to team and customer impact (Maslow’s Self-Transcendence).

---

## 📂 Project Structure

| Folder / File | Purpose |
| :--- | :--- |
| [`/tree`](./tree) | Contains the `reflection-tree.json` (the brain) and the visual logic map. |
| [`/agent`](./agent) | CLI-based Python script that executes the tree logic. |
| [`/transcripts`](./transcripts) | Recorded sessions showing different employee personas. |
| [`write-up.md`](./write-up.md) | Detailed design rationale and psychological grounding. |

---

## 🛠️ How it Works

The system operates on a **Node-Signal-State** architecture:
- **Deterministic Branching:** Every user choice leads to a pre-defined path.
- **Signals:** As the user answers, the system tallies 'signals' (e.g., `axis1:internal`) to build a persona profile.
- **Interpolation:** The final reflection summary dynamically injects the user's own words and tallies back into the conversation.

### Visualizing the Tree
You can view the full branching logic here:  
👉 **[View Decision Tree Diagram](./tree/tree-diagram.md)**

---

## 💻 Running the Agent (Part B)

If you have Python installed, you can run the reflection tool locally:

1. Clone the repo:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/daily-reflection-tree.git](https://github.com/YOUR_USERNAME/daily-reflection-tree.git)
