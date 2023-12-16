def de_Bruijn_graph(readings):
    pre = [readings[0][0:len_readings-1]]
    suf = [readings[0][1:]]
    nodes = []
    links = []
  
    for i in range(1, number_of_readings): 
        pre.append(readings[i][0:len_readings-1])
        suf.append(readings[i][1:])
      
        for j in range(len(pre)): 
            if pre[i] == suf[j] and i != j :

                nodes.append(pre[i])
                links.append((j, i))
              
            if suf[i] == pre[j] and i!= j:
                nodes.append(pre[j])
                links.append((i,j))
              
    return(nodes, links)
  
nodes, links = de_Bruijn_fraph(readings)
