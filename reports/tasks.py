import pandas as pd
from reports.models import Report

from metasharks.celery import app
from students.models import StudentGroup


@app.task(ignore_result=True)
def create_report(report_id):
    """Create excel file with report about every Course and StudentGroup

    Args:
        report_id (int): report ID that needs to have it's excel file generated
    """
    report = Report.objects.get(id=report_id)
    report.state = "done"

    queryset = StudentGroup.objects.get_data_for_students_report()
    data = list(queryset.values())  # Convert queryset to a list of dictionaries
    # make datetimes timezone unaware
    for item in data:
        item["created_at"] = item["created_at"].replace(tzinfo=None)
        item["updated_at"] = item["updated_at"].replace(tzinfo=None)
    df = pd.DataFrame(data)

    excel_file = f"report_{report.pk}.xlsx"
    # make it several pages, first one for all, then for each model
    with pd.ExcelWriter(excel_file) as writer:
        df.to_excel(writer, sheet_name="all", index=False, engine="openpyxl")
        for studentgroup in queryset:
            values = list(studentgroup.students.all().values())
            for item in values:
                item["date_joined"] = item["date_joined"].replace(tzinfo=None)
                item["updated_at"] = item["updated_at"].replace(tzinfo=None)
            df = pd.DataFrame(values)
            df.to_excel(
                writer, sheet_name=studentgroup.name, index=False, engine="openpyxl"
            )
    # df.to_excel(excel_file, index=False, engine='openpyxl')
    report.file = excel_file
    report.state = "done"
    report.save()
