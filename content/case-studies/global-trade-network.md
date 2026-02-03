# Case Study: Global Trade Network Graph Analysis

## Part 1: The STAR Analysis

<div class="star-grid">
<div class="star-box">
<h3>Situation</h3>
A major logistics client faced a <strong>"black box" supply chain</strong>. They had visibility into Tier 1 suppliers but zero insight into sub-tier dependencies. A disruption in a Tier 3 raw material supplier in Vietnam could silently derail production lines in Germany weeks later.
</div>

<div class="star-box">
<h3>Task</h3>
Map the invisible. Build a graph-based connectivity model to illuminate deep-tier nodes, relationships, and geographic risks across the global trade network, enabling proactive risk management.
</div>

<div class="star-box">
<h3>Action</h3>
I architected a graph solution using <strong>Neo4j</strong> and <strong>AWS</strong>:
<ul>
<li><strong>Data Fusion:</strong> Ingested unstructured trade data (Bills of Lading, customs filings) via Databricks.</li>
<li><strong>Graph Modeling:</strong> Modeled suppliers, ports, and factories as nodes; trade lanes as edges with volume properties.</li>
<li><strong>Risk Propagation:</strong> Algorithms to simulate disruption cascading effects across the graph.</li>
</ul>
</div>

<div class="star-box">
<h3>Result</h3>
<ul>
<li><strong>Mult-Tier Visibility:</strong> Mapped 15,000+ previously hidden sub-tier nodes.</li>
<li><strong>Risk Mitigation:</strong> Identified 12 critical single points of failure deep in the network.</li>
<li><strong>Agility:</strong> Reduced impact analysis time from weeks to minutes during geopolitical events.</li>
</ul>
</div>
</div>

---

## Part 2: The Story: Mapping the Butterfly Effect

<div class="story-split">
<div class="story-text">

The client’s supply chain officer described their problem as "fighting ghosts." They knew disruptions were coming, but they never knew from where until it was too late. My challenge was to turn millions of scattered customs records into a coherent *map of the world*.

We used **Neo4j** to build a knowledge graph where every node represented a physical entity—a factory, a port, a warehouse. But the real magic happened in the edges. We didn't just map "A connects to B"; we mapped "A relies on B for 30% of critical input X."

When a major port strike hit in 2024, while competitors were scrambling to call suppliers, our client’s dashboard lit up red. The system traced the disruption through four layers of the supply chain instantly. They re-routed shipments *before* the bottleneck physically occurred.

> "We stopped reacting to disasters and started predicting them. This graph is the nervous system of our operations."
</div>

<div class="story-plot">

<div id="graph-nodes-chart"></div>
<p style="text-align: center; font-size: 0.8rem; color: #64748b; margin-top: 1rem;"><em>Figure 1: Node Discovery (Tier 1 vs Sub-Tier)</em></p>

</div>
</div>

