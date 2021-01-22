def search_and_replace_text(search_dest, src):
    src = src.split(" ")

    if len(src) < 2:
        return "[ERROR] Please Enter at Least 2 Words"

    for i in range(len(src)):
        if src[i] in search_dest:
            search_dest += src[i]
        search_dest = search_dest.replace(src[i], "", 1)

    return search_dest
