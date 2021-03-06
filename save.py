                                                                
moonNode = sg.SceneGraphNode('moonNode')   
moonNode.transform = np.array([[0.02, 0.  , 0.  , 0.  ],
 [0.  , 0.02, 0.  , 0.  ],
 [0.  , 0.  , 0.02, 0.  ],
 [0.  , 0.  , 0.  , 1.  ]], dtype=np.float32)                
moonNode.childs += [insertGPUShape]
      
                                                                
moonRotation = sg.SceneGraphNode('moonRotation')   
moonRotation.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
moonRotation.childs += [moonNode]
      
                                                                
moonPosition = sg.SceneGraphNode('moonPosition')   
moonPosition.transform = np.array([[1. , 0. , 0. , 0.3],
 [0. , 1. , 0. , 0. ],
 [0. , 0. , 1. , 0. ],
 [0. , 0. , 0. , 1. ]], dtype=np.float32)                
moonPosition.childs += [moonRotation]
      
                                                                
moonSystem = sg.SceneGraphNode('moonSystem')   
moonSystem.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
moonSystem.childs += [moonPosition]
      
                                                                
earthNode = sg.SceneGraphNode('earthNode')   
earthNode.transform = np.array([[0.1, 0. , 0. , 0. ],
 [0. , 0.1, 0. , 0. ],
 [0. , 0. , 0.1, 0. ],
 [0. , 0. , 0. , 1. ]], dtype=np.float32)                
earthNode.childs += [insertGPUShape]
      
                                                                
earthRotation = sg.SceneGraphNode('earthRotation')   
earthRotation.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
earthRotation.childs += [earthNode]
      
                                                                
earthPosition = sg.SceneGraphNode('earthPosition')   
earthPosition.transform = np.array([[1. , 0. , 0. , 1.5],
 [0. , 1. , 0. , 0. ],
 [0. , 0. , 1. , 0. ],
 [0. , 0. , 0. , 1. ]], dtype=np.float32)                
earthPosition.childs += [earthRotation, moonSystem]
      
                                                                
earthSystem = sg.SceneGraphNode('earthSystem')   
earthSystem.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
earthSystem.childs += [earthPosition]
      
                                                                
sunNode = sg.SceneGraphNode('sunNode')   
sunNode.transform = np.array([[0.3, 0. , 0. , 0. ],
 [0. , 0.3, 0. , 0. ],
 [0. , 0. , 0.3, 0. ],
 [0. , 0. , 0. , 1. ]], dtype=np.float32)                
sunNode.childs += [insertGPUShape]
      
                                                                
sunRotation = sg.SceneGraphNode('sunRotation')   
sunRotation.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
sunRotation.childs += [sunNode]
      
                                                                
solarSystem = sg.SceneGraphNode('solarSystem')   
solarSystem.transform = np.array([[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 1., 0.],
 [0., 0., 0., 1.]], dtype=np.float32)                
solarSystem.childs += [sunRotation, earthSystem]
      
