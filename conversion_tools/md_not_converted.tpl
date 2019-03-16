{%- extends 'basic.tpl' -%}


{% block markdowncell scoped %}
{{ cell.source | strip_files_prefix }}
{%- endblock markdowncell %}