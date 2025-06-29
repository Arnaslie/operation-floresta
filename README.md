## Ancient Footprints, Modern Pathways to Sustainability
AI-Guided Discovery of Amazonian Dark Earths and Earthworks in the Upper Xingu

The **Upper Xingu** region of Brazil, long inhabited by the **Kuikuro** and other Xinguano groups, holds one of the most intricate pre-Columbian landscapes in Amazonia—marked by ringed settlements, canals, engineered soils (ADE), and forest management systems. While prior studies have illuminated the spatial logic of these "garden cities," much of the region remains **unmapped** and **underexplored**.

This project introduces a **novel AI-assisted pipeline** to identify potential new archaeological sites in the Upper Xingu, focusing on the prediction of **Amazonian Dark Earth (ADE)** zones and **earthworks**. By combining:
- **Synthetic test sites generation**
- **Remote sensing**  
- **Machine learning**  
- **GPT-4–based generative reasoning**,  

we build a replicable framework that links Indigenous settlement logic to environmental signatures—enhancing archaeological discovery while honoring cultural context.

---

## Methods Overview
### Synthetic Test Generation: 
We use GPT to select locations based on regional terrain, settlement logic, and environmental patterns drawn from its knowledge base.

### Remote Sensing
We use publicly available environmental data collected via satellite or airborne platforms to extract relevant features:
- **Sentinel-2 imagery** for vegetation indices (NDVI, BSI, NDBI)
- **LiDAR-derived DEM** for elevation and slope
- **WorldClim v3** for climate variables (temperature, precipitation, seasonality)
- **ISRIC SoilGrids** for soil composition (clay %, pH, carbon content)

---

### Training Data
- 2,021 labeled sites from Walker et al. (2022), categorized as:
  - 455 ADE  
  - 1,253 Earthworks  
  - 373 Non-sites

### Feature Matrix (32 Total Variables)
- **Soil**: clay %, organic carbon, pH, bulk density, cation exchange capacity  
- **Hydrology**: distance to major/minor rivers, slope-based drainage index  
- **Climate**: 19 bioclimatic variables from 1970–2000  
- **Topography**: LiDAR-derived elevation & slope  
- **Vegetation**: NDVI, NDBI, BSI (from Sentinel-2)  
- **Accessibility**: distance to roads, remoteness index  

---

### Machine Learning Model
- **Model**: Random Forest classifier  
- **Training**: Stratified 5-fold cross-validation  
- **Target**: Multiclass label — `ADE`, `earthwork`, or `non-site`  
- **Interpretability**: SHAP values to identify important predictors:
  - River distance  
  - Soil carbon  
  - Vegetation index stability  
  - Elevation  

---

### Novelty: GPT-Generated Test Site Coordinates ✨

We used **GPT-4** to generate **50 hypothetical site coordinates** in the Upper Xingu, simulating culturally and environmentally plausible locations not included in the training data. This step served two purposes:

1. **Synthetic Test Generation**: GPT selected locations based on regional terrain, settlement logic, and environmental patterns drawn from its knowledge base.
2. **Post-prediction Reasoning**: For top-ranked predictions, GPT performed qualitative reasoning to interpret spatial plausibility based on cultural patterns and terrain resemblance to known sites.

This dual application of GPT represents a **novel method** in archaeological discovery—combining structured prediction with semantic interpretation.

---

### Proposed Field Validation
Top candidate sites are intended for future collaborative validation with:
- **Kuikuro Institute for Indigenous Technology (IKTI)**
- **Museu Paraense Emílio Goeldi**

Proposed methods include:
- Drone-based LiDAR scanning  
- Soil sampling (for ADE confirmation)  
- Oral history integration with local knowledge holders  


