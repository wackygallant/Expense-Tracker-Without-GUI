# Expense Tracker (No GUI)

A minimal, file-based expense tracker implemented in Python with no graphical user interface. This repository provides a simple command-line-style core for adding, listing, and persisting expense records.

## Features

- Lightweight, single-user expense tracking
- Simple file-backed repository layer
- Testable modules separated into `models`, `repository`, and `utils`

## Requirements

- Python 3.8+

## Installation

1. Clone the repository:

	git clone <repo-url>
	cd Expense-Tracker-Without-GUI

2. (Optional) Create a virtual environment and activate it:

	python3 -m venv venv
	source venv/bin/activate

3. Install dependencies (if any). This project has no external dependencies by default; if you add packages, create a `requirements.txt` and run:

	pip install -r requirements.txt

## Running the project

Run the main script to exercise the core functionality:

	python main.py

See `test.py` for example usage and quick checks:

	python test.py

## Project layout

- [main.py](main.py) — entry point / simple runner
- [models.py](models.py) — data model(s) for expenses
- [repository.py](repository.py) — persistence and repository logic
- [utils.py](utils.py) — helper utilities used across the project
- [test.py](test.py) — basic runnable tests/examples

## Example

Check `test.py` for a short example of how the modules interact — it demonstrates creating and persisting sample expenses and reading them back.

## Contributing

Contributions are welcome. Open an issue or a pull request with a short description of the change.

## License

This project does not include a license file. If you intend to publish, add a `LICENSE` file (for example, the MIT license).

## Contact

If you have questions, open an issue in the repository.

