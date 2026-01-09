# Singapore Phone Number Generator

A Python script to generate all possible Singapore mobile and landline phone numbers.

## Description

This project generates comprehensive lists of valid Singapore phone numbers based on the official numbering plan. It creates text files containing all possible combinations for PSTN/residential lines (6xxx), mobile/data services (8xxx), and mobile/pager numbers (9xxx). Useful for testing, data validation, or educational purposes.

## Features

- Generates all 6xxx xxxx numbers (Public Switched Telephone Network and Residential IP Telephony Services)
- Generates all 8zxx xxxx numbers (Mobile, Data Services, New Numbers, and Prepaid Numbers)
- Generates all 9yxx xxxx numbers (Mobile, Data Services, and Pager)
- Outputs to separate text files for easy access

## Technologies Used

- Python 3.x

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/sgNumbers2020.git

# Navigate to project directory
cd sgNumbers2020
```

## Usage

```bash
# Run the script
python numbers.py
```

This will generate three text files:
- `six.txt` - Contains 6xxx xxx numbers (6000000 to 6999998)
- `eight.txt` - Contains 8zxx xxxx numbers (81000000 to 89999998)
- `nine.txt` - Contains 9yxx xxxx numbers (90000000 to 98999998)

### Number Format Reference

| Prefix | Range | Service Type |
|--------|-------|--------------|
| 6xxx xxx | 6000000 - 6999998 | PSTN and Residential IP Telephony |
| 8zxx xxxx | 81000000 - 89999998 | Mobile, Data Services, New Numbers, Prepaid |
| 9yxx xxxx | 90000000 - 98999998 | Mobile, Data Services, Pager |

**Note:** z denotes 1-9 only, y denotes 0-8 only

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
