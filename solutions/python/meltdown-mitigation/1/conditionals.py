"""
Functions to prevent a nuclear meltdown.
"""


def is_criticality_balanced(temperature, neutrons_emitted):
    """
    Verify if the reactor is in a balanced critical state.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_emitted: int or float - neutrons emitted per second.
    :return: bool - is criticality balanced?

    Conditions:
    - temperature < 800 K
    - neutrons_emitted > 500
    - temperature * neutrons_emitted < 500000
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and (temperature * neutrons_emitted) < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power for 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', 'black').

    Efficiency % = (generated power / theoretical max power) * 100
    """
    generated_power = voltage * current
    efficiency_percentage = (generated_power / theoretical_max_power) * 100

    if efficiency_percentage >= 80:
        return "green"
    elif efficiency_percentage >= 60:
        return "orange"
    elif efficiency_percentage >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    Assess and return the reactor safety status.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for safe operation.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    Rules:
    - 'LOW' if product < 90% of threshold.
    - 'NORMAL' if product within ±10% of threshold.
    - 'DANGER' otherwise.
    """
    product = temperature * neutrons_produced_per_second

    lower_bound = threshold * 0.9
    upper_bound = threshold * 1.1

    if product < lower_bound:
        return "LOW"
    elif lower_bound <= product <= upper_bound:
        return "NORMAL"
    else:
        return "DANGER"
