import json


def prepare_products_names_and_ids(products_list: list):
    return [(json.loads(product)['result']['products']['id'], json.loads(product)['result']['products']['name']) for
            product in products_list]


def extract_product_styles(product_info: dict):
    product_styles = []
    for product_type in product_info['result']['product']['prices']:
        for id in product_type['variation_value_to_product_ids']:
            product_styles.append(int(id))

    product_styles = list(set(product_styles))
    product_styles.sort()

    return product_styles
