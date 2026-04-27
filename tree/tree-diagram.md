graph TD
    START((Start)) --> A1_OPEN[Q: Day's Vibe?]
    
    A1_OPEN --> A1_D1{Decision}
    
    A1_D1 -- Productive/Smooth --> A1_Q_VICTOR[Q: Your Role?]
    A1_D1 -- Frustrating/Out of Control --> A1_Q_VICTIM[Q: First Instinct?]
    
    A1_Q_VICTOR --> A1_R_INTERNAL[Reflection: Internal Locus]
    A1_Q_VICTIM --> A1_R_EXTERNAL[Reflection: External Locus]
    
    A1_R_INTERNAL --> BRIDGE1[Bridge to Axis 2]
    A1_R_EXTERNAL --> BRIDGE1
    
    BRIDGE1 --> A2_OPEN[Q: Interactions Today?]
    
    A2_OPEN --> A2_D1{Decision}
    
    A2_D1 -- Helping/Teaching --> A2_Q_CONTRIB[Q: Motivation?]
    A2_D1 -- Needing Support/Overlooked --> A2_Q_ENTITLE[Q: What was missing?]
    
    A2_Q_CONTRIB --> A2_R_HIGH[Reflection: Contribution]
    A2_Q_ENTITLE --> A2_R_LOW[Reflection: Entitlement]
    
    A2_R_HIGH --> BRIDGE2[Bridge to Axis 3]
    A2_R_LOW --> BRIDGE2
    
    BRIDGE2 --> A3_OPEN[Q: Primary Concern?]
    
    A3_OPEN --> A3_D1{Decision}
    
    A3_D1 -- Workload/Reputation --> A3_Q_SELF[Q: Inward Focus Feel?]
    A3_D1 -- Team/Customer --> A3_Q_ALTRO[Q: Why Big Picture?]
    
    A3_Q_SELF --> A3_R1[Reflection: Self-Centric]
    A3_Q_ALTRO --> A3_R2[Reflection: Altrocentric]
    
    A3_R1 --> SUMMARY[Summary Node]
    A3_R2 --> SUMMARY
    
    SUMMARY --> END((End Session))

    style START fill:#f9f,stroke:#333
    style END fill:#f9f,stroke:#333
    style A1_D1 fill:#fff4dd,stroke:#d4a017
    style A2_D1 fill:#fff4dd,stroke:#d4a017
    style A3_D1 fill:#fff4dd,stroke:#d4a017
