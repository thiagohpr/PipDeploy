#!python
from dev_aberto import hello
from datetime import datetime
from babel.dates import format_datetime
import pytz
import gettext

gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    date_obj = pytz.utc.localize(date_obj) 
    formatted_date = format_datetime(date_obj)

    print(_('Último commit feito em:'), formatted_date, _(' por'), name)
