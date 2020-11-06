#!/usr/bin/env python3

import os
import datetime
import reports
import emails

PATH = "supplier-data/descriptions/"
ATTACHMENT = "/tmp/processed.pdf"


def create_paragraph(path: str) -> str:
    """
    Creates a paragraph for pdf document with data about fruits.
    :param path: path to directory with fruit descriptions in text files
    :return: pdf paragraph (formatted string)
    """
    fruits = ''
    for infile in os.listdir(path):
        if infile.endswith('.txt'):
            with open(path + infile, "r") as file:
                name = file.readline().strip('\n\r')
                weight = file.readline().strip('\n\r')
                # <br/> results in new line in pdf document
                fruit = 'name: {}<br/>weight: {}<br/><br/>'.format(name, weight)
                fruits += fruit
    return fruits


if __name__ == "__main__":
    # generate pdf report
    today = datetime.datetime.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
    paragraph = create_paragraph(PATH)
    reports.generate_report(ATTACHMENT, title, paragraph)

    # generate email
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. "
    "A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, ATTACHMENT)

    # send email
    try:
        emails.send_email(message)
    except ConnectionRefusedError as err:
        print(f"Cannot send an e-mail => {err}")
