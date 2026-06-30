# Customer Segmentation Analysis (iFood Dataset)

This project applies **K-Means Clustering** and **Principal Component Analysis (PCA)** to segment a customer base into 4 distinct strategic archetypes. This allows marketing teams to transition from generic generic campaigns to hyper-targeted, high-conversion strategies.

---

## 👥 Customer Segments (The 4 Clusters)

The unsupervised learning model segments the customer base using three structural features: `Income`, `MntTotal` (Total Spend), and `In_relationship`. The data splits into the following quadrants:

* **🥇 Cluster 0 (High-Value Partners):** High-income households living with a partner. They show maximum expenditure across premium categories, heavily skewed toward **Wine** and **Meat Products**. (The primary revenue engine of the business).
* **🥈 Cluster 1 (Affluent Singles):** High-income single individuals (Single, Divorced, or Widowed). They bypass bulk buying and strictly prioritize premium single-serve luxury items, agility, and convenience.
* **🥉 Cluster 2 (Budget-Bound Households):** Low-income households living with partners and dependents (`Kidhome`/`Teenhome`). They have a high digital footprint (`NumWebVisitsMonth`) but possess extreme price elasticity—converting almost exclusively when targeted with a discount (`NumDealsPurchases`).
* **☠️ Cluster 3 (Value-Seeking Singles):** Lower-income single individuals. They show minimal basket sizes across all operational SKU categories and display zero brand loyalty.

---

## 🛠️ Data Audits & Fixed Code Bugs

Two major architectural flaws from the exploratory pipeline were identified and documented for refactoring:

1. **Boxplot Text Overlap Bug (Fixed):** The original script utilized a data index mapping loop (`for i in range(...)`) over single-variable vertical boxplots. Because Seaborn anchors vertical distributions strictly at the $X=0$ coordinate, this loop scattered raw data strings horizontally across the frame up to $X=2200+$, breaking chart legibility. **Fix:** This loop must be completely stripped out of production plotting blocks.
2. **Feature Circularity Redundancy:** `MntTotal` is an exact mathematical aggregate of individual product category spends. Clustering on an aggregate total and subsequently evaluating child product habits creates a circular analytical dependency. Future optimization scales better by clustering directly on independent product features.

---

## 📈 Strategic Recommendation Matrix

| Target Cluster | Core Business Mandate | Product & Inventory Strategy | Optimal Activation Channel |
| :--- | :--- | :--- | :--- |
| **Cluster 0** | Customer Lifetime Value Lock-in | High-end Wine bundles, premium meat curation boxes | Direct Catalogs & Premium In-Store Updates |
| **Cluster 1** | Margin Optimization | High-end ready meals, artisanal single-serve luxury items | Mobile App Push Notifications & Web Checkout |
| **Cluster 2** | Basket Size Scaling | Multi-packs, private label groceries, target value packs | Email Campaigns loaded with dynamic Coupon Codes |
| **Cluster 3** | Excess Stock Liquidation | Low-margin items, extreme clearance sales, loss-leaders | Programmatic Social Media Ad Remarketing |