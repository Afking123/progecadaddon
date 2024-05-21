import os
import shutil

def copy_folder_contents(src_folder, dest_folder):
    # 檢查來源資料夾是否存在
    if not os.path.exists(src_folder):
        raise FileNotFoundError(f"來源資料夾不存在: {src_folder}")
    
    # 確保目的資料夾存在，若不存在則創建它
    os.makedirs(dest_folder, exist_ok=True)
    
    # 遍歷來源資料夾中的所有文件和資料夾
    for item in os.listdir(src_folder):
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)
        
        # 如果是文件則複製文件
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)
        # 如果是資料夾則遞歸地複製資料夾內容
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)

# 構建使用者資料夾路徑
user_home = os.path.expanduser("~")
current_working_directory = os.getcwd()
appdata_roaming_path = os.path.join(user_home, "AppData", "Roaming")

# 定義來源和目的資料夾路徑
src_folder1 = os.path.join(current_working_directory, "複製貼上至Fonts")
dest_folder1 = "C:\Program Files\PSOFT\progeCAD 2024 Professional CHT\Fonts"

src_folder2 = os.path.join(current_working_directory, "複製貼上至Professional - Traditional Chinese")
dest_folder2 = os.path.join(appdata_roaming_path, "PSOFT","progeCAD x64","R24","Professional - Traditional Chinese")

destdel_file = "C:\Program Files\PSOFT\progeCAD 2024 Professional CHT\Fonts\LSP.shx"
destdel_file2 = "C:\Program Files\PSOFT\progeCAD 2024 Professional CHT\Fonts\CHINA.shx"

try:
    copy_folder_contents(src_folder1, dest_folder1)
    print(f"資料夾內容已成功複製從 {src_folder1} 到 {dest_folder1}")
    
    copy_folder_contents(src_folder2, dest_folder2)
    print(f"資料夾內容已成功複製從 {src_folder2} 到 {dest_folder2}")
    
    # 刪除指定文件
    if os.path.exists(destdel_file):
        os.remove(destdel_file)
        print(f"文件 {destdel_file} 已成功刪除")
    else:
        print(f"文件 {destdel_file} 不存在")
    if os.path.exists(destdel_file2):
        os.remove(destdel_file2)
        print(f"文件 {destdel_file2} 已成功刪除")
    else:
        print(f"文件 {destdel_file2} 不存在")

except Exception as e:
    print(f"發生錯誤: {e}")
