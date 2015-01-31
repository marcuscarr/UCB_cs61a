def troy():
    abed = 0
    while abed < 10:
        def britta():
            return abed
        abed += 1
    abed = 20
    return britta

annie = troy()
def shirley():
    return annie

pierce = shirley()

pierce()
