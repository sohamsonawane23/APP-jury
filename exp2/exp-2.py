class Report:
    templates = {}
    formatters = {}

    def __init__(self, data, template, title="Report"):
        self.data = list(data)
        self.template = template
        self.title = title

    @classmethod
    def template(cls, name):
        def decorator(func):
            cls.templates[name] = func
            return func
        return decorator

    @classmethod
    def formatter(cls, name):
        def decorator(func):
            cls.formatters[name] = func
            return func
        return decorator

    def __str__(self):
        return self.render("plain")

    def __iter__(self):
        return iter(self.data)

    def __add__(self, other):
        if not isinstance(other, Report) or self.template != other.template:
            raise ValueError("Reports must have the same template")
        return Report(self.data + other.data, self.template, self.title)

    def render(self, fmt):
        if self.template not in Report.templates:
            raise ValueError("Template not found")
        if fmt not in Report.formatters:
            raise ValueError("Formatter not found")
        structured = Report.templates[self.template](self.data, self.title)
        return Report.formatters[fmt](structured, self.title)


@Report.template("table")
def table_template(data, title):
    if not data:
        return {"headers": [], "rows": []}
    headers = list(data[0].keys())
    rows = [list(item.values()) for item in data]
    return {"headers": headers, "rows": rows}


@Report.formatter("plain")
def plain_formatter(structured, title):
    lines = [title]
    lines.append(" | ".join(structured["headers"]))
    lines.append("-" * 20)
    for row in structured["rows"]:
        lines.append(" | ".join(map(str, row)))
    return "\n".join(lines)

@Report.formatter("csv")
def csv_formatter(structured, title):
    lines = [",".join(structured["headers"])]
    for row in structured["rows"]:
        lines.append(",".join(map(str, row)))
    return "\n".join(lines)


data1 = [{"Name": "Alice", "Score": 90},
         {"Name": "Bob", "Score": 85}]

report1 = Report(data1, "table", "Exam Results")
print("=== Plain ===")
print(report1)

print("\n=== CSV ===")
print(report1.render("csv"))

data2 = [{"Name"}]
