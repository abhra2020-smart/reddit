def read_template(file):
    with open(f"templates/{file}", "r") as text:
        return text.read()
