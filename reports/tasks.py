from reports.models import Report

from metasharks.celery import app


@app.task(ignore_result=True)
def create_report(report_id):
    """Create excel file with report about every Course and StudentGroup

    Args:
        report_id (int): report ID that needs to have it's excel file generated
    """
    report = Report.objects.get(id=report_id)
    print(report)
