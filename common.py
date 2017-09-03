
def title_from_route(route_list):
    title_list = []
    for route in route_list:
        title_words = []
        for word in route.split("_"):
            title_words.append(word.capitalize())
        title_list.append(" ".join(title_words))

    return title_list
