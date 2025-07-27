[![Author](https://img.shields.io/badge/author-Pulsar7-lightgrey.svg?colorB=9900cc&style=flat-square)](https://github.com/Pulsar7)
[![Release](https://img.shields.io/github/release/dmhendricks/file-icon-vectors.svg?style=flat-square)](https://github.com/Pulsar7/Electromagnetic-Spectrum-Visualisation/releases)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/dmhendricks/file-icon-vectors.svg?style=social)](https://twitter.com/SevenPulsar)

# Visualisation of the electromagnetic spectrum

## :pushpin: Table of contents

* :point_right: [Explanation](#explanation)
* :point_right: [Installation](#installation)
* :point_right: [Example](#example)
* :point_right: [ToDo](#todo)
* :point_right: [Suggestions & Reports](#suggestions--reports)

## Explanation

Frequencies in the specified interval (e.g.: 0.1 to 1 Hz) are used to calculate information about these electromagnetic waves. These include: wavelength and energy.

## Installation

:small_orange_diamond: **Download Repository & Requirements**
    
    sudo apt install git
    git clone https://github.com/Pulsar7/Electromagnetic-Spectrum-Visualisation.git
    pip3 install rich matplotlib
    
:small_orange_diamond: **Asking for help**

    python3 electromagnetic_spectrum_visualisation.py --help

## Example

    python3 electromagnetic_spectrum_visualisation.py --min 0.1 --step 0.1 --max 1
    

**Output:**

![](https://github.com/Pulsar7/Electromagnetic-Spectrum-Visualisation/blob/main/github_output_example.png)
    
## ToDo

- [ ] Add Animations
