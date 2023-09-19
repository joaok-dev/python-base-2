email_tmpl = """
Hello, %(name)s

Are you interested in purchasing %(product)s?

This product is great for solving 
%(text)s

Click here now %(link)s

Only %(amount)d available!

Sales price %(price).2f
"""

customers = ["Maria", "Joao", "Jose"]

for customer in customers:
    print(
        email_tmpl
        % {
            "name": customer,
            "product": "pen",
            "text": "Write very well",
            "link": "https://coolpens.com",
            "amount": 1,
            "price": 50.5,
        }
    )
