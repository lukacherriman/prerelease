from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import datetime

"""from nameRideClass import Name_ride
from profileUpdateClass import Update_profile
from canvasClass import Canvas
from constants import *"""


class Main_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, connection, username):
        super().__init__()
        self.testing = testing
        self.connection = connection
        self.username = username
        self.menu = False
        self.segments = []
        self.new_window = False

        self.resize(1600, 1000)
        self.centralwidget = QtWidgets.QWidget(self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # sets up the title, username, menu bar
        self.topFrame = QtWidgets.QFrame(self.centralwidget)
        self.topFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.topFrame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topFrame)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameLabel = QtWidgets.QLabel(self.topFrame)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.usernameLabel)

        self.line = QtWidgets.QFrame(self.topFrame)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLayout.addWidget(self.line)

        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(16)
        self.titleLabel = QtWidgets.QLabel(self.topFrame)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.titleLabel)

        self.line_2 = QtWidgets.QFrame(self.topFrame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLayout.addWidget(self.line_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuButton = QtWidgets.QPushButton(self.topFrame)
        self.menuButton.setFont(font)
        self.menuButton.clicked.connect(self.menuPressed)
        self.horizontalLayout.addWidget(self.menuButton)
        self.verticalLayout.addWidget(self.topFrame)

        # sets up the main lower frame (invisible)
        self.mainFrameLower = QtWidgets.QFrame(self.centralwidget)
        self.mainFrameLower.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrameLower.setFrameShadow(QtWidgets.QFrame.Plain)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrameLower)

        # sets up the left box frame
        self.frame_3 = QtWidgets.QFrame(self.mainFrameLower)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)

        # splits the box for the choice radio buttons and the data view
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.dataRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.dataRadioButton.setChecked(True)
        self.dataRadioButton.clicked.connect(self.viewDataChoice)
        self.dataRadioButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addWidget(self.dataRadioButton)

        self.line_5 = QtWidgets.QFrame(self.frame_3)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLayout_3.addWidget(self.line_5)

        self.compareRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.compareRadioButton.clicked.connect(self.compareChoice)
        self.compareRadioButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addWidget(self.compareRadioButton)

        self.line_6 = QtWidgets.QFrame(self.frame_3)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLayout_3.addWidget(self.line_6)

        self.progressRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.progressRadioButton.clicked.connect(self.progressChoice)
        self.progressRadioButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addWidget(self.progressRadioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # line under the radio buttons
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticalLayout_2.addWidget(self.line_3)

        # splits the data area in half
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLayout_4.addWidget(self.line_4)

        spacerItem1 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        # sets up the right box a scroll area box
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.scrollArea = QtWidgets.QScrollArea(self.mainFrameLower)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.scrollArea.setMinimumWidth(536)
        self.scrollArea.setMaximumWidth(536)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 2500))

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.slider_average_value = 1
        self.chart_selecter_value = 0

        self.ridesSelected = False
        self.frames_selected = []
        self.frames = []
        self.ridesShown = 5

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.mainFrameLower)

        self.setCentralWidget(self.centralwidget)

        self.updateUi()
        self.settupScrollWindow()

        QtCore.QMetaObject.connectSlotsByName(self)

    def updateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Training Tips"))
        self.usernameLabel.setText(_translate("MainWindow", self.username))
        self.titleLabel.setText(_translate("MainWindow", "Lukapeaks"))
        self.menuButton.setText(_translate("MainWindow", "Menu"))
        self.dataRadioButton.setText(_translate("MainWindow", "View Data"))
        self.compareRadioButton.setText(_translate("MainWindow", "compare"))
        self.progressRadioButton.setText(_translate("MainWindow", "Progress"))

    def settupScrollWindow(self):
        # sets up the scroll window with the selectable rides and maps
        self.menuButton.setText("Menu")
        self.menu = False

        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT * FROM userRide WHERE username = '{self.username}' ORDER BY date DESC LIMIT {self.ridesShown}")
        num_rides = len(cursor.fetchall())
        self.scrollAreaWidgetContents.resize(500, num_rides * 500 + 100)
        cursor.execute(
            f"SELECT * FROM userRide WHERE username = '{self.username}' ORDER BY date DESC, rideId DESC LIMIT {self.ridesShown}")

        while True:
            result = cursor.fetchone()
            if result is None:
                break
            rideFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            rideFrame.setFrameShape(QtWidgets.QFrame.Box)
            rideFrame.setFrameShadow(QtWidgets.QFrame.Plain)
            self.verticalLayout_3.addWidget(rideFrame)

            verticalLayout_4 = QtWidgets.QVBoxLayout(rideFrame)
            horizontalLayout_5 = QtWidgets.QHBoxLayout()

            rideDateLabel = QtWidgets.QLabel(rideFrame)
            rideDateLabel.setText(f"Date: {result[2]}")
            horizontalLayout_5.addWidget(rideDateLabel)

            rideNameLabel_1 = QtWidgets.QLabel(rideFrame)
            rideNameLabel_1.setText(f"Name: {result[3]}")
            horizontalLayout_5.addWidget(rideNameLabel_1)
            verticalLayout_4.addLayout(horizontalLayout_5)

            line_7 = QtWidgets.QFrame(rideFrame)
            line_7.setFrameShadow(QtWidgets.QFrame.Plain)
            line_7.setFrameShape(QtWidgets.QFrame.HLine)
            verticalLayout_4.addWidget(line_7)

            horizontalLayout_6 = QtWidgets.QHBoxLayout()

            ride_id = result[0]

            map = self.get_map(ride_id)
            horizontalLayout_6.addWidget(map)

            line_8 = QtWidgets.QFrame(rideFrame)
            line_8.setFrameShadow(QtWidgets.QFrame.Plain)
            line_8.setFrameShape(QtWidgets.QFrame.VLine)
            horizontalLayout_6.addWidget(line_8)

            rideCheckBox_1 = QtWidgets.QCheckBox(rideFrame)
            rideCheckBox_1.setLayoutDirection(QtCore.Qt.RightToLeft)
            rideCheckBox_1.setText("")
            rideCheckBox_1.setIconSize(QtCore.QSize(20, 20))
            rideCheckBox_1.clicked.connect(self.ride_clicked)
            horizontalLayout_6.addWidget(rideCheckBox_1)

            verticalLayout_4.addLayout(horizontalLayout_6)

            self.frames.append([rideFrame, rideCheckBox_1, ride_id])

        # button to display more rides to the user
        self.show_more_rides = QtWidgets.QPushButton(self)
        self.show_more_rides.setText("Show 5 more rides")
        self.show_more_rides.clicked.connect(lambda: self.more_rides(5))
        self.verticalLayout_3.addWidget(self.show_more_rides)

    def more_rides(self, num):
        # adds more rides and sets all rides to selectable
        self.ridesShown += num
        layout = self.verticalLayout_3
        self.clear_layout(layout)

        self.frames = []
        self.ridesSelected = False
        self.frames_selected = []
        self.settupScrollWindow()

        # if the progress radio button is checked then the check buttons must remain uncheckable
        if self.progressRadioButton.isChecked():
            if num == 0:
                layout = self.horizontalLayout_4
                self.clear_layout(layout)
                self.fitness_progress_panel()
            else:
                for frame in self.frames:
                    frame[1].setChecked(False)
                    frame[1].setEnabled(False)
                    self.ridesSelected = False

    def get_map(self, ride_id):
        # produces the widget for a map
        data = self.data_from_ride_table(ride_id)

        # 0time, 1moving, 2distance, 3watts, 4heart rate, 5cadence, 6velocity_smooth, 7lat, 8lng, 9temp, 10alt
        longitude = []
        for i in range(1, len(data)):
            point = data[i][8]
            longitude.append(float(point))
        latitude = []
        for i in range(1, len(data)):
            point = data[i][7]
            latitude.append(float(point))

        canvas = Canvas(self, )
        canvas.plot_graph(longitude, latitude, "", "", "")
        canvas.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        return canvas

    def ride_clicked(self):
        # when a ride is checked it sets all the others to disabled and calls ride data panel with that ride ID
        # when a ride is unchecked it sets all the others to enabled
        if self.dataRadioButton.isChecked():
            if not self.ridesSelected:
                for frame in self.frames:
                    if frame[1].isChecked():
                        ride_id = frame[2]
                        for fram in self.frames:
                            fram[1].setEnabled(False)
                        frame[1].setEnabled(True)
                        self.ridesSelected = True
                self.ride_data_panel(ride_id)
            else:
                for fram in self.frames:
                    fram[1].setEnabled(True)
                    self.ridesSelected = False

        elif self.compareRadioButton.isChecked():
            # check box is checked finds which one is checked, adds to selected list, if there is 2 rides selected
            # the rest of the ride boxes are disabled then the compare function is called with the ride Ids
            if not self.ridesSelected or self.ridesSelected and len(self.frames_selected) == 1:
                for frame in self.frames:
                    if frame[1].isChecked():
                        if [frame[1], frame[2]] not in self.frames_selected:
                            self.frames_selected.append([frame[1], frame[2]])
                if len(self.frames_selected) == 2:
                    self.ridesSelected = True
                    for fram in self.frames:
                        fram[1].setEnabled(False)
                    self.frames_selected[0][0].setEnabled(True)
                    self.frames_selected[1][0].setEnabled(True)
                    self.ride_compare_panel(self.frames_selected[0][1], self.frames_selected[1][1])
            else:
                # if 2 rides were selected it checks which one has recently been clicked by seeing if it is enabled but not checked
                # then removed it from selected list and enables the remaining check boxes
                for frame in self.frames:
                    if frame[1].isEnabled() and not frame[1].isChecked():
                        unselected_frame = [frame[1], frame[2]]
                        self.frames_selected.remove(unselected_frame)
                        if len(self.frames_selected) == 1:
                            self.ridesSelected = True
                for frame in self.frames:
                    frame[1].setEnabled(True)

            # if a ride is still checked then the program needs to make note of one being selected
            # if both have been deselected then is makes sure that no frames are in the selected list
            selected = False
            for frame in self.frames:
                if frame[1].isChecked():
                    selected = True
            if not selected:
                self.frames_selected = []
                self.ridesSelected = False

    def clear_layout(self, layout):
        # removes all the child widgets and child layouts from a layout using recursion
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().hide()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())
                    child.layout().deleteLater()

    def ride_data_panel(self, ride_id):
        # sets up the page when view data check box is selected
        layout = self.horizontalLayout_4
        self.clear_layout(layout)

        # sets up editable widgets
        self.chart_selecter = QtWidgets.QComboBox(self)
        self.chart_selecter.addItems(['Power & Hr vs Time', 'Power, HR Time Curve', 'HR vs Power'])
        self.chart_selecter.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.average_slider = QtWidgets.QSlider(1)
        self.average_slider.setRange(1, 60)
        self.average_slider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.average_slider.setPageStep(0)
        self.average_slider.valueChanged.connect(self.slider_update)

        self.redraw_button = QtWidgets.QPushButton(self)
        self.redraw_button.setText("Redraw Graph")
        self.redraw_button.clicked.connect(lambda: self.update_data_graph(ride_id))

        # sets up charts
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM ride{ride_id}")
        power = []
        heart_rate = []
        time = []
        while True:
            result = cursor.fetchone()
            if result is None:
                break
            time.append(result[0])
            power.append(result[3])
            heart_rate.append(result[4])

        self.data_chart = Canvas(self, 12, 7)
        self.data_chart.plot_dual_graph(time, power, time, heart_rate, "Power", "Heart Rate", "Time / s", "w, bpm",
                                        "Power & Heart Rate over ride")
        self.data_chart.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticle_layout = QtWidgets.QGridLayout(self)
        self.verticle_layout.addWidget(self.data_chart, 0, 0)

        self.heart_rate_variance_chart = Canvas(self, 12, 4)
        data = self.calc_heart_rate_variance(ride_id)
        self.heart_rate_variance_chart.plot_graph(data[1], data[0], "Time", "%bpm", "Heart Rate Variance")
        self.heart_rate_variance_chart.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticle_layout.addWidget(self.heart_rate_variance_chart, 1, 0)

        self.horizontalLayout_4.addLayout(self.verticle_layout)

        # sets up the readable data next to the charts
        self.verticle_layout2 = QtWidgets.QVBoxLayout(self)
        self.choose_graph_label = QtWidgets.QLabel(self)
        self.choose_graph_label.setText("Choose Graph")
        self.choose_graph_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(self.choose_graph_label)

        self.verticle_layout2.addWidget(self.chart_selecter)

        self.rolling_average_label = QtWidgets.QLabel(self)
        self.rolling_average_label.setText("Rolling Average: 1")
        self.rolling_average_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(self.rolling_average_label)

        self.verticle_layout2.addWidget(self.average_slider)
        self.verticle_layout2.addWidget(self.redraw_button)

        normalised_data = self.normalised_power(ride_id)
        average_power_label = QtWidgets.QLabel(self)
        average_power = normalised_data[3]
        average_power_label.setText(f"Average Power:  {average_power}")
        average_power_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(average_power_label)

        cursor.execute(f"SELECT weight FROM users WHERE username = '{self.username}'")
        weight = cursor.fetchall()[0][0]

        average_wkg_label = QtWidgets.QLabel(self)
        wkg = np.round(normalised_data[3] / weight, 1)
        average_wkg_label.setText(f"Average Watts/kg:   {wkg}")
        average_wkg_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(average_wkg_label)

        normalised_power_label = QtWidgets.QLabel(self)
        normalised_power = normalised_data[0]
        normalised_power_label.setText(f"Normalised Power:  {normalised_power}")
        normalised_power_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(normalised_power_label)

        Intensity_factor_label = QtWidgets.QLabel(self)
        Intensity_factor = normalised_data[2]
        Intensity_factor_label.setText(f"Intensity Factor:  {Intensity_factor}")
        Intensity_factor_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(Intensity_factor_label)

        training_stress_score_label = QtWidgets.QLabel(self)
        training_stress_score = normalised_data[1]
        training_stress_score_label.setText(f"TSS:  {training_stress_score}")
        training_stress_score_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(training_stress_score_label)

        Maximum_power_label = QtWidgets.QLabel(self)
        Maximum_power = normalised_data[4]
        Maximum_power_label.setText(f"Maximum Power:  {Maximum_power}")
        Maximum_power_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(Maximum_power_label)

        total_kilojoules_label = QtWidgets.QLabel(self)
        kj = sum(self.get_averaged_data(3, 4, 0, 1, ride_id, [])[0]) // 1000
        total_kilojoules_label.setText(f"Total Kilojoules:  {kj}")
        total_kilojoules_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(total_kilojoules_label)

        data = self.get_power_quartiles(ride_id)
        power_qualtiles_label = QtWidgets.QLabel(self)
        power_qualtiles_label.setText(f"Power Quartiles")
        power_qualtiles_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(power_qualtiles_label)

        qualtiles_label = QtWidgets.QLabel(self)
        qualtiles_label.setText(f"Q1: {data[0]}    Q2: {data[1]}   Q3: {data[2]}")
        qualtiles_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(qualtiles_label)

        self.suggested_increase = QtWidgets.QLabel(self)
        self.suggested_increase.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout2.addWidget(self.suggested_increase)

        self.horizontalLayout_4.addLayout(self.verticle_layout2)
        self.get_power_quartiles(ride_id)

    def ride_compare_panel(self, ride_id1, ride_id2):
        # sets up the page when compare rides is selected
        layout = self.horizontalLayout_4
        self.clear_layout(layout)

        overlap_graph = Canvas(self, 10, 10)
        overlap_graph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # selectes all records from the first rides table where the lat and lng are the same
        cursor = self.connection.cursor()
        cursor.execute(f"""
                        SELECT * FROM ride{ride_id1}
                        JOIN ride{ride_id2} ON ride{ride_id1}.latitude = ride{ride_id2}.latitude 
                        AND ride{ride_id1}.longitude = ride{ride_id2}.longitude
                        """)
        result = cursor.fetchall()
        if result == []:
            result = [0]
        data = self.get_averaged_data(7, 8, 0, 1, ride_id1, result)
        overlap_graph.plot_overlap_graph(data[1], data[0], data[2])

        self.horizontalLayout_4.addWidget(overlap_graph)

        self.verticle_layout3 = QtWidgets.QGridLayout()
        self.choice_combo_box = QtWidgets.QComboBox()
        self.choice_combo_box.addItems(["Compare Segments", ""])
        self.verticle_layout3.addWidget(self.choice_combo_box, 0, 0)

        # sets up graph where selected segments are displayed
        self.segment_graph = Canvas(self, 6, 4)
        self.segment_graph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.segment_graph.ax.set_yticklabels([])
        self.segment_graph.ax.set_xticklabels([])

        sides = [self.segment_graph.ax.spines["right"], self.segment_graph.ax.spines["left"],
                 self.segment_graph.ax.spines["top"],
                 self.segment_graph.ax.spines["bottom"]]
        for side in sides:
            side.set_visible(False)

        self.verticle_layout3.addWidget(self.segment_graph, 1, 0)

        # sets up viewable data for the two compared rides
        self.rolling_average_label = QtWidgets.QLabel(self)
        self.rolling_average_label.setText("Segment: 1")
        self.rolling_average_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.verticle_layout3.addWidget(self.rolling_average_label, 2, 0)

        self.average_slider = QtWidgets.QSlider(1)
        self.average_slider.setRange(1, len(self.segments))
        self.average_slider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.average_slider.valueChanged.connect(self.slider_update)
        self.average_slider.sliderReleased.connect(lambda: self.draw_segment(ride_id1, ride_id2))
        self.average_slider.setPageStep(0)
        self.verticle_layout3.addWidget(self.average_slider, 3, 0)

        line = QtWidgets.QFrame()
        line.setFrameShadow(QtWidgets.QFrame.Plain)
        line.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLayout_3.addWidget(line)

        self.grid_layout = QtWidgets.QGridLayout()

        cursor.execute(f"SELECT name, date from userRide WHERE rideId = {ride_id1} or rideId =  {ride_id2}")
        result = cursor.fetchall()
        dates = [[num[0], num[1]] for num in result]

        self.ride_name_1 = QtWidgets.QLabel()
        self.ride_name_1.setText(f"{dates[0][0]}, {dates[0][1]}")
        self.ride_name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.ride_name_1, 0, 0)

        self.ride_name_2 = QtWidgets.QLabel()
        self.ride_name_2.setText(f"{dates[1][0]}, {dates[1][1]}")
        self.ride_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.ride_name_2, 0, 1)

        self.time_1 = QtWidgets.QLabel()
        self.time_1.setText("time1")
        self.time_1.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.time_1, 1, 0)

        self.time_2 = QtWidgets.QLabel()
        self.time_2.setText("time2")
        self.time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.time_2, 1, 1)

        self.average_power_1 = QtWidgets.QLabel()
        self.average_power_1.setText("power1")
        self.average_power_1.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.average_power_1, 2, 0)

        self.average_power_2 = QtWidgets.QLabel()
        self.average_power_2.setText("power2")
        self.average_power_2.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.average_power_2, 2, 1)

        self.wkg1 = QtWidgets.QLabel()
        self.wkg1.setText("Watts/kg1")
        self.wkg1.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.wkg1, 3, 0)

        self.wkg2 = QtWidgets.QLabel()
        self.wkg2.setText("Watts/kg2")
        self.wkg2.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_layout.addWidget(self.wkg2)

        self.verticle_layout3.addLayout(self.grid_layout, 5, 0)
        self.horizontalLayout_4.addLayout(self.verticle_layout3)

    def fitness_progress_panel(self):
        # sets up the page if progress radio button is selected
        today_date = datetime.date.today()

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT rideId, date FROM userRide WHERE username = '{self.username}' ORDER BY date ASC")
        result = cursor.fetchall()
        if result:
            layout = self.horizontalLayout_4
            self.clear_layout(layout)

            rides = [ride_id[0] for ride_id in result]
            dates = [date[1] for date in result]

            date_start = datetime.date.fromisoformat(dates[0])

            date_delta = f"{today_date - date_start}"
            new = ""
            for ch in date_delta:
                if ch == " ":
                    break
                new += ch
            days_difference = int(new)

            # gets all the dates between the date of the first ride and the date of the last ride
            all_date_formated_list = []
            all_date_list = []
            for i in range(days_difference + 1):
                time_delta = datetime.timedelta(days=i)
                date = date_start + time_delta
                date_formated = datetime.date.strftime(date, "%Y-%m-%d")
                all_date_formated_list.append(date_formated)
                all_date_list.append(date)

            # runs through all the dates, then runs through all rides for each date, if the dates are the same the TSS for that ride is added to the daily TSS
            TSS_list = []

            for date in all_date_formated_list:
                total = 0
                for i in range(len(dates)):
                    if dates[i] == date:
                        total += self.normalised_power(rides[i])[1]
                TSS_list.append(total)

            """for date in all_date_formated_list:
                if date in dates:
                    date_index = dates.index(date)
                    TSS_list.append(self.normalised_power(rides[date_index])[1])
                else:
                    TSS_list.append(0)"""

            # gets the fatigue and fitness for each day based on the TSS
            fatigue_list = []
            total = 0
            for tss in TSS_list:
                total = total * 0.9
                total += tss
                fatigue_list.append(total / 10)

            fitness_list = []
            total = 0
            for fat in fatigue_list:
                total = total * 0.9
                total += fat
                fitness_list.append(total / 10)

            min = 10000
            for tss in TSS_list:
                if tss < min:
                    min = tss

            # plots the 3 lines, TSS, fitness and fatigue onto a graph
            progress_graph = Canvas(self, 16, 12)
            progress_graph.plot_triple_graph(all_date_list, TSS_list, fitness_list, fatigue_list,
                                             "Training Stress Score", "Fitness Score", "Fatigue Score", "Date", "",
                                             "Progress")
            progress_graph.ax.set(ylim=min)
            self.horizontalLayout_4.addWidget(progress_graph)

    def get_averaged_data(self, v1, v2, v3, rolling_average, ride_id, result):
        # takes 3 data points from a ride table and calculates a averaged smoothed table of values
        if result == []:
            result = self.data_from_ride_table(ride_id)
        elif result == [0]:
            return [[], [], []]

        averaged_v1 = []
        averaged_v2 = []
        list_v3 = []
        for i in range(rolling_average, len(result)):
            average1 = 0
            average2 = 0
            for j in range(i - rolling_average, i):
                average1 += result[j][v1]
                average2 += result[j][v2]
            averaged_v1.append(average1 / rolling_average)
            averaged_v2.append(average2 / rolling_average)
            list_v3.append(result[i][v3])

        return [averaged_v1, averaged_v2, list_v3]

    def data_from_ride_table(self, ride_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM ride{ride_id}")
        result = cursor.fetchall()
        return result

    def normalised_power(self, ride_id):
        # gets the NP, IF, TSS, max power, average power
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT watts FROM ride{ride_id}")
        result = cursor.fetchall()
        average_np = 0

        for i in range(30, len(result)):
            total = 0
            for j in range(i - 30, i):
                total += result[j][0]
            weighted_average = (total / 30) ** 4
            average_np += weighted_average

        average_np = average_np / len(result)
        normalised_power = np.round(average_np ** (1 / 4), 0)

        total = 0
        for i in range(len(result)):
            total += result[i][0]
        average_power = np.round(total / len(result), 0)

        cursor.execute(f"SELECT FTP FROM users WHERE username = '{self.username}'")
        FTP = cursor.fetchall()[0][0]

        intensity_factor = np.round(normalised_power / FTP, 2)
        training_stress_score = np.round(intensity_factor ** 2 * (len(result) / 36), 0)

        cursor.execute(f"SELECT MAX(watts) from ride{ride_id}")
        maximum_power = cursor.fetchall()[0][0]

        return normalised_power, training_stress_score, intensity_factor, average_power, maximum_power

    def get_power_quartiles(self, ride_id):
        result = self.get_averaged_data(3, 4, 0, 1, ride_id, [])[0]
        sorted_result = self.quick_sort(result)

        first_quartile = sorted_result[len(sorted_result) // 4]
        second_quartile = sorted_result[len(sorted_result) // 2]
        third_quartile = sorted_result[len(sorted_result) // 4 * 3]
        return [first_quartile, second_quartile, third_quartile]

    def calc_heart_rate_variance(self, ride_id):
        # calculates the change in heart rate for a given power compared to the first 10 minutes
        result = self.data_from_ride_table(ride_id)
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT FTP FROM users WHERE username = '{self.username}'")
        FTP = cursor.fetchall()[0][0]
        power = []
        hr = []
        power_div_hr = []
        ends = []
        start = 60
        end = 660
        while True:
            if end > len(result):
                end = len(result)
            total_power = 0
            total_hr = 0
            for i in range(start, end):
                total_power += result[i][3]
                total_hr += result[i][4]

            if total_power == 0 or total_hr == 0:
                return [], []

            if total_power // (end - start) < FTP * 0.8 and total_power // (end - start) > FTP * 0.5:
                power.append(total_power // (end - start))
                hr.append(total_hr // (end - start))
                power_div_hr.append(total_hr / total_power)
                ends.append(end)

            if end == len(result):
                percentages_list = [0]
                if ends == []:
                    ends = [0]

                for i in range(1, len(power_div_hr)):
                    percentage = (power_div_hr[i] - power_div_hr[0]) / power_div_hr[0] * 100
                    percentages_list.append(np.round(percentage, 3))
                return percentages_list, ends

            start += 600
            end += 600

    def power_curve(self, ride_id):
        # Gets the highest average power and heartrate over periods of time
        points = [1, 3, 5, 10, 30, 60, 300, 600, 1200, 3600]
        custom_ax = ['1', '3', '5', '10', '30', '1min', '5min', '10min', '20min', '1hr']
        power_points = []
        heartrate_points = []

        result = self.data_from_ride_table(ride_id)

        for point in points:
            if point > len(result):
                index = 10 - points.index(point)
                for i in range(index):
                    power_points.append(0)
                    heartrate_points.append(0)

            power_total = 0
            heartrate_total = 0
            power = []
            heartrate = []
            max_power = 0
            max_heartrate = 0
            for i in range(len(result)):
                power.append(result[i][3])
                heartrate.append(result[i][4])
                power_total += result[i][3]
                heartrate_total += result[i][4]
                if len(power) > point:
                    removed_power = power.pop(0)
                    removed_heartrate = heartrate.pop(0)
                    power_total -= removed_power
                    heartrate_total -= removed_heartrate
                    average_power = power_total // point
                    average_heartrate = heartrate_total // point
                    if average_power > max_power:
                        max_power = average_power
                    if average_heartrate > max_heartrate:
                        max_heartrate = average_heartrate
            power_points.append(max_power)
            heartrate_points.append(max_heartrate)

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT HRThreshold, FTP FROM users WHERE username = '{self.username}'")
        result = cursor.fetchone()
        hr_threshold = result[0]
        FTP = result[1]

        test_string = ""
        if power_points[7] * 0.9 > FTP or power_points[8] * 0.95 > FTP or power_points[9] > FTP:
            test_string += 'power'
        if heartrate_points[7] * 0.9 > hr_threshold or heartrate_points[8] * 0.95 > hr_threshold or heartrate_points[
            9] > hr_threshold:
            test_string += 'hr'
        self.suggest_hr_power_increase(test_string)

        return [power_points, heartrate_points, custom_ax]

    def suggest_hr_power_increase(self, string):
        if string == "powerhr":
            self.suggested_increase.setText("Increase to FTP and HRT detected")
        elif string == "power":
            self.suggested_increase.setText("Increase to FTP detected")
        elif string == 'hr':
            self.suggested_increase.setText("Increase to HRT detected")

    def quick_sort(self, array):
        if len(array) <= 1 or sum(array) == 0:
            return array

        pivot = array[-1]
        left = []
        right = []
        for i in range(len(array) - 1):
            if array[i] <= pivot:
                left.append(array[i])
            else:
                right.append(array[i])

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    # def get_power_heartrate_curve(self, ride_id):
    #     # gets the data points for a power curve
    #     cursor = self.connection.cursor()
    #     cursor.execute(f"SELECT time, watts, heartRate FROM ride{ride_id}")
    #     result = cursor.fetchall()
    #
    #     time_points = [1, 5, 10, 30, 60, 300, 600, 1200, 3600]
    #     power_points = []
    #     heartrate_points = []
    #
    #     for time in time_points:
    #         max_power = 0
    #         max_hr = 0
    #         for i in range(len(result) - time):
    #             sum_power = 0
    #             sum_hr = 0
    #             for j in range(i, i + time):
    #                 sum_power += result[j][1]
    #                 sum_hr += result[j][2]
    #             if sum_power > max_power:
    #                 max_power = sum_power
    #             if sum_hr > max_hr:
    #                 max_hr = sum_hr
    #
    #         max_average_power = max_power / time
    #         max_average_hr = max_hr / time
    #         power_points.append(max_average_power)
    #         heartrate_points.append(max_average_hr)
    #
    #     return [power_points, heartrate_points, time_points]

    def slider_update(self, value):
        # updates slider label
        if self.dataRadioButton.isChecked():
            self.rolling_average_label.setText(f"Rolling Average: {value}")
        else:
            self.rolling_average_label.setText(f"Segment: {value}")

    def update_data_graph(self, ride_id):
        # redraws the graph on the data page for the rolling average or power curve
        self.chart_selecter_value = self.chart_selecter.currentIndex()
        self.slider_average_value = self.average_slider.value()

        self.data_chart.deleteLater()
        self.data_chart = Canvas(self, 12, 7)
        self.data_chart.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        if self.chart_selecter_value == 0:
            data = self.get_averaged_data(3, 4, 0, self.slider_average_value, ride_id, [])
            self.data_chart.plot_dual_graph(data[2], data[0], data[2], data[1], "Power", "Heart Rate", "Time", "w, bpm",
                                            "Power & Heart rate over ride")

        elif self.chart_selecter_value == 1:
            # data = self.get_power_heartrate_curve(ride_id)
            data = self.power_curve(ride_id)
            self.data_chart.plot_dual_graph(data[2], data[0], data[2], data[1], "Power", "Heart Rate", "Time", "w, bpm",
                                            "Power & Heart rate curves")

        elif self.chart_selecter_value == 2:
            data = self.get_averaged_data(3, 4, 0, 180, ride_id, [])
            self.data_chart.plot_scatter(data[0], data[1], 'Power', 'Heart Rate', 'Heart Rate vs Power')

        self.verticle_layout.addWidget(self.data_chart, 0, 0)

    def draw_segment(self, ride_id1, ride_id2):
        # draws the segment when the slider is released
        slider_value = self.average_slider.value() - 1
        compare_mode = self.choice_combo_box.currentIndex()

        if compare_mode == 0:
            self.segment_graph.deleteLater()
            data = (self.segments[slider_value][0], self.segments[slider_value][1])
            self.segment_graph = Canvas(self, 6, 4)
            self.segment_graph.plot_graph(data[0], data[1], '', '', '')
            self.segment_graph.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.verticle_layout3.addWidget(self.segment_graph, 1, 0)

            segment = self.segments[slider_value]
            start_point = [segment[0][0], segment[1][0]]
            end_point = [segment[0][-1], segment[1][-1]]

            cursor = self.connection.cursor()
            cursor.execute(
                f"SELECT time from ride{ride_id1} WHERE longitude = {start_point[0]} and latitude = {start_point[1]}")
            ride_1_start_time = cursor.fetchall()[0][0]
            cursor.execute(
                f"SELECT time from ride{ride_id1} WHERE longitude = {end_point[0]} and latitude = {end_point[1]}")
            ride_1_end_time = cursor.fetchall()[0][0]
            time_1 = ride_1_end_time - ride_1_start_time

            cursor.execute(
                f"SELECT time from ride{ride_id2} WHERE longitude = {start_point[0]} and latitude = {start_point[1]}")
            ride_2_start_time = cursor.fetchall()[0][0]
            cursor.execute(
                f"SELECT time from ride{ride_id2} WHERE longitude = {end_point[0]} and latitude = {end_point[1]}")
            ride_2_end_time = cursor.fetchall()[0][0]
            time_2 = ride_2_end_time - ride_2_start_time

            self.time_1.setText(f"Time: {time_1 // 60:02.0f}:{time_1 % 60:02.0f}")
            self.time_2.setText(f"Time: {time_2 // 60:02.0f}:{time_2 % 60:02.0f}")

            cursor.execute(
                f"SELECT watts from ride{ride_id1} WHERE time >= {ride_1_start_time} and time <= {ride_1_end_time}")
            power1 = [watts[0] for watts in cursor.fetchall()]
            total = 0
            for power in power1:
                total += power
            if len(power1) > 0:
                average_power_1 = total // len(power1)
            else:
                average_power_1 = 0

            if time_2 > 0:
                cursor.execute(
                    f"SELECT watts from ride{ride_id2} WHERE time >= {ride_2_start_time} and time <= {ride_2_end_time}")
                power2 = [watts[0] for watts in cursor.fetchall()]
                total = 0
                for power in power2:
                    total += power
                if len(power2) > 0:
                    average_power_2 = total // len(power2)
                else:
                    average_power_2 = 0
            else:
                cursor.execute(
                    f"SELECT watts from ride{ride_id2} WHERE time >= {ride_2_end_time} and time <= {ride_2_start_time}")
                power2 = [watts[0] for watts in cursor.fetchall()]
                total = 0
                for power in power2:
                    total += power
                if len(power2) > 0:
                    average_power_2 = total // len(power2)
                else:
                    average_power_2 = 0

            self.average_power_1.setText(f"Average Power: {average_power_1}")
            self.average_power_2.setText(f"Average Power: {average_power_2}")

            cursor.execute(f"SELECT weight FROM users WHERE username = '{self.username}'")
            weight = cursor.fetchall()[0][0]

            self.wkg1.setText(f"Watts/kg: {np.round(average_power_1 / weight, 1)}")
            self.wkg2.setText(f"Watts/kg: {np.round(average_power_2 / weight, 1)}")

    def menuPressed(self):
        # changes the scroll window when menu is pressed or goes back
        layout = self.verticalLayout_3
        self.clear_layout(layout)

        if not self.menu:
            self.scrollAreaWidgetContents.resize(500, 200)
            self.menu = True
            self.menuButton.setText("See Rides")
            self.menu_widgets_setup()

        else:
            self.more_rides(0)
            self.menuButton.setText("Menu")
            self.ridesSelected = False
            self.frames_selected = []
            self.menu = False

            if self.progressRadioButton.isChecked():
                for frame in self.frames:
                    frame[1].setEnabled(False)

    def menu_widgets_setup(self):
        self.add_ride_button = QtWidgets.QPushButton()
        self.add_ride_button.setText("Add Ride")
        self.add_ride_button.clicked.connect(self.open_file)
        self.verticalLayout_3.addWidget(self.add_ride_button)

        self.update_user_profile = QtWidgets.QPushButton()
        self.update_user_profile.setText("Update Profile")
        self.update_user_profile.clicked.connect(self.profile_update)
        self.verticalLayout_3.addWidget(self.update_user_profile)

    def open_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "/PythonFiles", "Ride Files (*.csv)", )
        if filename != "":

            with open(filename, 'r') as reader:
                data = reader.readlines()
                reader.close()

            attributes = []
            new = ""
            for ch in data[0]:
                if ch == "," or ch == "\n":
                    if new == "":
                        attributes.append(0)
                    else:
                        attributes.append(new)
                        new = ""
                elif ch != " ":
                    new += ch
            attributes.append(new)

            if 'time' in attributes and 'moving' in attributes and 'distance' in attributes and 'cadence' in attributes and 'velocity_smooth' in attributes and 'lat' in attributes and 'lng' in attributes and 'temp' in attributes and 'altitude' in attributes:

                self.connection.execute(f"INSERT INTO userRide(username) VALUES('{self.username}')")

                cursor = self.connection.cursor()
                cursor.execute(
                    f"SELECT rideId FROM userRide WHERE username = '{self.username}' ORDER BY rideId DESC LIMIT 1")
                rideId = cursor.fetchall()
                ride_num = (rideId[0][0])

                self.app = QtWidgets.QApplication(sys.argv)
                self.ui = Name_ride(self, self.connection, self.username, ride_num)
                self.new_window = True
                self.close()
                self.ui.show()
                self.app.exec_()

                self.connection.execute(f"""CREATE TABLE 'ride{ride_num}' (
                                        'time' INTEGER PRIMARY KEY,
                                        'moving' BOOLEAN, 
                                        'distance' REAL,
                                        'watts' INTEGER,
                                        'heartRate' INTEGER,
                                        'cadence' INTEGER,
                                        'velocitySmooth' REAL,
                                        'latitude' REAL,
                                        'longitude' REAL,
                                        'temp' REAL,
                                        'altitude' REAL
                                        )
                                        """)

                for i in range(1, len(data)):
                    datapoint = []
                    new = ""
                    for ch in data[i]:
                        if ch == "," or ch == "\n":
                            if new == "":
                                datapoint.append(0)
                            else:
                                datapoint.append(new)
                                new = ""
                        elif ch != " ":
                            new += ch
                    datapoint.append(new)

                    if attributes[3] != "watts" and attributes[3] != "heartrate":
                        self.connection.execute(f"""
                                                INSERT INTO ride{ride_num}(time, moving, distance, watts, heartRate, cadence, velocitySmooth, latitude, longitude, temp, altitude)
                                                VALUES({int(datapoint[0])}, {datapoint[1]}, {float(datapoint[2])}, {0}, {0},
                                                {int(datapoint[3])}, {float(datapoint[4])}, {np.round(float(datapoint[5]), 4)}, {np.round(float(datapoint[6]), 4)}, {float(datapoint[7])}, {float(datapoint[8])})
                                                                        """)
                    elif attributes[3] != "watts":
                        self.connection.execute(f"""
                                                INSERT INTO ride{ride_num}(time, moving, distance, watts, heartRate, cadence, velocitySmooth, latitude, longitude, temp, altitude)
                                                VALUES({int(datapoint[0])}, {datapoint[1]}, {float(datapoint[2])}, {0}, {int(datapoint[3])},
                                                {int(datapoint[4])}, {float(datapoint[5])}, {np.round(float(datapoint[6]), 4)}, {np.round(float(datapoint[7]), 4)}, {float(datapoint[8])}, {float(datapoint[9])})
                                                                        """)
                    elif attributes[4] != "heartrate":
                        self.connection.execute(f"""
                                                INSERT INTO ride{ride_num}(time, moving, distance, watts, heartRate, cadence, velocitySmooth, latitude, longitude, temp, altitude)
                                                VALUES({int(datapoint[0])}, {datapoint[1]}, {float(datapoint[2])}, {int(datapoint[3])}, {0},
                                                {int(datapoint[4])}, {float(datapoint[5])}, {np.round(float(datapoint[6]), 4)}, {np.round(float(datapoint[7]), 4)}, {float(datapoint[8])}, {float(datapoint[9])})
                                                                        """)
                    else:
                        self.connection.execute(f"""
                                                INSERT INTO ride{ride_num}(time, moving, distance, watts, heartRate, cadence, velocitySmooth, latitude, longitude, temp, altitude)
                                                VALUES({int(datapoint[0])}, {datapoint[1]}, {float(datapoint[2])}, {int(datapoint[3])}, {int(datapoint[4])},
                                                {int(datapoint[5])}, {float(datapoint[6])}, {np.round(float(datapoint[7]), 4)}, {np.round(float(datapoint[8]), 4)}, {float(datapoint[9])}, {float(datapoint[10])})
                                                                        """)

        if not testing:
            self.connection.commit()

    def profile_update(self):
        self.new_window = True

        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Update_profile(self.connection, self.username)
        self.close()
        self.ui.show()
        self.app.exec_()

    def reset_panel(self):
        # changes the page back to the plain screen
        layout = self.horizontalLayout_4
        self.clear_layout(layout)

        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)

        spacerItem1 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

    def viewDataChoice(self):
        self.reset_panel()
        for frame in self.frames:
            frame[1].setChecked(False)
            frame[1].setEnabled(True)
            self.ridesSelected = False

    def compareChoice(self):
        self.reset_panel()
        for frame in self.frames:
            frame[1].setChecked(False)
            frame[1].setEnabled(True)
            self.ridesSelected = False
            self.frames_selected = []

    def progressChoice(self):
        for frame in self.frames:
            frame[1].setChecked(False)
            frame[1].setEnabled(False)
            self.ridesSelected = False
        self.fitness_progress_panel()

    def mapShow(self):
        print("map")

    def closeEvent(self, event):
        if not self.new_window:
            dlg = QtWidgets.QMessageBox.warning(self, 'Quit?', 'Are you sure?',
                                                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if dlg == QtWidgets.QMessageBox.Ok:
                event.accept()
            else:
                event.ignore()