import numpy as np
import os, sys
import gmsh

# ========================================================= #
# ===  make__geometry.py                                === #
# ========================================================= #

def make__geometry():
    import nkGmshRoutines.generate__sector180 as gsc
    ret1 = gsc.generate__sector180( r1=0.0, r2=1.0, height=0.4, side="+", \
                                    defineVolu=True, fuse=True )
    ret2 = gsc.generate__sector180( r1=0.0, r2=1.0, height=0.4, side="-", \
                                    defineVolu=True, fuse=True )
    return()


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    
    # ------------------------------------------------- #
    # --- [1] initialization of the gmsh            --- #
    # ------------------------------------------------- #
    gmsh.initialize()
    gmsh.option.setNumber( "General.Terminal", 1 )
    gmsh.option.setNumber( "Mesh.Algorithm"  , 5 )
    gmsh.option.setNumber( "Mesh.Algorithm3D", 4 )
    gmsh.option.setNumber( "Mesh.SubdivisionAlgorithm", 0 )
    gmsh.model.add( "model" )
    
    # ------------------------------------------------- #
    # --- [2] Modeling                              --- #
    # ------------------------------------------------- #

    make__geometry()
    
    gmsh.model.occ.synchronize()
    gmsh.model.occ.removeAllDuplicates()
    gmsh.model.occ.synchronize()


    # ------------------------------------------------- #
    # --- [3] Mesh settings                         --- #
    # ------------------------------------------------- #
    
    meshFile = "dat/mesh_rxy.conf"
    physFile = "dat/phys_rxy.conf"
    import nkGmshRoutines.assign__meshsize as ams
    meshes = ams.assign__meshsize( meshFile=meshFile, physFile=physFile )
    
    # gmsh.option.setNumber( "Mesh.CharacteristicLengthMin", 0.1 )
    # gmsh.option.setNumber( "Mesh.CharacteristicLengthMax", 0.1 )
    

    # ------------------------------------------------- #
    # --- [4] post process                          --- #
    # ------------------------------------------------- #
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(3)
    gmsh.write( "msh/model.msh" )
    gmsh.finalize()
    

