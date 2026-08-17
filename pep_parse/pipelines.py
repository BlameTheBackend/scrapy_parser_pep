from pathlib import Path
from datetime import datetime
from collections import Counter


class PepParsePipeline:
    def __init__(self):
        self.statuses = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = Path('results')
        results_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        csv_path = results_dir / f'status_summary_{timestamp}.csv'
        with open(csv_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, quantity in self.statuses.items():
                f.write(f'{status},{quantity}\n')
            f.write(f'Total,{sum(self.statuses.values())}\n')
