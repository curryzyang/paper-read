# Explainable Geospatial AI for Satellite Ground Station Siting Using LiDAR-Derived Terrain Intelligence

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Shohini Sarkar, Smithi Mahendran, Rishi Chudasama, Varun Mannam, Arav Luthra, Yuvraj Rekhi, Vivek Nadig, Arsh Goenka
- 机构：University of Maryland, College Park
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14127v1) · [PDF](https://arxiv.org/pdf/2607.14127v1)

## TLDR
The paper presents an interpretable, globally deployable machine learning framework that predicts representative clutter height from open geospatial data using LiDAR-derived labels, achieving a mean absolute error of 1.79 meters and reducing error by over 60% relative to traditional fixed ITU-R clutter defaults for satellite ground station siting and spectrum coordination.

## Abstract
Representative clutter height (RCH) is a key parameter in radio propagation and interference analysis because it captures the dominant height of local obstructions that drive terminal clutter loss. Current practice often relies on fixed clutter heights assigned to land use classes in Recommendation ITU-R P.452-18, but this misses within class variation and can lead to conservative exclusion zones and poor site ranking for low Earth orbit ground station siting and spectrum coordination. We present an interpretable, globally deployable machine learning framework for predicting RCH from open geospatial data. The model is trained using LiDAR derived labels from the U.S. Geological Survey 3D Elevation Program and inference time features from global land-cover, terrain, demographic, thermal, and optical remote sensing products. We define RCH using a robust 75th percentile clutter height statistic, evaluate multiple regressors, and select LightGBM for its accuracy, efficiency, and compatibility with feature attribution analysis. The final model achieves a mean absolute error of 1.79m and an R^2=0.765, reducing absolute error by more than 60% relative to the ITU baseline. Beyond aggregate fit, we evaluate domain facing criteria relevant to RF planning, including meter scale error, tolerance band accuracy, over and under estimation tails, agreement with ITU clutter height regimes, and SHAP-based physical plausibility. SHAP identifies tree canopy cover, land-cover semantics, and spectral reflectance as the most influential predictors. Studies on segmentation derived features, non-forest ablations, and land-cover matched international validation show that open geospatial data can improve clutter modeling at scale without sacrificing interpretability or deployability.
