import webview
import os
import sys

# دالة للبحث عن ملف HTML سواء كنت تشغل الكود كملف عادي أو كملف EXE
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def start():
    # تحديد مسار ملف الـ HTML
    html_file = resource_path('index.html')
    
    # طباعة المسار للتحقق (يمكنك حذف هذا السطر لاحقاً)
    print(f"Looking for HTML at: {html_file}")
    
    # التأكد من وجود الملف قبل التشغيل
    if not os.path.exists(html_file):
        print("Error: index.html not found!")
        # هنا نقوم بإنشاء ملف افتراضي بسيط لتجنب توقف البرنامج تماماً (للتجربة فقط)
        webview.create_window('Error', html='<h1>index.html is missing from the build!</h1>')
    else:
        # تشغيل النافذة
        webview.create_window(
            title='Guard Security Tool',
            url=html_file,
            width=1280,
            height=800,
            resizable=True,
            text_select=False
        )
    
    webview.start(debug=False)

if __name__ == '__main__':
    start()