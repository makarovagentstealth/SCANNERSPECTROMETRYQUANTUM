import json
import numpy as np
import time

# Constantes de física quântica
h = 6.626e-34  # Constante de Planck, J·s
c = 3e8        # Velocidade da luz, m/s
k_B = 1.381e-23 # Constante de Boltzmann, J/K

def load_payload(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def planck_law(wavelengths, temperature):
    wavelengths_m = wavelengths * 1e-9  # Convertendo nm para m
    exponent = (h * c) / (wavelengths_m * k_B * temperature)
    spectral_radiance = (2 * h * c**2) / (wavelengths_m**5) * 1 / (np.exp(exponent) - 1)
    return spectral_radiance

def generate_spectrometry(density_range, spectrometry_parameters, temperature):
    min_density = density_range['min']
    max_density = density_range['max']
    
    wavelength_start = spectrometry_parameters['wavelength_start']
    wavelength_end = spectrometry_parameters['wavelength_end']
    resolution = spectrometry_parameters['resolution']
    
    wavelengths = np.arange(wavelength_start, wavelength_end, resolution)
    density_spectrum = np.random.uniform(min_density, max_density, size=wavelengths.shape)
    
    # Aplicando a lei de Planck para cada comprimento de onda
    planck_spectrum = planck_law(wavelengths, temperature)
    
    return wavelengths, density_spectrum, planck_spectrum

if __name__ == "__main__":
    payload = load_payload('payload.json')
    density_range = payload['density_range']
    spectrometry_parameters = payload['spectrometry_parameters']
    temperature = payload['temperature']
    
    try:
        while True:
            wavelengths, density_spectrum, planck_spectrum = generate_spectrometry(density_range, spectrometry_parameters, temperature)
            print("\nWavelengths (nm):", wavelengths)
            print("Density Spectrum:", density_spectrum)
            print("Planck Spectrum:", planck_spectrum)
            time.sleep(1)  # Simulating some processing delay
    except KeyboardInterrupt:
        print("\nReal-time spectrometry scan stopped.")
      
