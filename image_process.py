import cv2


class ImageProcessing():
    def __init__(self,fold_path=None,image_path=None):
        self.fold_path = fold_path
        self.image_path = image_path
        self.image = None
        self.baocun = None
        
    def load_image(self, image_path):
        self.image_path = image_path
        # image_path 必须是字符串
        assert isinstance(self.image_path,str)
        # 将文件夹路径与图片路径拼接起来
        if image_path.startswith("/"):
            pass
        else:
            self.image_path = "".join([self.fold_path, self.image_path])
        print(self.image_path)
        self.image = cv2.imread(self.image_path)
        assert self.image is not None
#         print(self.image)
        
    def show_image(self, name="picture"):
        assert self.image is not None
        cv2.imshow(name,self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def beautify(self, d, sigmaColor, sigmaSpace):
        # 双边滤波器
        dst = cv2.bilateralFilter(self.image, d, sigmaColor, sigmaSpace)
        cv2.imshow("dst", dst)
        cv2.imshow("src", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.baocun = dst

    def bc(self,bclj):
        assert bclj is not None
        cv2.imwrite( bclj ,self.baocun)
        print(bclj)

# 实例化ImageProcessing 类，获得实例image_process
image_process = ImageProcessing("/home/lzw/git_rep/opencv_class")
image_process.load_image(image_path="1.jpg") 

#美化参数
image_process.show_image()
image_process.beautify(-2,20,10)

# 实例image_process 调用 bc 函数 ，保存图片。
image_process.bc(bclj="/home/lzw/git_rep/opencv_class/2.jpg")



