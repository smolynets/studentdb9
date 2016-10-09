# -*- coding: utf-8 -*-
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from ..models.monthjournal import MonthJournal
from ..models.student import  Student
from ..util import paginate
class JournalView(TemplateView):
  template_name = 'students/journal.html'
  def get_context_data(self, **kwargs):
    # get context data from TemplateView class
    context = super(JournalView, self).get_context_data(**kwargs)
    if self.request.GET.get('month'):
           month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
    else:
           # otherwise just displaying current month data
           today = datetime.today()
           month = date(today.year, today.month, 1)
    next_month = month + relativedelta(months=1)
    prev_month = month - relativedelta(months=1)
    context['prev_month'] = prev_month.strftime('%Y-%m-%d')
    context['next_month'] = next_month.strftime('%Y-%m-%d')
    context['year'] = month.year
    context['cur_month'] = month.strftime('%Y-%m-%d')
    context['month_verbose'] = month.strftime('%B')
    myear, mmonth = month.year, month.month
    number_of_days = monthrange(myear, mmonth)[1]
    context['month_header'] = [{'day': d,'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
        for d in range(1, number_of_days+1)]
    queryset = Student.objects.all().order_by('last_name')
    update_url = reverse('journal')
    students = []
    for student in queryset:
      try:
          journal = MonthJournal.objects.get(student=student, date=month)
      except Exception:
          journal = None
      days = []
      for day in range(1, number_of_days+1):
        days.append({
          'day': day,
          'present': journal and getattr(journal, 'present_day%d' %  day, False) or False,
          'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
          })
      students.append({
        'fullname': u'%s %s' % (student.last_name, student.first_name),
        'days': days,
        'id': student.id,
        'update_url': update_url,
      })
    context = paginate(students, 2, self.request, context, var_name='students')
    return context

        