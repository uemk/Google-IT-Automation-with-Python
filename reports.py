#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment: str, title: str, paragraph: str) -> None:
    """
    Creates a pdf report.
    :param attachment: name (path) of pdf report to be created
    :param title: title of pdf report
    :param paragraph: body of pdf report
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])

