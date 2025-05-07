# GPT2Obsidian

一个简单的 Python 工具，用于将包含 LaTeX 数学公式的文本转换为 Obsidian 支持的 Markdown 格式。

## 功能特点

- 将 LaTeX 格式的数学公式转换为 Obsidian 兼容的格式
- 支持行内公式 `\(...\)` 转换为 `$...$`
- 支持块级公式 `\[...\]` 转换为 `$$...$$`
- 支持从文件读取或从剪贴板读取内容
- 支持输出到文件或复制到剪贴板

## 安装要求

```bash
pip install pyperclip
```

## 使用方法

1. 从文件转换：
```bash
python gpt2obsidian.py input.txt output.txt
```

2. 从剪贴板转换：
```bash
python gpt2obsidian.py
```

## 快捷操作

### Windows
请参考 [Windows 快捷操作指南](docs/windows_shortcut.md)

### macOS (Raycast)
请参考 [Raycast 快捷操作指南](docs/raycast_shortcut.md)

## 示例

输入文本：
```
行内公式：\(E = mc^2\) 是著名的质能方程。

块级公式：
\[
\frac{d}{dx}(x^n) = nx^{n-1}
\]
```

转换后：
```
行内公式：$E = mc^2$ 是著名的质能方程。

块级公式：
$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$
``` 