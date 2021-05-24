coordinates = [[(295.5258238486492, 216.52582384864922), (348.5774715459477, 216.52582384864922), (401.6291192432461, 216.52582384864922), (454.6807669405446, 216.52582384864922), (507.732414637843, 216.52582384864922)], [(269.0, 262.5774715459477), (322.05164769729845, 262.5774715459477), (375.1032953945969, 262.5774715459477), (428.15494309189535, 262.5774715459477), (481.2065907891938, 262.5774715459477), (534.2582384864922, 262.5774715459477)], [(242.47417615135078, 308.6291192432461), (295.5258238486492, 308.6291192432461), (348.5774715459477, 308.6291192432461), (401.6291192432461, 308.6291192432461), (454.6807669405446, 308.6291192432461), (507.732414637843, 308.6291192432461), (560.7840623351415, 308.6291192432461)], [(215.94835230270155, 354.6807669405446), (269.0, 354.6807669405446), (322.05164769729845, 354.6807669405446), (375.1032953945969, 354.6807669405446), (428.15494309189535, 354.6807669405446), (481.2065907891938, 354.6807669405446), (534.2582384864922, 354.6807669405446), (587.3098861837907, 354.6807669405446)], [(189.42252845405233, 400.732414637843), (242.47417615135078, 400.732414637843), (295.5258238486492, 400.732414637843), (348.5774715459477, 400.732414637843), (401.6291192432461, 400.732414637843), (454.6807669405446, 400.732414637843), (507.732414637843, 400.732414637843), (560.7840623351415, 400.732414637843), (613.8357100324399, 400.732414637843)], [(215.94835230270155, 446.78406233514147), (269.0, 446.78406233514147), (322.05164769729845, 446.78406233514147), (375.1032953945969, 446.78406233514147), (428.15494309189535, 446.78406233514147), (481.2065907891938, 446.78406233514147), (534.2582384864922, 446.78406233514147), (587.3098861837907, 446.78406233514147)], [(242.47417615135078, 492.8357100324399), (295.5258238486492, 492.8357100324399), (348.5774715459477, 492.8357100324399), (401.6291192432461, 492.8357100324399), (454.6807669405446, 492.8357100324399), (507.732414637843, 492.8357100324399), (560.7840623351415, 492.8357100324399)], [(269.0, 538.8873577297384), (322.05164769729845, 538.8873577297384), (375.1032953945969, 538.8873577297384), (428.15494309189535, 538.8873577297384), (481.2065907891938, 538.8873577297384), (534.2582384864922, 538.8873577297384)], [(295.5258238486492, 584.9390054270368), (348.5774715459477, 584.9390054270368), (401.6291192432461, 584.9390054270368), (454.6807669405446, 584.9390054270368), (507.732414637843, 584.9390054270368)]]

def neighbor(coordinates, xy):
    var = [e for e in coordinates if xy in e][0]
    indice_y = coordinates.index(var)
    indice_x = var.index(xy)
    neighbor = []
    print(indice_x)
    
    
        # neighbor = [    
        #         coordinates[indice_y][indice_x-1],
        #         coordinates[indice_y][indice_x+1],

        #         coordinates[indice_y-1][indice_x-1],
        #         coordinates[indice_y-1][indice_x],
                    # Change This #
        #         coordinates[indice_y+1][indice_x],
        #         coordinates[indice_y+1][indice_x+1],
        # ]
    
    #     neighbor = [   
    #             # Change This # 
    #             coordinates[indice_y][indice_x-1],
    #             coordinates[indice_y][indice_x+1],

    #             coordinates[indice_y-1][indice_x+1],
    #             coordinates[indice_y-1][indice_x],

    #             coordinates[indice_y+1][indice_x],
    #             coordinates[indice_y+1][indice_x-1],
    #     ]

    # if indice_y == 4:
    if indice_y-1 < len(coordinates) and 0 <= indice_y-1:
        if indice_x < len(coordinates[indice_y-1]) and 0 <= indice_x:
            neighbor.append(coordinates[indice_y-1][indice_x])
        if indice_x-1 < len(coordinates[indice_y-1]) and 0 <= indice_x-1:
            neighbor.append(coordinates[indice_y-1][indice_x+1 if indice_y>4 else indice_x-1])
            
    if indice_y+1 < len(coordinates) and -1 < indice_y+1:
        if indice_x < len(coordinates[indice_y+1]) and 0 <= indice_x:
            neighbor.append(coordinates[indice_y+1][indice_x])
        if indice_x-1 < len(coordinates[indice_y+1]) and 0 <= indice_x-1:
            neighbor.append(coordinates[indice_y+1][indice_x+1 if indice_y<4 and indice_x>0 else indice_x-1])

    if indice_y < len(coordinates) and -1 < indice_y:
        if indice_x+1 < len(coordinates[indice_y]) and 0 <= indice_x+1:
            neighbor.append(coordinates[indice_y][indice_x+1])
        if indice_x-1 < len(coordinates[indice_y]) and -1 < indice_x-1:
            neighbor.append(coordinates[indice_y][indice_x-1])

        # neighbor = [
        #             
        #             coordinates[indice_y][indice_x-1],
        #             coordinates[indice_y][indice_x+1],

        #             coordinates[indice_y+1][indice_x],
        #             coordinates[indice_y+1][indice_x-1],  
                    
        #             coordinates[indice_y-1][indice_x],
        #             coordinates[indice_y-1][indice_x-1],
        #             ]

    return neighbor
