from models.invoice import Invoice
from models.item import Item


class InvoiceParser:

    def parse(self, lines: list[str]) -> Invoice:
        order_id = None
        customer_id = None
        order_date = None

        items = []

        reading_products = False

        for line in lines:

            if line.startswith("Order ID:"):
                order_id = line.replace("Order ID:", "").strip()

            elif line.startswith("Customer ID:"):
                customer_id = line.replace("Customer ID:", "").strip()

            elif line.startswith("Order Date:"):
                order_date = line.replace("Order Date:", "").strip()

            elif line.startswith("Product ID"):
                reading_products = True
                continue

            elif line.startswith("TotalPrice"):
                reading_products = False

            elif reading_products:

                parts = line.split()

                if len(parts) >= 4:

                    product_id = int(parts[0])

                    # Os dois últimos elementos sempre são
                    # quantidade e preço unitário.
                    quantity = int(parts[-2])
                    unit_price = float(parts[-1])

                    product_name = " ".join(parts[1:-2])

                    item = Item(
                        product_id=product_id,
                        product_name=product_name,
                        quantity=quantity,
                        unit_price=unit_price
                    )

                    items.append(item)

        invoice = Invoice(
            order_id=order_id,
            customer_id=customer_id,
            order_date=order_date,
            items=items
        )

        return invoice