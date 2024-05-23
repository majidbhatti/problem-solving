from venv import logger
from datetime import datetime


def alert_occurrence_range(alerts):
    if alerts:
        try:
            logger.info(f'finding alerts occurrence date range')
            dates = sorted([a.get("generatedAt") for a in alerts])
            dates = [dates[0], dates[-1]]
            dates = [d.rsplit(':', 1)[0] for d in dates]
            formated_dates = [datetime.strptime(d, "%Y-%m-%dT%H:%M") for d in dates]
            if len(alerts) > 1:
                formated_dates = [d.strftime("%B %d, %Y, %H:%M") for d in formated_dates]
            else:
                formated_dates = [d.strftime("%B %d, %Y") for d in formated_dates]
            return formated_dates
        except Exception as E:
            logger.warning(f'There was an error in date formats, or something related to dates in alerts')
            return dates


if __name__ == '__main__':
    alert = {'generatedAt': '2024-02-13T13:25:26.547316Z'}
    x = [alert, {'generatedAt': '2024-03-13T13:25:26.547316Z'}]
    print(alert_occurrence_range(x))
