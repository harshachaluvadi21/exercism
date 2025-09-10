"""
Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """
    Calculate the exchanged value of foreign currency you can receive.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate how much of your original currency you have left after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - remaining amount of your starting currency.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of a given number of bills of a certain denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated total value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate the number of bills obtainable from the amount, based on denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of full bills that can be obtained.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount that cannot form a full bill of given denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum exchangeable value in whole bills after applying the spread.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum exchangeable value (in whole bills).
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    exchanged_amount = exchange_money(budget, effective_rate)
    number_of_bills = get_number_of_bills(exchanged_amount, denomination)
    return get_value_of_bills(denomination, number_of_bills)
