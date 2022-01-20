


class SearchPicture:

    def SP_start(path):
        import os
        Picturename = []
        for filename in os.listdir(path):
            if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
               Picturename.append(filename)
        return Picturename
class EditPictureName():
    def EP_start(name):
        OnlyName = []
        i = 0
        while i < len(name):
            OnlyName.append(str(name[i]).split('.')[0])
            i+=1
        return OnlyName

class CreateFolder():

    def CF_start(self,path):
        import os
        i = 0
        while i < len(self):

                try:
                    os.mkdir(path+self[i])
                except(Exception):
                    print('Ошибка',Exception)
                i+=1

class SwipePicture:
    def SP_start(path_old,path_new,name,onlyname):
        from shutil import copyfile as cf
        i = 0
        while i < len(name):
            old = str(path_old+name[i])
            new = str(path_new+onlyname[i]+"/"+name[i])
            try:
                cf(old,new)
            except(Exception):
                print('error:',Exception)
            i+=1

if __name__ == '__main__':
    #path to import image
    path_PictureFolder = '/home/persone1/Документы/Zakazchik/'
    #path to folder-save image
    NewFolder = '/home/persone1/Документы/new path/'

    #start class
    PictureName = SearchPicture.SP_start(path_PictureFolder)
    OnlyNamePicture = EditPictureName.EP_start(PictureName)
    CreateFolder.CF_start(OnlyNamePicture,NewFolder)
    SwipePicture.SP_start(path_PictureFolder,NewFolder,PictureName,OnlyNamePicture)
    print("DONE")