# Time to take action! New participatory (GIS) approaches and current GIS practices for disaster risk reduction and anticipatory action
This project is a final assignment for a class at the University of Heidelberg Geographical Institute in conjunction with HeiGIT.

## Assignment
Tasked with either a literature review or a small project and accompanying report of 2000-3000 words, I came up with a relatively large task. Namely, my idea was to write a python script or QGIS Plug-In that would allow for a multi-modal Reachability Analysis involving schedule based public transport in an urban healthcare accessibility context. I specifically chose Heidelberg as an area of interest for an anylysis both due to data availability as well as to my on the ground knowledge of the area that would provide useful sanity checks of the data. However I had fast arrived at the conclusion that such a task might overshoot a project-paper of 2000-3000 words. One of the main issues I encountered was consistent data availability in sensible formats including stations, departures, and routes. Therefore this project's scope reduced a bit and will focus on data processing and assesment as well as the first steps of a reachability analysis

## Tasks
* Process available public transit data for the Heidelberg region
    + deal with GTFS files
        + find stop locations ✅
        + process route information
    + display station locations on a map ✅
    + quality assesment ✅
        - assess against personal knowledge of the area, find deficits ✅
        - assess against OSM data ✅
* Pull Hospital Locations from OSM Data within selected region ✅
    + display hospital locations against a map ✅
    + quality assesment ✅
        - ohsome data quality tools ✅ (but was unhelpful)
        - personal knowledge ✅
* Reachability Analysis
    + get walking-isochrones from ORS ✅
    + find stations within walking-isochrone ✅
    + display on map ✅

## Stretch Goals
* public transport routing
    + Combine walking times (from ORS) with station departures to find reachable departures
    + find previous stops within time limit
    + walking isochrones based on remaining time
    + iterate until timelimit is reached
    + automate GTFS processing (without quality assesment)
* Optimisation
    + pre-process routing data as a network that interacts with the street network
        - stations as nodes with geolocation
        - find useful algorithm

## Data Sources
 LGL (2017): Kreise. https://www.lgl-bw.de/Produkte/Open-Data/#Vektordaten
 
 RNV (2022). Soll-Fahrplandaten RNV. https://gtfs-sandbox-dds.rnv-online.de/latest/gtfs.zip.
 
 VRN GmbH (2022). Archiv der Soll-Fahrplandaten (GTFS Archiv). https://www.vrn.de/opendata/datasets/archiv-der-soll-fahrplandaten-gtfs-archiv.

