# NVDB Road Network Analysis

## Project Overview

This project demonstrates the acquisition and inspection of Norwegian road network data from the National Road Database (NVDB) using the official NVDB API V4 and Python.

The project focuses on geodata processing, transport network data, API usage, and preparation of road network data for GIS-based quality assurance and analysis.

---

## Objectives

- Retrieve road network data from NVDB API
- Inspect and process JSON geodata in Python
- Explore road network attributes and geometry
- Understand how transport network data can be integrated into GIS workflows
- Demonstrate skills relevant to geodata management and quality assurance

---

## Study Area

Bergen Municipality (4601), Norway

---

## Data Source

- National Road Database (NVDB) API V4
- Bergen road network segments

---

## Workflow

NVDB API  
↓  
JSON Download  
↓  
Python Processing  
↓  
Geometry Inspection (WKT)  
↓  
GIS Integration  
↓  
Quality Assurance

---

## Python Tasks

### Read NVDB JSON Data

```python
import json

with open("response_1784412846986.json", "r") as f:
    data = json.load(f)


## Workflow Example

The screenshot below shows the process of loading NVDB road network data, inspecting attributes and extracting road geometry using Python.

screenshots_nvdb_workflow.png
