# Package Sorter for Robotic Automation Factory

## Overview

This project implements a package sorting function for Thoughtful's robotic arm, which dispatches packages into the correct stack based on their dimensions and mass. It utilizes the `pint` library for type-safe unit handling and provides sorting rules based on specific criteria.

## Sorting Criteria

- **Bulky Package**: A package is considered bulky if:
  - Its volume is greater than or equal to 1,000,000 cm³, OR
  - Any of its dimensions (width, height, or length) exceeds 150 cm

- **Heavy Package**: A package is considered heavy if:
  - Its mass is greater than or equal to 20 kg

## Installation

To get started with the Package Sorter:

1. Clone the repository:
```bash
git clone <repo-url>
cd package_sorter
```
2. Install the required dependencies using Poetry:
```bash
poetry install
```

## Usage
Import the sorting function and use it in your code:

```pthon
from package_sorter.sorter import sort, Stack

result = sort(width_cm=100, height_cm=50, length_cm=80, mass_kg=15)
print(f"The package should be placed in the {result.value} stack.")
```
## Runnint Tests
To run the test suite:

```bash
poetry run pytest
```
