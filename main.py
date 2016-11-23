import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
import yaml
import json


wWitdh=789
wHeight=650

root = tk.Tk()
root.geometry("{0}x{1}".format(wWitdh, wHeight))
root.resizable(width=False, height=False)
root.title("YAML<->JSON")
root.configure(bg='#13478c')

#text 字体
f = font.Font(family='Helvetica', size=16)

#text column
text_column = 35
text_line = 32

#设置yml编辑框
yml_text = tk.Text(root, width=text_column, height=text_line, exportselection=0, bg='#0a7a19', fg='#ffffff', font=f)
yml_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=yml_text.yview)
yml_text['yscrollcommand'] = yml_scrollbar.set
yml_text.grid(row=0, column=0, sticky=tk.NS)
yml_scrollbar.grid(row=0, column=1, sticky=tk.NS)

#设置json编辑框
json_text = tk.Text(root, width=text_column, exportselection=0, bg='#0a7a19', fg='#ffffff', font=f)
json_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=json_text.yview)
json_text['yscrollcommand'] = json_scrollbar.set
json_text.grid(row=0, column=3, sticky=tk.NS)
json_scrollbar.grid(row=0, column=4, sticky=tk.NS)

#设置错误提示label
tips_str = '提示:'
error_tips = tk.Label(root, text=tips_str, fg='#d92b2b', bg='#13478c')
error_tips.grid(row=1, column=0, sticky=tk.NW)

def clean_command():
    yml_text.delete(1.0, tk.END)
    json_text.delete(1.0, tk.END)


def yml_2_json():
    json_text.delete(1.0, tk.END)
    error_tips['text']=tips_str
    txt = yml_text.get(1.0, tk.END)
    if len(txt) <= 1:
        return
    try:
        yml_doc = yaml.load_all(txt)
        j = ""
        for obj in yml_doc:
            j += json.dumps(obj, indent=4)
        json_text.insert(1.0, j)
    except:
        error_tips['text']=tips_str + 'YAML解析错误'


def json_2_yml():
    yml_text.delete(1.0, tk.END)
    error_tips['text']=tips_str
    try:
        txt = json_text.get(1.0, tk.END)
        if len(txt) <= 1:
            return
        json_doc = json.loads(txt)
        yml_text.insert(1.0, yaml.dump(json_doc, default_flow_style=False))
    except:
        error_tips['text']=tips_str + 'JSON解析错误'


#设置功能按钮
btn_frame = tk.Frame(root, bg='#13478c')
yml2json_btn = ttk.Button(btn_frame, text="YML->JSON", command=yml_2_json)
yml2json_btn.pack(side=tk.TOP)
json2yml_btn = ttk.Button(btn_frame, text="YML<-JSON", command=json_2_yml)
json2yml_btn.pack(side=tk.TOP)
clear_btn = ttk.Button(btn_frame, text="CLEAN", command=clean_command)
clear_btn.pack(side=tk.TOP, fill=tk.X)
btn_frame.grid(row=0, column=2)


root.mainloop()
