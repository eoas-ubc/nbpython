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

def get_key(nb_obj):
    """
    return the key for eqch question
    """
    new_dict = {}
    for count,the_cell in enumerate(nb_obj['cells']):
        if 'ctype' in the_cell['metadata']:
            if the_cell['metadata']['ctype']=="answer":
                print(the_cell['metadata'])
                if 'key' in the_cell['metadata']:
                    qnum = the_cell['metadata']['qnum']
                    answer = the_cell['metadata']['key']
                    if qnum in new_dict:
                        raise ValueError(f"found multiple qnums for {qnum}")
                    new_dict[qnum] = answer
    
    return new_dict


def get_qorder(nb_obj):
    """
    return the exam A order for eqch B question
    """
    new_list = []
    index=1
    for count,the_cell in enumerate(nb_obj['cells']):
        if 'ctype' in the_cell['metadata']:
            if the_cell['metadata']['ctype']=="question":
                print(the_cell['metadata'])
                if 'qnum' in the_cell['metadata']:
                    qnum = the_cell['metadata']['qnum']
                    new_list.append({'qnumB':index,'qnumA':qnum})
                    index+=1
    return new_list
