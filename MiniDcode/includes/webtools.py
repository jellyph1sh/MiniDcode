#coding:utf-8

def include(file, *args):
    with open(file, 'r', encoding='utf-8') as file:
        file_content = file.read().format(content=args)
        print(f"{ file_content }")

def scripts_include(file, *args):
    with open(file, 'r', encoding='utf-8') as file:
        file_content = file.read().format(content=args)
        print(f"<script>{ file_content }</script>")