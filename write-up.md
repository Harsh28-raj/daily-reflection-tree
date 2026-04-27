# Design Rationale: The Daily Reflection Tree

## 1. Choice of Questions
The questions were designed to move from **observation** to **introspection**. Instead of asking "Did you have a good day?", the tree asks "How would you describe the vibe?". This subtle shift avoids binary (Yes/No) thinking and forces the user to categorize their experience.

- **Axis 1 (Locus):** Questions focus on the *reaction* to events. By asking what their first instinct was during chaos, we surface whether they feel like a 'passenger' (External) or a 'driver' (Internal).
- **Axis 2 (Orientation):** Questions are framed around *interactions*. Entitlement is often invisible, so I used options that highlight "feeling overlooked" versus "proactive sharing" to make the distinction clear without being accusatory.
- **Axis 3 (Radius):** Questions target the *focus of stress*. Under pressure, humans naturally zoom in. The options guide them to see if their concern was purely self-preservation or if it included the team/customer.

## 2. Branching Logic & Trade-offs
The tree uses a **Deterministic Branching Model**. 
- **Trade-off:** I chose *Fixed Options* over free-text. While free-text feels more natural, fixed options ensure the data is "crisp and auditable." It removes the risk of LLM hallucinations and ensures the user stays within the psychological framework.
- **Decision Nodes:** These are invisible to the user. They act as a logic gate that tallies the user’s "Signals" to ensure the final reflection feels personalized.

## 3. Psychological Grounding
The design is rooted in three core frameworks:
- **Locus of Control (Julian Rotter, 1954):** Used to distinguish between those who believe they influence events vs. those who blame external circumstances.
- **Growth Mindset (Carol Dweck):** Embedded in Axis 1 to see if challenges are viewed as development opportunities.
- **Self-Transcendence (Abraham Maslow, 1969):** The foundation for Axis 3, identifying that the highest level of human maturity is orienting toward a purpose beyond the self.
- **Organizational Citizenship Behavior (Organ, 1988):** The basis for Axis 2, measuring discretionary effort that goes beyond formal requirements.

## 4. Future Improvements
Given more time, I would:
1. **Longitudinal Analysis:** Track signals over weeks to show the user a "Growth Trend" (e.g., "Your agency has increased by 20% this month").
2. **Contextual Templates:** Create specific trees for different roles (e.g., a Sales-specific tree vs. an Engineering-specific tree).
3. **Multi-Signal Weighting:** Use more complex decision nodes that look at answers across *all* axes before giving a reflection, rather than axis-by-axis.
