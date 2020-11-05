#!/usr/bin/env python3

import os
import psutil
import socket
import emails


CPU_THRESHOLD = 80  # percent (error if cpu usage higher than threshold)
DISC_THRESHOLD = 20  # percent (error if available disc space lower than threshold)
MEMORY_THRESHOLD = 500  # MB (error if available memory lower than threshold)


def check_cpu_usage(cpu_threshold):
    cpu_usage = psutil.cpu_percent()
    print(f"cpu usage: {cpu_usage}%")
    if cpu_usage > cpu_threshold:
        return 'NOK'
    return 'OK'


def check_disc_usage(disc_threshold):
    disc_available = 100 - psutil.disk_usage('/').percent
    print(f"disc available: {disc_available}%")
    if disc_available < disc_threshold:
        return 'NOK'
    return 'OK'


def check_memory_usage(memory_threshold):
    memory_available = psutil.virtual_memory().available / 1000000
    print(f"memory available: {int(memory_available)}MB")
    if memory_available < memory_threshold:
        return 'NOK'
    return 'OK'


def check_hostname():
    local_address = socket.gethostbyname('localhost')
    print(f"local address: {local_address}")
    if local_address != '127.0.0.1':
        return 'NOK'
    return 'OK'


def send_error_email(subject):
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, recipient, subject, body)
    try:
        emails.send_email(message)
    except ConnectionRefusedError as err:
        print(f"Cannot send an e-mail => {err}")


def monitoring():

    subject = {"cpu": "Error - CPU usage is over {}%".format(CPU_THRESHOLD),
               "disc": "Error - Available disk space is less than {}%".format(DISC_THRESHOLD),
               "memory": "Error - Available memory is less than {}MB".format(MEMORY_THRESHOLD),
               "hostname": "Error - localhost cannot be resolved to 127.0.0.1"}

    if check_cpu_usage(CPU_THRESHOLD) == 'NOK':
        send_error_email(subject['cpu'])

    if check_disc_usage(DISC_THRESHOLD) == 'NOK':
        send_error_email(subject['disc'])

    if check_memory_usage(MEMORY_THRESHOLD) == 'NOK':
        send_error_email(subject['memory'])

    if check_hostname() == 'NOK':
        send_error_email(subject['hostname'])


monitoring()

# to launch this script every minute edit crontab:
# (bash) crontab -e
# (cronetab) * * * * * full_path_to_health_check.py
