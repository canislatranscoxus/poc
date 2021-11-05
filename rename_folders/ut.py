from DirRenamer import DirRenamer

dir_path = '/home/art/git/poc/rename_folders'
#dir_path = '/home/art/git/cbd/basmati/static/shop/images/products/x'

def ut_01( ):
    dr = DirRenamer()
    dr.get_subfolders   ( dir_path )
    dr.rename_subfolders( dir_path, delta= 10 )
    dr.get_subfolders   ( dir_path )

def ut_02(  ):
    dr = DirRenamer()
    dr.get_subfolders   ( dir_path )    
    dr.del_prefix_2_subfolders( dir_path, prefix='tmp_' )
    dr.get_subfolders   ( dir_path )

if __name__ == '__main__' : 
    ut_01()
