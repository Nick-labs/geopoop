import geo
toponym_to_find = "Москва, ул. Ак. Королева, 12"

map_params = geo.get_span(toponym_to_find)
geo.show_map(**map_params, map_type="sat")