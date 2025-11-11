# Project-Folder-Creator
Automated project folder creation tool with customizable subdirectories and integrated Bill of Materials (BOM) template.

<img width="608" height="546" alt="image" src="https://github.com/user-attachments/assets/51fe17bb-c216-4475-b99e-cd64b0cf3446" />

---

## ✨ Features

This tool streamlines the setup process for engineering and design projects:

* **Quick Setup:** Create a new project folder and a predefined set of subfolders with just a few clicks.
* **Custom Selection:** Choose exactly which subfolders you need for the current project.
* **BOM Template Inclusion:** Automatically copies a specified `BOM template.xls` into the designated "**Bill of Material**" folder.
* **Conflict Handling:** Checks if the main project folder already exists and asks for confirmation before adding/updating subfolders.

---

## 🛠️ Requirements & Setup

To run this script, you only need Python and the template file properly placed.

1.  **Python 3:** The script requires a standard Python 3 installation.
2.  **Required Libraries:** `os`, `tkinter`, and `shutil` are used.
3.  **Template File:** The application relies on a template file named **`BOM template.xls`** being present in the **same directory** as the Python script.

### 🚀 How to Run

There are two ways to launch the Project Creator:

#### Option 1: Using the Batch File (Recommended)

1.  **Download the Batch File:** Save batch file named `RunFolderCreator.bat` in the same directory as the Python script.
2.  **Edit the Path:** You must **update the path** in the batch file to reflect the location where the script is saved.
3.  **Double-Click:** Simply double-click the `.bat` file to run the application.

    **Example Batch File (`RunFolderCreator.bat`):**
    ```batch
    @echo off
    python "C:\Users\USER_NAME\ProjectFolderCreator.py"
    pause
    ```
    > **Note:** Remember to modify the path (`C:\Users\USER_NAME\ProjectFolderCreator.py`) to your own save location.

#### Option 2: Direct Command Line

1.  **Save & Place Files:** Save the Python code as `ProjectFolderCreator.py` and place `BOM template.xls` in the same directory.
2.  **Navigate:** Open your terminal/command prompt and navigate to the directory where you saved the files.
3.  **Execute:** Run the script using the Python interpreter:

    ```bash
    python ProjectFolderCreator.py
    ```

---

## 📋 Usage Instructions

The GUI makes project setup intuitive:

1.  **Project Name:** Enter the name for your new main project folder (e.g., `25001-kinetic facade`).
2.  **Base Location:** Click the **"Browse..."** button to select the parent directory where the new folder will be created.
3.  **Select Subfolders:** Check the boxes next to the subfolders you wish to create. Default options include:
    * **CAD Files**
    * **PDF**
    * **DXF**
    * **Bill of Material**
    * **Other**
4.  **Create:** Click the **"Create Selected Project Structure"** button.
    * The script will create the main project folder and all selected subfolders.
    * If **"Bill of Material"** is checked, the template file is copied.
5.  **Success:** A confirmation pop-up will notify you when the folder structure has been created.

---

## ⚙️ Configuration (For Developers)

You can easily modify the script's default behavior by editing the **Configuration** section near the top of the `ProjectFolderCreator.py` file:

| Variable | Description |
| :--- | :--- |
| `TEMPLATE_FILENAME` | Change this to match your template's file name (e.g., `"MyCompany_BOM.xlsx"`). |
| `DEFAULT_SUBFOLDERS` | Edit this list to change, add, or remove the standard subfolder names presented to the user. |

The configuration block in `ProjectFolderCreator.py` looks like this:

```python
# --- Configuration ---
TEMPLATE_FILENAME = "BOM template.xls"
# Define the available subfolders (without numbering)
DEFAULT_SUBFOLDERS = ["CAD Files", "PDF", "DXF", "Bill of Material", "Other"]
# -------------------
