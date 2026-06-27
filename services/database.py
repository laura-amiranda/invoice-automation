import json
import os

from models.invoice import Invoice


class Database:

    def __init__(self):
        self.file_path = "data/database.json"

    def save_invoice(self, invoice: Invoice):

        invoices = []

        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                invoices = json.load(file)

        for saved_invoice in invoices:

            if saved_invoice["order_id"] == invoice.order_id:
                print(f"Fatura {invoice.order_id} já existe no banco de dados.")
                return

        invoices.append(invoice.model_dump())

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(invoices, file, indent=4)

        print(f"Fatura {invoice.order_id} salva com sucesso!")