# Gerekli kütüphanelerin eklenmesi
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    # Uygulama nesnesini oluşturma
    app = QApplication(sys.argv) 
    
    # Ana pencere nesnesini oluşturma
    win = QMainWindow() 
    # Pencere başlığı  
    win.setWindowTitle("MY First Frame Ozan:")   
    # Pencere konumu ve boyutu (x, y, genişlik, yükseklik)
    win.setGeometry(400, 300, 600, 600)  
    # Pencere ikonu ayarlama
    win.setWindowIcon(QIcon("Python.png"))   

    # Etiket oluşturma ve pencereye ekleme (şu an kullanılmıyor ama örnek olarak bırakıldı)
    label_name = QtWidgets.QLabel(win)

    # Resim eklemek için QLabel kullan ve resmi yükleme
    content2 = QtWidgets.QLabel(win)
    content2.setPixmap(QtGui.QPixmap("Python.png"))  # Resmi ekleme
    # Resmin konumu ve boyutu
    content2.setGeometry(50, 80, 500, 400)   

    # Giriş butonu oluşturma
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Giriş:")
    # Buton konumu ve boyutu
    btn_save.setGeometry(0, 500, 100, 100)   

    # Çıkış butonu oluşturma
    btn_save2 = QtWidgets.QPushButton(win)
    btn_save2.setText("Çıkış:")
    # Buton konumu ve boyutu
    btn_save2.setGeometry(500, 500, 100, 100)   

    win.show()  # Pencereyi göster
    # Uygulamayı çalıştır ve çıkışı kontrol et
    sys.exit(app.exec_())  
# Fonksiyonu çalıştır
window()  
