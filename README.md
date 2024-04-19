# UnsteadyConduction

## Introduction

"1D_UnsteadyConduction.py" and "2D_UnsteadyConduction.py" are python scripts written by Spencer Kenison to predict the temperature distribution due to unsteady heat conduction. The programs were written for MAE 5440 at Utah State University.

## Requirements

The scripts were written using Python 3.11 interpreter but any similar 
version should function normally.

The scripts require the following libraries to be installed:
- numpy
- matplotlib.pyplot
- math
- tqdm
- timeit
using PIP or other package-management system.

## Warnings

Running simulations of higher grid sizes (>50x50) can result in long runtimes. A 100x100 grid took upwards of 2 hours during testing.

## Running program

Run the scripts using a Python interpreter. They can be run
in terminal using a command such as "py 2D_UnsteadyConduction.py" command or from IDE such as VSCode.

Both programs generate temperature over time plots at two points along the temperature distribution in addition to a temperature distribution plot. The plots will be saved to the computer in the folder where the Python file is ran.

Different variable in the programs can be varied to model differing situations including:
- Temperature range
- X/Y Range
- Time period
- Thermal conductivity




