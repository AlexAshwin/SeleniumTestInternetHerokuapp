# Selenium Test Automation – the-internet.herokuapp.com

This project is a complete Selenium automation framework built using Python and Pytest to test various scenarios from [the-internet.herokuapp.com](https://the-internet.herokuapp.com/). It follows the **Page Object Model (POM)** design pattern for modularity and maintainability.

## 📁 Project Structure

```
SeleniumTestInternetHerokuapp/
├── Data/                    # Test data (e.g., credentials)
│   └── credentials.json
├── PageObject/             # Page classes for all tested modules
│   ├── BasePage.py
│   ├── LandingPage.py
│   └── (Other page classes)
├── TestCases/              # Pytest test classes
│   └── (Individual test modules)
├── conftest.py             # Pytest fixtures
├── pytest.ini              # Pytest configuration
├── Reports/                # Generated test reports (after execution)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ✅ Covered Test Scenarios

Includes automation for pages like:

- A/B Testing  
- Add/Remove Elements  
- Basic & Digest Authentication  
- Broken Images  
- Checkboxes  
- Context Menu  
- Disappearing Elements  
- Drag and Drop  
- Dropdown  
- Dynamic Controls  
- Dynamic Content  
- Dynamic Loading
- and more...

(Refer to the `TestCases/` folder for all implemented tests)

## 🧪 How to Run the Tests

### 1. Clone the repository

```bash
git clone https://github.com/AlexAshwin/SeleniumTestInternetHerokuapp.git
cd SeleniumTestInternetHerokuapp
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run tests

```bash
pytest
```

> Logs will be printed in the terminal and saved if implemented in test cases.

## 📋 Prerequisites

- Python 3.7+  
- Google Chrome (or update WebDriver to match your browser)  
- ChromeDriver installed and added to PATH  
