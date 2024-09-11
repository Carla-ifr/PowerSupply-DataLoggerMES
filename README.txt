# ----------------------------------------------------------------------
#  Power Supply and Datta Logger Prototype (PSLer) hardware and software
# ----------------------------------------------------------------------

PSLer is a cost-effective system designed to enhance microbial electrolysis 
by delivering and capturing voltage using commercial boards and open-source 
codes. 
It includes an automatic monitoring device with a Power Supply Unit, 
Arduino UNO, and ADS1256 boards. 

The prototype offers a flexible alternative to expensive commercial devices, 
facilitating efficient microbial electrolysis research while reducing costs 
and fostering interdisciplinary collaboration.

The PSLer is equipped with 4 sensors (2-wire sensor each), allowing it to 
simultaneously monitor 4 different experiments.

The circuit sensor for electrical signals can be adapted to accommodate up to
4 pairs of electrodes MES, in case multiple-electrode MES is required.

The PSLer prototype is adapted to reach a maximum input voltage of 1.25 V. 
Maintaining an external voltage within this range is crucial for scaling up 
MES reactors as they can harness energy from renewable sources like wind, solar, 
and biomass to close the sustainable cycle.


Folder description:

1. PSLer_AR: Arduino IDE code (code 1) that sense and record electrical signals.
   Modified from https://github.com/adienakhmad/ADS1256.git 

2. PSLer_PY: PYTHON code (code 2) that records and saves electrical signals data
in CSV file.
   Modofied from https://doi.org/10.5281/zenodo.12808300

3. PSLer_DescriptionMethod: Is a document with the Step-by-step build instructions. 

Important references:
References
1.	Fernando K. Dá para criar uma empresa disso! [Internet]. Tutoriais Tecnologia Tendencias. 2020. Available from: https://www.fernandok.com/2020/10/da-para-criar-uma-empresa-disso.html
2.	Akhmad A, Sepúlveda A, Axel. ADS1256 [Internet]. 2019. Available from: https://github.com/adienakhmad/ADS1256.git
3.	TI. Very Low Noise , 24-Bit Analog to Digital Converter. Texas Instruments [Internet]. 2013; Available from: https://www.alldatasheet.com/datasheet-pdf/pdf/336384/TI/ADS1256.html
4.	Flores-Rodriguez C. The AGDAC: An Innovative Market-Oriented, Open-Source Multiplexing System for Advanced Biogas Volume Measurements in Research Experiments.  Zenodo. https://doi.org/10.5281/zenodo.12808300  

