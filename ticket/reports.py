from .models import Item, Category
from model_report.report import reports, ReportAdmin

class ItemsReport(ReportAdmin):
    title = ('Items report')
    model = Item
    fields = [
        'name',
        'cost',
    ]
    list_order_by = ('name',)
    type = 'report'

reports.register('items-report', ItemsReport)