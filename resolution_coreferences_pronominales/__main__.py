import extraction_mot

if __name__ == '__main__':
    relations_mot = extraction_mot.relations_mot('puits', 'all', 0)
    for rid in relations_mot.keys():
        print(rid + " : " + str(relations_mot[rid]))
