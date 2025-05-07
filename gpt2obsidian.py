import re
import pyperclip
import sys

def convert_to_obsidian_format(input_text):
    """
    将输入的文档转换为 Obsidian 支持的 Markdown 格式，处理数学公式。
    :param input_text: 输入的文档内容（字符串）
    :return: 处理后的 Markdown 格式字符串
    """
    # 处理数学公式：将 \[ ... \] 转换为 $$ ... $$（块级公式）
    text = re.sub(r'\\\[([\s\S]*?)\\\]', r'$$\n\1\n$$', input_text)
    
    # 处理内联公式：将 \( ... \) 转换为 $ ... $（行内公式）
    text = re.sub(r'\\\(([\s\S]*?)\\\)', r'$\1$', text)
    
    # 如果有其他 LaTeX 格式的公式（未用 \( 或 \[ 包裹），可以添加额外规则
    # 这里假设大部分公式已按标准 LaTeX 格式编写
    
    # 保留其他 Markdown 结构（如标题、列表、表格等）
    # 可以根据需求添加更多处理规则，比如处理图片、链接等
    
    return text

def process_file(input_file=None, output_file=None):
    """
    从文件读取内容，或从剪切板读取，处理后输出到文件或复制到剪切板。
    :param input_file: 输入文件路径（可选）
    :param output_file: 输出文件路径（可选）
    :return: 处理后的内容
    """
    if input_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        # 如果没有输入文件，从剪切板读取内容
        content = pyperclip.paste()
        if not content:
            raise ValueError("剪切板为空，请复制内容后再运行脚本。")
    
    processed_content = convert_to_obsidian_format(content)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        print(f"转换完成，结果已保存到 {output_file}")
    else:
        # 将结果复制到剪切板
        pyperclip.copy(processed_content)
        print("转换完成，结果已复制到剪切板。")
    
    return processed_content

def main():
    try:
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else None
            process_file(input_file, output_file)
        else:
            # 默认从剪切板读取内容，处理后复制到剪切板
            process_file()
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
