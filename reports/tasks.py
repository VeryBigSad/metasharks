import pandas as pd
from courses.models import Course
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

    queryset = StudentGroup.objects.get_data_for_report()
    data = list(queryset.values())  # Convert queryset to a list of dictionaries
    # make datetimes timezone unaware
    for item in data:
        item["created_at"] = item["created_at"].replace(tzinfo=None)
        item["updated_at"] = item["updated_at"].replace(tzinfo=None)

    excel_file = f"media/reports/report_{report.pk}.xlsx"
    with pd.ExcelWriter(excel_file) as writer:
        # all groups
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name="All Groups", index=False, engine="openpyxl")

        courses = list(Course.objects.get_data_for_report())
        df = pd.DataFrame(courses)
        df.to_excel(writer, sheet_name="Courses", index=False, engine="openpyxl")

        # individual student groups
        for studentgroup in queryset:
            values = list(studentgroup.students.get_data_for_report())
            df = pd.DataFrame(values)
            df.to_excel(
                writer,
                sheet_name=f"Group {studentgroup.name}",
                index=False,
                engine="openpyxl",
            )

    report.file = f"reports/report_{report.pk}.xlsx"
    report.state = "done"
    report.save()
