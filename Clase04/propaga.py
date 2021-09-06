# Está medio desprolijo pero funciona

#%%
def propagar(fosforos):
    fosforos_nuevo = []
    for i, fosforo in enumerate(fosforos):
        if fosforo == 1:
            quemado = False
            pos = i + 1
            while not quemado and pos < len(fosforos):
                if fosforos[pos] == 0:
                    fosforos[pos] = 1
                elif fosforos[pos] == -1:
                    quemado = True
                pos += 1
            pos = i - 1
            quemado = False
            while not quemado and pos >=0:
                if fosforos[pos] == 0:
                    fosforos[pos] = 1
                elif fosforos[pos] == -1:
                    quemado = True
                pos -= 1
    return fosforos
# %%
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# %%
propagar([ 0, 0, 0, 1, 0, 0])
# %%
