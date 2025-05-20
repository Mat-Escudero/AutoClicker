# Import ui file
from ui_main_window import *
from ui_clickSettingsWindow import *
from ui_recordingWindow import *
from ui_changeButtonWindow import *
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt, QEventLoop, QTimer, Signal, QObject
import pyautogui
import keyboard

class MainWindow(QMainWindow):
    trigger_hotkey = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variáveis para o autoClicker
        self.tempo_click = {
            "horas": 0,
            "minutos": 0,
            "segundos": 1,
            "milissegundos": 0
        }
        self.botao_clique = "Left"
        self.botao_amount = "Single"
        self.ativa_autoclick = False
        self.botao_ativar = "F8"
        self.record_click = False
        self.order_click = [[],[]]
        self.order_time_click = []

        self.auto_click_timer_simples = QTimer()
        self.auto_click_timer_simples.timeout.connect(self.fazer_click_simples)
        self.auto_click_timer_order = QTimer()
        self.auto_click_timer_order.timeout.connect(self.fazer_click_order)


        # Crie referências para manter as janelas vivas
        self.click_settings_window = None
        self.recording_window = None

        self.ui.changeActiveButton.clicked.connect(self.abrir_change_button)

        self.ui.changeActiveButton.setText("Press " + self.botao_ativar + " to active")

        self.ui.actionClick_Settings_2.triggered.connect(self.abrir_click_settings)
        self.ui.actionRecording.triggered.connect(self.abrir_recording)
        self.ui.actionExit.triggered.connect(self.exit)

        self.trigger_hotkey.connect(self.condicional_auto_click)

        keyboard.add_hotkey(self.botao_ativar.lower(), self.emitir_trigger)

    def emitir_trigger(self):
        self.trigger_hotkey.emit()

    def mudar_botao_ativar(self):
        keyboard.add_hotkey(self.botao_ativar.lower(), self.emitir_trigger)

    def abrir_click_settings(self):
        if self.ativa_autoclick == False:
            self.click_settings_window = clickSettingsWindow(self)
            self.click_settings_window.exec()

    def abrir_recording(self):
        if self.ativa_autoclick == False:
            self.recording_window = recordingWindow(self)
            self.recording_window.exec()
    
    def exit(self):
        if self.ativa_autoclick == False:
            QApplication.quit()
    
    def abrir_change_button(self):
        if self.ativa_autoclick == False:
            self.changeButtonWindow = changeButtonWindow(self)
            self.changeButtonWindow.exec()
            self.ui.changeActiveButton.setText("Press " + self.botao_ativar + " to active")

    def condicional_auto_click(self):
        self.quantidade = 1 if self.botao_amount == "Single" else 2
        if self.ativa_autoclick == True:
            self.ui.changeActiveButton.setText("Press " + self.botao_ativar + " to active")
            self.ativa_autoclick = False
            self.parar_autoclick()
        elif self.ativa_autoclick == False and self.record_click == False:
            self.ui.changeActiveButton.setText("Press " + self.botao_ativar + " to desactive")
            self.ativa_autoclick = True
            self.ativar_autoclick_simples()
        else:
            if len(self.order_click[0]) >= 1:
                self.ui.changeActiveButton.setText("Press " + self.botao_ativar + " to desactive")
                self.ativa_autoclick = True
                self.ativar_autoclick_order()      

    def parar_autoclick(self):
        self.auto_click_timer_order.stop()
        self.auto_click_timer_simples.stop()

    def ativar_autoclick_simples(self):
        self.auto_click_timer_simples.stop()
        self.tempo = (
            self.tempo_click["horas"] * 3600000 +
            self.tempo_click["minutos"] * 60000 +
            self.tempo_click["segundos"] * 1000 +
            self.tempo_click["milissegundos"] 
        )
        self.auto_click_timer_simples.start(self.tempo)
    
    def fazer_click_simples(self):
        pyautogui.click(
            button=self.botao_clique.lower(),
            clicks=self.quantidade
        )

    def ativar_autoclick_order(self):
        self.auto_click_timer_order.stop()
        self.indice_intervalo = 0
        self.auto_click_timer_order.start(0) 

    def fazer_click_order(self):
        if self.indice_intervalo >= len(self.order_time_click):
            self.indice_intervalo = 0  # Reinicia


        pyautogui.click(
            self.order_click[0][self.indice_intervalo],
            self.order_click[1][self.indice_intervalo],
            button=self.botao_clique.lower(),
            clicks=self.quantidade
        )


        # Pega próximo tempo como dicionário
        tempo_dict = self.order_time_click[self.indice_intervalo]

        # Converte para milissegundos
        intervalo_ms = (
            tempo_dict["horas"] * 3600000 +
            tempo_dict["minutos"] * 60000 +
            tempo_dict["segundos"] * 1000 +
            tempo_dict["milissegundos"]
        )

        self.indice_intervalo += 1
        self.auto_click_timer_order.start(intervalo_ms)




