#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def create_paragraph(path):
    fruits = ''
    for infile in os.listdir(path):
        with open(path + infile, "r") as file:
            name = file.readline().strip('\n\r')
            weight = file.readline().strip('\n\r')
            fruit = 'name: {}<br/>weight: {}<br/><br/>'.format(name, weight)
            fruits += fruit
    return fruits


if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    attachment = "/tmp/processed.pdf"
    today = datetime.datetime.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
    paragraph = create_paragraph(path)
    reports.generate_report(attachment, title, paragraph)

    # generate email
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. "
    "A detailed list is attached to this email."

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    try:
        emails.send_email(message)
    except ConnectionRefusedError as err:
        print(f"Cannot send an e-mail => {err}")

