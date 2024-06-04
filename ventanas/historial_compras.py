# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historial_compras.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas.imagenes import imagenes
from PyQt5.QtCore import Qt


class Ui_HistorialCompras(object):
    def setupUi(self, HistorialCompras):
        HistorialCompras.setObjectName("HistorialCompras")
        HistorialCompras.resize(1195, 722)
        HistorialCompras.setMinimumSize(QtCore.QSize(1195, 645))
        HistorialCompras.setMaximumSize(QtCore.QSize(1195, 645))
        HistorialCompras.setStyleSheet("")
        self.widget = QtWidgets.QWidget(HistorialCompras)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1195, 645))
        self.widget.setMinimumSize(QtCore.QSize(1195, 645))
        self.widget.setMaximumSize(QtCore.QSize(1195, 645))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget.setStyleSheet(
            "QPushButton{\n"
            "border:2px solid rgb(28, 165, 206);\n"
            "border-radius: 10px;\n"
            "color: #fff;\n"
            'font: 57 12pt "Yu Gothic Medium";\n'
            "padding:5px;\n"
            "background-color:none;\n"
            "}\n"
            "QPushButton:hover {\n"
            "border:1px solid rgb(200, 158, 91);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    padding-top: 10px;\n"
            "    padding-left: 10px;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "background-color:transparent;\n"
            "border-bottom:2px solid rgb(28, 165, 206);\n"
            "border-radius: 0px;\n"
            "padding: 7px;\n"
            "color: #fff;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "background-color:transparent;\n"
            "}\n"
            "QLineEdit:focus {\n"
            "background-color:transparent;\n"
            "}\n"
            "\n"
            "QTreeView{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(45, 45, 45, 162));\n"
            "color: #fff;\n"
            "border: 1px solid #000;\n"
            "font-size:15px;\n"
            "}\n"
            "QHeaderView::section {\n"
            "color: #000;\n"
            "border: 1px solid #000;\n"
            "font-size:14px;\n"
            "}\n"
            "QTreeView::item {\n"
            "color: #fff;\n"
            "border-right: 0.5px solid #fff;\n"
            "border-bottom: 0.5px solid #fff;\n"
            "}\n"
            "QTreeView::item:selected {\n"
            "background-color: red;\n"
            "}\n"
            "QWidget#widget{\n"
            "    background-image: url(:/historial_compras/380346.jpg);\n"
            "}\n"
            "\n"
            "QRadioButton{\n"
            "color:#fff;\n"
            "font-size:14px;\n"
            "}"
        )
        self.widget.setObjectName("widget")
        self.boton_filtrar_compras_cregar = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_compras_cregar.setGeometry(QtCore.QRect(630, 460, 201, 51))
        self.boton_filtrar_compras_cregar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_compras_cregar.setStyleSheet("")
        self.boton_filtrar_compras_cregar.setObjectName("boton_filtrar_compras_cregar")
        self.boton_mostrar_compras_totales = QtWidgets.QPushButton(self.widget)
        self.boton_mostrar_compras_totales.setGeometry(QtCore.QRect(630, 400, 201, 51))
        self.boton_mostrar_compras_totales.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_mostrar_compras_totales.setStyleSheet("")
        self.boton_mostrar_compras_totales.setObjectName(
            "boton_mostrar_compras_totales"
        )
        self.boton_consultar_costos = QtWidgets.QPushButton(self.widget)
        self.boton_consultar_costos.setGeometry(QtCore.QRect(630, 280, 201, 51))
        self.boton_consultar_costos.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_consultar_costos.setStyleSheet("")
        self.boton_consultar_costos.setObjectName("boton_consultar_costos")
        self.label_modificar_compra = QtWidgets.QLabel(self.widget)
        self.label_modificar_compra.setGeometry(QtCore.QRect(620, 170, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_modificar_compra.setFont(font)
        self.label_modificar_compra.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_modificar_compra.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_modificar_compra.setText("")
        self.label_modificar_compra.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modificar_compra.setObjectName("label_modificar_compra")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(130, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet(
            'font: 25pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.boton_filtrar_compras_fara = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_compras_fara.setGeometry(QtCore.QRect(630, 520, 201, 51))
        self.boton_filtrar_compras_fara.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_compras_fara.setStyleSheet("")
        self.boton_filtrar_compras_fara.setObjectName("boton_filtrar_compras_fara")
        self.treeview_compras = QtWidgets.QTreeView(self.widget)
        self.treeview_compras.setGeometry(QtCore.QRect(10, 60, 611, 591))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.treeview_compras.setFont(font)
        self.treeview_compras.setStyleSheet("")
        self.treeview_compras.setObjectName("treeview_compras")
        self.modelo_compras = QtGui.QStandardItemModel()
        self.treeview_compras.setModel(self.modelo_compras)

        self.treeview_compras.setFocusPolicy(Qt.NoFocus)
        self.modelo_compras.setHorizontalHeaderLabels(
            ["N°", "Fecha", "Empresa", "Producto", "Cant", "Costo c/u", "Total"]
        )
        header = self.treeview_compras.header()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.resizeSection(0, 70)
        header.resizeSection(1, 90)
        header.resizeSection(2, 60)
        header.resizeSection(3, 155)
        header.resizeSection(4, 30)
        header.resizeSection(5, 90)
        header.resizeSection(6, 70)

        self.boton_eliminar_compra = QtWidgets.QPushButton(self.widget)
        self.boton_eliminar_compra.setGeometry(QtCore.QRect(630, 200, 201, 51))
        self.boton_eliminar_compra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_eliminar_compra.setStyleSheet("")
        self.boton_eliminar_compra.setObjectName("boton_eliminar_compra")
        self.boton_modificar_compra = QtWidgets.QPushButton(self.widget)
        self.boton_modificar_compra.setGeometry(QtCore.QRect(630, 120, 201, 51))
        self.boton_modificar_compra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_modificar_compra.setStyleSheet("")
        self.boton_modificar_compra.setObjectName("boton_modificar_compra")
        self.label_eliminar_compra = QtWidgets.QLabel(self.widget)
        self.label_eliminar_compra.setGeometry(QtCore.QRect(610, 250, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_eliminar_compra.setFont(font)
        self.label_eliminar_compra.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_eliminar_compra.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_eliminar_compra.setText("")
        self.label_eliminar_compra.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eliminar_compra.setObjectName("label_eliminar_compra")
        self.boton_filtrar_compras_fontana = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_compras_fontana.setGeometry(QtCore.QRect(630, 580, 201, 51))
        self.boton_filtrar_compras_fontana.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_compras_fontana.setStyleSheet("")
        self.boton_filtrar_compras_fontana.setObjectName(
            "boton_filtrar_compras_fontana"
        )
        self.boton_volver = QtWidgets.QPushButton(self.widget)
        self.boton_volver.setGeometry(QtCore.QRect(1070, 30, 101, 31))
        self.boton_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_volver.setStyleSheet("")
        self.boton_volver.setObjectName("boton_volver")
        self.widget_consultar_costos = QtWidgets.QWidget(self.widget)
        self.widget_consultar_costos.setGeometry(QtCore.QRect(830, 160, 341, 431))
        self.widget_consultar_costos.setStyleSheet("")
        self.widget_consultar_costos.setObjectName("widget_consultar_costos")
        self.label_fecha_inicial = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_fecha_inicial.setGeometry(QtCore.QRect(130, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fecha_inicial.setFont(font)
        self.label_fecha_inicial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_fecha_inicial.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_fecha_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha_inicial.setObjectName("label_fecha_inicial")
        self.input_dia_inicial = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_dia_inicial.setGeometry(QtCore.QRect(70, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_dia_inicial.setFont(font)
        self.input_dia_inicial.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_dia_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.input_dia_inicial.setObjectName("input_dia_inicial")
        self.input_mes_inicial = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_mes_inicial.setGeometry(QtCore.QRect(140, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_mes_inicial.setFont(font)
        self.input_mes_inicial.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_mes_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.input_mes_inicial.setObjectName("input_mes_inicial")
        self.input_anio_inicial = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_anio_inicial.setGeometry(QtCore.QRect(210, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_anio_inicial.setFont(font)
        self.input_anio_inicial.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_anio_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.input_anio_inicial.setObjectName("input_anio_inicial")
        self.label_fecha_final = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_fecha_final.setGeometry(QtCore.QRect(130, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fecha_final.setFont(font)
        self.label_fecha_final.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_fecha_final.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_fecha_final.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha_final.setObjectName("label_fecha_final")
        self.input_dia_final = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_dia_final.setGeometry(QtCore.QRect(70, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_dia_final.setFont(font)
        self.input_dia_final.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_dia_final.setAlignment(QtCore.Qt.AlignCenter)
        self.input_dia_final.setObjectName("input_dia_final")
        self.input_mes_final = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_mes_final.setGeometry(QtCore.QRect(140, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_mes_final.setFont(font)
        self.input_mes_final.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_mes_final.setAlignment(QtCore.Qt.AlignCenter)
        self.input_mes_final.setObjectName("input_mes_final")
        self.input_anio_final = QtWidgets.QLineEdit(self.widget_consultar_costos)
        self.input_anio_final.setGeometry(QtCore.QRect(210, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_anio_final.setFont(font)
        self.input_anio_final.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_anio_final.setAlignment(QtCore.Qt.AlignCenter)
        self.input_anio_final.setObjectName("input_anio_final")
        self.label_fecha_no_valida = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_fecha_no_valida.setGeometry(QtCore.QRect(50, 180, 241, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fecha_no_valida.setFont(font)
        self.label_fecha_no_valida.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_fecha_no_valida.setStyleSheet(
            'font: 10pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_fecha_no_valida.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha_no_valida.setObjectName("label_fecha_no_valida")
        self.boton_consultar = QtWidgets.QPushButton(self.widget_consultar_costos)
        self.boton_consultar.setGeometry(QtCore.QRect(110, 310, 131, 41))
        self.boton_consultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_consultar.setStyleSheet("")
        self.boton_consultar.setObjectName("boton_consultar")
        self.label_total_gastado = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_total_gastado.setGeometry(QtCore.QRect(90, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_total_gastado.setFont(font)
        self.label_total_gastado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_total_gastado.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_total_gastado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_gastado.setObjectName("label_total_gastado")
        self.label_resultado_total_gastado = QtWidgets.QLabel(
            self.widget_consultar_costos
        )
        self.label_resultado_total_gastado.setGeometry(QtCore.QRect(-10, 400, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_resultado_total_gastado.setFont(font)
        self.label_resultado_total_gastado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_resultado_total_gastado.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "color: rgb(67, 255, 67);\n"
            "background: none;"
        )
        self.label_resultado_total_gastado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado_total_gastado.setObjectName(
            "label_resultado_total_gastado"
        )
        self.label_stock_2 = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_stock_2.setGeometry(QtCore.QRect(50, 210, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_stock_2.setFont(font)
        self.label_stock_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stock_2.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_stock_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stock_2.setObjectName("label_stock_2")
        self.eleccion_cregar = QtWidgets.QRadioButton(self.widget_consultar_costos)
        self.eleccion_cregar.setGeometry(QtCore.QRect(50, 240, 61, 17))
        self.eleccion_cregar.setObjectName("eleccion_cregar")
        self.eleccion_fara = QtWidgets.QRadioButton(self.widget_consultar_costos)
        self.eleccion_fara.setGeometry(QtCore.QRect(140, 240, 51, 17))
        self.eleccion_fara.setObjectName("eleccion_fara")
        self.eleccion_fontana = QtWidgets.QRadioButton(self.widget_consultar_costos)
        self.eleccion_fontana.setGeometry(QtCore.QRect(210, 240, 71, 17))
        self.eleccion_fontana.setObjectName("eleccion_fontana")
        self.eleccion_todas = QtWidgets.QRadioButton(self.widget_consultar_costos)
        self.eleccion_todas.setGeometry(QtCore.QRect(140, 270, 61, 20))
        self.eleccion_todas.setObjectName("eleccion_todas")
        self.label_seleccione_opcion = QtWidgets.QLabel(self.widget_consultar_costos)
        self.label_seleccione_opcion.setGeometry(QtCore.QRect(50, 290, 241, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_seleccione_opcion.setFont(font)
        self.label_seleccione_opcion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_seleccione_opcion.setStyleSheet(
            'font: 10pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_seleccione_opcion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seleccione_opcion.setObjectName("label_seleccione_opcion")
        self.widget_modificar_compra = QtWidgets.QWidget(self.widget)
        self.widget_modificar_compra.setEnabled(True)
        self.widget_modificar_compra.setGeometry(QtCore.QRect(830, 160, 341, 431))
        self.widget_modificar_compra.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_modificar_compra.setStyleSheet("")
        self.widget_modificar_compra.setObjectName("widget_modificar_compra")
        self.label_fecha = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_fecha.setGeometry(QtCore.QRect(90, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fecha.setFont(font)
        self.label_fecha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_fecha.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha.setObjectName("label_fecha")
        self.input_fecha_dia = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_fecha_dia.setGeometry(QtCore.QRect(60, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_fecha_dia.setFont(font)
        self.input_fecha_dia.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_fecha_dia.setText("")
        self.input_fecha_dia.setAlignment(QtCore.Qt.AlignCenter)
        self.input_fecha_dia.setObjectName("input_fecha_dia")
        self.input_fecha_mes = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_fecha_mes.setGeometry(QtCore.QRect(130, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_fecha_mes.setFont(font)
        self.input_fecha_mes.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_fecha_mes.setText("")
        self.input_fecha_mes.setAlignment(QtCore.Qt.AlignCenter)
        self.input_fecha_mes.setObjectName("input_fecha_mes")
        self.input_fecha_anio = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_fecha_anio.setGeometry(QtCore.QRect(200, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_fecha_anio.setFont(font)
        self.input_fecha_anio.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_fecha_anio.setText("")
        self.input_fecha_anio.setAlignment(QtCore.Qt.AlignCenter)
        self.input_fecha_anio.setObjectName("input_fecha_anio")
        self.label_nombre_producto = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_nombre_producto.setGeometry(QtCore.QRect(50, 100, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_nombre_producto.setFont(font)
        self.label_nombre_producto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_nombre_producto.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_nombre_producto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nombre_producto.setObjectName("label_nombre_producto")
        self.input_nombre_producto = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_nombre_producto.setGeometry(QtCore.QRect(30, 120, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_nombre_producto.setFont(font)
        self.input_nombre_producto.setStyleSheet(
            "border-radius: 10px;\n" "padding: 4px;\n" "color: #fff;"
        )
        self.input_nombre_producto.setAlignment(QtCore.Qt.AlignCenter)
        self.input_nombre_producto.setObjectName("input_nombre_producto")
        self.label_stock = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_stock.setGeometry(QtCore.QRect(40, 170, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_stock.setFont(font)
        self.label_stock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stock.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_stock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stock.setObjectName("label_stock")
        self.input_stock = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_stock.setGeometry(QtCore.QRect(120, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_stock.setFont(font)
        self.input_stock.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_stock.setAlignment(QtCore.Qt.AlignCenter)
        self.input_stock.setObjectName("input_stock")
        self.label_costo_unitario = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_costo_unitario.setGeometry(QtCore.QRect(40, 250, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_costo_unitario.setFont(font)
        self.label_costo_unitario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_costo_unitario.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_costo_unitario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_costo_unitario.setObjectName("label_costo_unitario")
        self.input_costo_unitario = QtWidgets.QLineEdit(self.widget_modificar_compra)
        self.input_costo_unitario.setGeometry(QtCore.QRect(100, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_costo_unitario.setFont(font)
        self.input_costo_unitario.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_costo_unitario.setAlignment(QtCore.Qt.AlignCenter)
        self.input_costo_unitario.setObjectName("input_costo_unitario")
        self.label_signo_peso = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_signo_peso.setGeometry(QtCore.QRect(80, 270, 21, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_signo_peso.setFont(font)
        self.label_signo_peso.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_signo_peso.setStyleSheet(
            'font: 15pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_signo_peso.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signo_peso.setWordWrap(True)
        self.label_signo_peso.setObjectName("label_signo_peso")
        self.label_campos_no_validos = QtWidgets.QLabel(self.widget_modificar_compra)
        self.label_campos_no_validos.setGeometry(QtCore.QRect(20, 340, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_campos_no_validos.setFont(font)
        self.label_campos_no_validos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_campos_no_validos.setStyleSheet("color:#f00;\n" "background:none;")
        self.label_campos_no_validos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_campos_no_validos.setWordWrap(True)
        self.label_campos_no_validos.setObjectName("label_campos_no_validos")
        self.boton_confirmar_modificacion = QtWidgets.QPushButton(
            self.widget_modificar_compra
        )
        self.boton_confirmar_modificacion.setGeometry(QtCore.QRect(100, 340, 131, 41))
        self.boton_confirmar_modificacion.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_confirmar_modificacion.setStyleSheet("")
        self.boton_confirmar_modificacion.setObjectName("boton_confirmar_modificacion")

        self.retranslateUi(HistorialCompras)
        QtCore.QMetaObject.connectSlotsByName(HistorialCompras)

    def retranslateUi(self, HistorialCompras):
        _translate = QtCore.QCoreApplication.translate
        HistorialCompras.setWindowTitle(_translate("HistorialCompras", "Form"))
        self.boton_filtrar_compras_cregar.setText(
            _translate("HistorialCompras", "Filtrar Compras Cregar")
        )
        self.boton_mostrar_compras_totales.setText(
            _translate("HistorialCompras", "Mostrar Compras Totales")
        )
        self.boton_consultar_costos.setText(
            _translate("HistorialCompras", "Consultar Costos")
        )
        self.label_15.setText(_translate("HistorialCompras", "LISTA DE COMPRAS"))
        self.boton_filtrar_compras_fara.setText(
            _translate("HistorialCompras", "Filtrar Compras Fara")
        )
        self.boton_eliminar_compra.setText(
            _translate("HistorialCompras", "Eliminar Compra")
        )
        self.boton_modificar_compra.setText(
            _translate("HistorialCompras", "Modificar Compra")
        )
        self.boton_filtrar_compras_fontana.setText(
            _translate("HistorialCompras", "Filtrar Compras Fontana")
        )
        self.boton_volver.setText(_translate("HistorialCompras", "Volver"))
        self.label_fecha_inicial.setText(
            _translate("HistorialCompras", "Fecha Inicial")
        )
        self.label_fecha_final.setText(_translate("HistorialCompras", "Fecha Final"))
        self.boton_consultar.setText(_translate("HistorialCompras", "CONSULTAR"))
        self.label_total_gastado.setText(
            _translate("HistorialCompras", "TOTAL GASTADO ($):")
        )
        self.label_stock_2.setText(_translate("HistorialCompras", "Empresa:"))
        self.eleccion_cregar.setText(_translate("HistorialCompras", "Cregar"))
        self.eleccion_fara.setText(_translate("HistorialCompras", "Fara"))
        self.eleccion_fontana.setText(_translate("HistorialCompras", "Fontana"))
        self.eleccion_todas.setText(_translate("HistorialCompras", "Todas"))
        self.label_fecha.setText(
            _translate("HistorialCompras", "Fecha (dia, mes, año):")
        )
        self.label_nombre_producto.setText(_translate("HistorialCompras", "Producto:"))
        self.label_stock.setText(_translate("HistorialCompras", "Cantidad Vendida:"))
        self.label_costo_unitario.setText(
            _translate("HistorialCompras", "Precio unitaro:")
        )
        self.label_signo_peso.setText(_translate("HistorialCompras", "$"))
        self.boton_confirmar_modificacion.setText(
            _translate("HistorialCompras", "CONFIRMAR")
        )
