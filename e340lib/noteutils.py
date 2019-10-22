import jupytext as jp

def update_cell_meta(nbobj,key,value):
    """
    add an empty key,value pair as metadata to every input cell
    in a notebook
    """
    for count,the_cell in enumerate(nbobj['cells']):
        the_cell['metadata'].update({key:value})
    return nbobj

def strip_answers(nb_obj):
    """
    remove all cells with metadata "answer" from
    cell list
    """
    new_list = []
    for count,the_cell in enumerate(nb_obj['cells']):
        if 'ctype' in the_cell['metadata']:
            if the_cell['metadata']['ctype']=="answer":
                continue
        new_list.append(the_cell)
    nb_obj['cells'] = new_list
    return nb_obj


def update_headers(nb_obj,lhead = " ", chead = " "):
    """
    add header fields to the notebook metadata
    """
    latex_meta = dict()
    header_dict={'lhead':lhead,'chead':chead}
    latex_meta["latex_metadata"] = header_dict
    nb_obj['metadata'].update(latex_meta)
    return nb_obj
