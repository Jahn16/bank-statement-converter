import csv
import io


class CsvWriter:
    @staticmethod
    def write(transactions: list[dict[str, str]]) -> io.StringIO:
        data = io.StringIO()
        field_names = transactions[0].keys()
        writer = csv.DictWriter(data, field_names, delimiter=";")
        writer.writeheader()
        writer.writerows(transactions)

        return data
