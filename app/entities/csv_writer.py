import csv
import io


class CsvWriter:
    @staticmethod
    def write(transactions: list[dict[str, str]]) -> io.StringIO:
        output = io.StringIO()
        field_names = transactions[0].keys()
        writer = csv.DictWriter(output, field_names, delimiter=";")
        writer.writeheader()
        writer.writerows(transactions)

        return output
