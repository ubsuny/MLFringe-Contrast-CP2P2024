import random

def simulate_experiment(parameters, num_measurements):
    """Simulate neutron beam experiment with random variations.

    Args:
        parameters (dict): Dictionary containing experiment parameters.
        num_measurements (int): Number of measurements to simulate.

    Returns:
        dict: Dictionary with simulated measurements for each parameter.
    """
    simulated_measurements = {param: [] for param in parameters}

    for _ in range(num_measurements):
        for param, value_info in parameters.items():
            value = value_info['value']
            uncertainty_factor = value_info['uncertainty_factor']
            
            variation = value * uncertainty_factor
            simulated_value = value + random.uniform(-variation, variation)
            simulated_measurements[param].append(simulated_value)

    return simulated_measurements

# Example usage:
experiment_parameters = {
    'baseline_intensity': {'value': 1000.0, 'uncertainty_factor': 0.05},
    'grating_thickness': {'value': 2.0, 'uncertainty_factor': 0.02},
    'detector_efficiency': {'value': 0.95, 'uncertainty_factor': 0.01},
    'beam_alignment': {'value': 1.5, 'uncertainty_factor': 0.03},
    # Add more parameters as needed
}

num_measurements = 50

simulated_results = simulate_experiment(experiment_parameters, num_measurements)
print(simulated_results)
