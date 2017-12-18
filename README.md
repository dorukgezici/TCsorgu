# TCsorgu
[![PyPI](https://img.shields.io/pypi/v/TCsorgu.svg)]() [![PyPI](https://img.shields.io/pypi/status/Django.svg)]() [![PyPI](https://img.shields.io/pypi/l/TCsorgu.svg)]()

TC Identity Number Check

## Installation
- `pip3 install TCsorgu`

## Usage as CLI
- `TCsorgu <id> <name> <surname> <birth_year>`
- Returns and prints bool (True or False)
- To see the parameters: `TCsorgu --help`

## Usage as Package
- `from TCsorgu import check_tc_id`
- `is_valid = check_tc_id(id, name, surname, birth_year)`
