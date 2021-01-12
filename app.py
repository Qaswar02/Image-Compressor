import sys
from PyQt5.QtWidgets import QApplication, QFileDialog,QInputDialog, QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PIL import Image
from PyQt5.QtCore import Qt
import os
import PIL





class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 10
        self.top = 10
        self.width = 700
        self.compress_width = 0
        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName("status")
        self.height = 600
        self.setObjectName("mainwindow")
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        self.setFixedSize(self.width, self.height)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Main Window Start
        self.single_border = QFrame(self)
        self.single_border.setObjectName("border")
        self.single_border.move(40,200)
        self.single_border.mousePressEvent =  self.single_border_clicked

        self.single_border_heading= QLabel(self.single_border)
        self.single_border_heading.setObjectName("Border_Heading")
        self.single_border_heading.setText("Compress One Image")
        self.single_border_heading.move(65,8)

        self.single_border_para = QLabel(self.single_border)
        self.single_border_para.setText("Click here in order to compress one image")
        self.single_border_para.setObjectName("Border_Para")
        self.single_border_para.move(15, 55)


        self.dir_border = QFrame(self)
        self.dir_border.setObjectName("border")
        self.dir_border.move(360,200)
        self.dir_border.mousePressEvent = self.dir_border_clicked


        self.dir_border_heading = QLabel(self.dir_border)
        self.dir_border_heading.setText("Compress Multiple Images")
        self.dir_border_heading.setObjectName("Border_Heading")
        self.dir_border_heading.move(45, 8)

        self.dir_border_para = QLabel(self.dir_border)
        self.dir_border_para.setText("If you want to compress multiple images at once. Select the folder and get a compressed version of that folder")
        self.dir_border_para.setObjectName("Border_Para")
        self.dir_border_para.setWordWrap(True)
        self.dir_border_para.move(15,55)



    #single border expanded


        self.single_border_expanded= QFrame(self)
        self.single_border_expanded.setObjectName("border_expanded")
        self.single_border_expanded.move(125, 110)
        self.single_border_expanded.setVisible(False)

        self.back_arrow_s= QLabel(self.single_border_expanded)
        self.back_arrow_s.move(25,0)
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked

        self.single_border_heading = QLabel(self.single_border_expanded)
        self.single_border_heading.setObjectName("Border_Heading")
        self.single_border_heading.setText("Compress One Image")
        self.single_border_heading.move(150, 8)

        self.select_image_label = QLabel(self.single_border_expanded)
        self.select_image_label.setObjectName("Border_Para")
        self.select_image_label.setText("Choose Image")
        self.select_image_label.move(30, 50)

        self.image_path= QLineEdit(self.single_border_expanded)
        self.image_path.setObjectName("path_text")
        self.image_path.move(60,85)

        self.browse_button = QPushButton(self.single_border_expanded)
        self.browse_button.setText("...")
        self.browse_button.move(325,83)
        self.browse_button.clicked.connect(self.select_file)
        self.browse_button.setObjectName("browse_button")

        self.select_image_quality = QLabel(self.single_border_expanded)
        self.select_image_quality.setObjectName("Border_Para")
        self.select_image_quality.setText("Choose Quality")
        self.select_image_quality.move(30,130)

        self.quality_path = QLineEdit(self.single_border_expanded)
        self.quality_path.setObjectName("quality_path_text")
        self.quality_path.move(60,160)


        self.quality_combo = QComboBox(self.single_border_expanded)
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.move(230,160)
        self.quality_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_combo.setObjectName('quality_combo')
        self.quality_combo.resize(96,26)

        self.compress_image = QPushButton(self.single_border_expanded)
        self.compress_image.setText("Compress Image")
        self.compress_image.clicked.connect(self.resize_pic)
        self.compress_image.move(150, 250)
        self.compress_image.setObjectName("compress_button")


    # single Border End



    # dir border expanded
        self.dir_border_expanded = QFrame(self)
        self.dir_border_expanded.setObjectName("border_expanded")
        self.dir_border_expanded.move(125, 110)
        self.dir_border_expanded.setVisible(False)

        self.back_arrow_d = QLabel(self.dir_border_expanded)
        self.back_arrow_d.move(25, 0)
        self.back_arrow_d.setTextFormat(Qt.RichText)
        self.back_arrow_d.setText("&#8592;")
        self.back_arrow_d.setObjectName("back_arrow")
        self.back_arrow_d.mousePressEvent = self.back_arrow_clicked

        self.dir_border_heading = QLabel(self.dir_border_expanded)
        self.dir_border_heading.setObjectName("Border_Heading")
        self.dir_border_heading.setText("Compress Multiple Images")
        self.dir_border_heading.move(130, 13)

        self.select_image_label = QLabel(self.dir_border_expanded)
        self.select_image_label.setObjectName("Border_Para")
        self.select_image_label.setText("Choose Directory")
        self.select_image_label.move(30, 50)

        self.source_path = QLineEdit(self.dir_border_expanded)
        self.source_path.setObjectName("path_text")
        self.source_path.move(60, 85)

        self.browse_button = QPushButton(self.dir_border_expanded)
        self.browse_button.setText("...")
        self.browse_button.move(325, 83)
        self.browse_button.setObjectName("browse_button")

        self.select_source_label = QLabel(self.dir_border_expanded)
        self.select_source_label.setObjectName("Border_Para")
        self.select_source_label.setText("Choose Directory")
        self.select_source_label.move(30, 50)

        self.source_path = QLineEdit(self.dir_border_expanded)
        self.source_path.setObjectName("path_text")
        self.source_path.move(60, 85)

        self.browse_source_button = QPushButton(self.dir_border_expanded)
        self.browse_source_button.setText("...")
        self.browse_source_button.move(325, 83)
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.clicked.connect(self.select_folder_source)

        self.select_dest_label = QLabel(self.dir_border_expanded)
        self.select_dest_label.setObjectName("Border_Para")
        self.select_dest_label.setText("Choose Destination Directory")
        self.select_dest_label.move(30,130)

        self.dest_path = QLineEdit(self.dir_border_expanded)
        self.dest_path.setObjectName("path_text")
        self.dest_path.move(60, 160)

        self.browse_dest_button = QPushButton(self.dir_border_expanded)
        self.browse_dest_button.setText("...")
        self.browse_dest_button.move(325, 158)
        self.browse_dest_button.clicked.connect(self.select_folder_dest)
        self.browse_dest_button.setObjectName("browse_button")

        self.select_dir_quality = QLabel(self.dir_border_expanded)
        self.select_dir_quality.setObjectName("Border_Para")
        self.select_dir_quality.setText("Choose Quality")
        self.select_dir_quality.move(30, 205)

        self.quality_dir_path = QLineEdit(self.dir_border_expanded)
        self.quality_dir_path.setObjectName("quality_path_text")
        self.quality_dir_path.move(60, 235)

        self.quality_dir_combo = QComboBox(self.dir_border_expanded)
        self.quality_dir_combo.addItem("High")
        self.quality_dir_combo.addItem("Medium")
        self.quality_dir_combo.addItem("Low")
        self.quality_dir_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_dir_combo.move(230, 235)
        self.quality_dir_combo.setObjectName('quality_combo')
        self.quality_dir_combo.resize(96, 26)

        self.compress_dir = QPushButton(self.dir_border_expanded)
        self.compress_dir.setText("Compress Images")
        self.compress_dir.clicked.connect(self.resize_folder)
        self.compress_dir.move(150, 300)
        self.compress_dir.setObjectName("compress_button")

    # dir border end
        self.show()
    #End of Border

    # Functions Start

    def select_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;JPEG(*.jpeg);;JPG(*.jpg)", )
        if fileName:
            print(fileName, _)
            self.image_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.quality_path.setText(str(self.image_width))
            self.compress_width = self.image_width

    def select_folder_source(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        print(folder)
        self.source_path.setText(folder)
        files = os.listdir(folder)
        first_pic = folder + "/" + files[0]
        img = Image.open(first_pic)
        self.image_width = img.width
        self.compress_width = self.image_width
        self.quality_dir_path.setText(str(self.image_width))

    def select_folder_dest(self):
        folder = (QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder)
        self.dest_path.setText(folder)
    def quality_current_value(self):
        if self.quality_combo.currentText() == "High":
            self.quality_path.setText(str(self.image_width))
            self.compress_width=self.image_width

        if self.quality_combo.currentText() == "Medium":
            self.quality_path.setText(str(int(self.image_width / 2)))
            self.compress_width = int(self.image_width / 2)
            self.compress_width = self.image_width

        if self.quality_combo.currentText() == "Low":
            self.quality_path.setText(str(int(self.image_width / 4)))
            self.compress_width = int(self.image_width / 4)

        if self.quality_dir_combo.currentText() == "High":
            self.quality_dir_path.setText(str(self.image_width))

        if self.quality_dir_combo.currentText() == "Medium":
            self.quality_dir_path.setText(str(int(self.image_width / 2)))
            self.compress_width = int(self.image_width / 2)

        if self.quality_dir_combo.currentText() == "Low":
            self.quality_dir_path.setText(str(int(self.image_width / 4)))
            self.compress_width = int(self.image_width / 4)

    def back_arrow_clicked(self,event):
        self.single_border.setVisible(True)
        self.dir_border.setVisible(True)
        self.single_border_expanded.setVisible(False)
        self.dir_border_expanded.setVisible(False)

    def single_border_clicked(self,event):
        print("single border clicked")
        self.single_border.setVisible(False)
        self.dir_border.setVisible(False)
        self.single_border_expanded.setVisible(True)
        self.dir_border_expanded.setVisible(False)

    def dir_border_clicked(self,event):
        print("dir border clicked")
        self.single_border.setVisible(False)
        self.dir_border.setVisible(False)
        self.single_border_expanded.setVisible(False)
        self.dir_border_expanded.setVisible(True)
    def resize_pic(self):

        old_pic = self.image_path.text()

        if old_pic == "":
            self.statusBar().showMessage("Message: Please choose an image")
            return

        print(old_pic)
        print(int(self.quality_path.text()))

        directories = self.image_path.text().split("/")
        print(directories)
        new_pic = ""
        new_pic_name, okPressed = QInputDialog.getText(self, "Save Image as", "Image Name:", QLineEdit.Normal, "")
        if okPressed and new_pic_name != '':
            print(new_pic_name)

            if old_pic[-4:] == ".jpeg":
                new_pic_name += ".jpeg"

            if old_pic[-4:] == ".png":
                new_pic_name += ".png"

            if old_pic[-4:] == ".jpg":
                new_pic_name += ".jpg"
            else:
                new_pic_name += ".jpeg"

            for directory in directories[:-1]:
                new_pic = new_pic + directory + "/"

            new_pic += new_pic_name
            print(new_pic)

        self.compreesion_code(old_pic, new_pic, int(self.quality_path.text()))
        self.statusBar().showMessage("Message: Compressed")

    def resize_folder(self):
        source_directory = self.source_path.text()
        files = os.listdir(source_directory)

        dest_directory = self.dest_path.text()

        if dest_directory == "" or source_directory == "":
            self.statusBar().showMessage("Message: Please select source and destination directory")
            return

        i = 0
        for file in files:
            i += 1
            print(file)
            if file[-4:] == '.jpg' or file[-4:] == '.png' or file[-5:] == '.jpeg' or file[-4:] == '.JPG' or file[
                                                                                                            -5:] == '.PNG' or file[
                                                                                                                              -5:] == '.JPEG':

                old_pic = source_directory + "/" + file
                new_pic = dest_directory + "/" + file

                img = Image.open(old_pic)
                self.image_width = img.width
                self.quality_dir_path.setText(str(self.image_width))

                old_pic = source_directory + "/" + file
                new_pic = dest_directory + "/" + file

                print(old_pic)
                print(new_pic)

                self.compreesion_code(old_pic, new_pic, self.image_width)

                total_images = len(files)
                images_done = i
                percentage = int(images_done / total_images * 100)
                print("Message: Compressed " + str(int(images_done / total_images * 100)) + "%")
                self.statusBar().showMessage("Message: Compressed " + str(int(images_done / total_images * 100)) + "%")
                QApplication.processEvents()
            else:
                print("ignored" + file)
                continue
        self.statusBar().showMessage("Message: Compressed")

    def compreesion_code(self, old_pic, new_pic, mywidth):
        try:
            img = Image.open(old_pic)

            wpercent = (mywidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            img.save(new_pic)
        except Exception as e:
            self.statusBar().showMessage("Message: "+str(e))







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())