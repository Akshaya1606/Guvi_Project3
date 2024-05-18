
# Airbnb Analysis

This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.


## Problem Statement

- Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.

- Develop a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
- Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.
- Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
- Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.
- Create interactive visualizations that enable users to filter and drill down into the data.
- Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.

## Solution Approach

-  Data Cleaning and Preparation: Clean the Airbnb dataset by handling missing values, removing duplicates, and transforming data types as necessary. Prepare the dataset for EDA and visualization tasks, ensuring data integrity and consistency.

- Geospatial Visualization: Develop a streamlit web application that utilizes  the geospatial data from the Airbnb dataset to create interactive maps. Visualize the distribution of listings across different locations, allowing users to explore prices, ratings, and other relevant factors.

- Price Analysis and Visualization: Use the cleaned data to analyze and visualize how prices vary across different locations, property types, and seasons. Create dynamic plots and charts that enable users to explore price trends, outliers, and correlations with other variables.

- Location-Based Insights: Investigate how the price of listings varies across different locations.  Visualize these insights on interactive maps or create dashboards in tools like Tableau or Power BI.

- Interactive Visualizations: Develop dynamic and interactive visualizations that allow users to filter and drill down into the data based on their preferences. Enable users to interact with the visualizations to explore specific regions, property types, or time periods of interest.

- Dashboard Creation: Utilize Power BI to create a comprehensive dashboard that presents key insights from your analysis. Combine different visualizations, such as maps, charts, and tables, to provide a holistic view of the Airbnb dataset and its patterns.
## Streamlit Dashboard Features

- Mimic the original AIRBNB Website
-  Insight from the data
- Able to get price and details of the Property
- Geovisualisation of the Property

## Power BI Dashboard

- Stay Details Comparison
- Property type Distribution
- Review Based Trends
## Features

- User Friendly
- Dynamic performance
- Colourful Theme
- Visually Attractive
- Valuable Insights from the visuals
## Installation

Install following packages

```bash
import pandas as pd
import json
import os
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
```
    
## Deployment

To deploy this project run

```bash
  streamlit run airbnb.py
```


## Demo

Link of the project demo video

https://www.linkedin.com/feed/update/urn:li:activity:7197642518342082560/

