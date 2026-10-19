# How to Initialize the PureCalculator Project on Linux

## Requirements

Before initializing the PureCalculator project, ensure you have the following:

- **Python:** Version 3.12.3 or later
- **IDE:** Visual Studio Code (VS Code) or any IDE of your choice
- **Terminal:** Terminal application for your Linux distribution

## Step 1: Update Your Linux System

Before cloning and initializing the project, update your Linux system to the latest available packages.

Run the following commands in your terminal:

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Clone the Project

To clone the PureCalculator repository, run the following command:

```bash
git clone https://github.com/Ajjan90/PureCalculator.git
```

**If Git is not installed** on your Linux machine, install it by running:

```bash
sudo apt install git
```

Alternatively, you can download Git from the official website: [Git - Install for Linux](https://git-scm.com/download/linux).

Once Git is installed, run the clone command provided above.

## Step 3: Navigate to the PureCalculator Folder

After cloning the repository, navigate to the project directory by running:

```bash
cd PureCalculator
```

## Step 4: Install Python and Other Prerequisites

Before making changes to the code, ensure that the necessary prerequisites are installed.

Update your package lists and install Python, pip, the virtual environment module, and Git:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

### Verify the Installed Versions

Run the following commands to check the installed versions:

```bash
python3 --version
pip3 --version
git --version
```

Ensure that your Python version is **3.12.3 or later**.

> **Note:** Depending on your Linux distribution, the default Python version provided by `apt` may be older than 3.12.3. If that is the case, install a compatible Python version before proceeding.

## Step 5: Initialize the Virtual Environment

Within the `PureCalculator` project folder, run the following commands to create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

After activating the virtual environment, your terminal prompt should look similar to this:

```text
(.venv) user@linux:~/PureCalculator$
```

The `(.venv)` prefix indicates that the virtual environment is active.

### Install the Required Python Libraries

The PureCalculator project requires Python libraries such as PySide6, QtAwesome, CountryInfo, and others.

All required libraries are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```

This process may take some time, depending on your internet connection and system performance.

Once the installation is complete, your PureCalculator virtual environment will be ready for development.

## Step 6: Configure Visual Studio Code

To configure VS Code to use the project's virtual environment, follow these steps:

1. Open the `PureCalculator` project folder in VS Code.
2. Press `Ctrl + Shift + P` to open the Command Palette.
3. Search for **Python: Select Interpreter**.
4. Select the Python interpreter located at:

   ```text
   .venv/bin/python
   ```

### Verify the Selected Interpreter

Open the VS Code terminal and run:

```bash
which python
```

The output should point to the Python executable inside your project's `.venv` directory. For example:

```text
/home/user/PureCalculator/.venv/bin/python
```

This confirms that VS Code is using the project's virtual environment.

## Step 7: Run and Test the Program

Once all dependencies have been installed, you can run the PureCalculator application.

### Option 1: Using the Terminal

From the project directory, run:

```bash
python Main.py
```

Alternatively, if your virtual environment is active, you can use:

```bash
python3 Main.py
```

### Option 2: Using Visual Studio Code

To run or debug the program in VS Code:

1. Open the `Main.py` file.
2. Go to **Run > Start Debugging**.
3. Alternatively, press `F5` on your keyboard.

   If you are using a laptop, you may need to press `Fn + F5`.

If everything is configured correctly, the PureCalculator application should start.

---

## Conclusion

You have now initialized the PureCalculator project on Linux. Your development environment is ready, and you can begin exploring the code, making changes, and testing the application.

### Quick Reference

| Task | Command |
|---|---|
| Update package lists | `sudo apt update` |
| Upgrade installed packages | `sudo apt upgrade -y` |
| Clone the repository | `git clone https://github.com/Ajjan90/PureCalculator.git` |
| Navigate to the project | `cd PureCalculator` |
| Create a virtual environment | `python3 -m venv .venv` |
| Activate the virtual environment | `source .venv/bin/activate` |
| Upgrade pip | `python -m pip install --upgrade pip` |
| Install dependencies | `pip install -r requirements.txt` |
| Verify Python version | `python3 --version` |
| Run the application | `python Main.py` |