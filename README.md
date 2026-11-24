# Programmeerimisest maalähedaselt (MTAT.TK.006)

Python solutions and practice code for the University of Tartu course **Programmeerimisest maalähedaselt** (MTAT.TK.006), autumn 2024.

The course material is available at <https://courses.cs.ut.ee/2024/progmaa/fall/Main/>.

## Structure

The code is organised by week. Each folder contains the following kinds of files:

| Type | Name pattern | Purpose |
|---|---|---|
| Control task | `... - kontrollülesanne <number>.py` | Graded weekly task |
| Extra task | `Lisaülesanne ... .py` | Optional additional task |
| Practice | `<week> nädala proovid.py` | Examples from the course pages, mostly commented out so they can be enabled one by one |
| Test | `<week> nädala test.py` | Practice for the weekly test (code-reading questions) |

```
.
├── 9 september - 15 september/
├── 16 september - 22 september/
├── 23 september - 29 september/
├── 30 september - 6 oktoober/
├── LICENSE
└── README.md
```

## Contents

### Week 1 (9 – 15 September): variables and data types

| File | Description |
|---|---|
| `Muutujad - kontrollülesanne II.py` | Builds and prints a sentence from variables ("2024. aasta puu on tamm") |
| `küpsisetort.py` | Cookie cake: calculates how many cookies and how many packs are needed from tray size, layers and pack size |
| `proovid esimene nädal.py` | Course examples on programs, variables and data types |
| `esimese nädal test.py` | Test practice, including extracting the birth month from an Estonian personal ID code |

### Week 2 (16 – 22 September): conditionals, strings and turtle

| File | Description |
|---|---|
| `Valikulause - kontrollülesanne III.py` | Determines gender ("He" or "She") from the first digit of a personal ID code |
| `Sõned - kontrollülesanne IV.py` | Asks for first and last name and prints them in upper case |
| `Lisaülesanne Eurod ja sendid.py` | Converts cents to euros and cents with correct Estonian singular and plural forms |
| `Lisaülesanne Nädalapalk.py` | Weekly pay calculation with 1.5 times pay for hours over 40 |
| `teise nädala proovid.py` | Course examples on conditionals, strings and turtle graphics. Ends with a turtle program that draws a circle in a random colour |
| `teise nädala test.py` | Test practice, ends with a short turtle drawing |

### Week 3 (23 – 29 September): loops and regular expressions

| File | Description |
|---|---|
| `Tsükkel - kontrollülesanne V.py` | Calculates the total number of logs in a stack of rows (1 + 2 + ... + n) with a `while` loop |
| `Regulaaravaldis - kontrollülesanne VI.py` | Checks with a regular expression whether input is an Estonian personal ID code |
| `Lisaülesanne Autonumber.py` | Checks with a regular expression whether input is an Estonian licence plate (3 digits and 3 letters) |
| `Lisaülesanne Supp.py` | Simulates soup cooling for 10 minutes (19 % of the temperature difference to the room per minute) |
| `kolmanda nädala proovid.py` | Course examples on `while` loops. Ends with a number guessing game |
| `kolmanda nädala test.py` | Test practice with loops, powers and regular expressions |

### Week 4 (30 September – 6 October): functions and files

| File | Description |
|---|---|
| `Funktsioonid - kontrollülesanne VII.py` | Function that calculates the distance a ship travels in a day from its speed in knots |
| `Lisaülesanne Pere sissetulek 2017.py` | Monthly family income: net pay of both parents (tax-free minimum 170, income tax 20 %) plus 50 per child |
| `neljanda nädala proovid.py` | Course examples on functions. Ends by reading a text file from the web |
| `neljanda nädala test.py` | Test practice with functions and writing to a file |
| `andmed.txt` | Example file for the file-writing exercise (username and password) |

## Requirements

- Python 3.8 or newer
- `tkinter`, which is needed by the `turtle` module. It is included in the standard Python installers for Windows and macOS. On Debian and Ubuntu install it with `sudo apt install python3-tk`
- Internet access for `neljanda nädala proovid.py`, which downloads a text file from `kodu.ut.ee`

No additional packages are required.

## Running

File names contain spaces and Estonian letters, so put them in quotes:

```bash
python3 "9 september - 15 september/küpsisetort.py"
```

Most programs ask for input in the terminal. Programs that use `turtle` open a drawing window, which closes on click.

The `proovid` and `test` files are mostly commented out. To try an example, remove the leading `#` characters from the block you want to run.

## Notes

- The code and comments are in Estonian.
- Many lines in the `proovid` and `test` files were commented out on purpose, because they show errors (for example, a syntax error or a function used before it is defined) or have no output.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
