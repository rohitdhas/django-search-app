from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant

def search_view(request):
    query = request.GET.get('q')
    location = request.GET.get('location')

    all_results = Restaurant.objects.all()
    location_list = set()
    filtered_results = []
    relevant_results = []

    # Filtering
    for item in all_results:
        location_list.add(item.location)

    if location:
        all_results = all_results.filter(Q(location__icontains=location))

    if query:
        query_words = query.split()

        # Create a Q object for matching each word in the query with menu items
        menu_query = Q()
        for word in query_words:
            menu_query |= Q(menu__icontains=word)

        all_results = all_results.filter(menu_query)

        for restaurant in all_results:
            menu_items = get_filtered_menu_items(restaurant, query)
            if menu_items['filtered_menu_items']:
                restaurant.menu = menu_items['filtered_menu_items']
                filtered_results.append(restaurant)
            elif menu_items['relevant_menu_items']:
                restaurant.menu = menu_items['relevant_menu_items']
                relevant_results.append(restaurant)
                
    return render(request, 'search.html', {'results': filtered_results, "relevant_results": relevant_results, 'query': query, 'location': location, 'location_list': location_list })


def get_filtered_menu_items(restaurant, query):
    menu_data = restaurant.get_menu_as_dict()
    filtered_menu_items = []
    relevant_menu_items = []

    for menu_item, price in menu_data.items():
        item_contains_query = all(word.lower() in menu_item.lower() for word in query.split(" "))
        if item_contains_query:
            filtered_menu_items.append({menu_item: price})
        elif any(word.lower() in menu_item.lower() for word in query.split(" ")):
            relevant_menu_items.append({menu_item: price})

    return {'filtered_menu_items': filtered_menu_items, 'relevant_menu_items': relevant_menu_items}

