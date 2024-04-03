# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrar_ventas_vendedor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt


class Ui_RegistrarVentaVendedor(object):
    def setupUi(self, RegistrarVentaVendedor):
        RegistrarVentaVendedor.setObjectName("RegistrarVentaVendedor")
        RegistrarVentaVendedor.resize(1195, 645)
        RegistrarVentaVendedor.setMinimumSize(QtCore.QSize(1195, 645))
        RegistrarVentaVendedor.setMaximumSize(QtCore.QSize(1195, 645))
        RegistrarVentaVendedor.setStyleSheet("")
        self.widget = QtWidgets.QWidget(RegistrarVentaVendedor)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1195, 645))
        self.widget.setMinimumSize(QtCore.QSize(1195, 645))
        self.widget.setMaximumSize(QtCore.QSize(1195, 645))
        self.widget.setStyleSheet(
            "QPushButton{\n"
            'font: 57 11pt "Yu Gothic Medium";\n'
            "color: #fff;\n"
            "padding:5px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0568182 rgba(0, 0, 0, 255), stop:1 rgba(0, 142, 133, 255));\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.118644 rgba(0, 100, 0, 243), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    padding-top: 10px;\n"
            "    padding-left: 10px;\n"
            "}\n"
            "QLineEdit{\n"
            "padding: 3px;\n"
            "color: #fff; \n"
            'font: 11pt "MS Shell Dlg 2";\n'
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0568182 rgba(0, 0, 0, 255), stop:1 rgba(0, 142, 133, 255));\n"
            "}\n"
            "QLineEdit:hover {\n"
            "background-color:none;\n"
            "}\n"
            "QLineEdit:focus {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.118644 rgba(0, 100, 0, 243), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QWidget#widget{\n"
            "background-image: url(:/registrar_ventas/3294425.jpg);\n"
            "}\n"
            "QRadioButton{\n"
            "color: #fff;\n"
            "background-color: none;\n"
            'font: 57 12pt "Yu Gothic Medium";\n'
            "}\n"
            "QTreeView{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(45, 45, 45, 162));\n"
            "color: #000;\n"
            "border: 1px solid #000;\n"
            "font-size: 15px;\n"
            "}\n"
            "QHeaderView::section {\n"
            "color: #000;\n"
            "border: 1px solid #000;\n"
            "font-size:13px;\n"
            "}\n"
            "QTreeView::item {\n"
            "color: #fff;\n"
            "border-right:0.5px solid #000;\n"
            "border-bottom:0.5px solid #000;\n"
            "}"
            "QTreeView::item:selected {\n"
            "background-color: #f00;\n"
            "}"
        )
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(850, 50, 161, 21))
        self.label_5.setStyleSheet(
            "\n"
            'font: 57 14pt "Yu Gothic Medium";\n'
            "color: #fff;\n"
            "background: none;"
        )
        self.label_5.setObjectName("label_5")
        self.label_cantidad_invalida = QtWidgets.QLabel(self.widget)
        self.label_cantidad_invalida.setGeometry(QtCore.QRect(760, 120, 351, 31))
        self.label_cantidad_invalida.setStyleSheet(
            "\n"
            'font: 57 14pt "Yu Gothic Medium";\n'
            "color: #f00;\n"
            "background: none;"
        )
        self.label_cantidad_invalida.setText("")
        self.label_cantidad_invalida.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cantidad_invalida.setObjectName("label_cantidad_invalida")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(810, 140, 261, 31))
        self.label_6.setStyleSheet(
            "\n"
            'font: 57 14pt "Yu Gothic Medium";\n'
            "color: #fff;\n"
            "background: none;"
        )
        self.label_6.setObjectName("label_6")
        self.eleccion_efectivo = QtWidgets.QRadioButton(self.widget)
        self.eleccion_efectivo.setGeometry(QtCore.QRect(780, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.eleccion_efectivo.setFont(font)
        self.eleccion_efectivo.setStyleSheet("")
        self.eleccion_efectivo.setObjectName("eleccion_efectivo")
        self.input_cantidad_vendida = QtWidgets.QLineEdit(self.widget)
        self.input_cantidad_vendida.setGeometry(QtCore.QRect(900, 80, 71, 41))
        self.input_cantidad_vendida.setStyleSheet("")
        self.input_cantidad_vendida.setText("")
        self.input_cantidad_vendida.setFrame(True)
        self.input_cantidad_vendida.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cantidad_vendida.setDragEnabled(False)
        self.input_cantidad_vendida.setClearButtonEnabled(False)
        self.input_cantidad_vendida.setObjectName("input_cantidad_vendida")
        self.treeview_productos = QtWidgets.QTreeView(self.widget)
        self.treeview_productos.setGeometry(QtCore.QRect(10, 90, 631, 551))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.treeview_productos.setFont(font)
        self.treeview_productos.setStyleSheet("")
        self.treeview_productos.setAllColumnsShowFocus(False)
        self.treeview_productos.setObjectName("treeview_productos")

        self.modelo_productos = QtGui.QStandardItemModel()
        self.treeview_productos.setModel(self.modelo_productos)
        self.modelo_productos.setHorizontalHeaderLabels(
            [
                "ID",
                "Producto",
                "Stock",
                "Efectivo",
                "Posnet",
                "Constructor",
            ]
        )
        self.treeview_productos.setFocusPolicy(Qt.NoFocus)
        header = self.treeview_productos.header()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.resizeSection(0, 50)
        header.resizeSection(1, 300)
        header.resizeSection(2, 40)
        header.resizeSection(3, 80)
        header.resizeSection(4, 80)
        header.resizeSection(5, 80)

        self.eleccion_posnet = QtWidgets.QRadioButton(self.widget)
        self.eleccion_posnet.setGeometry(QtCore.QRect(900, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.eleccion_posnet.setFont(font)
        self.eleccion_posnet.setStyleSheet("")
        self.eleccion_posnet.setObjectName("eleccion_posnet")
        self.boton_registrar_venta = QtWidgets.QPushButton(self.widget)
        self.boton_registrar_venta.setGeometry(QtCore.QRect(870, 230, 141, 41))
        self.boton_registrar_venta.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_registrar_venta.setStyleSheet("")
        self.boton_registrar_venta.setObjectName("boton_registrar_venta")
        self.label_tipo_pago_no_elegido = QtWidgets.QLabel(self.widget)
        self.label_tipo_pago_no_elegido.setGeometry(QtCore.QRect(780, 200, 321, 21))
        self.label_tipo_pago_no_elegido.setStyleSheet(
            'font: 57 12pt "Yu Gothic Medium";\n' "color: #f00;\n" "background: none;"
        )
        self.label_tipo_pago_no_elegido.setText("")
        self.label_tipo_pago_no_elegido.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo_pago_no_elegido.setObjectName("label_tipo_pago_no_elegido")
        self.treeview_ventas = QtWidgets.QTreeView(self.widget)
        self.treeview_ventas.setGeometry(QtCore.QRect(650, 280, 531, 361))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.treeview_ventas.setFont(font)
        self.treeview_ventas.setStyleSheet("")
        self.treeview_ventas.setAllColumnsShowFocus(False)
        self.treeview_ventas.setObjectName("treeview_ventas")

        self.modelo_ventas = QtGui.QStandardItemModel()
        self.treeview_ventas.setModel(self.modelo_ventas)
        self.modelo_ventas.setHorizontalHeaderLabels(
            [
                "N°",
                "Fecha",
                "Producto",
                "Cant",
                "Precio c/u",
                "Pago",
            ]
        )
        self.treeview_ventas.setFocusPolicy(Qt.NoFocus)
        header = self.treeview_ventas.header()
        header.setDefaultAlignment(QtCore.Qt.AlignHCenter)
        header.resizeSection(0, 65)
        header.resizeSection(1, 85)
        header.resizeSection(2, 150)
        header.resizeSection(3, 40)
        header.resizeSection(4, 90)
        header.resizeSection(5, 60)

        self.producto_no_encontrado = QtWidgets.QLabel(self.widget)
        self.producto_no_encontrado.setGeometry(QtCore.QRect(160, 70, 231, 21))
        self.producto_no_encontrado.setStyleSheet(
            'font: 57 14pt "Yu Gothic Medium";\n' "color: #f00;\n" "background: none;"
        )
        self.producto_no_encontrado.setText("")
        self.producto_no_encontrado.setObjectName("producto_no_encontrado")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(140, 0, 361, 41))
        self.label.setStyleSheet(
            'font: 24pt "MS Shell Dlg 2";\n' "color: #fff;\n" "background: none;"
        )
        self.label.setObjectName("label")
        self.boton_buscar_producto = QtWidgets.QPushButton(self.widget)
        self.boton_buscar_producto.setGeometry(QtCore.QRect(490, 40, 101, 31))
        self.boton_buscar_producto.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.boton_buscar_producto.setStyleSheet("border-radius: 7px;")
        self.boton_buscar_producto.setObjectName("boton_buscar_producto")
        self.input_buscar_producto = QtWidgets.QLineEdit(self.widget)
        self.input_buscar_producto.setGeometry(QtCore.QRect(70, 40, 411, 31))
        self.input_buscar_producto.setStyleSheet("")
        self.input_buscar_producto.setText("")
        self.input_buscar_producto.setAlignment(QtCore.Qt.AlignCenter)
        self.input_buscar_producto.setObjectName("input_buscar_producto")
        self.eleccion_constructor = QtWidgets.QRadioButton(self.widget)
        self.eleccion_constructor.setGeometry(QtCore.QRect(1010, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.eleccion_constructor.setFont(font)
        self.eleccion_constructor.setStyleSheet("")
        self.eleccion_constructor.setObjectName("eleccion_constructor")
        self.boton_todos = QtWidgets.QPushButton(self.widget)
        self.boton_todos.setGeometry(QtCore.QRect(650, 100, 91, 31))
        self.boton_todos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_todos.setStyleSheet("")
        self.boton_todos.setObjectName("boton_todos")
        self.boton_cregar = QtWidgets.QPushButton(self.widget)
        self.boton_cregar.setGeometry(QtCore.QRect(650, 140, 91, 31))
        self.boton_cregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_cregar.setStyleSheet("")
        self.boton_cregar.setObjectName("boton_cregar")
        self.boton_fara = QtWidgets.QPushButton(self.widget)
        self.boton_fara.setGeometry(QtCore.QRect(650, 180, 91, 31))
        self.boton_fara.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_fara.setStyleSheet("")
        self.boton_fara.setObjectName("boton_fara")
        self.boton_fontana = QtWidgets.QPushButton(self.widget)
        self.boton_fontana.setGeometry(QtCore.QRect(650, 220, 91, 31))
        self.boton_fontana.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_fontana.setStyleSheet("")
        self.boton_fontana.setObjectName("boton_fontana")
        self.boton_actualizar = QtWidgets.QPushButton(self.widget)
        self.boton_actualizar.setGeometry(QtCore.QRect(20, 40, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.boton_actualizar.setFont(font)
        self.boton_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_actualizar.setStyleSheet("font-size:30px;")
        self.boton_actualizar.setObjectName("boton_actualizar")

        self.retranslateUi(RegistrarVentaVendedor)
        QtCore.QMetaObject.connectSlotsByName(RegistrarVentaVendedor)

    def retranslateUi(self, RegistrarVentaVendedor):
        _translate = QtCore.QCoreApplication.translate
        RegistrarVentaVendedor.setWindowTitle(
            _translate("RegistrarVentaVendedor", "Form")
        )
        self.label_5.setText(_translate("RegistrarVentaVendedor", "Cantidad Vendida:"))
        self.label_6.setText(
            _translate("RegistrarVentaVendedor", "Seleccione el precio de venta:")
        )
        self.eleccion_efectivo.setText(_translate("RegistrarVentaVendedor", "Efectivo"))
        self.eleccion_posnet.setText(_translate("RegistrarVentaVendedor", "Posnet"))
        self.boton_registrar_venta.setText(
            _translate("RegistrarVentaVendedor", "REGISTRAR")
        )
        self.label.setText(_translate("RegistrarVentaVendedor", "LISTA DE PRODUCTOS"))
        self.boton_buscar_producto.setText(
            _translate("RegistrarVentaVendedor", "Buscar")
        )
        self.eleccion_constructor.setText(
            _translate("RegistrarVentaVendedor", "Constructor")
        )
        self.boton_todos.setText(_translate("RegistrarVentaVendedor", "Todos"))
        self.boton_cregar.setText(_translate("RegistrarVentaVendedor", "Cregar"))
        self.boton_fara.setText(_translate("RegistrarVentaVendedor", "Fara"))
        self.boton_fontana.setText(_translate("RegistrarVentaVendedor", "Fontana"))
        self.boton_actualizar.setText(_translate("RegistrarVentaVendedor", "↻"))
