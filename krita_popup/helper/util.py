from krita import *
from typing import Callable
from .QtAll import *
from time import perf_counter

def get_window_from_object_name(window_object_name: str):
    """
    get krita window object from object_name, raise AssertionError if corresponding window does not exist
    """
    for i in Krita.instance().windows():
        if i.objectName() == window_object_name:
            return i
    raise AssertionError(f'window "{window_object_name}" not exists')

def display_msg_box(text: str, icon: QMessageBox.Icon):
    box = QMessageBox()
    box.setIcon(icon)
    box.setText(text)
    box.exec()

def get_pixel_data(doc: Document, cb: Callable[[bytearray], None]): 
    """性能无法忍受，建议用截图"""
    THRESHOLD = 1200000
    DELAY = 20
    w = doc.width()
    h = doc.height()
    pixel_size = len(doc.pixelData(0,0,1,1))
    BUFFER_HEIGHT = THRESHOLD // w

    h_ranges = [(i, min(i + BUFFER_HEIGHT, h)) for i in range(0, h, BUFFER_HEIGHT)]
    h_range_iter = iter(h_ranges)

    combined_byte_array = bytearray(pixel_size * w * h)
    
    current_position = 0
    def loop_me():
        nonlocal current_position
        try:
            h_start, h_end = next(h_range_iter)
        except StopIteration:
            cb(combined_byte_array)
            return 
        
        start = perf_counter()
        qbytearray = doc.pixelData(0, h_start, w, h_end - h_start)
        end = perf_counter()
        print(f"get: {(end - start) * 1000} ms")

        start = perf_counter()
        size = len(qbytearray)
        combined_byte_array[current_position:current_position + size] = bytes(qbytearray)
        end = perf_counter()
        print(f"copy: {(end - start) * 1000} ms")
        
        current_position += size
        
        QTimer.singleShot(DELAY, loop_me)
    QTimer.singleShot(0, loop_me)


def krita_window_id(window: Window):
    return window.qwindow().objectName()
    

# 我tm在干嘛？？
# executor = ThreadPoolExecutor(1)

# @singleton
# class SignalHandler(QObject):
#     result_ready = pyqtSignal()
#     result = None
#     def __init__(self):
#         super().__init__()

#     @pyqtSlot()
#     def result_ready_emit(self):
#         print('result_ready: me dynamicly emit')
#         self.result_ready.emit()
        
#     @pyqtSlot(object)
#     def result_ready_connect(self, go):
#         print('result_ready: me dynamicly connect')
#         def mygo():
#             go(self.result)
#             self.result_ready.disconnect(mygo)
#         self.result_ready.connect(mygo)

# # 从上到下分多次把所有像素拿到
# # 阈值定为一次 1200000 像素，对宽度取整
# def get_pixel_data(doc: Document, cb: Callable[[bytearray], None]): 
#     handler = SignalHandler()
#     handler.result_ready_connect(cb)
#     THRESHOLD = 1000000
#     DELAY = 10
#     w = doc.width()
#     h = doc.height()
#     BUFFER_HEIGHT = THRESHOLD // w

#     tasks = [(i, min(i + BUFFER_HEIGHT, h)) for i in range(0, h, BUFFER_HEIGHT)]
#     task_iter = iter(tasks)

#     res: List[QByteArray] = []
    
#     def callback():
#         # 在其他线程中执行，使用QTimer去再挪到本地
#         start = perf_counter()
#         total_size = sum(len(qb) for qb in res)
#         # 预先分配指定大小的 bytearray
#         combined_byte_array = bytearray(total_size)
#         # 填充数据
#         current_position = 0
#         for qbytearray in res:
#             size = len(qbytearray)
#             combined_byte_array[current_position:current_position + size] = qbytearray
#             current_position += size
#         end = perf_counter()

#         handler.result = combined_byte_array
#         QMetaObject.invokeMethod(handler, "result_ready_emit")
#         print(f"combine: {(end - start) * 1000} ms")

#     def loop_me():
#         try:
#             h_start, h_end = next(task_iter)
#         except StopIteration:
#             executor.submit(callback)
#             return 
#         start = perf_counter()
#         res.append(doc.pixelData(0, h_start, w, h_end - h_start + 1))
#         end = perf_counter()
#         print(f"part: {(end - start) * 1000} ms")
#         QTimer.singleShot(DELAY, loop_me)
#     QTimer.singleShot(0, loop_me)
        

# def test_me():
#     doc=Krita.instance().activeDocument()
#     def go(_):
#         QTimer.singleShot(30, test_me)
#     get_pixel_data(doc, go)