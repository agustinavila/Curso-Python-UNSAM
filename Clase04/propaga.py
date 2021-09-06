#%%
def propagar(fosforos):
    fosforos_nuevo = []
    for i, fosforo in enumerate(fosforos):
        if fosforo == 0 and i != 0:
            if fosforos[i-1] == 1:
                fosforos_nuevo.append(1)
                continue
        elif fosforo == 0 and i < len(fosforos)-1:   
            if fosforos[i+1] == 1:
                fosforos_nuevo.append(1)
        else:
            fosforos_nuevo.append(fosforos[i])
    return fosforos_nuevo
# %%
