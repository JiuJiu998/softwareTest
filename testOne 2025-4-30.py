import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class DateCalculator:
    def __init__(self, master):
        self.master = master
        master.title("第二日日期计算器")
        master.geometry("380x250")

        # 输入框架
        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        # 年输入
        self.year_label = tk.Label(input_frame, text="年：")
        self.year_entry = tk.Entry(input_frame, width=10)
        self.year_label.grid(row=0, column=0, padx=5)
        self.year_entry.grid(row=0, column=1, padx=5)

        # 月输入
        self.month_label = tk.Label(input_frame, text="月：")
        self.month_entry = tk.Entry(input_frame, width=10)
        self.month_label.grid(row=1, column=0, padx=5)
        self.month_entry.grid(row=1, column=1, padx=5)

        # 日输入
        self.day_label = tk.Label(input_frame, text="日：")
        self.day_entry = tk.Entry(input_frame, width=10)
        self.day_label.grid(row=2, column=0, padx=5)
        self.day_entry.grid(row=2, column=1, padx=5)

        # 按钮框架
        button_frame = tk.Frame(master)
        button_frame.pack(pady=15)

        self.confirm_btn = tk.Button(button_frame, text="确定", command=self.validate_date, width=8)
        self.calc_btn = tk.Button(button_frame, text="计算", command=self.calculate_next_day, width=8)
        self.clear_btn = tk.Button(button_frame, text="清除", command=self.clear_input, width=8)
        self.cancel_btn = tk.Button(button_frame, text="取消", command=master.quit, width=8)

        self.confirm_btn.grid(row=0, column=0, padx=5)
        self.calc_btn.grid(row=0, column=1, padx=5)
        self.clear_btn.grid(row=0, column=2, padx=5)
        self.cancel_btn.grid(row=0, column=3, padx=5)

        # 结果标签
        self.result_label = tk.Label(master, text="", fg="blue")
        self.result_label.pack(pady=10)

        # 初始化有效日期
        self.valid_date = None

    def validate_date(self):
        """验证输入的日期有效性"""
        try:
            year = int(self.year_entry.get())
            month = int(self.month_entry.get())
            day = int(self.day_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return

        if not (1800 <= year <= 2050):
            messagebox.showerror("错误", "年份必须在1800-2050之间")
            return

        try:
            datetime(year, month, day)
            self.valid_date = (year, month, day)
            messagebox.showinfo("成功", "日期验证通过！")
        except ValueError:
            messagebox.showerror("错误", "无效的日期")
            self.valid_date = None

    def calculate_next_day(self):
        """计算下一天日期"""
        if not self.valid_date:
            messagebox.showerror("错误", "请先验证日期有效性")
            return

        year, month, day = self.valid_date
        try:
            current_date = datetime(year, month, day)
            next_date = current_date.replace(day=current_date.day + 1)
            self.result_label.config(text=f"第二日日期：{next_date.year}-{next_date.month}-{next_date.day}")
        except ValueError:
            # 处理月末特殊情况
            try:
                next_date = datetime(year, month + 1, 1)
            except ValueError:
                next_date = datetime(year + 1, 1, 1)
            self.result_label.config(text=f"第二日日期：{next_date.year}-{next_date.month}-{next_date.day}")

    def clear_input(self):
        """清除所有输入"""
        self.year_entry.delete(0, tk.END)
        self.month_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.valid_date = None
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = DateCalculator(root)
    root.mainloop()