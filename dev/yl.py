#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.14.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import roi
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 15.625e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr=192.168.20.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(2.535e9, 0)
        self.uhd_usrp_source_0_0.set_gain(45, 0)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_0_0.set_center_freq(2.535e9, 1)
        self.uhd_usrp_source_0_0.set_gain(45, 1)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 1)
        self.uhd_usrp_source_0_0.set_center_freq(2.535e9, 2)
        self.uhd_usrp_source_0_0.set_gain(45, 2)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 2)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 2)
        self.uhd_usrp_source_0_0.set_center_freq(2.535e9, 3)
        self.uhd_usrp_source_0_0.set_gain(45, 3)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 3)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 3)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 3)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.20.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(2.535e9, 0)
        self.uhd_usrp_sink_0_0.set_gain(40, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0_0.set_center_freq(2.535e9, 1)
        self.uhd_usrp_sink_0_0.set_gain(40, 1)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0_0.set_center_freq(2.535e9, 2)
        self.uhd_usrp_sink_0_0.set_gain(40, 2)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_sink_0_0.set_center_freq(2.535e9, 3)
        self.uhd_usrp_sink_0_0.set_gain(40, 3)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 3)
        self.roi_file_source_roi_0_2 = roi.file_source_roi(gr.sizeof_gr_complex*1, '/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/tx_data_sine_16_00', False, 3)
        self.roi_file_source_roi_0_1 = roi.file_source_roi(gr.sizeof_gr_complex*1, '/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/tx_data_sine_16_00', False, 2)
        self.roi_file_source_roi_0_0 = roi.file_source_roi(gr.sizeof_gr_complex*1, '/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/tx_data_sine_16_00', False, 1)
        self.roi_file_source_roi_0 = roi.file_source_roi(gr.sizeof_gr_complex*1, '/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/tx_data_sine_16_00', False, 0)
        self.roi_file_sink_roi_0_2 = roi.file_sink_roi('/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/detect_data4', False, 8, 8, 128, True, (window.blackmanharris(128)), False, 2, 1)


        self.roi_file_sink_roi_0_1 = roi.file_sink_roi('/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/detect_data3', False, 8, 8, 128, True, (window.blackmanharris(128)), False, 2, 1)


        self.roi_file_sink_roi_0_0 = roi.file_sink_roi('/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/detect_data2', False, 8, 8, 128, True, (window.blackmanharris(128)), False, 2, 1)


        self.roi_file_sink_roi_0 = roi.file_sink_roi('/home/sdr/matlab_files/802.11ax_RX_Process_Newest/RX_Process/data/detect_data1', False, 8, 8, 128, True, (window.blackmanharris(128)), False, 2, 1)


        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_c(
        	10240, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude_ch0', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.roi_file_source_roi_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.roi_file_source_roi_0, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.roi_file_source_roi_0_0, 0), (self.uhd_usrp_sink_0_0, 1))
        self.connect((self.roi_file_source_roi_0_1, 0), (self.uhd_usrp_sink_0_0, 2))
        self.connect((self.roi_file_source_roi_0_2, 0), (self.uhd_usrp_sink_0_0, 3))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.roi_file_sink_roi_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 1), (self.roi_file_sink_roi_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 2), (self.roi_file_sink_roi_0_1, 0))
        self.connect((self.uhd_usrp_source_0_0, 3), (self.roi_file_sink_roi_0_2, 0))


	self.msg_connect(self.roi_file_sink_roi_0, "msg_status_file", self.roi_file_source_roi_0, "msg_status_file")
	self.msg_connect(self.roi_file_sink_roi_0_0, "msg_status_file", self.roi_file_source_roi_0, "msg_status_file")
	self.msg_connect(self.roi_file_sink_roi_0_1, "msg_status_file", self.roi_file_source_roi_0, "msg_status_file")
	self.msg_connect(self.roi_file_sink_roi_0_2, "msg_status_file", self.roi_file_source_roi_0, "msg_status_file")

	self.msg_connect(self.roi_file_source_roi_0, "msg_status_file_1", self.roi_file_source_roi_0_0, "msg_status_file_1")
	self.msg_connect(self.roi_file_source_roi_0, "msg_status_file_2", self.roi_file_source_roi_0_1, "msg_status_file_2")
	self.msg_connect(self.roi_file_source_roi_0, "msg_status_file_3", self.roi_file_source_roi_0_2, "msg_status_file_3")

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
