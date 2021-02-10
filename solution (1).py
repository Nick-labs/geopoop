import solution
toponym_to_find = "Канаш Москавская 19"

coord = 47.496938, 55.507703
span = 0.001, 0.001
map_params = {'ll': ",".join(map(str, coord)),
              "spn": ",".join(map(str,span))
}

solution.show_map(**map_params, map_type="sat")