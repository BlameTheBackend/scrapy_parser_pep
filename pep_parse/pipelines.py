import csv
from datetime import datetime
from collections import Counter

from .settings import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.statuses = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        csv_path = results_dir / f'status_summary_{timestamp}.csv'
        with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.statuses.items())
            writer.writerow(['Total', sum(self.statuses.values())])
