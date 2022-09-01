"""
> Python 3.8.10
> Electromagnetic Spectrum Visualisation
"""
import os,sys,math,matplotlib.pyplot as plt,argparse,numpy as np
from rich.console import Console
from rich import pretty

pretty.install()

class CALCULATOR():
    def __init__(self,console,args):
        (self.console,self.min_frequency,self.max_frequency,self.plancks_quantum_of_action,self.lightspeed,self.frequency_steps) = (
            console,args.min,args.max,args.p,args.lightspeed,args.steps)

    def get_energy(self,frequencies):
        energies = [(self.plancks_quantum_of_action*frequency) for frequency in frequencies]
        return energies

    def get_wavelength(self,energies):
        wavelengths = [((self.plancks_quantum_of_action*self.lightspeed)/(energy)) for energy in energies]
        return wavelengths

class VISUALISE(CALCULATOR):
    def show(self):
        (fig,axs) = plt.subplots(2,1)
        frequencies = np.arange(self.min_frequency,self.max_frequency,self.frequency_steps)
        energies = self.get_energy(frequencies)
        axs[0].plot(frequencies, energies, linewidth=2.0, color="blue")
        axs[0].fill_between(frequencies, energies, where=frequencies, interpolate=True, color='blue',alpha=0.30)
        axs[0].grid(True)
        axs[1].grid(True)
        axs[0].set_xlabel("Frequency in Hz")
        axs[0].set_ylabel("Energie in eV")
        axs[1].set_xlabel("Wavelength in nm")
        axs[1].set_ylabel("Energie in eV")
        wavelengths = self.get_wavelength(energies)
        axs[1].plot(wavelengths,energies,linewidth=2.0,color="red",marker='o')
        axs[1].fill_between(wavelengths, energies, where=wavelengths, interpolate=True, color='red',alpha=0.30)
        plt.show()

#
console = Console()
(default_min_frequency,default_max_frequency,default_plancks_quantum_of_action,default_lightspeed,default_frequency_steps) = (
    1,500,6.6260693*10**-34,299792458,1)
parser = argparse.ArgumentParser()
parser.add_argument('--min', help=f"Minimal frequency in Hz (Default = {default_min_frequency})",
    default = default_min_frequency, type = float
)
parser.add_argument('--max', help=f"Maximal frequency in Hz (Default = {default_max_frequency})",
    default = default_max_frequency, type = float
)
parser.add_argument('-p',help=f"Planck's quantum of action (Default = {default_plancks_quantum_of_action} eV)",
    default = default_plancks_quantum_of_action, type = float
)
parser.add_argument('--lightspeed',help=f"Lightspeed in m/s (Default = {default_lightspeed} m/s)",
    default = default_lightspeed, type = float
)
parser.add_argument('--steps',help=f"'Frequency-steps': decrease/increase accuracy of visualisation (Default = {default_frequency_steps} steps)",
    default = default_frequency_steps, type = float
)
args = parser.parse_args()
pr_help = False
if (args.min == 0):
    console.log(f"[red]Cannot calculate with energy equals zero! [bold red](float division by zero)[/bold red]")
    pr_help = True
if (args.steps == 0):
    console.log(f"[red]The 'Frequency-steps' cannot equals zero!")
    pr_help = True
if (pr_help == True):
    parser.print_help()
    sys.exit()
#

if (__name__ == '__main__'):
    os.system("clear") #
    visualisation = VISUALISE(console,args)
    visualisation.show()
