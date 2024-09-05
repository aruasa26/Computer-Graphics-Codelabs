import re
import pandas as pd

import re
import pandas as pd


def combine_dataframes(df1, df2):
    """
    Combine two DataFrames and return the combined result.
    :param df1: First DataFrame
    :param df2: Second DataFrame
    :return: Combined DataFrame
    """
    combined_df = pd.concat([df1, df2], ignore_index=True)
    return combined_df

def generate_email(name):
    """
    Generate an email from the student's name.
    Takes the first letter of the first name and combines it with the last name.
    :param name: student name
    :return: email
    """
    name_parts = re.split(r'[\s,]+', name)
    email_name = name_parts[0][0].lower() + name_parts[-1].lower()

    # Remove any special characters
    email_name = re.sub(r'[^a-zA-Z]', '', email_name)
    return f"{email_name}@gmail.com"


def make_unique(emails):
    """
    Make email addresses unique by appending a number if duplicates exist.
    :param emails: list of email addresses
    :return: unique list of email addresses
    """
    seen = {}
    unique_emails = []

    for email in emails:
        if email not in seen:
            seen[email] = 0
            unique_emails.append(email)
        else:
            seen[email] += 1
            unique_email = f"{email.split('@')[0]}{seen[email]}@gmail.com"
            unique_emails.append(unique_email)

    return unique_emails

def get_students_by_gender(df, gender):
    """
    Get all students of a specified gender.
    :param df: DataFrame containing student names and genders
    :param gender: The student gender
    :return: DataFrame containing students of the specified gender
    """
    for index, row in df.iterrows():
        if row['Gender'] == gender:
            yield row