# Janela de configurações de clique
class clickSettingsWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_clickSettingsWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.ui.comboBox.addItems(["Left", "Right"])
        self.ui.comboBox.setCurrentText(self.main_window.botao_clique)
        self.ui.spinBox.setValue(self.main_window.tempo_click["horas"])
        self.ui.spinBox_2.setValue(self.main_window.tempo_click["minutos"])
        self.ui.spinBox_3.setValue(self.main_window.tempo_click["segundos"])
        self.ui.spinBox_4.setValue(self.main_window.tempo_click["milissegundos"])

        # Conectando mudança de seleção à função de atualização
        self.ui.comboBox.currentTextChanged.connect(self.atualizar_botao_clique)
        self.ui.spinBox.valueChanged.connect(self.atualizar_tempo)
        self.ui.spinBox_2.valueChanged.connect(self.atualizar_tempo)
        self.ui.spinBox_3.valueChanged.connect(self.atualizar_tempo)
        self.ui.spinBox_4.valueChanged.connect(self.atualizar_tempo)

        

        self.ui.comboBox_2.addItems(["Single", "Double"])
        self.ui.comboBox_2.setCurrentText(self.main_window.botao_amount)

        # Conectando mudança de seleção à função de atualização
        self.ui.comboBox_2.currentTextChanged.connect(self.atualizar_botao_amount)

    def atualizar_botao_clique(self, novo_valor):
        self.main_window.botao_clique = novo_valor

    def atualizar_botao_amount(self, novo_valor):
        self.main_window.botao_amount = novo_valor
    
    def atualizar_tempo(self):
        self.main_window.tempo_click = {
            "horas": self.ui.spinBox.value(),
            "minutos": self.ui.spinBox_2.value(),
            "segundos": self.ui.spinBox_3.value(),
            "milissegundos": self.ui.spinBox_4.value()
        }

# Janela de gravação
class recordingWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_recordingWindow()
        self.ui.setupUi(self)

        self.main_window = main_window
        
        self.pos = None

        self.habilitar_ou_desabilitar()

        self.ui.label_2.setText(f"{len(self.main_window.order_click[0])}")

        self.ui.pushButton.clicked.connect(self.pick_botao)
        self.ui.pushButton_2.clicked.connect(self.clear_botao)

        self.ui.spinBox.setValue(0)
        self.ui.spinBox_2.setValue(0)
        self.ui.spinBox_3.setValue(1)
        self.ui.spinBox_4.setValue(0)

        self.ui.radioButton.setChecked(self.main_window.record_click)
        
        self.ui.radioButton.toggled.connect(self.isChecked)


    def clear_botao(self):
        for linha in self.main_window.order_click:
            linha.clear()

        self.main_window.order_time_click.clear()
        self.ui.label_2.setText(f"{len(self.main_window.order_click[0])}")

    def pick_botao(self):
        self.ui.pushButton.setText("Waiting click")
        overlay = MouseCaptureOverlay(self)
        overlay.exec()
        self.salvar_posicao()
        self.salvar_tempo()
        self.ui.label_2.setText(f"{len(self.main_window.order_click[0])}")

    def salvar_posicao(self):
        if self.pos is not None:
            self.main_window.order_click[0].append(self.pos.x())
            self.main_window.order_click[1].append(self.pos.y())

        self.ui.pushButton.setText("Pick point")

    def salvar_tempo(self):
        if self.pos is not None:
            self.main_window.order_time_click.append({
                "horas": self.ui.spinBox.value(),
                "minutos": self.ui.spinBox_2.value(),
                "segundos": self.ui.spinBox_3.value(),
                "milissegundos": self.ui.spinBox_4.value()
            })

    def isChecked(self):
        if self.ui.radioButton.isChecked():
            self.main_window.record_click = True
        else:
            self.main_window.record_click = False
        self.habilitar_ou_desabilitar()

    def habilitar_ou_desabilitar(self):
        
        self.ui.pushButton.setEnabled(self.main_window.record_click)
        self.ui.pushButton_2.setEnabled(self.main_window.record_click)
        self.ui.spinBox.setEnabled(self.main_window.record_click)
        self.ui.spinBox_2.setEnabled(self.main_window.record_click)
        self.ui.spinBox_3.setEnabled(self.main_window.record_click)
        self.ui.spinBox_4.setEnabled(self.main_window.record_click)
        self.ui.label.setEnabled(self.main_window.record_click)
        self.ui.label_2.setEnabled(self.main_window.record_click)
        self.ui.label_3.setEnabled(self.main_window.record_click)
        self.ui.label_4.setEnabled(self.main_window.record_click)
        self.ui.label_5.setEnabled(self.main_window.record_click)
        self.ui.label_6.setEnabled(self.main_window.record_click)
        self.ui.label_7.setEnabled(self.main_window.record_click)
        self.ui.label_8.setEnabled(self.main_window.record_click)


# Tela invisível para selecionar coordenadas
class MouseCaptureOverlay(QDialog):
    def __init__(self, recording_window):
        super().__init__()
        self.recording_window = recording_window
        self._mouse_pos = None

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint 
        )
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setWindowOpacity(0.1)
        QApplication.setOverrideCursor(Qt.CrossCursor)

        self.showFullScreen()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_pos = QCursor.pos()
            self.recording_window.pos = self._mouse_pos
            QApplication.restoreOverrideCursor()
            self.accept()


# Janela de mudança de botão
class changeButtonWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_changeButtonWindow()
        self.ui.setupUi(self)

        self.main_window = main_window
        self.tecla_anterior = self.main_window.botao_ativar

        self.escutando_tecla = False

        self.ui.label.setText(self.main_window.botao_ativar)
        self.ui.label.setStyleSheet("border: 1px solid black; padding: 4px;")

        self.ui.OKButton.clicked.connect(self.ok_botao)
        self.ui.CancelButton.clicked.connect(self.cancel_botao)

        self.ui.pushButton.clicked.connect(self.mudar_botao)

    def mudar_botao(self):
        self.ui.label.setText("Press key")
        self.escutando_tecla = True
    
    def keyPressEvent(self, event):
        if self.escutando_tecla:
            tecla = event.key()
            nome_tecla = QKeySequence(tecla).toString()
            self.main_window.botao_ativar = nome_tecla
            self.ui.label.setText(self.main_window.botao_ativar)
            self.main_window.mudar_botao_ativar()
            self.escutando_tecla = False

    def ok_botao(self):
        self.close()

    def cancel_botao(self):
        self.main_window.botao_ativar = self.tecla_anterior
        self.close()
        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())