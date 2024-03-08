# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historial_ventas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas.imagenes import imagenes


class Ui_HistorialVentas(object):
    def setupUi(self, HistorialVentas):
        HistorialVentas.setObjectName("HistorialVentas")
        HistorialVentas.resize(1195, 877)
        HistorialVentas.setMinimumSize(QtCore.QSize(1195, 877))
        HistorialVentas.setMaximumSize(QtCore.QSize(1195, 877))
        HistorialVentas.setStyleSheet("")
        self.widget = QtWidgets.QWidget(HistorialVentas)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1195, 877))
        self.widget.setMinimumSize(QtCore.QSize(1195, 877))
        self.widget.setMaximumSize(QtCore.QSize(1195, 877))
        self.widget.setStyleSheet(
            "QPushButton{\n"
            "border:1px solid rgb(176, 255, 226);\n"
            "border-radius: 10px;\n"
            "color: #fff;\n"
            'font: 57 12pt "Yu Gothic Medium";\n'
            "padding:5px;\n"
            "background-color:none;\n"
            "}\n"
            "QPushButton:hover {\n"
            "border:1px solid  rgb(108, 193, 146);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    padding-top: 10px;\n"
            "    padding-left: 10px;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "background-color:transparent;\n"
            "border-bottom:2px solid rgb(176, 255, 226);\n"
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
            " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(84, 84, 84, 162));\n"
            "color: #fff;\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QHeaderView::section {\n"
            "color: #000;\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QTreeView::item {\n"
            "color: #fff;\n"
            "}\n"
            "QWidget#widget{\n"
            "    background-image: url(:/historia_ventas/drc2.jpg);\n"
            "}"
        )
        self.widget.setObjectName("widget")
        self.eleccion_posnet_2 = QtWidgets.QRadioButton(self.widget)
        self.eleccion_posnet_2.setGeometry(QtCore.QRect(950, 520, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_posnet_2.setFont(font)
        self.eleccion_posnet_2.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_posnet_2.setObjectName("eleccion_posnet_2")
        self.input_dia_inicial = QtWidgets.QLineEdit(self.widget)
        self.input_dia_inicial.setGeometry(QtCore.QRect(890, 320, 61, 31))
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
        self.input_dia_final = QtWidgets.QLineEdit(self.widget)
        self.input_dia_final.setGeometry(QtCore.QRect(890, 410, 61, 31))
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
        self.label_fecha_no_valida = QtWidgets.QLabel(self.widget)
        self.label_fecha_no_valida.setGeometry(QtCore.QRect(870, 450, 241, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fecha_no_valida.setFont(font)
        self.label_fecha_no_valida.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_fecha_no_valida.setStyleSheet(
            'font: 10pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_fecha_no_valida.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha_no_valida.setObjectName("label_fecha_no_valida")
        self.eleccion_efectivo = QtWidgets.QRadioButton(self.widget)
        self.eleccion_efectivo.setGeometry(QtCore.QRect(860, 570, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_efectivo.setFont(font)
        self.eleccion_efectivo.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_efectivo.setObjectName("eleccion_efectivo")
        self.treeview_ventas = QtWidgets.QTreeView(self.widget)
        self.treeview_ventas.setGeometry(QtCore.QRect(20, 100, 541, 751))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.treeview_ventas.setFont(font)
        self.treeview_ventas.setStyleSheet("")
        self.treeview_ventas.setObjectName("treeview_ventas")
        self.boton_filtrar_ventas_posnet = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_ventas_posnet.setGeometry(QtCore.QRect(570, 660, 231, 51))
        self.boton_filtrar_ventas_posnet.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_ventas_posnet.setStyleSheet("")
        self.boton_filtrar_ventas_posnet.setObjectName("boton_filtrar_ventas_posnet")
        self.label_tipo_pago_consulta = QtWidgets.QLabel(self.widget)
        self.label_tipo_pago_consulta.setGeometry(QtCore.QRect(940, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_tipo_pago_consulta.setFont(font)
        self.label_tipo_pago_consulta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tipo_pago_consulta.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_tipo_pago_consulta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo_pago_consulta.setObjectName("label_tipo_pago_consulta")
        self.input_fecha_mes = QtWidgets.QLineEdit(self.widget)
        self.input_fecha_mes.setGeometry(QtCore.QRect(960, 250, 61, 31))
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
        self.label_tipo_pago = QtWidgets.QLabel(self.widget)
        self.label_tipo_pago.setGeometry(QtCore.QRect(940, 530, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_tipo_pago.setFont(font)
        self.label_tipo_pago.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tipo_pago.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_tipo_pago.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo_pago.setObjectName("label_tipo_pago")
        self.input_stock = QtWidgets.QLineEdit(self.widget)
        self.input_stock.setGeometry(QtCore.QRect(950, 400, 81, 31))
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
        self.eleccion_total = QtWidgets.QRadioButton(self.widget)
        self.eleccion_total.setGeometry(QtCore.QRect(960, 550, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_total.setFont(font)
        self.eleccion_total.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_total.setObjectName("eleccion_total")
        self.label_signo_peso = QtWidgets.QLabel(self.widget)
        self.label_signo_peso.setGeometry(QtCore.QRect(900, 480, 21, 31))
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
        self.boton_volver = QtWidgets.QPushButton(self.widget)
        self.boton_volver.setGeometry(QtCore.QRect(1070, 20, 101, 31))
        self.boton_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_volver.setStyleSheet("")
        self.boton_volver.setObjectName("boton_volver")
        self.boton_confirmar_registro = QtWidgets.QPushButton(self.widget)
        self.boton_confirmar_registro.setGeometry(QtCore.QRect(930, 620, 131, 41))
        self.boton_confirmar_registro.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_confirmar_registro.setStyleSheet("")
        self.boton_confirmar_registro.setObjectName("boton_confirmar_registro")
        self.label_fecha_final = QtWidgets.QLabel(self.widget)
        self.label_fecha_final.setGeometry(QtCore.QRect(940, 370, 91, 31))
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
        self.input_mes_final = QtWidgets.QLineEdit(self.widget)
        self.input_mes_final.setGeometry(QtCore.QRect(960, 410, 61, 31))
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
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(120, 40, 341, 31))
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
        self.boton_modificar_venta = QtWidgets.QPushButton(self.widget)
        self.boton_modificar_venta.setGeometry(QtCore.QRect(570, 230, 231, 51))
        self.boton_modificar_venta.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_modificar_venta.setStyleSheet("")
        self.boton_modificar_venta.setObjectName("boton_modificar_venta")
        self.label_fecha = QtWidgets.QLabel(self.widget)
        self.label_fecha.setGeometry(QtCore.QRect(910, 210, 161, 31))
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
        self.boton_confirmar_modificacion = QtWidgets.QPushButton(self.widget)
        self.boton_confirmar_modificacion.setGeometry(QtCore.QRect(930, 620, 131, 41))
        self.boton_confirmar_modificacion.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_confirmar_modificacion.setStyleSheet("")
        self.boton_confirmar_modificacion.setObjectName("boton_confirmar_modificacion")
        self.boton_eliminar_venta = QtWidgets.QPushButton(self.widget)
        self.boton_eliminar_venta.setGeometry(QtCore.QRect(570, 310, 231, 51))
        self.boton_eliminar_venta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_eliminar_venta.setStyleSheet("")
        self.boton_eliminar_venta.setObjectName("boton_eliminar_venta")
        self.label_seleccione_tipo_pago = QtWidgets.QLabel(self.widget)
        self.label_seleccione_tipo_pago.setGeometry(QtCore.QRect(1070, 620, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_seleccione_tipo_pago.setFont(font)
        self.label_seleccione_tipo_pago.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_seleccione_tipo_pago.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_seleccione_tipo_pago.setText("")
        self.label_seleccione_tipo_pago.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seleccione_tipo_pago.setWordWrap(True)
        self.label_seleccione_tipo_pago.setObjectName("label_seleccione_tipo_pago")
        self.input_fecha_anio = QtWidgets.QLineEdit(self.widget)
        self.input_fecha_anio.setGeometry(QtCore.QRect(1030, 250, 61, 31))
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
        self.label_resultado_total_ganado = QtWidgets.QLabel(self.widget)
        self.label_resultado_total_ganado.setGeometry(QtCore.QRect(810, 680, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_resultado_total_ganado.setFont(font)
        self.label_resultado_total_ganado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_resultado_total_ganado.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "background: none;\n"
            "color: rgb(56, 255, 56);"
        )
        self.label_resultado_total_ganado.setText("")
        self.label_resultado_total_ganado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado_total_ganado.setObjectName("label_resultado_total_ganado")
        self.boton_filtrar_ventas_mercadopago = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_ventas_mercadopago.setGeometry(
            QtCore.QRect(570, 740, 231, 51)
        )
        self.boton_filtrar_ventas_mercadopago.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_ventas_mercadopago.setStyleSheet("")
        self.boton_filtrar_ventas_mercadopago.setObjectName(
            "boton_filtrar_ventas_mercadopago"
        )
        self.eleccion_mercadopago = QtWidgets.QRadioButton(self.widget)
        self.eleccion_mercadopago.setGeometry(QtCore.QRect(1040, 570, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_mercadopago.setFont(font)
        self.eleccion_mercadopago.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_mercadopago.setObjectName("eleccion_mercadopago")
        self.eleccion_mercadopago_2 = QtWidgets.QRadioButton(self.widget)
        self.eleccion_mercadopago_2.setGeometry(QtCore.QRect(1040, 520, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_mercadopago_2.setFont(font)
        self.eleccion_mercadopago_2.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_mercadopago_2.setObjectName("eleccion_mercadopago_2")
        self.label_eliminar_venta = QtWidgets.QLabel(self.widget)
        self.label_eliminar_venta.setGeometry(QtCore.QRect(560, 360, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_eliminar_venta.setFont(font)
        self.label_eliminar_venta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_eliminar_venta.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_eliminar_venta.setText("")
        self.label_eliminar_venta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eliminar_venta.setObjectName("label_eliminar_venta")
        self.boton_mostrar_ventas_totales = QtWidgets.QPushButton(self.widget)
        self.boton_mostrar_ventas_totales.setGeometry(QtCore.QRect(570, 500, 231, 51))
        self.boton_mostrar_ventas_totales.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_mostrar_ventas_totales.setStyleSheet("")
        self.boton_mostrar_ventas_totales.setObjectName("boton_mostrar_ventas_totales")
        self.boton_agregar_venta = QtWidgets.QPushButton(self.widget)
        self.boton_agregar_venta.setGeometry(QtCore.QRect(570, 150, 231, 51))
        self.boton_agregar_venta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_agregar_venta.setStyleSheet("")
        self.boton_agregar_venta.setObjectName("boton_agregar_venta")
        self.label_modificar_venta = QtWidgets.QLabel(self.widget)
        self.label_modificar_venta.setGeometry(QtCore.QRect(560, 280, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_modificar_venta.setFont(font)
        self.label_modificar_venta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_modificar_venta.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_modificar_venta.setText("")
        self.label_modificar_venta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modificar_venta.setObjectName("label_modificar_venta")
        self.label_total_ganado = QtWidgets.QLabel(self.widget)
        self.label_total_ganado.setGeometry(QtCore.QRect(900, 640, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_total_ganado.setFont(font)
        self.label_total_ganado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_total_ganado.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_total_ganado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_ganado.setObjectName("label_total_ganado")
        self.boton_consultar_ganancias = QtWidgets.QPushButton(self.widget)
        self.boton_consultar_ganancias.setGeometry(QtCore.QRect(570, 390, 231, 51))
        self.boton_consultar_ganancias.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_consultar_ganancias.setStyleSheet("")
        self.boton_consultar_ganancias.setObjectName("boton_consultar_ganancias")
        self.eleccion_posnet = QtWidgets.QRadioButton(self.widget)
        self.eleccion_posnet.setGeometry(QtCore.QRect(950, 570, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_posnet.setFont(font)
        self.eleccion_posnet.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_posnet.setObjectName("eleccion_posnet")
        self.input_nombre_producto = QtWidgets.QLineEdit(self.widget)
        self.input_nombre_producto.setGeometry(QtCore.QRect(860, 330, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_nombre_producto.setFont(font)
        self.input_nombre_producto.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_nombre_producto.setAlignment(QtCore.Qt.AlignCenter)
        self.input_nombre_producto.setObjectName("input_nombre_producto")
        self.input_precio_unitario = QtWidgets.QLineEdit(self.widget)
        self.input_precio_unitario.setGeometry(QtCore.QRect(920, 480, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_precio_unitario.setFont(font)
        self.input_precio_unitario.setStyleSheet(
            "border-radius: 10px;\n" "padding: 7px;\n" "color: #fff;"
        )
        self.input_precio_unitario.setAlignment(QtCore.Qt.AlignCenter)
        self.input_precio_unitario.setObjectName("input_precio_unitario")
        self.label_campos_no_validos = QtWidgets.QLabel(self.widget)
        self.label_campos_no_validos.setGeometry(QtCore.QRect(830, 620, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_campos_no_validos.setFont(font)
        self.label_campos_no_validos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_campos_no_validos.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #f00;\n" "background: none;"
        )
        self.label_campos_no_validos.setText("")
        self.label_campos_no_validos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_campos_no_validos.setWordWrap(True)
        self.label_campos_no_validos.setObjectName("label_campos_no_validos")
        self.input_anio_final = QtWidgets.QLineEdit(self.widget)
        self.input_anio_final.setGeometry(QtCore.QRect(1030, 410, 61, 31))
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
        self.label_precio_unitario = QtWidgets.QLabel(self.widget)
        self.label_precio_unitario.setGeometry(QtCore.QRect(870, 450, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_precio_unitario.setFont(font)
        self.label_precio_unitario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_precio_unitario.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label_precio_unitario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_precio_unitario.setObjectName("label_precio_unitario")
        self.label_stock = QtWidgets.QLabel(self.widget)
        self.label_stock.setGeometry(QtCore.QRect(870, 370, 241, 31))
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
        self.input_mes_inicial = QtWidgets.QLineEdit(self.widget)
        self.input_mes_inicial.setGeometry(QtCore.QRect(960, 320, 61, 31))
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
        self.input_fecha_dia = QtWidgets.QLineEdit(self.widget)
        self.input_fecha_dia.setGeometry(QtCore.QRect(890, 250, 61, 31))
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
        self.boton_filtrar_ventas_efectivo = QtWidgets.QPushButton(self.widget)
        self.boton_filtrar_ventas_efectivo.setGeometry(QtCore.QRect(570, 580, 231, 51))
        self.boton_filtrar_ventas_efectivo.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_filtrar_ventas_efectivo.setStyleSheet("")
        self.boton_filtrar_ventas_efectivo.setObjectName(
            "boton_filtrar_ventas_efectivo"
        )
        self.eleccion_efectivo_2 = QtWidgets.QRadioButton(self.widget)
        self.eleccion_efectivo_2.setGeometry(QtCore.QRect(860, 520, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eleccion_efectivo_2.setFont(font)
        self.eleccion_efectivo_2.setStyleSheet("background: none;\n" "color: white;")
        self.eleccion_efectivo_2.setObjectName("eleccion_efectivo_2")
        self.label_nombre_producto = QtWidgets.QLabel(self.widget)
        self.label_nombre_producto.setGeometry(QtCore.QRect(870, 300, 241, 21))
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
        self.boton_consultar = QtWidgets.QPushButton(self.widget)
        self.boton_consultar.setGeometry(QtCore.QRect(930, 590, 131, 41))
        self.boton_consultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_consultar.setStyleSheet("")
        self.boton_consultar.setObjectName("boton_consultar")
        self.input_anio_inicial = QtWidgets.QLineEdit(self.widget)
        self.input_anio_inicial.setGeometry(QtCore.QRect(1030, 320, 61, 31))
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
        self.label_fecha_inicial = QtWidgets.QLabel(self.widget)
        self.label_fecha_inicial.setGeometry(QtCore.QRect(940, 280, 91, 31))
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

        self.retranslateUi(HistorialVentas)
        QtCore.QMetaObject.connectSlotsByName(HistorialVentas)

    def retranslateUi(self, HistorialVentas):
        _translate = QtCore.QCoreApplication.translate
        HistorialVentas.setWindowTitle(_translate("HistorialVentas", "Form"))
        self.eleccion_posnet_2.setText(_translate("HistorialVentas", "Posnet"))
        self.label_fecha_no_valida.setText(
            _translate("HistorialVentas", "Ingrese fechas validas")
        )
        self.eleccion_efectivo.setText(_translate("HistorialVentas", "Efectivo"))
        self.boton_filtrar_ventas_posnet.setText(
            _translate("HistorialVentas", "Filtrar Ventas Posnet")
        )
        self.label_tipo_pago_consulta.setText(
            _translate("HistorialVentas", "Tipo de pago:")
        )
        self.label_tipo_pago.setText(_translate("HistorialVentas", "Tipo de pago:"))
        self.eleccion_total.setText(_translate("HistorialVentas", "Total"))
        self.label_signo_peso.setText(_translate("HistorialVentas", "$"))
        self.boton_volver.setText(_translate("HistorialVentas", "Volver"))
        self.boton_confirmar_registro.setText(
            _translate("HistorialVentas", "CONFIRMAR")
        )
        self.label_fecha_final.setText(_translate("HistorialVentas", "Fecha Final"))
        self.label_15.setText(_translate("HistorialVentas", "LISTA DE VENTAS"))
        self.boton_modificar_venta.setText(
            _translate("HistorialVentas", "Modificar Venta")
        )
        self.label_fecha.setText(
            _translate("HistorialVentas", "Fecha (dia, mes, año):")
        )
        self.boton_confirmar_modificacion.setText(
            _translate("HistorialVentas", "CONFIRMAR")
        )
        self.boton_eliminar_venta.setText(
            _translate("HistorialVentas", "Eliminar Venta")
        )
        self.boton_filtrar_ventas_mercadopago.setText(
            _translate("HistorialVentas", "Filtrar Ventas MP")
        )
        self.eleccion_mercadopago.setText(_translate("HistorialVentas", "MercadoPago"))
        self.eleccion_mercadopago_2.setText(
            _translate("HistorialVentas", "MercadoPago")
        )
        self.boton_mostrar_ventas_totales.setText(
            _translate("HistorialVentas", "Mostrar Ventas Totales")
        )
        self.boton_agregar_venta.setText(_translate("HistorialVentas", "Agregar Venta"))
        self.label_total_ganado.setText(
            _translate("HistorialVentas", "DINERO INGRESADO ($):")
        )
        self.boton_consultar_ganancias.setText(
            _translate("HistorialVentas", "Consultar Ingresos")
        )
        self.eleccion_posnet.setText(_translate("HistorialVentas", "Posnet"))
        self.label_precio_unitario.setText(
            _translate("HistorialVentas", "Precio unitaro:")
        )
        self.label_stock.setText(_translate("HistorialVentas", "Cantidad Vendida:"))
        self.boton_filtrar_ventas_efectivo.setText(
            _translate("HistorialVentas", "Filtrar Ventas Efectivo")
        )
        self.eleccion_efectivo_2.setText(_translate("HistorialVentas", "Efectivo"))
        self.label_nombre_producto.setText(_translate("HistorialVentas", "Producto:"))
        self.boton_consultar.setText(_translate("HistorialVentas", "CONSULTAR"))
        self.label_fecha_inicial.setText(_translate("HistorialVentas", "Fecha Inicial"))
