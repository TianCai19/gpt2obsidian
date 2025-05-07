# Windows 快捷操作指南

## 方法一：创建批处理文件

1. 创建一个名为 `gpt2obsidian.bat` 的文件，内容如下：

```batch
@echo off
python "完整路径\gpt2obsidian.py" %*
```

2. 将批处理文件放在系统 PATH 目录下（例如 `C:\Windows` 或 `C:\Users\用户名\AppData\Local\Programs\Python\Python3x\Scripts`）

3. 现在您可以在任何目录下使用以下命令：
```bash
gpt2obsidian input.txt output.txt
```

## 方法二：添加到右键菜单

1. 创建一个注册表文件 `add_context_menu.reg`，内容如下：

```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\ConvertToObsidian]
@="转换为 Obsidian 格式"

[HKEY_CLASSES_ROOT\*\shell\ConvertToObsidian\command]
@="python \"完整路径\\gpt2obsidian.py\" \"%1\" \"%1.obsidian.md\""
```

2. 双击运行该注册表文件

3. 现在您可以在任何文件上右键点击，选择"转换为 Obsidian 格式"

## 方法三：创建桌面快捷方式

1. 右键点击桌面，选择"新建" -> "快捷方式"
2. 在位置框中输入：
```
python "完整路径\gpt2obsidian.py"
```
3. 点击"下一步"，输入快捷方式名称（如"GPT2Obsidian"）
4. 点击"完成"

## 注意事项

- 请将上述所有"完整路径"替换为 `gpt2obsidian.py` 的实际路径
- 确保 Python 已添加到系统环境变量中
- 如果遇到权限问题，请以管理员身份运行相关命令 