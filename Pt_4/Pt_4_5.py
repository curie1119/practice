
def all_ways(graphh, startt, endd, way=[]):
    if way is None:
        way = []
    way = way + [startt]
    if startt == endd:
        return [way]
    if startt not in graphh or endd not in graphh:
        return "Какой-то из этих точек не существует"
    ways = []
    for el in graphh[startt]:
        if el not in way:
            new_ways = all_ways(graphh, el, endd, way)
            ways.extend(new_ways)
    return ways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
print("Все пути из точки A в точку F:", all_ways(graph, start, end))
