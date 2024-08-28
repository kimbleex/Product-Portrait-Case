import shutil
import os
from pathlib import Path

class TOOLS(object):
    def copy_files(self, src_dir, dest_dir, file_names):
        # 确保源目录存在
        if not os.path.isdir(src_dir):
            raise FileNotFoundError(f"源目录 {src_dir} 不存在")
        # 确保目标目录存在，不存在则创建
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
        # 遍历要复制的文件名列表
        for file_name in file_names:
            src_file_path = os.path.join(src_dir, file_name)
            dest_file_path = os.path.join(dest_dir, file_name)
            
            # 检查源文件是否存在
            if os.path.isfile(src_file_path):
                shutil.copy2(src_file_path, dest_file_path)
                print(f"文件 {src_file_path} 复制到 {dest_file_path}")
            else:
                print(f"源文件 {src_file_path} 不存在")

