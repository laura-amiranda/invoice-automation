import pandas as pd


class Analytics:
    """
    Responsável pelas consultas analíticas do database.json.
    """

    def __init__(self, database_path="data/database.json"):
        self.database_path = database_path
        self.df = self.load_data()

    def load_data(self):
        """Carrega o banco JSON em um DataFrame."""

        return pd.read_json(self.database_path)

    def average_invoice_value(self):
        """Calcula a média do valor total das faturas."""

        totals = []

        for items in self.df["items"]:

            total = 0

            for item in items:
                total += item["quantity"] * item["unit_price"]

            totals.append(total)

        return sum(totals) / len(totals)

    def most_frequent_product(self):
        """Retorna o produto com maior frequência de compra."""

        products = []

        for items in self.df["items"]:
            for item in items:
                products.append(item["product_name"])

        return pd.Series(products).value_counts().index[0]

    def total_spent_per_product(self):
        """Retorna o valor total gasto por produto."""

        totals: dict[str, float] = {}

        for items in self.df["items"]:

            for item in items:

                name = item["product_name"]

                value = item["quantity"] * item["unit_price"]

                if name not in totals:
                    totals[name] = value
                else:
                    totals[name] += value

        return totals

    def products_and_prices(self):
        """Lista os produtos e seus preços unitários."""

        products = []

        for items in self.df["items"]:

            for item in items:

                products.append(
                    {
                        "Produto": item["product_name"],
                        "Preço Unitário": item["unit_price"]
                    }
                )

        return pd.DataFrame(products).drop_duplicates()