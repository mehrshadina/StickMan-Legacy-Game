# StickMan-Legacy-Game
This Git repository contains a simple game management system written in Python. The system simulates a game where you manage an army to fight a dragon and mine resources.
Table of Contents

    Introduction
    Code Structure
    Functions
    Usage
    License

Introduction

The code simulates a game environment where the player manages an army and resources. The player can recruit soldiers, mine resources, and fight against a dragon.
Code Structure

The code consists of the following components:

    Variables and Initialization
    Functions for Game Logic
    Input and Output Processing

Functions

    add_soldier
        Adds a soldier to the army.

    add_miners
        Adds miners to the workforce.

    damage_soldier
        Deals damage to a soldier in the army.

    get_enemy_status
        Gets the current status of the enemy (dragon).

    get_army_status
        Gets the current status of the player's army.

    get_money_status
        Gets the current amount of money (coins).

    get_cost
        Gets the cost of recruiting a soldier.

    get_power
        Gets the power of a soldier.

    get_power_delay
        Gets the delay factor for a soldier's power.

    get_health
        Gets the health of a soldier.

    get_role_index
        Gets the index of a soldier's role.

    income_coins
        Updates the player's coins based on income from mining and other sources.

    dragon_damages
        Calculates damage to the dragon based on the player's army.

    process_request
        Processes a request based on the input command.

    process_requests
        Reads input commands from a file and processes them.

Usage

To use the game management system, follow these steps:

    Ensure you have Python installed on your system.
    Clone or download this repository to your local machine.
    Run the process_requests function with the appropriate input and output file paths.

Example usage:

python

input_file = "input.txt"
output_file = "output.txt"
process_requests(input_file, output_file)

License

This project is licensed under the MIT License - see the LICENSE file for details.
