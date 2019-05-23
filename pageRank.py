import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import my_function as func

def findPageRank(linkmatrix,pages):
    eigval, eigvector= np.linalg.eig(linkmatrix)
    dominant_eigval = np.abs(eigval).max()
    PageRank= np.where(eigval == dominant_eigval)
    print("The most important node is %s"% str(pages[PageRank[0][0]]))

if __name__== "__main__":
    
    node = func.load_list("node")
    edge = func.load_list("edge")
    
    G=nx.DiGraph()
    # a list of nodes:
    pages = []
    for i in range(0,len(node)):
        pages.append(str(i))
        
    G.add_nodes_from(pages)
    G.add_edges_from(edge)
    
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())
    
    print("Number of outward links for each node:")
    for page in pages:
        print(["Page %s = %s"% (page,str(len(G.out_edges(page))))])

#    nx.draw(G, with_labels = True)
#    plt.show() # display
    
    image = nx.draw_circular(G,node_color='red', with_labels = True)
    
    #linkmatrix = np.zeros(shape=(len(node),len(node)))
    #findPageRank(linkmatrix,pages)

    PR = nx.pagerank(G)
    value = max(PR, key=PR.get)
    print(PR)
    print("The most important node is " + value)
    print("The most important link is " + node[int(value)])