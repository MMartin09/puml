from mako.template import Template

Attr_Template = Template("""${accessor} ${name}: ${type}""")

Class_Template = Template(
    "\n".join(
        ("class ${class_name} {", "% for attr in attrs:", "   ${attr}", "% endfor", "}")
    )
)
