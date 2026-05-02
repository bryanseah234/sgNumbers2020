# PRD: sgNumbers2020

## Overview
A Python script that generates all valid Singapore mobile and landline phone number ranges and writes them to text files. Based on IDA (IMDA) number allocation rules: 6xxx-xxxx (PSTN), 8zxx-xxxx (mobile, z=1-9), 9yxx-xxxx (mobile, y=0-8). Educational tool showing the enumerable nature of Singapore's number system.

## Goals
- Generate all 6-prefix landline numbers (6,000,000 – 6,999,999)
- Generate all 8-prefix mobile numbers (81,000,000 – 89,999,999)
- Generate all 9-prefix mobile numbers (90,000,000 – 98,999,999)
- Write to `six.txt`, `eight.txt`, `nine.txt`

## Non-Goals
- Phone number validation or lookup
- Carrier identification (see sgPhoneNumbers65)
- Network requests

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: stdlib only

## Architecture
```
sgNumbers2020/
├── numbers.py    # Generates three number range files
├── six.txt       # Output: 6xxx range
├── eight.txt     # Output: 8xxx range
└── nine.txt      # Output: 9xxx range
```

## Deployment / Run
```bash
python numbers.py
```

## Constraints & Notes
- **Legal**: generating a number list is legal; using it for unsolicited calls/SMS is not (PDPA, Spam Control Act)
- **Output size**: ~1M lines each file; ~8MB each
- **Range rules**: 9y uses y=0-8 only (y=9 not allocated as of script creation); 8z uses z=1-9
