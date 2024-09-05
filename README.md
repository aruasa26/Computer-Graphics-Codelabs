# Project Title: Student Email Generator

This project generates unique email addresses for students based on their names, categorizes them by gender, and saves the results in various formats. The project utilizes Python and various libraries to perform data manipulation and logging.

# Table of Contents

- Prerequisites
- Project Structure
- Usage
- Logging
- Collaboration
- Google API key and Backup
- Stretch Goal: Similarity Matrix
- Conclusion

## Prerequisites
1. **Development Environment:** It is recommended to use [PyCharm Professional Edition](https://www.jetbrains.com/pycharm/download/?section=windows) for this project. You will need to install a [student license](https://www.jetbrains.com/community/education/#students) if you are eligible, which provides access to the full features of the IDE, enhancing your development experience.
2. **Create a new Environment:** Set up a new Python environment to keep dependencies organized.
3. **Install required libraries:** Ensure you have the necessary libraries installed.One can do this by running:
```
pip install pandas openpyxl
```
4. **Download the Test files:** Download the required Excel files ('File_A.xlsx' and 'File_B.xlsx') and place them in the project directory.

## Project Structure

The project consists of the following files:
- **main.py:** The main program that combines data, generates email addresses, and saves the output.
- **functions.py:** Contains utility functions for combining dataframes, generating emails, and ensuring uniqueness.
- **constraints.py:** Defines rules and constraints for the project.
- **computations.log:** A log file that records the computations and processes performed during execution.

## Usage

1. **Run the main program:** Execute the *'main.py'* file.
2. **Output files:** The program will generate the following output files in the *'output'* directory:
- **students.csv:** A CSV file containing student names and generated email addresses.
- **students.tsv:** A TSV file with the same data as the CSV file.
- **male_students.csv:** A CSV file containing make student data.
- **female_students.csv:** A CSV file containing female student data.
- **special_char_students.csv:** A CSV file listing students with special characters in their names.
- **shuffled_students.json:** A JSON file with shuffled student data.
- **shuffled_students.jsonl:** A JSON Lines file with shuffled student data.

## Logging

The program logs various computations, including:
- Generated email addresses
- The number of male and female students
- Names of students with special characters

Logs are saved in the *'computations.log'* file.

## Collaboration

This project is hosted on GitHub for collaboration. You can access the repository at [GitHub Repository Link](https://github.com/Twna-Jane/Computer-Graphics-Codelabs) = Tiffany Ndungi
Other GitHub collaborator repository links include:
- Lynn Wahito= https://github.com/Lynn-Wahito/Computer-Graphics-Codelabs 
- Lizaloureen Kitheka= https://github.com/Lizaloureen/Computer-Graphics-Codelabs.git
- Fidel Isaboke= https://github.com/Fidelisaboke/Computer-Graphics-Codelabs
- Caesar Aruasa= https://github.com/aruasa26/Computer-Graphics-Codelabs

## Google API Key and Backup
1. **Generate a Google API Key:** Create a Google API key to enable file storage in Google Drive.
2. **Backup files to Google Drive:** Save all output files and logs to Google Drive for backup.

## Stretch Goal: Similarity Goal
As a stretch goal, implement a similarity matrix using the LaBSE model to compare male and female student names. Save results in a JSON file, focusing on pairs with at least 50% similarity.

## Conclusion

This project provides a comprehensive solution for generating unique email addresses for students, categorizing them by gender, and saving the results in multiple formats. The modular structure of the code enhances maintainability, and the logging feature ensures transparency in computations.Using PyCharm Professional Edition is recommended for an optimal development experience.