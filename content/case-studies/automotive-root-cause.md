# Case Study: AI Root Cause Analysis for Automotive Manufacturing

## Part 1: The STAR Analysis

### Situation
A major automotive truck manufacturer was facing bottlenecks on the assembly floor. When a truck failed its final quality check, senior technicians had to manually trace through thousands of sensor logs and assembly records to find the defective component. This process took an average of **6.5 hours per vehicle**, and with 50+ trucks in the queue, it was causing catastrophic delivery delays.

### Task
Implement an intelligent Root Cause Analysis (RCA) system that enables shop floor employees to isolate defects instantly without waiting for senior engineering intervention.

### Action
I architected a specialized AI diagnostic platform:
- **Real-time Log Ingestion:** Streamed data from 400+ assembly point sensors into a centralized processing hub.
- **Pattern Matching AI:** Trained an anomaly detection model on five years of historical "failure patterns" to recognize the digital signature of specific component defects (e.g., fuel pump misalignment, wiring harness friction).
- **Shop Floor Interface:** Developed a ruggedized "Natural Language" interface where workers could input mobile symptoms (e.g., "Air pressure drop in Zone B") and receive a prioritized list of likely defect points with high-probability "Fix Suggestions."
- **Knowledge Capture Loop:** Built a feedback mechanism where successful fixes were tagged back into the training set, allowing the AI to learn from the floor employees' manual corrections.

### Result
- **85% Reduction** in defect isolation time—from 6.5 hours to 45 minutes.
- **20% Increase** in daily assembly throughput.
- **Zero-Wait Diagnostic:** Shop floor employees now handle 90% of failures independently, reserving senior engineers for complex design-level issues.
- **Significant Cost Reduction:** Eliminated $1.2M in annual overtime costs associated with quality-check backlog.

---

## Part 2: The Story: Empowering the Shop Floor

The breakthrough wasn't just the AI; it was the **Accessibility**. Traditionally, diagnostic data lived in complex databases that only data scientists could read. 

We brought that power to the person holding the wrench.

<div class="chart-container">
    <div id="automotive-time-chart"></div>
    <p style="text-align: center; font-size: 0.9rem; color: #64748b; margin-top: 1rem;"><em>Figure 1: Average hours spent on Defect Root Cause Analysis per truck.</em></p>
</div>

Previously, if a "Pressure Alert" went off, a worker would have to check 15 possible valves. Now, they scan the vehicle VIN, and the system tells them: *"92% Probability: Valve AC-4 is stuck open due to a gasket seal fault observed in Chassis #4492."*

By turning **Data into Directions**, we didn't just speed up the factory; we empowered the employees. The factory floor transition from "Searchers" to "Fixers" was the key to unlocking millions in hidden efficiency.
