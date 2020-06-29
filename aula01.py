# PyQt5 - Criando interfaces gráficas com Python
import numpy as np
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setup_main_window()
    self.initUI()
  
  def setup_main_window(self):
    self.x = 640
    self.y = 480
    self.setMinimumSize(QSize(self.x, self.y))
    self.setWindowTitle("Hello World - Processamento Digital de Imagens")
    self.wid = QWidget(self)
    self.setCentralWidget(self.wid)
    self.layout = QGridLayout()
    self.wid.setLayout(self.layout)

  def initUI(self):
    #Criar a barra de menu
    self.barrademenu = self.menuBar()

    #Criar os menus
    self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
    self.menuimagens = self.barrademenu.addMenu("&Transformações")
    self.menusobre = self.barrademenu.addMenu("&Sobre")

    #Criar as actions
    #menu arquivo
    self.opcaoabrir = self.menuarquivo.addAction("&Abrir")
    self.opcaoabrir.triggered.connect(self.open_file)
    self.opcaoabrir.setShortcut("Ctrl+A")
    #self.opcaoabrir.setCheckable(True)
    #self.opcaoabrir.setChecked(False)
    self.menuarquivo.addSeparator()
    self.opcaofechar = self.menuarquivo.addAction("&Fechar")
    self.opcaofechar.setShortcut("Ctrl+X")
    self.opcaofechar.triggered.connect(self.close)
    #self.opcaorecentes = self.menuarquivo.addMenu("&Recentes")
    #self.opcaoabrirrecente = self.opcaorecentes.addAction("&Abrir recentes...")
    
    #menu transformações
    self.opcaonegativo = self.menuimagens.addAction("Negativo")
    self.opcaoescaladecinza = self.menuimagens.addAction("Escala de cinza")
    self.opcaoescaladecinza.triggered.connect(self.transform_me)
    self.opcaodeteccaodebordas = self.menuimagens.addAction("Detecção de bordas")
    self.opcaodimensoes = self.menuimagens.addAction("Informações da imagem")
    self.opcaodimensoes.triggered.connect(self.getDimensoes)
    self.opcaosharpen = self.menuimagens.addAction("Sharpen Gideone")
    self.opcaosharpen.triggered.connect(self.sharpenGideone)

    #menu sobre
    self.opcaosobre = self.menusobre.addAction("Sobre")
    self.opcaosobre.triggered.connect(self.exibe_mensagem)
    self.opcaoapagar = self.menusobre.addAction("Apagar")
    self.opcaoapagar.triggered.connect(self.apagar_mensagem)

    #Criar barra de status
    self.barradestatus = self.statusBar()
    self.barradestatus.showMessage("Oi, bem-vindo ao meu software!", 3000)

    #Criar os widgets (Label, Button, Text, Image)

    #Criando um QLabel para texto
    self.texto = QLabel("Hello World from PyQt5 - IFTM", self)
    self.texto.adjustSize()
    self.largura = self.texto.frameGeometry().width()
    self.altura = self.texto.frameGeometry().height()
    self.texto.setAlignment(QtCore.Qt.AlignCenter)

    #Criando um botão
    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("Open me!")
    self.b1.clicked.connect(self.open_file)
    self.b2 = QtWidgets.QPushButton(self)
    self.b2.setText("Transform me!")
    self.b2.clicked.connect(self.transform_me)

    #Criando as imagens (QLabel)
    self.imagem1 = QLabel(self)
    self.endereco1 = 'images/arquivo_novo_2.ppm'
    self.pixmap1 = QtGui.QPixmap(self.endereco1)
    self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
    self.imagem1.setPixmap(self.pixmap1)
    self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

    
    self.imagem2 = QLabel(self)
    self.endereco2 = 'images/balao.ppm'
    self.pixmap2 = QtGui.QPixmap(self.endereco2)
    self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
    self.imagem2.setPixmap(self.pixmap2)
    self.imagem2.setAlignment(QtCore.Qt.AlignCenter)


    # Organizando os widgets dentro da GridLayout
    self.layout.addWidget(self.texto, 0, 0, 1, 2)
    self.layout.addWidget(self.b1, 2, 0)
    self.layout.addWidget(self.b2, 2, 1)
    self.layout.addWidget(self.imagem1, 1, 0)
    self.layout.addWidget(self.imagem2, 1, 1)
    self.layout.setRowStretch(0, 0)
    self.layout.setRowStretch(1, 1)
    self.layout.setRowStretch(2, 0)

  #Métodos para ações dos botões
  def getDimensoes(self):
    #abrir o arquivo
    self.arquivoentrada = open(self.endereco1, "r+")
    self.tipoarquivo = self.arquivoentrada.readline() # Tipo
    self.comentario = self.arquivoentrada.readline() # Comentário
    self.linha = self.arquivoentrada.readline() # Dimensões
    self.dimensoes = self.linha.split()
    self.dimensoes = np.array(self.dimensoes, dtype=int)
    self.arquivoentrada.close()

    #monta o texto da caixa de dialogo
    self.largura = self.dimensoes[0]
    self.altura = self.dimensoes[1]
    self.fileName = self.endereco1.rpartition('/')
    self.fileName = self.fileName[2]
    self.text_dimensoes = "Arquivo: " + str(self.fileName) + "\n"
    self.text_dimensoes = self.text_dimensoes + "Tipo: " + self.tipoarquivo
    self.text_dimensoes = self.text_dimensoes + "Comentário: " + self.comentario
    self.text_dimensoes = self.text_dimensoes + "Largura: " + str(self.largura) + "\n"
    self.text_dimensoes = self.text_dimensoes + "Altura: " + str(self.altura)
    
    #monta a caixa de dialogo
    self.msg = QMessageBox()
    self.msg.setText(self.text_dimensoes)
    self.msg.exec_()

  def apagar_mensagem(self):
    self.barradestatus.clearMessage()

  def exibe_mensagem(self):
    #self.barradestatus.showMessage("Você clicou no Sobre...")
    self.msg = QMessageBox()
    #self.msg.setIcon(QMessageBox.Information) #Icones padrão
    self.iconpixmap = QtGui.QPixmap('images/web.ico')
    self.iconpixmap = self.iconpixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
    self.msg.setIconPixmap(self.iconpixmap)
    self.msg.setText("Desenvolvido por André Luiz França Batista")
    self.msg.setWindowTitle("Sobre")
    self.msg.setInformativeText("Ituiutaba, 19 de Junho de 2020\nInstituto Federal do Triângulo Mineiro")
    self.msg.setDetailedText("Texto com mais detalhes sobre este aplicativo...")
    self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    self.msg.exec_() # exibir a caixa de mensagens, ou caixa de diálogo
    self.reply = self.msg.clickedButton()
    self.barradestatus.showMessage("Foi clicado o botão: " + str(self.reply.text()))

    if self.reply.text() == "OK":
      print('Apertou OK')
    if self.reply.text() == "Cancel":
      print('Apertou Cancel')
  
  def testaMenu(self):
    print("Menu clicado")
  
  def open_file(self):
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
      self, caption='Open image', 
      directory=QtCore.QDir.currentPath(),
      filter='All files (*.*);;Images (*.ppm; *.pgm; *.pbm)', 
      initialFilter='Images (*.ppm; *.pgm; *.pbm)'
    )
    print(fileName)
    if fileName != '':
      self.endereco1 = fileName
      self.pixmap1 = QtGui.QPixmap(self.endereco1)
      self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
      self.imagem1.setPixmap(self.pixmap1)

  def transform_me(self):
    self.entrada = self.endereco1
    self.saida = 'images/arquivo_novo.pgm'
    self.script = '.\ppm_to_pgm.py'
    self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
    print(self.program)
    subprocess.run(self.program, shell=True)
    self.endereco2 = self.saida
    self.pixmap2 = QtGui.QPixmap(self.endereco2)
    self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
    self.imagem2.setPixmap(self.pixmap2)

  def sharpenGideone(self):
    self.entrada = self.endereco1
    self.saida = 'images/arquivo_novo.ppm'
    self.script = '.\sharpengideone.py'
    self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
    print(self.program)
    subprocess.run(self.program, shell=True)
    self.endereco2 = self.saida
    self.pixmap2 = QtGui.QPixmap(self.endereco2)
    self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
    self.imagem2.setPixmap(self.pixmap2)

  def button_clicked(self):
    self.texto.setText("Você clicou no botão!!!")
    self.texto.adjustSize()
    self.novoEndereco = QtGui.QPixmap('images/balao.pbm')
    self.imagem1.setPixmap(self.novoEndereco)

def window():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

window()
  