from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import cv2
import time

class PrankApp(App):
    def build(self):
        # إنشاء و تخطيط عمودي
        layout = BoxLayout(orientation='vertical')

        # إنشاء التسميات
        self.label = Label(text="اضغط على الزر لتشغيل الكاميرا", font_size=40)  # زيادة حجم الخط
        layout.add_widget(self.label)

        # إنشاء زر للنقر
        prank_button = Button(text="اضغط هنا", font_size=40)  # زيادة حجم الخط
        prank_button.bind(on_press=self.run_prank)  # ربط الضغط على الزر بالوظيفة
        layout.add_widget(prank_button)

        return layout

    def run_prank(self, instance):
        # تغيير نص التسمية عند الضغط على الزر
        self.label.text = "جاري تفعيل الكاميرا..."
        time.sleep(1.5)  # تأخير 1.5 ثانية قبل بدء الكاميرا
        self.open_camera()

    def open_camera(self):
        # تفعيل الكاميرا
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.label.text = "فشل في فتح الكاميرا"
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                self.label.text = "خطأ في قراءة الإطار!"
                break

            # عرض الكاميرا على الشاشة
            cv2.imshow("الكاميرا", frame)

            # الخروج عند الضغط على "q"
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    PrankApp().run()
