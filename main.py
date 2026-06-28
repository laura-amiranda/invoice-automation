import os

from services.pdf_reader import PDFReader
from services.invoice_parser import InvoiceParser
from services.database import Database
from services.analytics import Analytics

INVOICE_FOLDER = "data/invoices"


def process_invoices():

    reader = PDFReader()
    parser = InvoiceParser()
    database = Database()

    for file_name in os.listdir(INVOICE_FOLDER):

        if file_name.endswith(".pdf"):

            pdf_path = os.path.join(INVOICE_FOLDER, file_name)

            lines = reader.read_pdf(pdf_path)

            invoice = parser.parse(lines)

            database.save_invoice(invoice)


def run_analytics():

    analytics = Analytics()

    print("\n========== CONSULTAS ANALÍTICAS ==========\n")

    print(f"Média do valor total das faturas: {analytics.average_invoice_value():.2f}")

    print("\nProduto com maior frequência de compra:")
    print(analytics.most_frequent_product())

    print("\nValor total gasto por cada produto:")

    for product, value in analytics.total_spent_per_product().items():
        print(f"{product}: {value:.2f}")

    print("\nProdutos e preços unitários:")

    print(analytics.products_and_prices())


if __name__ == "__main__":

    print("========== PROCESSANDO FATURAS ==========\n")

    process_invoices()

    run_analytics()